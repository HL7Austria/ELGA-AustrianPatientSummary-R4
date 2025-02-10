Profile: AtApsObservationResultsRadiology
Parent: Observation
Id: at-aps-observationresultsradiology
Title: "AT APS Observation Results Radiology"
Description: "This AT APS profile for the Observation resource is derived from the \"AtApsObservationResults\" profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS Observation Results Radiology"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationResultsRadiologyUvIps)
* partOf only Reference(AtApsImagingStudy)
* subject only Reference(AtApsPatient)
* performer only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or CareTeam or AtApsPatient or RelatedPerson)
* hasMember only Reference(AtApsObservationResultsRadiology)
