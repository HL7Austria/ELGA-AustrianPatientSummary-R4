Instance: tobacco-use-example
InstanceOf: AtIpsObservationTobaccoUse
Description: "Social History - Raucher Beispiel"
Usage: #example
* status = #final
* code = $loinc#72166-2 "Tobacco smoking status"
* subject = Reference(patient-01)
* effectiveDateTime = "2019-07-15"
* valueCodeableConcept = $current-smoking-status#8517006 "Ex-smoker"