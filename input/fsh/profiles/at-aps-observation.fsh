Profile: AtApsObservation
Parent: Observation
Id: at-aps-observation
Title: "AT APS Observation"
Description: "Das AT APS-Profil für die Observation-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient)."
* ^status = #active
* . ^short = "AT APS Observation"
* subject only Reference(AtApsPatient or Group or AtApsDevice or Location)
* basedOn only Reference(AtApsCarePlan or DeviceRequest or ImmunizationRecommendation or AtApsMedicationRequest or NutritionOrder or ServiceRequest)
* partOf only Reference(AtApsMedicationAdministration or AtApsMedicationDispense or AtApsMedicationStatement or AtApsProcedure or AtApsImmunization or AtApsImagingStudy)
* performer only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or CareTeam or AtApsPatient or RelatedPerson)
* specimen only Reference(AtApsSpecimen)
* device only Reference(AtApsDevice or DeviceMetric)
* hasMember only Reference(AtApsObservation or QuestionnaireResponse or MolecularSequence)
* derivedFrom only Reference(AtApsDocumentReference or AtApsImagingStudy or Media or QuestionnaireResponse or AtApsObservation or MolecularSequence)