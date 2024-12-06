Profile: AtIpsObservationAlcoholUse
Parent: Observation
Id: at-ips-observationalcoholuse
Title: "AT IPS Observation Alcohol Use"
Description: "This AT IPS profile for the Observation resource is derived from the general Observation resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Observation Alcohol Use"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(ObservationAlcoholUseUvIps)
* subject only Reference(AtIpsPatient)
