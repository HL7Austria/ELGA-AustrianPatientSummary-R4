Instance: AtApsExampleBundle-Journey-2
InstanceOf: AtApsBundle
Description: "APS Patient Journey-2"
Usage: #example
* identifier.system = "http://system-to-be-defined.com"
* identifier.value = "63fef90a-be11-4ddf-aece-d77da15c4f22"
* type = #document
* timestamp = "2025-02-08T14:31:30+00:00"
* entry[0].fullUrl = "urn:uuid:212fdc76-ccc3-40bf-8cdd-82f2ef88bd7b"
* entry[=].resource = AtApsExampleBundle-Journey-2-composition
* entry[+].fullUrl = "urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8"
* entry[=].resource = AtApsExampleBundle-Journey-2-patient
* entry[+].fullUrl = "urn:uuid:75db30ee-7028-486c-929a-c5126837f472"
* entry[=].resource = AtApsExampleBundle-Journey-2-author-device
* entry[+].fullUrl = "urn:uuid:75db30ee-7028-486c-929a-c5126837f473"
* entry[=].resource = AtApsExampleBundle-Journey-2-practitioner
* entry[+].fullUrl = "urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6"
* entry[=].resource = AtApsExampleBundle-Journey-2-custodian

// Medikationsliste (Medication Summary)
* entry[+].fullUrl = "urn:uuid:ecf9728f-fa50-4b46-b8f7-7768174df72a"
* entry[=].resource = AtApsExampleBundle-Journey-2-medication-summary-7

// Allergien und Intoleranzen (Allergies and Intolerances)
* entry[+].fullUrl = "urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b"
* entry[=].resource = AtApsExampleBundle-Journey-2-allergy-1

// Gesundheitsprobleme und Risiken (Problems)
// Problems
* entry[+].fullUrl = "urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde"
* entry[=].resource = AtApsExampleBundle-Journey-2-problem-5
// Problem List - periodontal disease risk
* entry[+].fullUrl = "urn:uuid:fa46fccb-5c24-4a40-a478-d6da4902ff33"
* entry[=].resource = AtApsExampleBundle-Journey-2-problem-17
* entry[+].fullUrl = "urn:uuid:f235c566-01aa-457d-ab49-9e422df69863"
* entry[=].resource = AtApsExampleBundle-Journey-2-problem-17-assessment-1 //21
// Family history
* entry[+].fullUrl = "urn:uuid:3f3140b1-9478-4491-b7bf-10560f38da0e"
* entry[=].resource = AtApsExampleBundle-Journey-2-problem-13
* entry[+].fullUrl = "urn:uuid:1fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc9"
* entry[=].resource = AtApsExampleBundle-Journey-2-Entlassungsbrief-2024-12

// Eingriffe und Therapien (History of Procedures)
* entry[+].fullUrl = "urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a"
* entry[=].resource = AtApsExampleBundle-Journey-2-procedure-history-1
* entry[+].fullUrl = "urn:uuid:8103f99c-64f0-4dd5-b92e-5c9680c91e47"
* entry[=].resource = AtApsExampleBundle-Journey-2-procedure-history-2
* entry[+].fullUrl = "urn:uuid:8a825f17-1599-4928-b384-0ca4a62daba8"
* entry[=].resource = AtApsExampleBundle-Journey-2-procedure-history-3

// Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)
* entry[+].fullUrl = "urn:uuid:490dab5c-271e-4736-8a6b-d04fd2a04606"
* entry[=].resource = AtApsExampleBundle-Journey-2-deviceUse-Hueftprothese
* entry[+].fullUrl = "urn:uuid:a1a80313-a757-4062-b0d7-d04fd2a04603"
* entry[=].resource = AtApsExampleBundle-Journey-2-device-Hueftprothese

// Impfungen (Immunization)
* entry[+].fullUrl = "urn:uuid:590dab5c-271e-4736-8a6b-d04fd2a04607"
* entry[=].resource = AtApsExampleBundle-Journey-2-Immunization-1

// Diagnostische Resultate (Results)

