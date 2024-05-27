Profile: AtIpsAllergyIntolerance
Parent: AllergyIntolerance
Id: at-ips-allergyintolerance
Title: "AT IPS AllergyIntolerance"
Description: "This AT IPS profile for the AllergyIntolerance resource is derived from the general AllergyIntolerance resource in absence of a corresponding profile in the HL7® Austria FHIR® Core Implementation Guide and also ensures IPS conformity via the IPS profile referenced by the so-called imposeProfile extension."
* . ^short = "AT IPS AllergyIntolerance"
* ^extension[$imposeProfile].valueCanonical = Canonical(AllergyIntoleranceUvIps)
* patient only Reference(HL7ATCorePatient)
