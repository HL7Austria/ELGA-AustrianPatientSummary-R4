Profile: AtApsPractitionerRole
Parent: HL7ATCorePractitionerRole
Id: at-aps-practitionerrole
Title: "AT APS PractitionerRole"
Description: "This AT APS profile for the PractitionerRole resource is derived from the corresponding HL7® Austria FHIR® Core profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* ^status = #active
* . ^short = "At APS PractitionerRole"
* ^extension[$imposeProfile].valueCanonical = Canonical(PractitionerRoleUvIps)
* practitioner only Reference(AtApsPractitioner)
* organization only Reference(AtApsOrganization)