// Vitalparameter (Vital Signs)
* entry[+].fullUrl = "urn:uuid:74c5e186-d765-4c93-a624-c9b0746e8142"
* entry[=].resource = AtApsExampleBundle-Journey-2-vital-sign-1
* entry[+].fullUrl = "urn:uuid:428259da-e0f7-4780-b1e3-c177515edd37"
* entry[=].resource = AtApsExampleBundle-Journey-2-vital-sign-2
* entry[+].fullUrl = "urn:uuid:daf9c15d-14d4-429c-b658-6842fdff67d8"
* entry[=].resource = AtApsExampleBundle-Journey-2-vital-sign-3
* entry[+].fullUrl = "urn:uuid:8248cc70-65a2-4d37-ae14-a3ef2abf8f32"
* entry[=].resource = AtApsExampleBundle-Journey-2-vital-sign-4
* entry[+].fullUrl = "urn:uuid:4d3f7ac4-fd0a-49af-a56b-303a2dbe67d1"
* entry[=].resource = AtApsExampleBundle-Journey-2-vital-sign-5

// Vergangene Gesundheitsprobleme und Risiken (History of  Past Illness)
* entry[+].fullUrl = "urn:uuid:82301518-66ca-4b4c-821d-087adf643cc4"
* entry[=].resource = AtApsExampleBundle-Journey-2-illness-history-1
* entry[+].fullUrl = "urn:uuid:ce2589a2-a5e5-4520-808f-8118e2863a95"
* entry[=].resource = AtApsExampleBundle-Journey-2-illness-history-2

// Beeinträchtigungen (Functional Status)

// Behandlungsplan (Plan of Care)

// Lebensstil / Soziale Umstände und Verhalten (Social History)
* entry[+].fullUrl = "urn:uuid:d0a5bbf1-6d01-4d44-bac5-05f12c98411e"
* entry[=].resource = AtApsExampleBundle-Journey-2-social-history-1
* entry[+].fullUrl = "urn:uuid:9add5c32-1ded-43d6-b163-c3fe13f94984"
* entry[=].resource = AtApsExampleBundle-Journey-2-social-history-2
* entry[+].fullUrl = "urn:uuid:9add5c32-1ded-43d6-b163-c3fe13f94985"
* entry[=].resource = AtApsExampleBundle-Journey-2-social-history-3

// Schwangerschaftshistorie (History of Pregnancy)

// Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)

// Warnungen (Alerts)

// Patientenbericht (Patient Story)


//***************************************************************************************/
Instance: AtApsExampleBundle-Journey-2-composition
InstanceOf: AtApsComposition
Usage: #inline
// * language = #de-AT
* status = #final
* type = $cs-loinc#60591-5 "Patient summary"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* date = "2025-02-08T14:31:30+00:00"
* author = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "APS Generator"
* title = "APS - Patient Journey 1"
* custodian = Reference(urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6) "Muster-Organisation"
* extension[countryOfAffiliation].valueString = "AT"

// Medikationsliste (Medication Summary)
* section[sectionMedications].title = "Medikationsliste"
* section[sectionMedications].code = $cs-loinc#10160-0 "Medikationsanamnese"
* section[sectionMedications].text.status = #empty
* section[sectionMedications].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionMedications].entry[+] = Reference(urn:uuid:ecf9728f-fa50-4b46-b8f7-7768174df72a) "RAMIPRIL 1A TBL  5MG (AtApsExampleBundle-Journey-2-medication-summary-7)"

// Allergien und Intoleranzen (Allergies and Intolerances)
* section[sectionAllergies].title = "Allergien und Intoleranzen"
* section[sectionAllergies].code = $cs-loinc#48765-2 "Allergien und unerwünschte Wirkungen"
* section[sectionAllergies].text.status = #empty
* section[sectionAllergies].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionAllergies].entry = Reference(urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b) "AtApsExampleBundle-Journey-2-allergy-1"

// Gesundheitsprobleme und Risiken (Problems)
// Problems
* section[sectionProblems].title = "Gesundheitsprobleme und Risiken"
* section[sectionProblems].code = $cs-loinc#11450-4 "Problemliste"
* section[sectionProblems].text.status = #empty
* section[sectionProblems].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionProblems].entry[+] = Reference(urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde) "Arterielle Hypertonie (AtApsExampleBundle-Journey-2-problem-5)"
// Problems - Family history
* section[sectionProblems].entry[+] = Reference(urn:uuid:3f3140b1-9478-4491-b7bf-10560f38da0e) "Diabetes mellitus in der Familienanamnese (AtApsExampleBundle-Journey-2-problem-13)"
// Problems - periodontal disease risk
* section[sectionProblems].entry[+] = Reference(urn:uuid:fa46fccb-5c24-4a40-a478-d6da4902ff33) "Parodontalerkrankung (AtApsExampleBundle-Journey-2-problem-17)"


