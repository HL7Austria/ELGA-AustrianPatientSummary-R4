Instance: AtApsExampleImmunizationRecommendation01
InstanceOf: AtApsImmunizationRecommendation
Title: "ImmunizationRecommendation-Beispiel 1"
Description: "Impfung Diphtherie, Pertussis, Poliomyelitis und Tetanus"
Usage: #example
* patient = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* date = "2026-10-10"
* recommendation
  * forecastStatus = $cs-sct#723620004
  * vaccineCode = $cs-eimpf-impfstoffe#2457324 "BOOSTRIX POLIO FSPR 0,5ML"
