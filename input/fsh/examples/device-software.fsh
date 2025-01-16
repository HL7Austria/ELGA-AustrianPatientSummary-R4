Instance: device-software
InstanceOf: Device
Description: "Beispiel einer Software"
Usage: #example
* patient = Reference(patient-01)
* type = $medical-devices#706687001 "Software"
* deviceName[0].name = "Best Health Software Application"
* deviceName[0].type = #model-name
* deviceName[1].name = "Good Health System"
* deviceName[1].type = #manufacturer-name
* version.value = "1.0.5"
* parent = Reference(device-01)

Instance: device-01
InstanceOf: Device
Description: "Beispiel eines Device"
Usage: #example
* patient = Reference(patient-01)
* type = $medical-devices#49062001 "Device"
* deviceName[0].name = "Best Health Device"
* deviceName[0].type = #model-name
* version.value = "1"