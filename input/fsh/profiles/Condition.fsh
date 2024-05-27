Profile: AtIpsCondition
Parent: Condition
Id: at-ips-condition
Title: "AT IPS Condition"
Description: "This AT IPS profile for the Condition resource is derived from the general Condition resource in absence of a corresponding profile in the HL7® Austria FHIR® Core Implementation Guide and also ensures IPS conformity via the IPS profile referenced by the so-called imposeProfile extension."
* . ^short = "AT IPS Condition"
* ^extension[$imposeProfile].valueCanonical = Canonical(ConditionUvIps)
* subject only Reference(AtIpsPatient)
