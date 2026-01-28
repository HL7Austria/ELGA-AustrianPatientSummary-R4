Profile: AtApsProcedure
Parent: Procedure
Id: at-aps-procedure
Title: "AT APS Procedure"
Description: "Das AT APS-Profil für die Procedure-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Procedure"
* ^extension[$imposeProfile].valueCanonical = Canonical(ProcedureUvIps)
* subject only Reference(AtApsPatient)
* performer.actor only Reference(AtApsPatient or RelatedPerson or DeviceObserverUvIps or AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization)
* performer.onBehalfOf only Reference(AtApsOrganization)
* code from $vs-procedures-uv-ips (extensible)
* bodySite ^binding.strength = #extensible
* basedOn only Reference(AtApsCarePlan or ServiceRequest)
* partOf only Reference(AtApsProcedure or AtApsObservation or AtApsMedicationAdministration)
* recorder only Reference(AtApsPatient or RelatedPerson or AtApsPractitioner or AtApsPractitionerRole)
* asserter only Reference(AtApsPatient or RelatedPerson or AtApsPractitioner or AtApsPractitionerRole)
* reasonReference only Reference(AtApsCondition or AtApsObservation or AtApsProcedure or AtApsDiagnosticReport or AtApsDocumentReference)
* report only Reference(AtApsDiagnosticReport or AtApsDocumentReference or AtApsComposition)
* complicationDetail only Reference(AtApsCondition)
* focalDevice.manipulated only Reference(AtApsDevice)
* usedReference only Reference(AtApsDevice or AtApsMedication or Substance)