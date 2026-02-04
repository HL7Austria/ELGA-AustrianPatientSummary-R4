Profile: AtApsMedicationDispense
Parent: MedicationDispense
Id: at-aps-medicationdispense
Title: "AT APS MedicationDispense"
Description: "Das AT APS-Profil für die MedicationDispense-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient)."
* ^status = #active
* . ^short = "At APS MedicationDispense"
* subject only Reference(AtApsPatient or Group)
* partOf only Reference(AtApsProcedure)
* medication[x] only Reference(AtApsMedication)
* performer.actor only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or AtApsPatient or AtApsDevice or RelatedPerson)
* authorizingPrescription only Reference(AtApsMedicationRequest)
* receiver only Reference(AtApsPatient or AtApsPractitioner)
* substitution.responsibleParty only Reference(AtApsPractitioner or AtApsPractitionerRole)