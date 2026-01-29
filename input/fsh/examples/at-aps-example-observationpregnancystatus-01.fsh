Instance: AtApsExampleObservationPregnancyStatus01
InstanceOf: AtApsObservationPregnancyStatus
Title: "AtApsObservationPregnancyStatus-Beispiel"
Description: "Observation Pregnancy Status"
Usage: #example
* status = #final
* code = $cs-loinc#82810-3 "Pregnancy status"
* code.text = "Schwangerschaftsstatus"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* effectiveDateTime = "2025-05-01T10:00:00+01:00"
* valueCodeableConcept = $cs-loinc#LA15173-0 "Pregnant"
* valueCodeableConcept.text = "Schwanger"
* hasMember = Reference(Observation/AtApsExampleObservationPregnancyEdd01) "Expected Delivery Date"
* performer = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"