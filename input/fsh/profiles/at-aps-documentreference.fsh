Profile: AtApsDocumentReference
Parent: DocumentReference
Id: at-aps-documentreference
Title: "AT APS DocumentReference"
Description: "Das AT APS-Profil für die DocumentReference-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient)."
* ^status = #active
* . ^short = "At APS DocumentReference"
* subject only Reference(AtApsPatient or AtApsPractitioner or Group or AtApsDevice)
* author only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or AtApsDevice or AtApsPatient or RelatedPerson)
* context.sourcePatientInfo only Reference(AtApsPatient)