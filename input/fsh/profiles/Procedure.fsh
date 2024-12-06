Profile: AtIpsProcedure
Parent: Procedure
Id: at-ips-Procedure
Title: "AT IPS Procedure"
Description: "This AT IPS profile for the Procedure resource is derived from the general Procedure resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Procedure"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(ProcedureUvIps)
* subject only Reference(AtIpsPatient)
* performer.actor only Reference(AtIpsPatient or RelatedPerson or DeviceObserverUvIps or AtIpsPractitioner or AtIpsPractitionerRole or AtIpsOrganization)
* performer.onBehalfOf only Reference(AtIpsOrganization)
