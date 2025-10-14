Instance: AtApsExampleFlagAlert01
InstanceOf: AtApsFlagAlert
Title: "AtApsFlagAlert-Beispiel"
Description: "Flag Alert"
Usage: #example
* identifier.value = "12345"
* status = #inactive
* category = http://terminology.hl7.org/CodeSystem/flag-category#safety "Safety"
* category.text = "Sicherheit"
* code = http://example.org/local#bigdog "Großer Hund"
* code.text = "Der Patient hat einen großen Hund zu Hause. Tragen Sie immer eine Schutzausrüstung oder ergreifen Sie andere aktive Gegenmaßnahmen."
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* period.start = "2015-01-17"
* period.end = "2016-12-01"
* author = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"