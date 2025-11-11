Instance: AtApsExampleImmunization01
InstanceOf: AtApsImmunization
Title: "Immunization-Beispiel 1"
Description: "Impfung Diphtherie, Pertussis, Poliomyelitis und Tetanus"
Usage: #example
* status = #completed
* id = "at-aps-example-immunization-01"
//* vaccineCode.coding[0] = $vs-eimpf-impfstoffe#2457324 "BOOSTRIX POLIO FSPR 0,5ML"
* vaccineCode.coding = $vs-eimpf-impfstoffe#2457324 "BOOSTRIX POLIO FSPR 0,5ML"
* vaccineCode.text = "Diphtherie-Pertussis-Poliomyelitis-Tetanus"
* patient = Reference(Patient/at-aps-example-patient-01) "Maria Mustermann"
* performer.actor = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* vaccineCode = $vs-eimpf-impfstoffe#2457324 "BOOSTRIX POLIO FSPR 0,5ML"
* occurrenceDateTime = "2021-10-01"
//* primarySource = true
* route = $vs-eimpf-medikationartanwendung#IM "Intramuskulär"
//* protocolApplied[0].series = "Standardimpfserie"
* protocolApplied[0].doseNumberPositiveInt = 1
* protocolApplied[0].targetDisease[0] = $vs-eimpf-immunizationtarget#397430003 "Diphtheria"
* protocolApplied[0].targetDisease[+] = $vs-eimpf-immunizationtarget#27836007 "Pertussis"
* protocolApplied[0].targetDisease[+] = $vs-eimpf-immunizationtarget#398102009 "Poliomyelitis"
* protocolApplied[0].targetDisease[+] = $vs-eimpf-immunizationtarget#76902006 "Tetanus"