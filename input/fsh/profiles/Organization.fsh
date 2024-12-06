Profile: AtIpsOrganization
Parent: HL7ATCoreOrganization
Id: at-ips-organization
Title: "AT IPS Organization"
Description: "This AT IPS profile for the Organization resource is derived from the corresponding HL7® Austria FHIR® Core profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Organization"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(OrganizationUvIps)
