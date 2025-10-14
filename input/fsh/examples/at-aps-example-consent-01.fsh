Instance: AtApsExampleConsent01
InstanceOf: AtApsConsent
Title: "AtApsConsent-Beispiel"
Description: "Patientenverfügung"
Usage: #example
* status = #active
* category[0].coding[0].system = "http://hl7.org/fhir/ValueSet/consent-category"
* category[0].coding[0].code = #acd
* scope.coding[0].system = "http://hl7.org/fhir/ValueSet/consent-scope"
* scope.coding[0].code = #adr
* patient = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
