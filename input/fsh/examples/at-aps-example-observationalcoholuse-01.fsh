Instance: AtApsExampleObservationAlcoholUse01
InstanceOf: AtApsObservationAlcoholUse
Title: "Social History-Beispiel 1"
Description: "Alkoholkonsum"
Usage: #example
* status = #final
* id = "at-aps-example-observationalcoholuse-01"
* code = $cs-loinc#74013-4 "Alkoholische Getränke pro Tag"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* performer = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* effectiveDateTime = "2024-09-20"
* valueQuantity = 2 '/d' "Weingläser pro Tag"