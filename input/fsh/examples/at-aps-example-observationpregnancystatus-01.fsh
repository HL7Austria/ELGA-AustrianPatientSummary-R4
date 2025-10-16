Instance: AtApsExampleObservationPregnancyStatus01
InstanceOf: AtApsObservationPregnancyStatus
Title: "AtApsObservationPregnancyStatus-Beispiel"
Description: "Observation Pregnancy Status"
Usage: #example
* status = #final
* code = $cs-loinc#82810-3 "Pregnancy status"
* code.text = "Schwangerschaftsstatus"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* effectiveDateTime = "2025-05-01T10:00:00+01:00"
* valueCodeableConcept = $vs-elga-pregnancystatus#pregnant "Pregnant"
* valueCodeableConcept.text = "Schwanger"
* hasMember = Reference(Observation/AtApsExampleObservationPregnancyEdd01) "Expected Delivery Date"