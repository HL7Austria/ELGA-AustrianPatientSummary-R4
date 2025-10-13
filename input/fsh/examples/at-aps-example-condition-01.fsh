Instance: AtApsExampleCondition01
InstanceOf: AtApsCondition
Title: "AtApsCondition-Beispiel"
Description: "Befund"
Usage: #example
* clinicalStatus = $cs-condition-clinical#active
* verificationStatus = $cs-condition-ver-status#confirmed
* category.coding[0] = $vs-elga-problemarten#404684003 "Befund"
* severity = $vs-elga-problemseverity#6736007 "mittel"
* code = https://fhir.hl7.at/CodeSystem/AT-APS-Problems#39065001 "Verbrennung des Ohrs"
* code.text = "Verbranntes Ohr"
* bodySite = $cs-sct#1910005 "Entire ear"
* bodySite.text = "Entire ear"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* onsetDateTime = "2025-05-24"