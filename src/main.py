import asyncio
from bleak import BleakScanner
from bleak import BleakClient
from asyncio import *

service = "00001525-1212-efde-1523-785feabcd124"
class main():
    async def scan(self, loop):
        devices = await BleakScanner.discover(timeout=5.0)
        device_list = []
        for d in devices:
            devices_name = d.name
            print(devices_name)
            if "LHB" in str(devices_name):
                device_list.append(d)

        await self.connect(device_list, loop)

    async def connect(self, device_list, loop):
        print(device_list)
        for d in device_list:
            async with BleakClient(d.address, loop=loop) as client:
                x = await client.is_connected()
                print("Connected: {0}".format(x))
                y = await client.read_gatt_char(service)
                # await client.write_gatt_char(service, b'\x00')
                print(y)


if __name__ == '__main__':
    main = main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main.scan(loop))
