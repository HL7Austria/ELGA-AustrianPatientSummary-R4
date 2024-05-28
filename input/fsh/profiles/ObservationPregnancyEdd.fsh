Profile: AtIpsObservationPregnancyEdd
Parent: Observation
Id: at-ips-observationpregnancyedd
Title: "AT IPS Observation Pregnancy Expected Delivery Date"
Description: "This AT IPS profile for the Observation resource is derived from the general Observation resource in absence of a corresponding profile in the HL7® Austria FHIR® Core Implementation Guide and also ensures IPS conformity via the IPS profile referenced by the so-called imposeProfile extension."
* . ^short = "AT IPS Observation Pregnancy Expected Delivery Date"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationPregnancyEddUvIps)
* subject only Reference(AtIpsPatient)
