Instance: AtApsExampleDevice02Software
InstanceOf: AtApsDevice
Title: "AtApsDevice-Beispiel 2"
Description: "Software eines Medizinprodukts"
Usage: #example
* id = "at-aps-example-device-02-software"
* patient = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* type = $cs-sct#706687001 "Software"
* deviceName[0].name = "Best Health Software Application"
* deviceName[0].type = #model-name
* deviceName[1].name = "Good Health System"
* deviceName[1].type = #manufacturer-name
* version.value = "1.0.5"
* parent = Reference(Device/at-aps-example-device-01) "Best Health Device"

Instance: AtApsExampleDevice01
InstanceOf: AtApsDevice
Title: "AtApsDevice-Beispiel 1"
Description: "Medizinprodukt"
Usage: #example
* id = "at-aps-example-device-01"
* patient = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* type = $cs-sct#49062001 "Gerät"
* deviceName[0].name = "Best Health Device"
* deviceName[0].type = #model-name
* version.value = "1"

Instance: AtApsExampleDevice03
InstanceOf: Device
Description: "Medizinprodukt"
Usage: #example
* id = "at-aps-example-device-03"
* patient = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* type = $cs-sct#49062001 "Gerät"
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Dieses Gerät erzeugt ein APS FHIR-Dokument.</p></div>"
* deviceName.name = "APS Generator"
* deviceName.type = #user-friendly-name

Instance: AtApsExampleDevice04
InstanceOf: Device
Description: "APS Generator"
Usage: #example
* type = $cs-sct#49062001 "Gerät"
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Dieses Gerät erzeugt ein APS FHIR-Dokument.</p></div>"
* deviceName.name = "APS Generator"
* deviceName.type = #user-friendly-name