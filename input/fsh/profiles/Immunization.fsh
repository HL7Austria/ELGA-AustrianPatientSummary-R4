Profile: AtIpsImmunization
Parent: Immunization
Id: at-ips-immunization
Title: "AT IPS Immunization"
Description: "This AT IPS profile for the Immunization resource is derived from the general Immunization resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Immunization"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(ImmunizationUvIps)
* patient only Reference(AtIpsPatient)
