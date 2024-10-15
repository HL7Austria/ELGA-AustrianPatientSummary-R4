Profile: AtIpsObservationResultsLaboratoryPathology
Parent: Observation
Id: at-ips-observationresultslaboratorypathology
Title: "AT IPS Observation Results Laboratory Pathology"
Description: "This AT IPS profile for the Observation resource is derived from the \"AtIpsObservationResults\" profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Observation Results Laboratory Pathology"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationResultsLaboratoryPathologyUvIps)
* subject only Reference(AtIpsPatient or Group or Device or Location)
* performer only Reference(AtIpsPractitioner or AtIpsPractitionerRole or AtIpsOrganization or CareTeam or AtIpsPatient or RelatedPerson)
* specimen only Reference(AtIpsSpecimen)
* hasMember only Reference(AtIpsObservationResultsLaboratoryPathology)