// Eingriffe und Therapien (History of Procedures)
* section[sectionProceduresHx].title = "Eingriffe und Therapien"
* section[sectionProceduresHx].code = $cs-loinc#47519-4 "Anamnese der Prozeduren oder Maßnahmen"
* section[sectionProceduresHx].text.status = #empty
* section[sectionProceduresHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionProceduresHx].entry[+] = Reference(urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a) "Totalersatz des linken Hüftgelenks (AtApsExampleBundle-Journey-2-procedure-history-1)"
* section[sectionProceduresHx].entry[+] = Reference(urn:uuid:8103f99c-64f0-4dd5-b92e-5c9680c91e47) "Appendektomie (AtApsExampleBundle-Journey-2-procedure-history-2)"
* section[sectionProceduresHx].entry[+] = Reference(urn:uuid:8a825f17-1599-4928-b384-0ca4a62daba8) "Koloskopie (AtApsExampleBundle-Journey-2-procedure-history-3)"

// Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)
* section[sectionMedicalDevices].title = "Implantate, medizinische Geräte und Heilbehelfe"
* section[sectionMedicalDevices].code = $cs-loinc#46264-8 "Anamnese zum Einsatz von Medizinprodukten"
* section[sectionMedicalDevices].text.status = #empty
* section[sectionMedicalDevices].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionMedicalDevices].entry = Reference(urn:uuid:490dab5c-271e-4736-8a6b-d04fd2a04606) "Hüftprothese"

// Impfungen (Immunization)
* section[sectionImmunizations].title = "Impfungen"
* section[sectionImmunizations].code = $cs-loinc#11369-6 "Impfungen"
* section[sectionImmunizations].text.status = #empty
* section[sectionImmunizations].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionImmunizations].entry[+]  = Reference(urn:uuid:590dab5c-271e-4736-8a6b-d04fd2a04607) "Diphtherie-Pertussis-Poliomyelitis-Tetanus"

// Diagnostische Resultate (Results)
* section[sectionResults].title = "Diagnostische Resultate"
* section[sectionResults].code = $cs-loinc#30954-2 "Relevante diagnostische Tests oder Labordaten"
* section[sectionResults].text.status = #empty
* section[sectionResults].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionResults].emptyReason[0] = $cs-list-empty-reason#nilknown

// Vitalparameter (Vital Signs)
* section[sectionVitalSigns].title = "Vitalparameter"
* section[sectionVitalSigns].code = $cs-loinc#8716-3 "Vitalparameter"
* section[sectionVitalSigns].text.status = #empty
* section[sectionVitalSigns].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionVitalSigns].entry[0] = Reference(urn:uuid:74c5e186-d765-4c93-a624-c9b0746e8142) "Körpergröße (AtApsExampleBundle-Journey-2-vital-sign-1)"
* section[sectionVitalSigns].entry[+] = Reference(urn:uuid:428259da-e0f7-4780-b1e3-c177515edd37) "Körpergewicht (AtApsExampleBundle-Journey-2-vital-sign-2)"
* section[sectionVitalSigns].entry[+] = Reference(urn:uuid:daf9c15d-14d4-429c-b658-6842fdff67d8) "BMI (AtApsExampleBundle-Journey-2-vital-sign-3)"
* section[sectionVitalSigns].entry[+] = Reference(urn:uuid:8248cc70-65a2-4d37-ae14-a3ef2abf8f32) "Blutdruck (AtApsExampleBundle-Journey-2-vital-sign-4)"
* section[sectionVitalSigns].entry[+] = Reference(urn:uuid:4d3f7ac4-fd0a-49af-a56b-303a2dbe67d1) "Herzfrequenz (AtApsExampleBundle-Journey-2-vital-sign-5)"

