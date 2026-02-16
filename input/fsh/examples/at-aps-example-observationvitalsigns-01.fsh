Instance: AtApsExampleObservationVitalSigns01
InstanceOf: AtApsObservationVitalSigns
Title: "AtApsObservationVitalSigns-Beispiel"
Description: "Observation Vital Signs"
Usage: #example
* status = #final
* category[VSCat] = $cs-observation-category#vital-signs
* code = $cs-loinc#8867-4 "Heart rate"
* code.text = "Vitalzeichen"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* effectiveDateTime = "2025-10-17T08:15:00+02:00"
* performer = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"
* valueQuantity = 72 '/min' "beats/min"