Profile: AtIpsObservationPregnancyOutcome
Parent: Observation
Id: at-ips-observationpregnancyoutcome
Title: "AT IPS Observation Pregnancy Outcome"
Description: "This AT IPS profile for the Observation resource is derived from the general Observation resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Observation Pregnancy Outcome"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(ObservationPregnancyOutcomeUvIps)
* subject only Reference(AtIpsPatient)
* valueCodeableConcept from $pregnancy-summary (extensible)