Alias: $elga-laborstruktur = https://termgit.elga.gv.at/CodeSystem/elga-laborstruktur
Alias: $v3-ObservationInterpretation = http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation

Instance: AtApsExampleObservationResultsLaboratoryPathology01
InstanceOf: AtApsObservationResultsLaboratoryPathology
Title: "AtApsObservationResultsLaboratoryPathology-Beispiel"
Description: "Observation Results Laboratory Pathology"
Usage: #example
* status = #final
* category = $cs-elga-laborparameterergaenzung#1 "Allgemeiner Laborbefund"
* code = $cs-loinc#88133-2 "Pathology report Narrative" //TODO
* code.text = "Pathologiebefund"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* effectiveDateTime = "2025-06-20T14:00:00+02:00"
* performer = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* specimen = Reference(Specimen/APS-Specimen-Example01) "Gewebeprobe Tumorbiopsie" //TODO
* hasMember = Reference(Observation/APS-Observation-LabPathology-SubExample01) "Subobservation 1" //TODO
* valueString = "Karzinom — maligne epitheliale Neoplasie"
* interpretation = $v3-ObservationInterpretation#H "High" //TODO
* interpretation.text = "Pathologischer Befund"
* component[0].code = $cs-loinc#33718-3 "Histologic type" //TODO
* component[=].code.text = "Histologischer Typ"
* component[=].valueCodeableConcept = $cs-sct#363406005 "Carcinoma"
* component[=].valueCodeableConcept.text = "Karzinom"
* component[=].interpretation = $v3-ObservationInterpretation#H "High"
* component[=].interpretation.text = "Pathologisch relevant"
* component[+].code = $cs-loinc#33719-1 "Tumor grade"
* component[=].code.text = "Tumorgrad"
* component[=].valueCodeableConcept = $cs-sct#255604002 "Grade 2"
* component[=].valueCodeableConcept.text = "Grad 2"
* component[=].interpretation = $v3-ObservationInterpretation#N "Normal"
* component[=].interpretation.text = "Normbereich"
* component[+].code = $cs-loinc#33720-9 "Invasion depth"
* component[=].code.text = "Invasionstiefe"
* component[=].valueQuantity = 4.5 'mm' "mm"
* component[=].interpretation = $v3-ObservationInterpretation#H "High"
* component[=].interpretation.text = "Erhöhte Invasionstiefe"