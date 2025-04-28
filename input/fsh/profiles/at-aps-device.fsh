Profile: AtApsDevice
Parent: Device
Id: at-aps-device
Title: "AT APS Device"
Description: "Das AT APS-Profil für die Device-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Device"
* ^extension[$imposeProfile].valueCanonical = Canonical(DeviceUvIps)
* patient only Reference(AtApsPatient)
* deviceName 1..*
* version 1..*
* type from $vs-elga-medicaldevices (extensible)