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
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* date = "2005-12-24T09:43:41+11:00"
* author[0] = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"
* authenticator = Reference(Organization/AtApsExampleOrganization01)
* custodian = Reference(Organization/AtApsExampleOrganization01)
* description = "Körperliche Untersuchung"
* securityLabel = $cs-v3-Confidentiality#V "very restricted"
* content.attachment.contentType = #application/hl7-v3+xml
* content.attachment.language = #de-DE
* content.attachment.url = "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510"
* content.attachment.size = 3654
* content.attachment.hash = "2jmj7l5rSw0yVb/vlWAYkK/YBwk="
* content.attachment.title = "Körperliche Untersuchung"
* content.attachment.creation = "2005-12-24T09:35:00+11:00"