Instance: AtApsExampleObservationPregnancyEdd01
InstanceOf: AtApsObservationPregnancyEdd
Title: "AtApsObservationPregnancyEdd-Beispiel"
Description: "Observation Pregnancy Expected Delivery Date"
Usage: #example
* status = #final
* code = $cs-loinc#11778-8 "Delivery date Estimated"
* code.text = "Voraussichtlicher Entbindungstermin"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* effectiveDateTime = "2025-05-10"
* valueDateTime = "2025-12-15"
* performer = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"