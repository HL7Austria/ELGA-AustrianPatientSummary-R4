Alias: $loinc = http://loinc.org
Alias: $v2-0203 = http://terminology.hl7.org/CodeSystem/v2-0203
Alias: $v3-MaritalStatus = http://terminology.hl7.org/CodeSystem/v3-MaritalStatus
Alias: $condition-clinical = http://terminology.hl7.org/CodeSystem/condition-clinical
Alias: $absent-unknown-uv-ips = http://hl7.org/fhir/uv/ips/CodeSystem/absent-unknown-uv-ips
Alias: $allergyintolerance-clinical = http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical

Instance: APS-1-no-problems-medication-allergies
InstanceOf: AtIpsBundle
Usage: #example
* identifier.system = "http://system-to-be-defined.com"
* identifier.value = "63fef90a-be11-4ddf-aece-d77da15c4f20"
* type = #document
* timestamp = "2024-02-08T14:01:30+00:00"
* entry[0].fullUrl = "urn:uuid:212fdc76-ccc3-40bf-8cdd-82f2ef88bd7b"
* entry[=].resource = APS-1-no-problems-medication-allergies-composition
* entry[+].fullUrl = "urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8"
* entry[=].resource = APS-1-no-problems-medication-allergies-patient
* entry[+].fullUrl = "urn:uuid:75db30ee-7028-486c-929a-c5126837f472"
* entry[=].resource = APS-1-no-problems-medication-allergies-author
* entry[+].fullUrl = "urn:uuid:72e85b9d-004d-4104-b166-86d129948bae"
* entry[=].resource = APS-1-no-problems-medication-allergies-problem-1
* entry[+].fullUrl = "urn:uuid:acac4c94-a752-4cf5-9a6b-0d84237d5076"
* entry[=].resource = APS-1-no-problems-medication-allergies-medication-summary-1
* entry[+].fullUrl = "urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b"
* entry[=].resource = APS-1-no-problems-medication-allergies-allergy-1

Instance: APS-1-no-problems-medication-allergies-composition
InstanceOf: AtIpsComposition
Usage: #inline
// * language = #de-AT
* status = #preliminary
* type = $loinc#60591-5 "Patient summary Document"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)
* date = "2024-02-08T14:01:30+00:00"
* author = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472)
* title = "International Patient Summary"
* attester.mode = #personal
* attester.party = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)
* section[sectionMedications].title = "Medication Summary"
* section[sectionMedications].code = $loinc#10160-0 "History of Medication use Narrative"
* section[sectionMedications].text.status = #empty
* section[sectionMedications].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>narrative needs to be generated</p></div>"
* section[sectionMedications].entry = Reference(urn:uuid:acac4c94-a752-4cf5-9a6b-0d84237d5076)
* section[sectionAllergies].title = "Allergies and Intolerances"
* section[sectionAllergies].code = $loinc#48765-2 "Allergies and adverse reactions Document"
* section[sectionAllergies].text.status = #empty
* section[sectionAllergies].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>narrative needs to be generated</p></div>"
* section[sectionAllergies].entry = Reference(urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b)
* section[sectionProblems].title = "Problem List"
* section[sectionProblems].code = $loinc#11450-4 "Problem list - Reported"
* section[sectionProblems].text.status = #empty
* section[sectionProblems].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>narrative needs to be generated</p></div>"
* section[sectionProblems].entry = Reference(urn:uuid:72e85b9d-004d-4104-b166-86d129948bae)

Instance: APS-1-no-problems-medication-allergies-patient
InstanceOf: AtIpsPatient
Usage: #inline
* identifier.type = $v2-0203#SS "Social Security Number"
* identifier.system = "urn:oid:1.2.40.0.10.1.4.3.1"
* identifier.value = "1111241261"
* identifier.assigner.display = "Dachverband der österreichischen Sozialversicherungsträger"
* name.family = "Musterfrau"
* name.given[0] = "Maria"
* name.given[+] = "Johanna"
* name.prefix = "Dr."
* telecom[0].system = #phone
* telecom[=].value = "+43.2682.40400"
* telecom[=].use = #home
* telecom[+].system = #phone
* telecom[=].value = "+43.664.1234567"
* telecom[=].use = #mobile
* telecom[+].system = #email
* telecom[=].value = "musterfrau@provider.at"
* gender = #female // 1..1 in AT Core
* birthDate = "1961-12-24" // 1..1 in IPS
* address.line = "Musterstraße 13a"
* address.use = #home
* address.city = "Eisenstadt"
* address.state = "Burgenland"
* address.postalCode = "7000"
* address.country = "AUT"
* maritalStatus = $v3-MaritalStatus#M "Married"

Instance: APS-1-no-problems-medication-allergies-author
InstanceOf: Device
Usage: #inline
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>This Device generates an IPS FHIR Document from in production used ELGA CDA</p></div>"
* deviceName.name = "IPS Generator"
* deviceName.type = #user-friendly-name

Instance: APS-1-no-problems-medication-allergies-problem-1
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#inactive "Inactive"
* code = $absent-unknown-uv-ips#no-known-problems "No known problems"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)

Instance: APS-1-no-problems-medication-allergies-medication-summary-1
InstanceOf: AtIpsMedicationStatement
Usage: #inline
* status = #unknown
* medicationCodeableConcept = $absent-unknown-uv-ips#no-known-medications "No known medications"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)
* effectiveDateTime = "2024-02-08T10:31:58+02:00"

Instance: APS-1-no-problems-medication-allergies-allergy-1
InstanceOf: AtIpsAllergyIntolerance
Usage: #inline
* clinicalStatus = $allergyintolerance-clinical#inactive "Inactive"
* code = $absent-unknown-uv-ips#no-known-allergies "No known allergies"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)