Instance: AtApsExampleObservation01
InstanceOf: AtApsObservation
Title: "AtApsObservation-Beispiel"
Description: "Observation"
Usage: #example
* status = #final
* category = $cs-observation-category#laboratory "Laboratory"
* code = $cs-loinc#718-7 "Hemoglobin"
* code.text = "Hämoglobin"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* effectiveDateTime = "2024-10-10T09:30:00+01:00"
* performer = Reference(Organization/AtApsExampleOrganization01) "Amadeus Spital"
* valueQuantity = 13.6 'g/dL' "g/dL"
* referenceRange.low = 12 'g/dL' "g/dL"
* referenceRange.high = 17.5 'g/dL' "g/dL"