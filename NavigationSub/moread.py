import dbus
from dbus.mainloop.glib import DBusGMainLoop
from NavigationSub.advertisement import Advertisement
from NavigationSub.service import Application, Service, Characteristic, Descriptor
import dbus.exceptions
import array
import time
import threading
from enum import Enum, auto
import multiprocessing

outcome = [None, None, None, None]

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
DBUS_PROP_IFACE = "org.freedesktop.DBus.Properties"

class ESP32Service(Service):
    ESP32_SERVICE_UUID = "DD3F0AD1-6239-4E1F-81F1-91F6C9F01D86"
    def __init__(self, index,queue):
        Service.__init__(self, index, self.ESP32_SERVICE_UUID, True)
        self.add_characteristic(WriteCharacteristic(self,queue))
        self.add_characteristic(IndicateCharacteristic(self))

class WriteCharacteristic(Characteristic):
    WRITE_CHARACTERISTIC_UUID = "DD3F0AD3-6239-4E1F-81F1-91F6C9F01D86"

    def __init__(self, service,queue):
        Characteristic.__init__(self, self.WRITE_CHARACTERISTIC_UUID, ["write"], service)
        self.queue = queue
    def WriteValue(self, value, options):
        print("Received Data: ", end="")
        data = bytearray(value)

        basic_data_indicator = data[0]
        speed_limit = data[1]
        direction_code = data[2]
        distance_bytes = data[3:]
        direction_value, direction_name = check_direction(direction_code)
        try:
            distance_str = distance_bytes.decode('ascii')
        except UnicodeDecodeError:
            print("Invalid distance data")


        outcome = {
            'speed_limit': speed_limit,
            'action': direction_name,
            'direction_code': direction_code,
            'distance': distance_str
        }
        self.queue.put(outcome)
        print(f"Speed Limit: {speed_limit} km/h, Action: {direction_name}, Distance: {distance_str}")


class Direction(Enum):
    NoEndPoint = 0
    Start = 1
    EasyLeft = 2
    EasyRight = 3
    End = 4
    Via = 5
    KeepLeft = 6
    KeepRight = 7
    TurnLeft = 8
    OutOfRoute = 9
    TurnRight = 10
    SharpLeft = 11
    SharpRight = 12
    GoStraight = 13
    UtterTurnLeft = 14
    UtterTurnRight = 15
    Ferry = 16
    StateBoundary = 17
    Follow = 18
    Motorway = 19
    Tunnel = 20
    ExitLeft = 21
    ExitRight = 22
    RoundaboutRSE = 23
    RoundaboutRE = 24
    RoundaboutRNE = 25
    RoundaboutRN = 26
    RoundaboutRNW = 27
    RoundaboutRW = 28
    RoundaboutRSW = 29
    RoundaboutRS = 30
    RoundaboutLSE = 31
    RoundaboutLE = 32
    RoundaboutLNE = 33
    RoundaboutLN = 34
    RoundaboutLNW = 35
    RoundaboutLW = 36
    RoundaboutLSW = 37
    RoundaboutLS = 38

def check_direction(direction_code):
    try:
        direction = Direction(direction_code)
        return direction.value, direction.name
    except ValueError:
        return None, "Invalid direction code"

class IndicateCharacteristic(Characteristic):
    INDICATE_CHARACTERISTIC_UUID = "DD3F0AD2-6239-4E1F-81F1-91F6C9F01D86"

    def __init__(self, service):
        Characteristic.__init__(self, self.INDICATE_CHARACTERISTIC_UUID, ["indicate"], service)
        self.value = array.array('B', [0])
        self.add_descriptor(UpdateDescriptor(self))

    def set_value(self, value):
        self.value = array.array('B', value)
        self.PropertiesChanged(GATT_CHRC_IFACE, {'Value': self.value}, [])

class UpdateDescriptor(Descriptor):
    UPDATE_DESCRIPTOR_UUID = "2902"

    def __init__(self, characteristic):
        Descriptor.__init__(self, self.UPDATE_DESCRIPTOR_UUID, ["read", "write"], characteristic)

    def ReadValue(self, options):
        return self.characteristic.value

    def WriteValue(self, value, options):
        self.characteristic.set_value(value)

class ESP32Advertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.add_service_uuid(ESP32Service.ESP32_SERVICE_UUID)
        self.add_local_name("ESP32 BLE Server")
        self.include_tx_power = True

def main_navi(q):
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    app = Application()
    esp32_service = ESP32Service(0,q)
    app.add_service(esp32_service)
    adv = ESP32Advertisement(0)
    app.register()
    adv.register()

    try:
        app.run()
    except KeyboardInterrupt:
        app.quit()

