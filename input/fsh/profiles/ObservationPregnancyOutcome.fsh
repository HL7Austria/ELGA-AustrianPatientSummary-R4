Profile: AtApsObservationPregnancyOutcome
Parent: Observation
Id: at-aps-observationpregnancyoutcome
Title: "AT APS Observation Pregnancy Outcome"
Description: "This AT APS profile for the Observation resource is derived from the general Observation resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS Observation Pregnancy Outcome"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationPregnancyOutcomeUvIps)
* subject only Reference(AtApsPatient)
* code from $pregnancy-summary (extensible)