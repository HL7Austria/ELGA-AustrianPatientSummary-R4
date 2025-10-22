Instance: AtApsExampleConsent01
InstanceOf: AtApsConsent
Title: "AtApsConsent-Beispiel"
Description: "Patientenverfügung"
Usage: #example
* status = #active
* category = $cs-loinc#59284-0 "Einwilligung - Dokument"
* scope = http://terminology.hl7.org/CodeSystem/consentscope#treatment "Treatment"
* patient = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* policyRule = http://terminology.hl7.org/CodeSystem/consentpolicycodes#cric "Common Rule Informed Consent"