Instance: AtApsExampleObservationResultsRadiology01
InstanceOf: AtApsObservationResultsRadiology
Title: "AtApsObservationResultsRadiology-Beispiel"
Description: "Observation Results Radiology"
Usage: #example
* status = #final
* code = $cs-loinc#24627-2 "CT Chest"
* code.text = "CT Thorax"
* category[+] = $observation-category#imaging "Imaging"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* partOf = Reference(ImagingStudy/AtApsExampleImagingStudy01)
* effectiveDateTime = "2025-08-15T09:30:00+02:00"
* performer = Reference(Practitioner/HL7ATCorePractitionerExample01) "Dr. Melanie Musterärztin"
* valueString = "Keine pathologischen Befunde im Thoraxbereich. Lunge belüftet, keine Infiltrate."
* interpretation = $cs-v3-ObservationInterpretation#N "Normal"
* interpretation.text = "Normalbefund"
//* hasMember = Reference(Observation/AtApsExampleObservationResultsRadiology01) "Subobservation 1"
* component.code = $cs-loinc#18748-4 "Lung opacity"
* component.code.text = "Lungenbefund"
* component.valueCodeableConcept = $cs-sct#260373001 "No abnormality detected"
* component.valueCodeableConcept.text = "Keine Auffälligkeiten"
* component.interpretation = $cs-v3-ObservationInterpretation#N "Normal"
* component.interpretation.text = "Normalbefund"