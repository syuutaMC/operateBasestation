import asyncio

from bleak import BleakScanner
from bleak import BleakClient

BLE_SERVICE_ID = '00001525-1212-efde-1523-785feabcd124'


async def scan():
    devices = await BleakScanner.discover(timeout=5.0)
    print(len(devices), 'devices found:')
    lhb_devices = list(filter(lambda device: 'LHB' in (device.name or ''), devices))
    print(len(lhb_devices), 'lhb devices found:')

    return lhb_devices


async def send(device, status):
    try:
        async with BleakClient(device.address) as client:
            await client.write_gatt_char(BLE_SERVICE_ID, status)
            result = await client.read_gatt_char(BLE_SERVICE_ID)
            print(result)
    except:
        print('send failed:', device)
