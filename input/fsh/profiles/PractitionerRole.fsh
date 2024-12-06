Profile: AtIpsPractitionerRole
Parent: HL7ATCorePractitionerRole
Id: at-ips-practitionerrole
Title: "AT IPS PractitionerRole"
Description: "This AT IPS profile for the PractitionerRole resource is derived from the corresponding HL7® Austria FHIR® Core profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "At IPS PractitionerRole"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(PractitionerRoleUvIps)
* practitioner only Reference(AtIpsPractitioner)
* organization only Reference(AtIpsOrganization)
