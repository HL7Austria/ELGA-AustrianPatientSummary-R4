Profile: AtApsDiagnosticReport
Parent: DiagnosticReport
Id: at-aps-diagnosticreport
Title: "AT APS DiagnosticReport"
Description: "This AT APS profile for the DiagnosticReport resource is derived from the general DiagnosticReport resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
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
