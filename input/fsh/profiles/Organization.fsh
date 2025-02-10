Profile: AtApsOrganization
Parent: HL7ATCoreOrganization
Id: at-aps-organization
Title: "AT APS Organization"
Description: "This AT APS profile for the Organization resource is derived from the corresponding HL7® Austria FHIR® Core profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS Organization"
* ^extension[$imposeProfile].valueCanonical = Canonical(OrganizationUvIps)
