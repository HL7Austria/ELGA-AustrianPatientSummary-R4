Instance: AtApsExampleObservationResultsLaboratoryPathology01
InstanceOf: AtApsObservationResultsLaboratoryPathology
Title: "AtApsObservationResultsLaboratoryPathology-Beispiel"
Description: "Observation Results Laboratory Pathology"
Usage: #example
* status = #final
* category[+] = $cs-observation-category#laboratory "Laboratory"
* category[+] = $cs-elga-laborparameterergaenzung#1 "Allgemeiner Laborbefund"
* code = $cs-elga-laborparameterergaenzung#17880 "Zytologie"
* code.text = "Pathologiebefund"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Mustermann"
* effectiveDateTime = "2025-06-20T14:00:00+02:00"
* performer = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* specimen = Reference(Specimen/AtApsExampleSpecimen01) "Gewebeprobe Tumorbiopsie"
* hasMember = Reference(Observation/AtApsExampleObservationResultsLaboratoryPathology01) "Subobservation 1"
* valueString = "Karzinom — maligne epitheliale Neoplasie"
* interpretation = $cs-v3-ObservationInterpretation#H "High"
* interpretation.text = "Pathologischer Befund"
* component[0].code = $cs-elga-laborparameterergaenzung#17881 "Histologischer Typ"
* component[=].code.text = "Histologischer Typ"
* component[=].valueCodeableConcept = $cs-sct#363406005 "Carcinoma"
* component[=].valueCodeableConcept.text = "Karzinom"
* component[=].interpretation = $cs-v3-ObservationInterpretation#H "High"
* component[=].interpretation.text = "Pathologisch relevant"