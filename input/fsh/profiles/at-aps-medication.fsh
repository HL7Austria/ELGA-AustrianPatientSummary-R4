Profile: AtApsMedication
Parent: Medication
Id: at-aps-medication
Title: "AT APS Medication"
Description: "Das AT APS-Profil für die Medication-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Medication"
* ^extension[$imposeProfile].valueCanonical = Canonical(MedicationIPS)
* ingredient.item[x] only CodeableConceptIPS or Reference(http://hl7.org/fhir/StructureDefinition/Substance or AtApsMedication)