// Vergangene Gesundheitsprobleme und Risiken (History of  Past Illness)
* section[sectionPastIllnessHx].title = "Vergangene Gesundheitsprobleme und Risiken"
* section[sectionPastIllnessHx].code = $cs-loinc#11348-0 "Anamnese früherer Krankheiten"
* section[sectionPastIllnessHx].text.status = #empty
* section[sectionPastIllnessHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionPastIllnessHx].entry[+] = Reference(urn:uuid:82301518-66ca-4b4c-821d-087adf643cc4) "Masern (AtApsExampleBundle-Journey-3-illness-history-1)"
* section[sectionPastIllnessHx].entry[+] = Reference(urn:uuid:ce2589a2-a5e5-4520-808f-8118e2863a95) "Windpocken (AtApsExampleBundle-Journey-2-illness-history-2)"

// Social History
* section[sectionSocialHistory].title = "Lebensstil / Soziale Umstände und Verhalten"
* section[sectionSocialHistory].code = $cs-loinc#29762-2 "Sozialanamnese"
* section[sectionSocialHistory].text.status = #empty
* section[sectionSocialHistory].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionSocialHistory].entry[0] = Reference(urn:uuid:d0a5bbf1-6d01-4d44-bac5-05f12c98411e) "Raucherstatus (AtApsExampleBundle-Journey-2-social-history-1)"
* section[sectionSocialHistory].entry[+] = Reference(urn:uuid:9add5c32-1ded-43d6-b163-c3fe13f94984) "Körperliche Aktivität (AtApsExampleBundle-Journey-2-social-history-2)"
* section[sectionSocialHistory].entry[+] = Reference(urn:uuid:9add5c32-1ded-43d6-b163-c3fe13f94985) "Alkoholkonsum (AtApsExampleBundle-Journey-2-social-history-3)"


//***************************************************************************************/

// Patient
Instance: AtApsExampleBundle-Journey-2-patient
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

// Arzt
Instance: AtApsExampleBundle-Journey-2-practitioner
InstanceOf: AtApsPractitioner
Usage: #inline
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:oid:1.2.40.0.10.99.1.2.3.4"
* identifier.assigner.display = "Bundesministerium für Gesundheit"
* name.prefix[0] = "Dr."
* name.family = "Hausärztin"
* name.given[0] = "Hanna"


// Gesundheitsprobleme und Risiken (Problems)
// Problems
Instance: AtApsExampleBundle-Journey-2-problem-5
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#38341003 "Arterielle Hypertonie"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* onsetDateTime = "2024-12-08T10:31:58+02:00"
* evidence.detail[0] = Reference(urn:uuid:1fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc9) "Entlassungsbrief AKH Amadeus"

// DocumentReference: Quelldokument
Instance: AtApsExampleBundle-Journey-2-Entlassungsbrief-2024-12
InstanceOf: DocumentReference
Usage: #inline
* status = #current
* type = $cs-loinc#11490-0 "Entlassungsbrief"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* date = "2024-12-08T10:00:00+02:00"
* content.attachment.url = "https://example.org/fhir/Binary/AtApsExampleBundle-Journey-2-Entlassungsbrief-2024-12.pdf"
* content.attachment.contentType = #application/pdf
* content.attachment.title = "Entlassungsbrief AKH Amadeus"

// Provenance
Instance: AtApsExampleBundle-Journey-2-provenance-1
InstanceOf: Provenance
Usage: #inline
* target[0] = Reference(urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde) "Target: AtApsExampleBundle-Journey-2-problem-5 (Arterielle Hypertonie)" //uuid of the condition
* recorded = "2024-12-08T11:00:00+02:00"
* entity[0].role = #source
* entity[0].what = Reference(urn:uuid:1fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc9) "Dokument: Entlassungsbrief AKH Amadeus"
* agent[0].who.display = "AKH Amadeus - Entlassungsmanagement"

Instance: AtApsExampleBundle-Journey-2-problem-17
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#inactive "Inactive"
* verificationStatus = $cs-condition-ver-status#provisional "Provisional"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#2556008 "Parodontalerkrankung"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* stage.assessment = Reference(urn:uuid:f235c566-01aa-457d-ab49-9e422df69863) "AtApsExampleBundle-Journey-2-problem-17-assessment-1"

Instance: AtApsExampleBundle-Journey-2-problem-17-assessment-1
InstanceOf: Observation
Usage: #inline
* status = #final
* category = $cs-observation-category#exam "Exam"
* code = $cs-sct#1237049003 "Bewertung der Risikofaktoren für Parodontalerkrankungen"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2025-02-08T14:31:30+00:00"
* valueCodeableConcept = $cs-sct#723509005 "Hohes Risiko"

