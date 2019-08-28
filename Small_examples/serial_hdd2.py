import os, subprocess

disk_drive = os.system('wmic diskdrive get serialnumber')
disk_drive_as_string = str(disk_drive)
disk_drive_model = os.system('wmic diskdrive get Model')
disk_drive_manufacturer = os.system('wmic diskdrive get Manufacturer')
disk_drive_systemname = os.system('wmic diskdrive get SystemName')
uuid_serial = subprocess.check_output('wmic csproduct get UUID')
memory_chip = os.system('wmic memorychip get serialnumber')
mobo = os.system('wmic baseboard get serialnumber')

print('HDD serial number is: ', disk_drive_as_string)
print('HDD model is: ', disk_drive_model)
print('HDD manufacturer is: ', disk_drive_manufacturer)
print('HDD manufacturer is: ', disk_drive_systemname)
print('Universall Unique Identifier (UUID)', uuid_serial)
print('Memorychip serial number:', memory_chip)
print('Mother board serial number: ', mobo)

