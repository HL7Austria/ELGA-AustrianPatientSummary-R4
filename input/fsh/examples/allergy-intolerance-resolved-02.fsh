Instance: allergy-intolerance-resolved
InstanceOf: AtApsAllergyIntolerance
Title: "AllergyIntolerance - Überwundene Allergie"
Usage: #example
* id = "002"
* extension.url = "http://hl7.org/fhir/StructureDefinition/allergyintolerance-abatement"
* extension.valueDateTime = "2020"
* clinicalStatus = $allergyintolerance-clinical#resolved
* verificationStatus = $allergyintolerance-verification#confirmed
* code = $sct-auszug#256303006 "Ambrosia-Pollen"
* patient = Reference(Patient/002) "Maria Musterfrau"
* onsetDateTime.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* onsetDateTime.extension.valueCode = #unknown