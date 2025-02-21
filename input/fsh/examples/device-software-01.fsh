Instance: device-software-02
InstanceOf: AtApsDevice
Description: "Beispiel einer Software"
Usage: #example
* id = "002"
* patient = Reference(Patient/002) "Maria Musterfrau"
* type = $sct#706687001 "Software"
* deviceName[0].name = "Best Health Software Application"
* deviceName[0].type = #model-name
* deviceName[1].name = "Good Health System"
* deviceName[1].type = #manufacturer-name
* version.value = "1.0.5"
* parent = Reference(Device/001) "Best Health Device"

Instance: device-01
InstanceOf: AtApsDevice
Description: "Beispiel eines Device"
Usage: #example
* id = "001"
* patient = Reference(Patient/002) "Maria Musterfrau"
* type = $sct#49062001 "Device"
* deviceName[0].name = "Best Health Device"
* deviceName[0].type = #model-name
* version.value = "1"