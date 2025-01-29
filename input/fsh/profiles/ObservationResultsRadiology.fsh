Profile: AtIpsObservationResultsRadiology
Parent: Observation
Id: at-ips-observationresultsradiology
Title: "AT IPS Observation Results Radiology"
Description: "This AT IPS profile for the Observation resource is derived from the \"AtIpsObservationResults\" profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Observation Results Radiology"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationResultsRadiologyUvIps)
* partOf only Reference(AtIpsImagingStudy)
* subject only Reference(AtIpsPatient)
* performer only Reference(AtIpsPractitioner or AtIpsPractitionerRole or AtIpsOrganization or CareTeam or AtIpsPatient or RelatedPerson)
* hasMember only Reference(AtIpsObservationResultsRadiology)
