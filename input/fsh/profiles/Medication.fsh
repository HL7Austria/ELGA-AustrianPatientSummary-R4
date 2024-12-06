Profile: AtIpsMedication
Parent: MedicationIPS
Id: at-ips-medication
Title: "AT IPS Medication"
Description: "This AT IPS profile for the Medication resource is derived from the IPS Medication resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide."
* . ^short = "AT IPS Medication"
// * ^extension[AtIpsImposeProfile].valueCanonical = Canonical(MedicationIPS)
* ingredient.item[x] only CodeableConceptIPS or Reference(http://hl7.org/fhir/StructureDefinition/Substance or AtIpsMedication)
