
import asyncio
from bleak import BleakClient, BleakScanner
import logging

# Bash output color codes

GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
GOLD = '\033[33m'
BOLD = '\033[1m'
END = '\033[0m'


logger = logging.getLogger(__name__)


async def find_b():
    devices = await BleakScanner.discover()
    for device in devices:
        print(device)


# Name: oura_A038F8102C57
# Address: 41C54EB0-EF91-9D73-18B1-610A5B87E037
# Details: (<CBPeripheral: 0x600003098340, identifier = 41C54EB0-EF91-9D73-18B1-610A5B87E037, name = oura_A038F8102C57, mtu = 0, state = disconnected>, <CentralManagerDelegate: 0x13df85bc0>)
# Metadata: {'uuids': ['98ed0001-a541-11e4-b6a0-0002a5d5c51b'], 'manufacturer_data': {690: b'\x04F[\x06'}}
# RSSI: -81
async def findDevices():
    return await BleakScanner.discover()

def printDevices(devices):
    for device in devices:
        print()
        print(f"Name: {device.name}")
        print(f"Address: {device.address}")
        print(f"Details: {device.details}")
        print(f"Metadata: {device.metadata}")
        print(f"RSSI: {device.rssi}")

def ouraDevice(devices, matcher='oura'):
    ods = [device for device in devices if device.name and matcher in device.name.lower()]
    if len(ods) == 1:
        return ods[0]
    else:
        tooManyOura = "Expected exactly one device with '{}' in its name, but found {} devices, with ids {}"
        ids = (device.name for device in ods)
        raise ValueError(tooManyOura.format(matcher, len(ods), ids))

async def printMetadata(device):
    try:
        this_device = await BleakScanner.find_device_by_address(device.address, timeout=20)
        async with BleakClient(this_device) as client:
            print(f'Services found for device')
            print(f'\tDevice address:{device.address}')
            print(f'\tDevice name:{device.name}')
            print('\tServices:')
            for service in client.services:
                print()
                print(f'\t\tDescription: {service.description}')
                print(f'\t\tService: {service}')
                print('\t\tCharacteristics:')
                for c in service.characteristics:
                    print()
                    print(f'\t\t\tUUID: {c.uuid}'),
                    print(f'\t\t\tDescription: {c.uuid}')
                    print(f'\t\t\tHandle: {c.uuid}'),
                    print(f'\t\t\tProperties: {c.uuid}')
                    print('\t\tDescriptors:')
                    for descriptor in c.descriptors:
                        print(f'\t\t\t{descriptor}')
    except Exception as e:
            print(f"Could not connect to device with info: {device}")
            print(f"Error: {e}")


async def mans():
    devices = await BleakScanner.discover()
    # for device in devices:
    #     print()
    #     print(f"Name: {device.name}")
    #     print(f"Address: {device.address}")
    #     print(f"Details: {device.details}")
    #     print(f"Metadata: {device.metadata}")
    #     print(f"RSSI: {device.rssi}")
    device = ouraDevice(devices)
    # for device in devices:
    try:
        this_device = await BleakScanner.find_device_by_address(device.address, timeout=20)
        async with BleakClient(this_device) as client:
            print(f'Services found for device')
            print(f'\tDevice address:{device.address}')
            print(f"Name: {GREEN}{device.name}{END}")
            print('\tServices:')
            for service in client.services:
                print()
                print(f'\t\tDescription: {service.description}')
                print(f"\t\t{GREEN}Service: {service}{END}")
                print('\t\tCharacteristics:')
                for c in service.characteristics:
                    print()
                    print(f'\t\t\tUUID: {c.uuid}'),
                    print(f'\t\t\tDescription: {c.uuid}')
                    print(f'\t\t\tHandle: {c.uuid}'),
                    print(f'\t\t\tProperties: {c.uuid}')
                    print('\t\tDescriptors:')
                    for descriptor in c.descriptors:
                        print(f'\t\t\t{descriptor}')
                        async with BleakClient.read_gatt_descriptor(descriptor) as desdetail:
                            print(f'\t\t\t\t{desdetail}')
    except Exception as e:
            print(f"Could not connect to device with info: {device}")
            print(f"Error: {e}")

asyncio.run(mans())
