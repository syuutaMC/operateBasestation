import asyncio
import configparser
import os

from bleak import BleakScanner
from bleak import BleakClient


def main():

    def __init__(self):
        config = configparser.ConfigParser()
        path = os.path.join(os.path.dirname(__file__), '..\config\config.ini')
        print(path)
        config.read(path)

        self.service = config['BLE']['service']

    async def scan(self):
        devices = await BleakScanner.discover(timeout=5.0)
        lhb_devices = []
        for d in devices:
            devices_name = d.name
            print(devices_name)
            if "LHB" in str(devices_name):
                lhb_devices.append(d)

        return lhb_devices

    async def connect(self, device_list, status, loop):
        print(device_list)
        for d in device_list:
            print(d)
            async with BleakClient(d.address, loop=loop) as client:
                await client.write_gatt_char(self.service, status)
                y = await client.read_gatt_char(self.service)
                print(y)


if __name__ == '__main__':
    main = Main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main.scan(loop, b'\x00'))
