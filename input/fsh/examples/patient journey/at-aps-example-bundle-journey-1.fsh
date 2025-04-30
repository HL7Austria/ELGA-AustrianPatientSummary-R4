Instance: AtApsExampleBundle-Journey-1
InstanceOf: AtApsBundle
Description: "APS Patient Journey-1"
Usage: #example
* identifier.system = "http://system-to-be-defined.com"
* identifier.value = "63fef90a-be11-4ddf-aece-d77da15c4f21"
* type = #document
* timestamp = "2024-02-08T14:01:30+00:00"
* entry[0].fullUrl = "urn:uuid:212fdc76-ccc3-40bf-8cdd-82f2ef88bd7b"
* entry[=].resource = AtApsExampleBundle-Journey-1-composition 
* entry[+].fullUrl = "urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8"
* entry[=].resource = AtApsExampleBundle-Journey-1-patient
* entry[+].fullUrl = "urn:uuid:75db30ee-7028-486c-929a-c5126837f472"
* entry[=].resource = AtApsExampleBundle-Journey-1-author-device
* entry[+].fullUrl = "urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6"
* entry[=].resource = AtApsExampleBundle-Journey-1-custodian
// Problem List
* entry[+].fullUrl = "urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde"
* entry[=].resource = AtApsExampleBundle-Journey-1-problem-5
// Problem List - Family history
* entry[+].fullUrl = "urn:uuid:3f3140b1-9478-4491-b7bf-10560f38da0e"
* entry[=].resource = AtApsExampleBundle-Journey-1-problem-13
* entry[+].fullUrl = "urn:uuid:entlassungsbrief-2023-12"
* entry[=].resource = Entlassungsbrief-2023-12

// Medication Summary
* entry[+].fullUrl = "urn:uuid:ecf9728f-fa50-4b46-b8f7-7768174df72a"
* entry[=].resource = AtApsExampleBundle-Journey-1-medication-summary-7
// Allergies and Intolerances
* entry[+].fullUrl = "urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b"
* entry[=].resource = AtApsExampleBundle-Journey-1-allergy-1
// History of Procedures
* entry[+].fullUrl = "urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a"
* entry[=].resource = AtApsExampleBundle-Journey-1-procedure-history-1
* entry[+].fullUrl = "urn:uuid:8103f99c-64f0-4dd5-b92e-5c9680c91e47"
* entry[=].resource = AtApsExampleBundle-Journey-1-procedure-history-2
* entry[+].fullUrl = "urn:uuid:8a825f17-1599-4928-b384-0ca4a62daba8"
* entry[=].resource = AtApsExampleBundle-Journey-1-procedure-history-3
// Specimen for Diagnostic Results
// Diagnostic Results
// Vital Signs
// Past History of Illness
* entry[+].fullUrl = "urn:uuid:ce2589a2-a5e5-4520-808f-8118e2863a95"
* entry[=].resource = AtApsExampleBundle-Journey-1-illness-history-2
// Social History
// Medical Devices
* entry[+].fullUrl = "urn:uuid:490dab5c-271e-4736-8a6b-d04fd2a04606"
* entry[=].resource = AtApsExampleBundle-Journey-1-deviceUse-Hueftprothese
* entry[+].fullUrl = "urn:uuid:a1a80313-a757-4062-b0d7-d04fd2a04603"
* entry[=].resource = AtApsExampleBundle-Journey-1-device-Hueftprothese

Instance: AtApsExampleBundle-Journey-1-composition
InstanceOf: AtApsComposition
Usage: #inline
// * language = #de-AT
* status = #final
* type = $cs-loinc#60591-5 "Patient summary"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* date = "2024-02-08T14:01:30+00:00"
* author = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "APS Generator"
* title = "APS - Patient Journey 1"
* custodian = Reference(urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6) "Muster-Organisation"
* extension[countryOfAffiliation].valueString = "AT"

// Problem List
* section[sectionProblems].title = "Gesundheitsprobleme und Risiken"
* section[sectionProblems].code = $cs-loinc#11450-4 "Problemliste"
* section[sectionProblems].text.status = #empty
* section[sectionProblems].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionProblems].entry[+] = Reference(urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde) "Arterielle Hypertonie (AtApsExampleBundle-Journey-1-problem-5)"
// Problem List - Family history
* section[sectionProblems].entry[+] = Reference(urn:uuid:3f3140b1-9478-4491-b7bf-10560f38da0e) "Diabetes mellitus in der Familienanamnese (AtApsExampleBundle-Journey-1-problem-13)"

