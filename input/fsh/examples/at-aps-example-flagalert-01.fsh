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
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* author = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"