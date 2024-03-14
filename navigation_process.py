import asyncio
from bleak import BleakClient

address = "DD3F0AD1-6239-4E1F-81F1-91F6C9F01D86"
uuid = "DD3F0AD2-6239-4E1F-81F1-91F6C9F01D86"

async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        x = await client.is_connected()
        print("Connected: {0}".format(x))

        def callback(sender, data):
            print(f"{sender}: {data}")

        await client.start_notify(uuid, callback)
        await asyncio.sleep(30)  # Keep receiving data for 30 seconds
        await client.stop_notify(uuid)

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))