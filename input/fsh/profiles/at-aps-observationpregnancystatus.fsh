Profile: AtApsObservationPregnancyStatus
Parent: Observation
Id: at-aps-observationpregnancystatus
Title: "AT APS Observation Pregnancy Status"
Description: "This AT APS profile for the Observation resource is derived from the general Observation resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* ^status = #active
* . ^short = "AT APS Observation Pregnancy Status"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationPregnancyStatusUvIps)
* subject only Reference(AtApsPatient)
* hasMember only Reference(AtApsObservationPregnancyEdd)
* valueCodeableConcept from $pregnancy-status (extensible)
