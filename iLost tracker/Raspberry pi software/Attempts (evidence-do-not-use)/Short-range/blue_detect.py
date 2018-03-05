import bluetooth

target_name = 'Puck.js c1a9'
target_address = None



nearby_devices = bluetooth.discover_devices()


for device_address in nearby_devices:
    if target_name == bluetooth.lookup_name(device_address):
        target_address = device_address
        break

if target_address is not None:
     print("Found watch."), target_address
     
else:
     print("Watch was not found.")
