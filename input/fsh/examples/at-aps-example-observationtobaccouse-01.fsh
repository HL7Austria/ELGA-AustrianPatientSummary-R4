Instance: AtApsExampleObservationTobaccoUse01
InstanceOf: AtApsObservationTobaccoUse
Title: "Social History-Beispiel 2"
Description: "Ehemalig rauchende Person"
Usage: #example
* status = #final
* id = "at-aps-example-observationtobaccouse-01"
* code = $loinc#72166-2 "Raucherstatus"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* performer = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* effectiveDateTime = "2019-07-15"
* valueCodeableConcept = $sct#8517006 "Ehemalig rauchende Person"