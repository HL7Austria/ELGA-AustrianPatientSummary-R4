Profile: AtApsDeviceUseStatement
Parent: DeviceUseStatement
Id: at-aps-deviceusestatement
Title: "AT APS DeviceUseStatement"
Description: "Das AT APS-Profil für die DeviceUseStatement-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS DeviceUseStatement"
* ^extension[$imposeProfile].valueCanonical = Canonical(DeviceUseStatementUvIps)
* subject only Reference(AtApsPatient)
* device only Reference(AtApsDevice)
* derivedFrom only Reference(ServiceRequest or AtApsProcedure or Claim or AtApsObservation or QuestionnaireResponse or AtApsDocumentReference)
* source only Reference(AtApsPatient or AtApsPractitioner or AtApsPractitionerRole or RelatedPerson)
* reasonReference only Reference(AtApsCondition or AtApsObservation or AtApsDiagnosticReport or AtApsDocumentReference or Media)