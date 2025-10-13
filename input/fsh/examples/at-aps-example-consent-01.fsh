Instance: AtApsExampleConsent01
InstanceOf: AtApsConsent
Title: "AtApsConsent-Beispiel"
Description: "Patientenverfügung"
Usage: #example
* meta.profile = "http://fhir.hl7.at/r4-ELGA-AustrianPatientSummary-ballot_2025_stu1/StructureDefinition/at-aps-consent"
* status = #active
* category[0].coding[0].system = "http://hl7.org/fhir/ValueSet/consent-category"
* category[0].coding[0].code = #acd
* scope.coding[0].system = "http://hl7.org/fhir/ValueSet/consent-scope"
* scope.coding[0].code = #adr
* patient = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