// Medication Summary
* section[sectionMedications].title = "Medikationsliste"
* section[sectionMedications].code = $cs-loinc#10160-0 "Medikationsanamnese"
* section[sectionMedications].text.status = #empty
* section[sectionMedications].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionMedications].entry[+] = Reference(urn:uuid:ecf9728f-fa50-4b46-b8f7-7768174df72a) "RAMIPRIL 1A TBL  5MG (AtApsExampleBundle-Journey-1-medication-summary-7)"

// Allergies and Intolerances
* section[sectionAllergies].title = "Allergien und Intoleranzen"
* section[sectionAllergies].code = $cs-loinc#48765-2 "Allergien und unerwünschte Wirkungen"
* section[sectionAllergies].text.status = #empty
* section[sectionAllergies].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionAllergies].entry = Reference(urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b) "AtApsExampleBundle-Journey-1-allergy-1"

// History of Procedures
* section[sectionProceduresHx].title = "Eingriffe und Therapien"
* section[sectionProceduresHx].code = $cs-loinc#47519-4 "Anamnese der Prozeduren oder Maßnahmen"
* section[sectionProceduresHx].text.status = #empty
* section[sectionProceduresHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionProceduresHx].entry[+] = Reference(urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a) "Totalersatz des linken Hüftgelenks (AtApsExampleBundle-Journey-1-procedure-history-1)"
* section[sectionProceduresHx].entry[+] = Reference(urn:uuid:8103f99c-64f0-4dd5-b92e-5c9680c91e47) "Appendektomie (AtApsExampleBundle-Journey-1-procedure-history-2)"
* section[sectionProceduresHx].entry[+] = Reference(urn:uuid:8a825f17-1599-4928-b384-0ca4a62daba8) "Koloskopie (AtApsExampleBundle-Journey-1-procedure-history-3)"


// Medical Devices
* section[sectionMedicalDevices].title = "Implantate, medizinische Geräte und Heilbehelfe"
* section[sectionMedicalDevices].code = $cs-loinc#46264-8 "Anamnese zum Einsatz von Medizinprodukten"
* section[sectionMedicalDevices].text.status = #empty
* section[sectionMedicalDevices].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionMedicalDevices].entry = Reference(urn:uuid:490dab5c-271e-4736-8a6b-d04fd2a04606) "Hüftprothese"

// Diagnostic Results 
* section[sectionResults].title = "Diagnostische Resultate"
* section[sectionResults].code = $cs-loinc#30954-2 "Relevante diagnostische Tests oder Labordaten"
* section[sectionResults].text.status = #empty
* section[sectionResults].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionResults].emptyReason[+] = $cs-list-empty-reason#nilknown

// Vital Signs - noch keine Einträge vorhanden

// Past History of Illness 
* section[sectionPastIllnessHx].title = "Vergangene Gesundheitsprobleme und Risiken"
* section[sectionPastIllnessHx].code = $cs-loinc#11348-0 "Anamnese früherer Krankheiten"
* section[sectionPastIllnessHx].text.status = #empty
* section[sectionPastIllnessHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionPastIllnessHx].entry[+] = Reference(urn:uuid:ce2589a2-a5e5-4520-808f-8118e2863a95) "Zustand nach Windpocken (AtApsExampleBundle-Journey-1-illness-history-2)"

// Social History - noch keine Einträge vorhanden

Instance: AtApsExampleBundle-Journey-1-patient
InstanceOf: AtApsPatient
Usage: #inline
* identifier[socialSecurityNumber].type = $cs-v2-0203#SS "Social Security number"
* identifier[socialSecurityNumber].system = "urn:oid:1.2.40.0.10.1.4.3.1"
* identifier[socialSecurityNumber].value = "0000121150"
* identifier[socialSecurityNumber].assigner.display = "Dachverband der österreichischen Sozialversicherungsträger"
* identifier[localPatientId].type = $cs-v2-0203#PI "Patient internal identifier"
* identifier[localPatientId].system = "urn:oid:1.2.3.4.5"
* identifier[localPatientId].value = "0002"
* identifier[localPatientId].assigner.display = "Ein GDA in Österreich"
* name.family = "Musterfrau"
* name.given[0] = "Maria"
* gender = #female
* birthDate = "1998-04-17"
* address.line = "Am Schulweg 5"
* address.use = #home
* address.city = "Hainfeld"
* address.postalCode = "3100"
* address.country = "AUT"

Instance: AtApsExampleBundle-Journey-1-practitioner
InstanceOf: AtApsPractitioner
Usage: #inline
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:oid:1.2.40.0.10.99.1.2.3.4"
* identifier.assigner.display = "Bundesministerium für Gesundheit"
* name.prefix[0] = "Dr."
* name.family = "Hausärztin"
* name.given[0] = "Hanna"

// Problem List

