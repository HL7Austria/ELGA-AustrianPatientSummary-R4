Instance: AtApsExampleObservationTobaccoUse01
InstanceOf: AtApsObservationTobaccoUse
Title: "Social History-Beispiel 2"
Description: "Ehemalig rauchende Person"
Usage: #example
* status = #final
* id = "at-aps-example-observationtobaccouse-01"
* code = $cs-loinc#72166-2 "Raucherstatus"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Mustermann"
* performer = Reference(Patient/at-aps-example-patient-01) "Maria Mustermann"
* effectiveDateTime = "2019-07-15"
* valueCodeableConcept = $cs-sct#8517006 "Ehemalig rauchende Person"