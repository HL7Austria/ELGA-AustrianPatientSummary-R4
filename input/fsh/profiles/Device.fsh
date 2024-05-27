Profile: AtIpsDevice
Parent: Device
Id: at-ips-device
Title: "AT IPS Device"
Description: "This AT IPS profile for the Device resource is derived from the general Device resource in absence of a corresponding profile in the HL7® Austria FHIR® Core Implementation Guide and also ensures IPS conformity via the IPS profile referenced by the so-called imposeProfile extension."
* . ^short = "AT IPS Device"
* ^extension[$imposeProfile].valueCanonical = Canonical(DeviceUvIps)
* patient only Reference(AtIpsPatient)
