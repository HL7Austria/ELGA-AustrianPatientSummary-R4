Profile: AtIpsDiagnosticReport
Parent: DiagnosticReport
Id: at-ips-diagnosticreport
Title: "AT IPS DiagnosticReport"
Description: "This AT IPS profile for the DiagnosticReport resource is derived from the general DiagnosticReport resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS DiagnosticReport"
* ^extension[$imposeProfile].valueCanonical = Canonical(DiagnosticReportUvIps)
* subject only Reference(AtIpsPatient or Group)
* performer only Reference(AtIpsPractitioner or AtIpsPractitionerRole or AtIpsOrganization or CareTeam)
* specimen only Reference(AtIpsSpecimen)

* result ^slicing.discriminator.type = #profile
* result ^slicing.discriminator.path = "resolve()"
* result ^slicing.rules = #open
* result ^slicing.ordered = false
* result contains observationResults 0..*
* result[observationResults] 0..*
* result[observationResults] only Reference(AtIpsObservationResultsLaboratoryPathology or AtIpsObservationResultsRadiology)
