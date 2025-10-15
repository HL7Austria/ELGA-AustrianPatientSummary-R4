Instance: AtApsExampleDiagnosticReport01
InstanceOf: AtApsDiagnosticReport
Title: "AtApsDiagnosticReport-Beispiel"
Description: "Diagnostic Report"
Usage: #example
* status = #final
* category = http://terminology.hl7.org/CodeSystem/v2-0074#LAB "Labor"
* code = $cs-loinc#58410-2 "Laboratory report"
* code.text = "Laborbefund"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* performer = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* effectiveDateTime = "2024-09-15T10:30:00+01:00"
* issued = "2024-09-15T11:00:00+01:00"
* specimen = Reference(Specimen/AT-APS-Specimen-Example01) "Blutprobe"
* result = Reference(Observation/AT-APS-Observation-Example01) "Hämoglobin"