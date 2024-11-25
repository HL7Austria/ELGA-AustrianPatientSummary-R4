Instance: APS-1-no-problems-medication-allergies
InstanceOf: AtIpsBundle
Description: "APS with no problems, medication or allergies"
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
* entry[+].fullUrl = "urn:uuid:6bcdcc96-1443-48bd-ab41-7692dc1baecd"
* entry[=].resource = APS-1-organization
* entry[+].fullUrl = "urn:uuid:27ef5ea9-5c9f-418d-9830-648d15ee2094"
* entry[=].resource = APS-1-no-problems-procedure-1
* entry[+].fullUrl = "urn:uuid:490dab5c-271e-4736-8a6b-5f6f089d0a05"
* entry[=].resource = APS-1-no-problems-device-use-1
* entry[+].fullUrl = "urn:uuid:9faadcc1-076d-4bb4-b818-96239e2b8bc8"
* entry[=].resource = APS-1-no-problems-device-1

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
* custodian = Reference(urn:uuid:6bcdcc96-1443-48bd-ab41-7692dc1baecd)
* attester.mode = #personal
* attester.party = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)
* extension[countryOfAffiliation].valueString = "AT"
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
* section[sectionProceduresHx].title = "History of Procedures"
* section[sectionProceduresHx].code = $loinc#47519-4
* section[sectionProceduresHx].text.status = #empty
* section[sectionProceduresHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>narrative needs to be generated</p></div>"
* section[sectionProceduresHx].entry = Reference(urn:uuid:27ef5ea9-5c9f-418d-9830-648d15ee2094)
* section[sectionMedicalDevices].title = "Medical Devices"
* section[sectionMedicalDevices].code = $loinc#46264-8 "History of medical device use"
* section[sectionMedicalDevices].text.status = #empty
* section[sectionMedicalDevices].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>narrative needs to be generated</p></div>"
* section[sectionMedicalDevices].entry = Reference(urn:uuid:490dab5c-271e-4736-8a6b-5f6f089d0a05)

Instance: APS-1-no-problems-medication-allergies-patient
InstanceOf: AtIpsPatient
Usage: #inline
* identifier[socialSecurityNumber].type = $v2-0203#SS "Social Security number"
* identifier[socialSecurityNumber].system = "urn:oid:1.2.40.0.10.1.4.3.1"
* identifier[socialSecurityNumber].value = "1111241261"
* identifier[socialSecurityNumber].assigner.display = "Dachverband der österreichischen Sozialversicherungsträger"
* identifier[localPatientId].type = $v2-0203#PI "Patient internal identifier"
* identifier[localPatientId].system = "urn:oid:1.2.3.4.5"
* identifier[localPatientId].value = "0001"
* identifier[localPatientId].assigner.display = "Ein GDA in Österreich"
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
* code = $sct#373572006  "Clinical finding absent (situation)"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)

Instance: APS-1-no-problems-medication-allergies-medication-summary-1
InstanceOf: AtIpsMedicationStatement
Usage: #inline
* status = #unknown
* medicationCodeableConcept = $sct#787481004 "No known medications (situation)"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)
* effectiveDateTime = "2024-02-08T10:31:58+02:00"

Instance: APS-1-no-problems-medication-allergies-allergy-1
InstanceOf: AtIpsAllergyIntolerance
Usage: #inline
* clinicalStatus = $allergyintolerance-clinical#active "Active"
* code = $sct#716186003 "No known allergy (situation)"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)

Instance: APS-1-no-problems-procedure-1
InstanceOf: AtIpsProcedure
Usage: #inline
* status = #unknown
* code = $sct#787480003 "No known procedures (situation)"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)
* performedDateTime.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* performedDateTime.extension.valueCode = #unknown

Instance: APS-1-no-problems-device-use-1
InstanceOf: AtIpsDeviceUseStatement
Usage: #inline
* status = #active
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)
* device = Reference(urn:uuid:9faadcc1-076d-4bb4-b818-96239e2b8bc8)
* timingDateTime.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* timingDateTime.extension.valueCode = #unknown

Instance: APS-1-no-problems-device-1
InstanceOf: AtIpsDevice
Usage: #inline
* type = $sct#787483001 "No known device use (situation)"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8)

Instance: APS-1-organization
InstanceOf: AtIpsOrganization
Usage: #inline
* name = "MusterOrganization"