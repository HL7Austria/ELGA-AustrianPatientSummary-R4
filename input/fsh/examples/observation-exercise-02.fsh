Instance: observation-exercise-02
InstanceOf: Observation
Description: "Patient Story - Workout Beispiel"
Usage: #example
* status = #final
* id = "002"
* code = $loinc#89555-7 "How many days per week did you engage in moderate to strenuous physical activity in the last 30 days"
* subject = Reference(Patient/002) "Maria Musterfrau"
* performer = Reference(Patient/002) "Maria Musterfrau"
* effectiveDateTime = "2024-12-02"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.value = 3
* valueQuantity.unit = "days per week"