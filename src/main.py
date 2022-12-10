import asyncio
import configparser
import os

from bleak import BleakScanner
from bleak import BleakClient


class Main:
    def __init__(self):
        config = configparser.ConfigParser()
        path = os.path.join(os.path.dirname(__file__), '..\config\config.ini')
        print(path)
        config.read(path)

        self.service = config['BLE']['service']

    async def scan(self):
        devices = await BleakScanner.discover(timeout=5.0)
        device_list = []
        for d in devices:
            devices_name = d.name
            print(devices_name)
            if "LHB" in str(devices_name):
                device_list.append(d)

        return device_list

    async def connect(self, device_list, status, loop):
        print(device_list)
        for d in device_list:
            print(d)
            async with BleakClient(d.address, loop=loop) as client:
                await client.write_gatt_char(self.service, status)
                y = await client.read_gatt_char(self.service)
                print(y)
            # client = BleakClient(d)
            # try:
            #     await client.connect()
            #     print("ok")
            #     model_number = await client.read_gatt_char(self.service)
            #     print("Model Number: {0}".format("".join(map(chr, model_number))))
            # except Exception as e:
            #     print(e)
            # finally:
            #     await client.disconnect()


if __name__ == '__main__':
    main = Main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main.scan(loop, b'\x00'))
