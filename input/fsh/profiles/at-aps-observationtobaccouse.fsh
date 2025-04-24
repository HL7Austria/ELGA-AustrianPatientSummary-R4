Profile: AtApsObservationTobaccoUse
Parent: Observation
Id: at-aps-observationtobaccouse
Title: "AT APS Observation Tobacco Use"
Description: "This AT APS profile for the Observation resource is derived from the general Observation resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* ^status = #active
* . ^short = "AT APS Observation Tobacco Use"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationTobaccoUseUvIps)
* subject only Reference(AtApsPatient)
* valueCodeableConcept from $vs-elga-currentsmokingstatus (extensible)
