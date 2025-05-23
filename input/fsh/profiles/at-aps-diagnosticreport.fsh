Profile: AtApsDiagnosticReport
Parent: DiagnosticReport
Id: at-aps-diagnosticreport
Title: "AT APS DiagnosticReport"
Description: "Das AT APS-Profil für die DiagnosticReport-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS DiagnosticReport"
* ^extension[$imposeProfile].valueCanonical = Canonical(DiagnosticReportUvIps)
* subject only Reference(AtApsPatient or Group)
* performer only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or CareTeam)
* specimen only Reference(AtApsSpecimen)

* result ^slicing.discriminator.type = #profile
* result ^slicing.discriminator.path = "resolve()"
* result ^slicing.rules = #open
* result ^slicing.ordered = false
* result contains observationResults 0..*
* result[observationResults] 0..*
* result[observationResults] only Reference(AtApsObservationResultsLaboratoryPathology or AtApsObservationResultsRadiology)
