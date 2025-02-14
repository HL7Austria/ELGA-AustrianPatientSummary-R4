Profile: AtApsProcedure
Parent: Procedure
Id: at-aps-Procedure
Title: "AT APS Procedure"
Description: "This AT APS profile for the Procedure resource is derived from the general Procedure resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS Procedure"
* ^extension[$imposeProfile].valueCanonical = Canonical(ProcedureUvIps)
* subject only Reference(AtApsPatient)
* performer.actor only Reference(AtApsPatient or RelatedPerson or DeviceObserverUvIps or AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization)
* performer.onBehalfOf only Reference(AtApsOrganization)
* code from $vs-procedures-uv-ips (extensible)
* bodySite ^binding.strength = #extensible
