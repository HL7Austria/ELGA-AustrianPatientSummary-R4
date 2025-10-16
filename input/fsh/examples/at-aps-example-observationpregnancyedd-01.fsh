Instance: AtApsExampleObservationPregnancyEdd01
InstanceOf: AtApsObservationPregnancyEdd
Title: "AtApsObservationPregnancyEdd-Beispiel"
Description: "Observation Pregnancy Expected Delivery Date"
Usage: #example
* status = #final
* code = $cs-loinc#57067-3 "Estimated delivery date"
* code.text = "Voraussichtlicher Entbindungstermin"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* effectiveDateTime = "2025-05-10"
* valueDateTime = "2025-12-15"