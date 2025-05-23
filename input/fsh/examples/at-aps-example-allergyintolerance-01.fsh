Instance: AtApsExampleAllergyIntolerance01
InstanceOf: AtApsAllergyIntolerance
Title: "AtApsAllergyIntolerance-Beispiel"
Description: "Überwundene Allergie"
Usage: #example
* id = "at-aps-example-allergyintolerance-01"
* extension.url = "http://hl7.org/fhir/StructureDefinition/allergyintolerance-abatement"
* extension.valueDateTime = "2020"
* clinicalStatus = $cs-allergyintolerance-clinical#resolved
* verificationStatus = $cs-allergyintolerance-verification#confirmed
* code = $cs-sct#256303006 "Ambrosiapollen"
* patient = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* onsetDateTime.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* onsetDateTime.extension.valueCode = #unknown