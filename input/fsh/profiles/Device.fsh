Profile: AtIpsDevice
Parent: Device
Id: at-ips-device
Title: "AT IPS Device"
Description: "This AT IPS profile for the Device resource is derived from the general Device resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Device"
* ^extension[$imposeProfile].valueCanonical = Canonical(DeviceUvIps)
* patient only Reference(AtIpsPatient)
* deviceName 1..*
* version 1..*