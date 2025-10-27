Instance: AtApsExampleAllergyIntolerance01
InstanceOf: AtApsAllergyIntolerance
Title: "AtApsAllergyIntolerance-Beispiel"
Description: "Überwundene Allergie"
Usage: #example
* id = "at-aps-example-allergyintolerance-01"
* clinicalStatus = $cs-allergyintolerance-clinical#resolved
* verificationStatus = $cs-allergyintolerance-verification#confirmed
* code = $cs-sct#256303006 "Ambrosiapollen"
* patient = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* onsetDateTime.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* onsetDateTime.extension.valueCode = #unknown