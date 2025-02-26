Profile: AtApsPractitioner
Parent: HL7ATCorePractitioner
Id: at-aps-practitioner
Title: "AT APS Practitioner"
Description: "This AT APS profile for the Practitioner resource is derived from the corresponding HL7® Austria FHIR® Core profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* ^status = #active
* . ^short = "AT APS Practitioner"
* ^extension[$imposeProfile].valueCanonical = Canonical(PractitionerUvIps)
