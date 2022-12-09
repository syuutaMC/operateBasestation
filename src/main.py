import asyncio
from bleak import BleakScanner


service = "00001523-1212-efde-1523-785feabcd124"

async def run():
    devices = await BleakScanner.discover()
    device_list = []
    for d in devices:
        devices_name = d.name
        if str(devices_name) in "LHB*":
            device_list.append(d)

    print(device_list)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
