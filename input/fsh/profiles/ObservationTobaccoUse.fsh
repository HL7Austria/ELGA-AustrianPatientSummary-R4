Profile: AtIpsObservationTobaccoUse
Parent: Observation
Id: at-ips-observationtobaccouse
Title: "AT IPS Observation Tobacco Use"
Description: "This AT IPS profile for the Observation resource is derived from the general Observation resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Observation Tobacco Use"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationTobaccoUseUvIps)
* subject only Reference(AtIpsPatient)
* valueCodeableConcept from $current-smoking-status (extensible)
