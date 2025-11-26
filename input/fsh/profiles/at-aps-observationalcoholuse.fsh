Profile: AtApsObservationAlcoholUse
Parent: AtApsObservation
Id: at-aps-observationalcoholuse
Title: "AT APS Observation Alcohol Use"
Description: "Das AT APS-Profil für die Observation-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Observation Alcohol Use"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationAlcoholUseUvIps)
* subject only Reference(AtApsPatient)
* basedOn only Reference(AtApsCarePlan or DeviceRequest or ImmunizationRecommendation or AtApsMedicationRequest or NutritionOrder or ServiceRequest)
* partOf only Reference(AtApsMedicationAdministration or AtApsMedicationDispense or AtApsMedicationStatement or AtApsProcedure or AtApsImmunization or AtApsImagingStudy)
* performer only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or CareTeam or AtApsPatient or RelatedPerson)
* specimen only Reference(AtApsSpecimen)
* hasMember only Reference(AtApsObservation or QuestionnaireResponse or MolecularSequence)
* derivedFrom only Reference(AtApsDocumentReference or AtApsImagingStudy or Media or QuestionnaireResponse or AtApsObservation or MolecularSequence)