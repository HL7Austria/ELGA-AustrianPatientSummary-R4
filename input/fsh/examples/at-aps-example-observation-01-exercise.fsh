Instance: AtApsExampleObservation01Exercise
InstanceOf: Observation
Title: "Patient Story-Beispiel"
Description: "Körperliche Aktivität"
Usage: #example
* status = #final
* id = "at-aps-example-observation-01-exercise"
* code = $cs-loinc#89555-7 "An wie vielen Tagen pro Woche haben Sie in den letzten 30 Tagen mäßige bis anstrengende körperliche Aktivitäten ausgeübt?"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* performer = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* effectiveDateTime = "2024-12-02"
* valueQuantity = 3 'd/wk' "Tage pro Woche"