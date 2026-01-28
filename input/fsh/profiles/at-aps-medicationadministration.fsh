Profile: AtApsMedicationAdministration
Parent: MedicationAdministration
Id: at-aps-medicationadministration
Title: "AT APS MedicationAdministration"
Description: "Das AT APS-Profil für die MedicationAdministration-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient)."
* ^status = #active
* . ^short = "At APS MedicationAdministration"
* subject only Reference(AtApsPatient or Group)
* partOf only Reference(AtApsMedicationAdministration or AtApsProcedure)
* medication[x] only Reference(AtApsMedication)
* performer.actor only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsPatient or RelatedPerson or AtApsDevice)
* reasonReference only Reference(AtApsCondition or AtApsObservation or AtApsDiagnosticReport)
* request only Reference(AtApsMedicationRequest)
* device only Reference(AtApsDevice)