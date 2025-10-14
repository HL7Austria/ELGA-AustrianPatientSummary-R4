Alias: $classCodes = http://ihe.net/xds/connectathon/classCodes
Alias: $v3-Confidentiality = http://terminology.hl7.org/CodeSystem/v3-Confidentiality
Alias: $eventCodes = http://ihe.net/xds/connectathon/eventCodes
Alias: $healthcareFacilityTypeCodes = http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes
Alias: $practiceSettingCodes = http://www.ihe.net/xds/connectathon/practiceSettingCodes

Instance: AtApsExampleDocumentReference01
InstanceOf: AtApsDocumentReference
Title: "AtApsDocumentReference-Beispiel"
Description: "Document Reference"
Usage: #example
* masterIdentifier.system = "urn:ietf:rfc:3986"
* masterIdentifier.value = "urn:oid:1.3.6.1.4.1.21367.2005.3.7"
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
* status = #current
* docStatus = #preliminary
* type = $cs-loinc#34108-1 "Outpatient Note"
* category = $classCodes#"History and Physical" "History and Physical"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* date = "2005-12-24T09:43:41+11:00"
* author[0] = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* authenticator = Reference(Organization/f001)
* custodian = Reference(Organization/f001)
* description = "Physical"
* securityLabel = $v3-Confidentiality#V "very restricted"
* content.attachment.contentType = #application/hl7-v3+xml
* content.attachment.language = #en-US
* content.attachment.url = "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510"
* content.attachment.size = 3654
* content.attachment.hash = "2jmj7l5rSw0yVb/vlWAYkK/YBwk="
* content.attachment.title = "Physical"
* content.attachment.creation = "2005-12-24T09:35:00+11:00"
* content.format = urn:oid:1.3.6.1.4.1.19376.1.2.3#urn:ihe:pcc:handp:2008 "History and Physical Specification"
* context.encounter = Reference(Encounter/xcda)
* context.event = $eventCodes#T-D8200 "Arm"
* context.period.start = "2004-12-23T08:00:00+11:00"
* context.period.end = "2004-12-23T08:01:00+11:00"
* context.facilityType = $healthcareFacilityTypeCodes#Outpatient "Outpatient"
* context.practiceSetting = $practiceSettingCodes#"General Medicine" "General Medicine"
* context.sourcePatientInfo = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* context.related = Reference(Patient/xcda)
* context.related.identifier.system = "urn:ietf:rfc:3986"
* context.related.identifier.value = "urn:oid:1.3.6.1.4.1.21367.2005.3.7.2345"