Profile: AtApsDevice
Parent: Device
Id: at-aps-device
Title: "AT APS Device"
Description: "This AT APS profile for the Device resource is derived from the general Device resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* ^status = #active
* . ^short = "AT APS Device"
* ^extension[$imposeProfile].valueCanonical = Canonical(DeviceUvIps)
* patient only Reference(AtApsPatient)
* deviceName 1..*
* version 1..*
* type from $medical-devices (extensible)