Profile: AtApsObservationAlcoholUse
Parent: Observation
Id: at-aps-observationalcoholuse
Title: "AT APS Observation Alcohol Use"
Description: "This AT APS profile for the Observation resource is derived from the general Observation resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* ^status = #active
* . ^short = "AT APS Observation Alcohol Use"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationAlcoholUseUvIps)
* subject only Reference(AtApsPatient)
