import dbus
from dbus.mainloop.glib import DBusGMainLoop
from advertisement import Advertisement
from service import Application, Service, Characteristic, Descriptor
import dbus.exceptions
import array
import time
import threading

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
DBUS_PROP_IFACE = "org.freedesktop.DBus.Properties"

class ESP32Service(Service):
    ESP32_SERVICE_UUID = "DD3F0AD1-6239-4E1F-81F1-91F6C9F01D86"

    def __init__(self, index):
        Service.__init__(self, index, self.ESP32_SERVICE_UUID, True)
        self.add_characteristic(WriteCharacteristic(self))
        self.add_characteristic(IndicateCharacteristic(self))

class WriteCharacteristic(Characteristic):
    WRITE_CHARACTERISTIC_UUID = "DD3F0AD3-6239-4E1F-81F1-91F6C9F01D86"

    def __init__(self, service):
        Characteristic.__init__(self, self.WRITE_CHARACTERISTIC_UUID, ["write"], service)

    def WriteValue(self, value, options):
        print("Received Data: ", end="")
        data = bytearray(value)

        basic_data_indicator = data[0]
        speed_limit = data[1]
        direction_code = data[2]
        distance_bytes = data[3:]
        try:
            distance_str = distance_bytes.decode('ascii')
        except UnicodeDecodeError:
            print("Invalid distance data")
        message = f"Basic Data: {basic_data_indicator}, Speed Limit: {speed_limit} km/h, Action: {direction_code}, Distance: {distance_str}"
        print(message)

        # Here you can add parsing of the received data

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

def main():
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()

    app = Application()
    esp32_service = ESP32Service(0)
    app.add_service(esp32_service)

    adv = ESP32Advertisement(0)
    app.register()
    adv.register()

    try:
        app.run()
    except KeyboardInterrupt:
        app.quit()

if __name__ == "__main__":
    main()
