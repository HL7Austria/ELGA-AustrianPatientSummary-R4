Profile: AtApsClinicalImpression
Parent: ClinicalImpression
Id: at-aps-clinicalimpression
Title: "AT APS ClinicalImpression"
Description: "Das AT APS-Profil für die ClinicalImpression-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient)."
* ^status = #active
* . ^short = "AT APS ClinicalImpression"
* subject only Reference(AtApsPatient or Group)
* assessor only Reference(AtApsPractitioner or AtApsPractitionerRole)
* previous only Reference(AtApsClinicalImpression)
* problem only Reference(AtApsCondition or AtApsAllergyIntolerance)
* investigation.item only Reference(AtApsObservation or QuestionnaireResponse or FamilyMemberHistory or AtApsDiagnosticReport or RiskAssessment or AtApsImagingStudy or Media)
* finding.itemReference only Reference(AtApsCondition or AtApsObservation or Media)