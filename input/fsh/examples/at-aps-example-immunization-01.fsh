Instance: AtApsExampleImmunization01
InstanceOf: AtApsImmunization
Title: "Immunization-Beispiel 1"
Description: "Impfung Diphtherie, Pertussis, Poliomyelitis und Tetanus"
Usage: #example
* contained = ExampleServiceRequest01
* status = #completed
* id = "at-aps-example-immunization-01"
* extension[ImmunizationBasedOnR5].valueReference = Reference(ExampleServiceRequest01)
* vaccineCode = $cs-eimpf-impfstoffe#2457324 "BOOSTRIX POLIO FSPR 0,5ML"
* vaccineCode.text = "Diphtherie-Pertussis-Poliomyelitis-Tetanus"
* patient = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* performer.actor = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"
* occurrenceDateTime = "2021-10-01"
//* primarySource = true
* route = $cs-medikationartanwendung#100000073600 "intramuskuläre Anwendung"
//* protocolApplied[0].series = "Standardimpfserie"
* protocolApplied[0].doseNumberPositiveInt = 1
* protocolApplied[0].targetDisease[0] = $cs-sct#397430003 "Diphtheria"
* protocolApplied[0].targetDisease[+] = $cs-sct#27836007 "Pertussis"
* protocolApplied[0].targetDisease[+] = $cs-sct#398102009 "Poliomyelitis"
* protocolApplied[0].targetDisease[+] = $cs-sct#76902006 "Tetanus"

Instance: ExampleServiceRequest01
InstanceOf: ServiceRequest
Usage: #inline
* status = #active
* intent = #order
* code = $cs-sct#390865008
* subject = Reference(Patient/at-aps-example-patient-01) "Max Mustermann"
* occurrenceDateTime = "2021-10-01"
* note.text = "Patient hat Angst vor Spritzen."
