Instance: AtApsExampleObservationPregnancyOutcome01
InstanceOf: AtApsObservationPregnancyOutcome
Title: "AtApsObservationPregnancyOutcome-Beispiel"
Description: "Observation Pregnancy Outcome"
Usage: #example
* status = #final
* code = $cs-loinc#11636-8
* code.text = "Schwangerschaftsergebnis"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Mustermann"
* effectiveDateTime = "2025-12-15T15:30:00+01:00"
* valueCodeableConcept = $cs-sct#281050002 "Lebendgeburt"
* valueCodeableConcept.text = "Lebendgeburt"
* performer = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* text.div = "<div xmlns='http://www.w3.org/1999/xhtml'>Lebendgeburt, 39. SSW, 3450 g, Sectio</div>"
* text.status = #generated