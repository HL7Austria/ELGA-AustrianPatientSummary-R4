Instance: AtApsExampleObservationPregnancyOutcome01
InstanceOf: AtApsObservationPregnancyOutcome
Title: "AtApsObservationPregnancyOutcome-Beispiel"
Description: "Observation Pregnancy Outcome"
Usage: #example
* status = #final
* code = $cs-loinc#11636-8 "[#] Births.live"
* code.text = "Schwangerschaftsergebnis"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* effectiveDateTime = "2025-12-15T15:30:00+01:00"
* valueCodeableConcept = $cs-sct#281050002 "Lebendgeburt"
* valueCodeableConcept.text = "Lebendgeburt"
* component[0].code = $cs-loinc#8339-4 "Birth weight"
* component[=].code.text = "Geburtsgewicht"
* component[=].valueQuantity = 3450 'g' "g"
* component[+].code = $cs-loinc#56081-3 "Fetal gestational age in weeks --at most recent delivery"
* component[=].code.text = "Gestationsalter bei Geburt"
* component[=].valueQuantity = 39 'wk' "weeks"
* component[+].code = $cs-sct##364336006 "Geburtsmodus"
* component[=].code.text = "Entbindungsart"
* component[=].valueCodeableConcept = $cs-sct#200144004 "Geburt durch Schnittentbindung"
* component[=].valueCodeableConcept.text = "Sectio"
* performer = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"