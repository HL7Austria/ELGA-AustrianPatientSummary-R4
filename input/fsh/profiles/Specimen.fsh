Profile: AtIpsSpecimen
Parent: Specimen
Id: at-ips-specimen
Title: "AT IPS Specimen"
Description: "This AT IPS profile for the Specimen resource is derived from the general Specimen resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Specimen"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(SpecimenUvIps)
* subject only Reference(AtIpsPatient)
