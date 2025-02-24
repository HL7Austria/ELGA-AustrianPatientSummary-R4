Instance: tobacco-use-03
InstanceOf: AtApsObservationTobaccoUse
Description: "Social History - Raucher Beispiel"
Usage: #example
* status = #final
* id = "003"
* code = $loinc#72166-2 "Tobacco smoking status"
* subject = Reference(Patient/002) "Maria Musterfrau"
* performer = Reference(Patient/002) "Maria Musterfrau"
* effectiveDateTime = "2019-07-15"
* valueCodeableConcept = $sct-auszug#8517006 "Ex-smoker"