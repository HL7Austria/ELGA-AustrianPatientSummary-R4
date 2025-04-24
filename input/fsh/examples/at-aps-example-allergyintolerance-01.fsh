Instance: AtApsExampleAllergyIntolerance01
InstanceOf: AtApsAllergyIntolerance
Title: "AtApsAllergyIntolerance-Beispiel"
Description: "Überwundene Allergie"
Usage: #example
* id = "at-aps-example-allergyintolerance-01"
* extension.url = "http://hl7.org/fhir/StructureDefinition/allergyintolerance-abatement"
* extension.valueDateTime = "2020"
* clinicalStatus = $allergyintolerance-clinical#resolved
* verificationStatus = $allergyintolerance-verification#confirmed
* code = $sct#256303006 "Ambrosiapollen"
* patient = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* onsetDateTime.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* onsetDateTime.extension.valueCode = #unknown