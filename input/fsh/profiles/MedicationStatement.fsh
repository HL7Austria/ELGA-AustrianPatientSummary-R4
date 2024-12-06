Profile: AtIpsMedicationStatement
Parent: MedicationStatement
Id: at-ips-medicationstatement
Title: "AT IPS MedicationStatement"
Description: "This AT IPS profile for the MedicationStatement resource is derived from the general MedicationStatement resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS MedicationStatement"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(MedicationStatementIPS)
* medication[x] only CodeableConcept or Reference(AtIpsMedication)
* subject only Reference(AtIpsPatient)
