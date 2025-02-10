Profile: AtApsMedication
Parent: MedicationIPS
Id: at-aps-medication
Title: "AT APS Medication"
Description: "This AT APS profile for the Medication resource is derived from the IPS Medication resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide."
* . ^short = "AT APS Medication"
// * ^extension[$imposeProfile].valueCanonical = Canonical(MedicationIPS)
* ingredient.item[x] only CodeableConceptIPS or Reference(http://hl7.org/fhir/StructureDefinition/Substance or AtApsMedication)
