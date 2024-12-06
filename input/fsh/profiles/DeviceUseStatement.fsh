Profile: AtIpsDeviceUseStatement
Parent: DeviceUseStatement
Id: at-ips-deviceusestatement
Title: "AT IPS DeviceUseStatement"
Description: "This AT IPS profile for the DeviceUseStatement resource is derived from the general DeviceUseStatement resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS DeviceUseStatement"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(DeviceUseStatementUvIps)
* subject only Reference(AtIpsPatient)
* device only Reference(AtIpsDevice)
