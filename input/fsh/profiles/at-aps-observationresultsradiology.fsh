Profile: AtApsObservationResultsRadiology
Parent: AtApsObservation
Id: at-aps-observationresultsradiology
Title: "AT APS Observation Results Radiology"
Description: "Das AT APS-Profil für die Observation-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Observation Results Radiology"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationResultsRadiologyUvIps)
* partOf only Reference(AtApsImagingStudy)
* subject only Reference(AtApsPatient)
* performer only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or CareTeam or AtApsPatient or RelatedPerson)
* hasMember only Reference(AtApsObservationResultsRadiology)