// Problems - Family history
Instance: AtApsExampleBundle-Journey-2-problem-13
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#160303001 "Diabetes mellitus in der Familienanamnese"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"

// Medication Summary

Instance: AtApsExampleBundle-Journey-2-medication-summary-7
InstanceOf: AtApsMedicationStatement
Usage: #inline
* status = #active
* medicationCodeableConcept = $cs-asp-liste#2450888 "RAMIPRIL 1A TBL  5MG"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectivePeriod.start = "2024-12-08T10:31:58+02:00"
* dosage.text = "S:1-0-0-0"

// Allergies and Intolerances

Instance: AtApsExampleBundle-Journey-2-allergy-1
InstanceOf: AtApsAllergyIntolerance
Usage: #inline
* clinicalStatus = $cs-allergyintolerance-clinical#active "Active"
* code = $cs-sct#128488006 "Hausstaub"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"

//
Instance: AtApsExampleBundle-Journey-2-Immunization-1
InstanceOf: AtApsImmunization
Usage: #inline
* status = #completed
* vaccineCode.coding[0] = $vs-eimpf-impfstoffe#2457324 "BOOSTRIX POLIO FSPR 0,5ML"
* vaccineCode.text = "Diphtherie-Pertussis-Poliomyelitis-Tetanus"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
//* performer.actor = Reference(Patient/at-aps-example-practitioner-01) "Dr. Hanna Hausärztin"
* vaccineCode = $vs-eimpf-impfstoffe#2457324 "BOOSTRIX POLIO FSPR 0,5ML"
* occurrenceDateTime = "2025-01-08T14:31:30+00:00"
//* primarySource = true
* route = $vs-eimpf-medikationartanwendung#IM "Intramuskulär"
//* protocolApplied[0].series = "Standardimpfserie"
* protocolApplied[0].doseNumberPositiveInt = 1
* protocolApplied[0].targetDisease[0] = $vs-eimpf-immunizationtarget#397430003 "Diphtheria"
* protocolApplied[0].targetDisease[+] = $vs-eimpf-immunizationtarget#27836007 "Pertussis"
* protocolApplied[0].targetDisease[+] = $vs-eimpf-immunizationtarget#398102009 "Poliomyelitis"
* protocolApplied[0].targetDisease[+] = $vs-eimpf-immunizationtarget#76902006 "Tetanus"

// History of Procedures

Instance: AtApsExampleBundle-Journey-2-procedure-history-1
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#770606008 "Totalersatz des linken Hüftgelenks"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performedDateTime = "2010"

Instance: AtApsExampleBundle-Journey-2-procedure-history-2
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#80146002 "Appendektomie"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performedDateTime = "2001-06-15"

Instance: AtApsExampleBundle-Journey-2-procedure-history-3
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#73761001 "Koloskopie"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// within the last 10 years
* performedDateTime = "2014-05-17"

// Vitalparameter (Vital Signs)

Instance: AtApsExampleBundle-Journey-2-vital-sign-1
InstanceOf: AtApsObservationVitalSigns
Usage: #inline
* status = #final
* category[VSCat] = $cs-observation-category#vital-signs "Vital Signs"
* code = $cs-loinc#8302-2 "Körpergröße"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2025-02-08T14:31:30+00:00"
* valueQuantity = 173 'cm' "cm"

Instance: AtApsExampleBundle-Journey-2-vital-sign-2
InstanceOf: AtApsObservationVitalSigns
Usage: #inline
* status = #final
* category[VSCat] = $cs-observation-category#vital-signs "Vital Signs"
* code = $cs-loinc#29463-7 "Körpergewicht"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2025-02-08T14:31:30+00:00"
* valueQuantity = 68 'kg' "kg"

Instance: AtApsExampleBundle-Journey-2-vital-sign-3
InstanceOf: AtApsObservationVitalSigns
Usage: #inline
* status = #final
* category[VSCat] = $cs-observation-category#vital-signs "Vital Signs"
* code = $cs-loinc#39156-5 "Body Mass Index (BMI) [Verhältnis]"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2025-02-08T14:31:30+00:00"
* valueQuantity = 22.72 'kg/m2' "kg/m2"
* interpretation = $cs-v3-ObservationInterpretation#H "High"

