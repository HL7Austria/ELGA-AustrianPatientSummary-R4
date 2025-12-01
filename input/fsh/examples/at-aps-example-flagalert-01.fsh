Instance: AtApsExampleFlagAlert01
InstanceOf: AtApsFlagAlert
Title: "AtApsFlagAlert-Beispiel"
Description: "Flag Alert"
Usage: #example
* identifier.value = "12345"
* status = #active
* category = http://terminology.hl7.org/CodeSystem/flag-category#safety "Safety"
* category.text = "Sicherheit"
* code = $cs-sct#165002 "Accident-prone"
* code.text = "Der Patient zeigt eine erhöhte Sturzgefährdung."
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* author = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"