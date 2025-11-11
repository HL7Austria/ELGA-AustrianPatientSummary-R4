Instance: AtApsExampleDeviceUseStatement01
InstanceOf: AtApsDeviceUseStatement
Title: "AtApsDeviceUseStatement-Beispiel"
Description: "Device Use Statement"
Usage: #example
* identifier.value = "51ebb7a9-4e3a-4360-9a05-0cc2d869086f"
* status = #active
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* device = Reference(Device/at-aps-example-device-01)
* timingDateTime = "2015-02-07"