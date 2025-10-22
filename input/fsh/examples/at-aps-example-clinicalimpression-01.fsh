Instance: AtApsExampleClinicalImpression01
InstanceOf: AtApsClinicalImpression
Title: "AtApsClinicalImpression-Beispiel"
Description: "Clinical Impression"
Usage: #example
* identifier.value = "12345"
* status = #completed
* description = "Dieser 26-jährige männliche Patient wird nach einem Verkehrsunfall mit dem Krankenwagen in die Notaufnahme gebracht."
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* effectivePeriod.start = "2014-12-06T20:00:00+11:00"
* effectivePeriod.end = "2014-12-06T22:33:00+11:00"
* date = "2014-12-06T22:33:00+11:00"
* assessor = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* problem.display = "MVA"
* investigation.code.text = "Erstuntersuchung"
* investigation.item[0].display = "tiefe Platzwunde an der Kopfhaut"
* investigation.item[+].display = "verminderte Bewusstseinslage"
* investigation.item[+].display = "zeitlich und örtlich desorientiert"
* investigation.item[+].display = "unruhig"
* summary = "Vorläufige Diagnosen: Kopfverletzung und traumatische Hirnverletzung"