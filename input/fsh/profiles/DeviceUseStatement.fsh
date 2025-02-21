Profile: AtApsDeviceUseStatement
Parent: DeviceUseStatement
Id: at-aps-deviceusestatement
Title: "AT APS DeviceUseStatement"
Description: "This AT APS profile for the DeviceUseStatement resource is derived from the general DeviceUseStatement resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS DeviceUseStatement"
* ^extension[$imposeProfile].valueCanonical = Canonical(DeviceUseStatementUvIps)
* subject only Reference(AtApsPatient)
* device only Reference(AtApsDevice)