Instance: AtApsExampleBundle-Journey-1-problem-5
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#38341003 "Arterielle Hypertonie"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* onsetDateTime = "2023-12-08T10:31:58+02:00"
//* evidence.detail[0] = Reference(DocumentReference/Entlassungsbrief-2023-12) "Entlassungsbrief AKH Amadeus"
* evidence.detail[0] = Reference(urn:uuid:entlassungsbrief-2023-12) "Entlassungsbrief AKH Amadeus"

// DocumentReference: source document
Instance: Entlassungsbrief-2023-12
InstanceOf: DocumentReference
Usage: #inline
* status = #current
* type = $cs-loinc#11490-0 "Entlassungsbrief"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* date = "2023-12-08T10:00:00+02:00"
* content.attachment.url = "https://example.org/fhir/Binary/entlassungsbrief-2023-12.pdf"
* content.attachment.contentType = #application/pdf
* content.attachment.title = "Entlassungsbrief AKH Amadeus"

// Provenance 
Instance: AtApsExampleBundle-Journey-1-provenance-1
InstanceOf: Provenance
Usage: #inline
* target[0] = Reference(urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde) "Target: AtApsExampleBundle-Journey-1-problem-5 (Arterielle Hypertonie)"
* recorded = "2023-12-08T11:00:00+02:00"
* entity[0].role = #source
* entity[0].what = Reference(urn:uuid:entlassungsbrief-2023-12) "Dokument: Entlassungsbrief AKH Amadeus"
* agent[0].who.display = "AKH Amadeus - Entlassungsmanagement"



// Problem List - Family history

Instance: AtApsExampleBundle-Journey-1-problem-13
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#160303001 "Diabetes mellitus in der Familienanamnese"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"

// Medication Summary

Instance: AtApsExampleBundle-Journey-1-medication-summary-7
InstanceOf: AtApsMedicationStatement
Usage: #inline
* status = #active
* medicationCodeableConcept = $cs-asp-liste#2450888 "RAMIPRIL 1A TBL  5MG"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectivePeriod.start = "2023-12-08T10:31:58+02:00"
* dosage.text = "S:1-0-0-0"

// Allergies and Intolerances

Instance: AtApsExampleBundle-Journey-1-allergy-1
InstanceOf: AtApsAllergyIntolerance
Usage: #inline
* clinicalStatus = $cs-allergyintolerance-clinical#active "Active"
* code = $cs-sct#128488006 "Hausstaub"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"

// History of Procedures

Instance: AtApsExampleBundle-Journey-1-procedure-history-1
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#770606008 "Totalersatz des linken Hüftgelenks"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performedDateTime = "2010"

Instance: AtApsExampleBundle-Journey-1-procedure-history-2
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#80146002 "Appendektomie"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performedDateTime = "2001-06-15"

Instance: AtApsExampleBundle-Journey-1-procedure-history-3
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#73761001 "Koloskopie"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// within the last 10 years
* performedDateTime = "2014-05-17"

// Diagnostic Results 

// Vital Signs

// Past History of Illness

Instance: AtApsExampleBundle-Journey-1-illness-history-1
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#resolved "Resolved"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#14189004 "Masern"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* onsetDateTime = "1994-02-08"

Instance: AtApsExampleBundle-Journey-1-illness-history-2
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#resolved "Resolved"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#38907003 "Windpocken"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* onsetDateTime = "1991"

// Social History

Instance: AtApsExampleBundle-Journey-1-deviceUse-Hueftprothese 
InstanceOf: AtApsDeviceUseStatement
Usage: #inline
* status = #active
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* device = Reference(urn:uuid:a1a80313-a757-4062-b0d7-d04fd2a04603) "Hüftprothese"
* device.display = "Verwendetes Gerät: Hüftprothese"
* timingDateTime.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* timingDateTime.extension.valueCode = #unknown
* bodySite = $cs-sct#362905007 "Gesamtes linkes Hüftgelenk"
* bodySite.coding[0].display = "Gesamtes linkes Hüftgelenk"

Instance: AtApsExampleBundle-Journey-1-device-Hueftprothese
InstanceOf: AtApsDevice
Usage: #inline
* type = $cs-sct#67270000 "Hüftprothese"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* deviceName.name = "Hüftprothese"
* deviceName.type = #other
* version.value = "123456"


Instance: AtApsExampleBundle-Journey-1-author-device
InstanceOf: Device
Usage: #inline
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* type = $cs-sct#49062001 "Gerät"
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Dieses Gerät erzeugt ein APS FHIR-Dokument.</p></div>"
* deviceName.name = "APS Generator"
* deviceName.type = #user-friendly-name

Instance: AtApsExampleBundle-Journey-1-custodian
InstanceOf: AtApsOrganization
Usage: #inline
* name = "Muster-Organization"
