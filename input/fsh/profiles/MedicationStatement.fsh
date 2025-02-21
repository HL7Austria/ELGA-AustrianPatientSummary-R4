Profile: AtApsMedicationStatement
Parent: MedicationStatement
Id: at-aps-medicationstatement
Title: "AT APS MedicationStatement"
Description: "This AT APS profile for the MedicationStatement resource is derived from the general MedicationStatement resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS MedicationStatement"
* ^extension[$imposeProfile].valueCanonical = Canonical(MedicationStatementIPS)
* medication[x] only CodeableConcept or Reference(AtApsMedication)
* subject only Reference(AtApsPatient)
