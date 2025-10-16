Instance: AtApsExampleObservationPregnancyOutcome01
InstanceOf: AtApsObservationPregnancyOutcome
Title: "AtApsObservationPregnancyOutcome-Beispiel"
Description: "Observation Pregnancy Outcome"
Usage: #example
* status = #final
* code = $cs-loinc#57067-3 "Pregnancy Outcome"
* code.text = "Schwangerschaftsergebnis"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* effectiveDateTime = "2025-12-15T15:30:00+01:00"
* valueCodeableConcept = $cs-sct#169074005 "Live birth"
* valueCodeableConcept.text = "Lebendgeburt"
* component[0].code = $cs-loinc#8339-4 "Birth weight"
* component[=].code.text = "Geburtsgewicht"
* component[=].valueQuantity = 3450 'g' "g"
* component[+].code = $cs-loinc#8339-6 "Gestational age at delivery"
* component[=].code.text = "Gestationsalter bei Geburt"
* component[=].valueQuantity = 39 'wk' "weeks"
* component[+].code = $cs-sct#16322009 "Cesarean section"
* component[=].code.text = "Entbindungsart"
* component[=].valueCodeableConcept = $cs-sct#16322009 "Cesarean section"
* component[=].valueCodeableConcept.text = "Sectio"