Instance: AtApsExampleBundle-Journey-2-vital-sign-4
InstanceOf: AtApsObservationVitalSigns
Usage: #inline
* status = #final
* category[VSCat] = $cs-observation-category#vital-signs "Vital Signs"
* code = $cs-loinc#85354-9 "Blood pressure panel with all children optional"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2025-02-08T14:31:30+00:00"
* component[0].code = $cs-loinc#8480-6 "Systolischer Blutdruck"
* component[=].valueQuantity = 180 'mm[Hg]' "mm[Hg]"
* component[+].code = $cs-loinc#8462-4 "Diastolischer Blutdruck"
* component[=].valueQuantity = 80 'mm[Hg]' "mm[Hg]"

Instance: AtApsExampleBundle-Journey-2-vital-sign-5
InstanceOf: AtApsObservationVitalSigns
Usage: #inline
* status = #final
* category[VSCat] = $cs-observation-category#vital-signs "Vital Signs"
* code = $cs-loinc#8867-4 "Herzfrequenz"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2025-02-08T14:31:30+00:00"
* valueQuantity = 100 '/min' "/min"

// Vergangene Gesundheitsprobleme und Risiken (History of  Past Illness)

Instance: AtApsExampleBundle-Journey-2-illness-history-1
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#resolved "Resolved"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#14189004 "Masern"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* onsetDateTime = "1994-02-08"

Instance: AtApsExampleBundle-Journey-2-illness-history-2
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#resolved "Resolved"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#38907003 "Windpocken"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* onsetDateTime = "1991"

// Lebensstil / Soziale Umstände und Verhalten (Social History)

Instance: AtApsExampleBundle-Journey-2-social-history-1
InstanceOf: AtApsObservationTobaccoUse
Usage: #inline
* status = #final
* code = $cs-loinc#72166-2 "Raucherstatus"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2024-02-08T08:30:00+01:00"
* valueCodeableConcept = $cs-sct#266919005 "Nie Tabak geraucht"

Instance: AtApsExampleBundle-Journey-2-social-history-2
InstanceOf: AtApsObservation
Usage: #inline
* status = #final
* code = $cs-sct#61686008 "Körperliche Aktivität"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2024-02-08T08:30:00+01:00"
* valueRatio.numerator = 2.5 'h' "h"
* valueRatio.numerator.comparator = #>
* valueRatio.denominator = 1 'wk' "wk"

Instance: AtApsExampleBundle-Journey-2-social-history-3
InstanceOf: AtApsObservationAlcoholUse
Usage: #inline
* status = #final
* code = $cs-loinc#74013-4 "Alcoholic drinks per day"
* code.coding.display = "Alkoholische Getränke pro Tag, 1-2 Gläser Wein/Bier"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2019-07-15"
* valueQuantity = 2 '/d' "wine glasses per day"

Instance: AtApsExampleBundle-Journey-2-deviceUse-Hueftprothese
InstanceOf: AtApsDeviceUseStatement
Usage: #inline
* status = #active
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* device = Reference(urn:uuid:a1a80313-a757-4062-b0d7-d04fd2a04603) "Hüftprothese"
* device.display = "Verwendetes Gerät: Hüftprothese"
// * timingDateTime.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
// * timingDateTime.extension.valueCode = #unknown
* timingPeriod.start = "2020"
* bodySite = $cs-sct#362905007 "Gesamtes linkes Hüftgelenk"
* bodySite.coding[0].display = "Gesamtes linkes Hüftgelenk"

Instance: AtApsExampleBundle-Journey-2-device-Hueftprothese
InstanceOf: AtApsDevice
Usage: #inline
* type = $cs-sct#67270000 "Hüftprothese"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* deviceName.name = "Hüftprothese"
* deviceName.type = #other
* version.value = "Version.value 123456"


Instance: AtApsExampleBundle-Journey-2-author-device
InstanceOf: Device
Usage: #inline
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* type = $cs-sct#49062001 "Gerät"
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Dieses Gerät erzeugt ein APS FHIR-Dokument.</p></div>"
* deviceName.name = "APS Generator"
* deviceName.type = #user-friendly-name

Instance: AtApsExampleBundle-Journey-2-custodian
InstanceOf: AtApsOrganization
Usage: #inline
* name = "Muster-Organization"