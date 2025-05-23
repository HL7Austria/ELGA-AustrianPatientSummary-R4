Instance: AtApsExampleBundle-Journey-3
InstanceOf: AtApsBundle
Description: "APS Patient Journey-3"
Usage: #example
* identifier.system = "http://system-to-be-defined.com"
* identifier.value = "63fef90a-be11-4ddf-aece-d77da15c4f23"
* type = #document
* timestamp = "2025-02-15T14:31:30+00:00"
* entry[0].fullUrl = "urn:uuid:212fdc76-ccc3-40bf-8cdd-82f2ef88bd7c"
* entry[=].resource = AtApsExampleBundle-Journey-3-composition
* entry[+].fullUrl = "urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8"
* entry[=].resource = AtApsExampleBundle-Journey-3-patient
* entry[+].fullUrl = "urn:uuid:75db30ee-7028-486c-929a-c5126837f472"
* entry[=].resource = AtApsExampleBundle-Journey-3-author-device
* entry[+].fullUrl = "urn:uuid:75db30ee-7028-486c-929a-c5126837f473"
* entry[=].resource = AtApsExampleBundle-Journey-3-practitioner
* entry[+].fullUrl = "urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6"
* entry[=].resource = AtApsExampleBundle-Journey-3-custodian

// Medikationsliste (Medication Summary)
* entry[+].fullUrl = "urn:uuid:ecf9728f-fa50-4b46-b8f7-7768174df72a"
* entry[=].resource = AtApsExampleBundle-Journey-3-medication-summary-7

// Allergien und Intoleranzen (Allergies and Intolerances)
* entry[+].fullUrl = "urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b"
* entry[=].resource = AtApsExampleBundle-Journey-3-allergy-1

// Gesundheitsprobleme und Risiken (Problems)
// Problems
* entry[+].fullUrl = "urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde"
* entry[=].resource = AtApsExampleBundle-Journey-3-problem-5
// Problem List - periodontal disease risk
* entry[+].fullUrl = "urn:uuid:fa46fccb-5c24-4a40-a478-d6da4902ff33"
* entry[=].resource = AtApsExampleBundle-Journey-3-problem-17
* entry[+].fullUrl = "urn:uuid:f235c566-01aa-457d-ab49-9e422df69863"
* entry[=].resource = AtApsExampleBundle-Journey-3-problem-17-assessment-1 //21
// Family history
* entry[+].fullUrl = "urn:uuid:3f3140b1-9478-4491-b7bf-10560f38da0e"
* entry[=].resource = AtApsExampleBundle-Journey-3-problem-13
* entry[+].fullUrl = "urn:uuid:1fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc9"
* entry[=].resource = AtApsExampleBundle-Journey-3-Entlassungsbrief-2024-12

// Eingriffe und Therapien (History of Procedures)
* entry[+].fullUrl = "urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a"
* entry[=].resource = AtApsExampleBundle-Journey-3-procedure-history-1
* entry[+].fullUrl = "urn:uuid:8103f99c-64f0-4dd5-b92e-5c9680c91e47"
* entry[=].resource = AtApsExampleBundle-Journey-3-procedure-history-2
* entry[+].fullUrl = "urn:uuid:8a825f17-1599-4928-b384-0ca4a62daba8"
* entry[=].resource = AtApsExampleBundle-Journey-3-procedure-history-3

// Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)
* entry[+].fullUrl = "urn:uuid:490dab5c-271e-4736-8a6b-d04fd2a04606"
* entry[=].resource = AtApsExampleBundle-Journey-3-deviceUse-Hueftprothese
* entry[+].fullUrl = "urn:uuid:a1a80313-a757-4062-b0d7-d04fd2a04603"
* entry[=].resource = AtApsExampleBundle-Journey-3-device-Hueftprothese

// Impfungen (Immunization)
* entry[+].fullUrl = "urn:uuid:590dab5c-271e-4736-8a6b-d04fd2a04607"
* entry[=].resource = AtApsExampleBundle-Journey-3-Immunization-1

// Diagnostische Resultate (Results)
// Specimen for Diagnostic Results
* entry[+].fullUrl = "urn:uuid:5218bc54-5d55-42fa-aa0c-169b61577ad0"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-specimen-1
// * entry[+].fullUrl = "urn:uuid:ee1e26a1-caba-45f7-928e-d93fc1a47da9"
// * entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-specimen-2
// Diagnostic Results
* entry[+].fullUrl = "urn:uuid:725bcf71-22e6-473b-a879-49a4b63cd654"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-1
* entry[+].fullUrl = "urn:uuid:aeff2319-2cc2-4fba-9541-7a4de3d20f91"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-2
* entry[+].fullUrl = "urn:uuid:d16dce15-bc5a-48a5-910e-6ac039785a2a"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-3
* entry[+].fullUrl = "urn:uuid:96314fcd-3b0c-4032-8cac-6eb59579d90a"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-4
* entry[+].fullUrl = "urn:uuid:30c8a990-ea39-4dcb-9e1e-b9ac74afffc9"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-5
* entry[+].fullUrl = "urn:uuid:f29ac02d-762e-436e-b40c-667ab89e15f2"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-6
* entry[+].fullUrl = "urn:uuid:28a773ea-38c7-4c77-86c4-7764325756e7"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-7
// * entry[+].fullUrl = "urn:uuid:4fe4b16a-14cb-4fd6-9da6-02c4b3797fdc"
// * entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-8
// * entry[+].fullUrl = "urn:uuid:24ff8632-0ccd-4279-88b2-325fdd936ecb"
// * entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-9
// * entry[+].fullUrl = "urn:uuid:8c11ad58-94ec-469c-ba4d-bfba9063067d"
// * entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-10
// * entry[+].fullUrl = "urn:uuid:8c7f9e94-b834-474e-818c-bbd6c3ce3e17"
// * entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-11
// * entry[+].fullUrl = "urn:uuid:e6e05f94-92be-4ae3-bf49-b0b7d4a62b35"
// * entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-12
// * entry[+].fullUrl = "urn:uuid:33e09da2-5f43-4046-b2eb-cf190031826b"
// * entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-13
// * entry[+].fullUrl = "urn:uuid:b675680e-9469-41b1-adc1-093904e3a1d2"
// * entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-14
* entry[+].fullUrl = "urn:uuid:b675680e-9469-41b1-adc1-093904e3a1d3"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-15
// Diagnostic Results - Performer
* entry[+].fullUrl = "urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6"
* entry[=].resource = AtApsExampleBundle-Journey-3-diagnostic-result-performer-1

// Vitalparameter (Vital Signs)
* entry[+].fullUrl = "urn:uuid:74c5e186-d765-4c93-a624-c9b0746e8142"
* entry[=].resource = AtApsExampleBundle-Journey-3-vital-sign-1
* entry[+].fullUrl = "urn:uuid:428259da-e0f7-4780-b1e3-c177515edd37"
* entry[=].resource = AtApsExampleBundle-Journey-3-vital-sign-2
* entry[+].fullUrl = "urn:uuid:daf9c15d-14d4-429c-b658-6842fdff67d8"
* entry[=].resource = AtApsExampleBundle-Journey-3-vital-sign-3
* entry[+].fullUrl = "urn:uuid:8248cc70-65a2-4d37-ae14-a3ef2abf8f32"
* entry[=].resource = AtApsExampleBundle-Journey-3-vital-sign-4
* entry[+].fullUrl = "urn:uuid:4d3f7ac4-fd0a-49af-a56b-303a2dbe67d1"
* entry[=].resource = AtApsExampleBundle-Journey-3-vital-sign-5

// Vergangene Gesundheitsprobleme und Risiken (History of  Past Illness)
* entry[+].fullUrl = "urn:uuid:82301518-66ca-4b4c-821d-087adf643cc4"
* entry[=].resource = AtApsExampleBundle-Journey-3-illness-history-1
* entry[+].fullUrl = "urn:uuid:ce2589a2-a5e5-4520-808f-8118e2863a95"
* entry[=].resource = AtApsExampleBundle-Journey-3-illness-history-2

// Beeinträchtigungen (Functional Status)

// Behandlungsplan (Plan of Care)

// Lebensstil / Soziale Umstände und Verhalten (Social History)
* entry[+].fullUrl = "urn:uuid:d0a5bbf1-6d01-4d44-bac5-05f12c98411e"
* entry[=].resource = AtApsExampleBundle-Journey-3-social-history-1
* entry[+].fullUrl = "urn:uuid:9add5c32-1ded-43d6-b163-c3fe13f94984"
* entry[=].resource = AtApsExampleBundle-Journey-3-social-history-2
* entry[+].fullUrl = "urn:uuid:9add5c32-1ded-43d6-b163-c3fe13f94985"
* entry[=].resource = AtApsExampleBundle-Journey-3-social-history-3

// Schwangerschaftshistorie (History of Pregnancy)

// Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)

// Warnungen (Alerts)

// Patientenbericht (Patient Story)


//***************************************************************************************/
Instance: AtApsExampleBundle-Journey-3-composition
InstanceOf: AtApsComposition
Usage: #inline
// * language = #de-AT
* status = #final
* type = $cs-loinc#60591-5 "Patient summary"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* date = "2025-02-15T14:31:30+00:00"
* author = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "APS Generator"
* title = "APS - Patient Journey 1"
* custodian = Reference(urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6) "Muster-Organisation"
* extension[countryOfAffiliation].valueString = "AT"

// Medikationsliste (Medication Summary)
* section[sectionMedications].title = "Medikationsliste"
* section[sectionMedications].code = $cs-loinc#10160-0 "Medikationsanamnese"
* section[sectionMedications].text.status = #empty
* section[sectionMedications].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionMedications].entry[medicationStatement][0] = Reference(urn:uuid:ecf9728f-fa50-4b46-b8f7-7768174df72a) "RAMIPRIL 1A TBL  5MG (AtApsExampleBundle-Journey-3-medication-summary-7)"

// Allergien und Intoleranzen (Allergies and Intolerances)
* section[sectionAllergies].title = "Allergien und Intoleranzen"
* section[sectionAllergies].code = $cs-loinc#48765-2 "Allergien und unerwünschte Wirkungen"
* section[sectionAllergies].text.status = #empty
* section[sectionAllergies].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionAllergies].entry[allergyOrIntolerance][0] = Reference(urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b) "AtApsExampleBundle-Journey-3-allergy-1"

// Gesundheitsprobleme und Risiken (Problems)
// Problems
* section[sectionProblems].title = "Gesundheitsprobleme und Risiken"
* section[sectionProblems].code = $cs-loinc#11450-4 "Problemliste"
* section[sectionProblems].text.status = #empty
* section[sectionProblems].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionProblems].entry[problem][+] = Reference(urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde) "Arterielle Hypertonie (AtApsExampleBundle-Journey-3-problem-5)"
// Problems - Family history
* section[sectionProblems].entry[problem][+] = Reference(urn:uuid:3f3140b1-9478-4491-b7bf-10560f38da0e) "Diabetes mellitus in der Familienanamnese (AtApsExampleBundle-Journey-3-problem-13)"
// Problems - periodontal disease risk
* section[sectionProblems].entry[problem][+] = Reference(urn:uuid:fa46fccb-5c24-4a40-a478-d6da4902ff33) "Parodontalerkrankung (AtApsExampleBundle-Journey-3-problem-17)"


// Eingriffe und Therapien (History of Procedures)
* section[sectionProceduresHx].title = "Eingriffe und Therapien"
* section[sectionProceduresHx].code = $cs-loinc#47519-4 "Anamnese der Prozeduren oder Maßnahmen"
* section[sectionProceduresHx].text.status = #empty
* section[sectionProceduresHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionProceduresHx].entry[procedure][+] = Reference(urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a) "Totalersatz des linken Hüftgelenks (AtApsExampleBundle-Journey-3-procedure-history-1)"
* section[sectionProceduresHx].entry[procedure][+] = Reference(urn:uuid:8103f99c-64f0-4dd5-b92e-5c9680c91e47) "Appendektomie (AtApsExampleBundle-Journey-3-procedure-history-2)"
* section[sectionProceduresHx].entry[procedure][+] = Reference(urn:uuid:8a825f17-1599-4928-b384-0ca4a62daba8) "Koloskopie (AtApsExampleBundle-Journey-3-procedure-history-3)"

// Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)
* section[sectionMedicalDevices].title = "Implantate, medizinische Geräte und Heilbehelfe"
* section[sectionMedicalDevices].code = $cs-loinc#46264-8 "Anamnese zum Einsatz von Medizinprodukten"
* section[sectionMedicalDevices].text.status = #empty
* section[sectionMedicalDevices].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionMedicalDevices].entry[deviceStatement][0] = Reference(urn:uuid:490dab5c-271e-4736-8a6b-d04fd2a04606) "Hüftprothese"

// Impfungen (Immunization)
* section[sectionImmunizations].title = "Impfungen"
* section[sectionImmunizations].code = $cs-loinc#11369-6 "Impfungen"
* section[sectionImmunizations].text.status = #empty
* section[sectionImmunizations].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionImmunizations].entry[immunization][+]  = Reference(urn:uuid:590dab5c-271e-4736-8a6b-d04fd2a04607) "Diphtherie-Pertussis-Poliomyelitis-Tetanus"

// Diagnostische Resultate (Results)
* section[sectionResults].title = "Diagnostische Resultate"
* section[sectionResults].code = $cs-loinc#30954-2 "Relevante diagnostische Tests oder Labordaten"
* section[sectionResults].text.status = #empty
* section[sectionResults].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionResults].entry[resultsObservationLaboratoryPathology][0] = Reference(urn:uuid:725bcf71-22e6-473b-a879-49a4b63cd654) "Blutgruppe A Rh(D) positiv (AtApsExampleBundle-Journey-3-diagnostic-result-1)"
* section[sectionResults].entry[resultsObservationLaboratoryPathology][+] = Reference(urn:uuid:aeff2319-2cc2-4fba-9541-7a4de3d20f91) "Klinische Chemie/Proteindiagnostik (AtApsExampleBundle-Journey-3-diagnostic-result-2)"
* section[sectionResults].entry[resultsObservationLaboratoryPathology][+] = Reference(urn:uuid:d16dce15-bc5a-48a5-910e-6ac039785a2a) "Cholesterin (AtApsExampleBundle-Journey-3-diagnostic-result-3)"
* section[sectionResults].entry[resultsObservationLaboratoryPathology][+] = Reference(urn:uuid:96314fcd-3b0c-4032-8cac-6eb59579d90a) "HDL-Cholesterin (AtApsExampleBundle-Journey-3-diagnostic-result-4)"
* section[sectionResults].entry[resultsObservationLaboratoryPathology][+] = Reference(urn:uuid:30c8a990-ea39-4dcb-9e1e-b9ac74afffc9) "Cholesterol in Blut oder Serum (AtApsExampleBundle-Journey-3-diagnostic-result-5)"
* section[sectionResults].entry[resultsObservationLaboratoryPathology][+] = Reference(urn:uuid:f29ac02d-762e-436e-b40c-667ab89e15f2) "Triglyceride (AtApsExampleBundle-Journey-3-diagnostic-result-6)"
* section[sectionResults].entry[resultsObservationLaboratoryPathology][+] = Reference(urn:uuid:28a773ea-38c7-4c77-86c4-7764325756e7) "Gamma-GT (AtApsExampleBundle-Journey-3-diagnostic-result-7)"
// * section[sectionResults].entry[+] = Reference(urn:uuid:4fe4b16a-14cb-4fd6-9da6-02c4b3797fdc) "Urindiagnostik (AtApsExampleBundle-Journey-3-diagnostic-result-8)"

// Vitalparameter (Vital Signs)
* section[sectionVitalSigns].title = "Vitalparameter"
* section[sectionVitalSigns].code = $cs-loinc#8716-3 "Vitalparameter"
* section[sectionVitalSigns].text.status = #empty
* section[sectionVitalSigns].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionVitalSigns].entry[vitalSign][0] = Reference(urn:uuid:74c5e186-d765-4c93-a624-c9b0746e8142) "Körpergröße (AtApsExampleBundle-Journey-3-vital-sign-1)"
* section[sectionVitalSigns].entry[vitalSign][+] = Reference(urn:uuid:428259da-e0f7-4780-b1e3-c177515edd37) "Körpergewicht (AtApsExampleBundle-Journey-3-vital-sign-2)"
* section[sectionVitalSigns].entry[vitalSign][+] = Reference(urn:uuid:daf9c15d-14d4-429c-b658-6842fdff67d8) "BMI (AtApsExampleBundle-Journey-3-vital-sign-3)"
* section[sectionVitalSigns].entry[vitalSign][+] = Reference(urn:uuid:8248cc70-65a2-4d37-ae14-a3ef2abf8f32) "Blutdruck (AtApsExampleBundle-Journey-3-vital-sign-4)"
* section[sectionVitalSigns].entry[vitalSign][+] = Reference(urn:uuid:4d3f7ac4-fd0a-49af-a56b-303a2dbe67d1) "Herzfrequenz (AtApsExampleBundle-Journey-3-vital-sign-5)"

// Vergangene Gesundheitsprobleme und Risiken (History of  Past Illness)
* section[sectionPastIllnessHx].title = "Vergangene Gesundheitsprobleme und Risiken"
* section[sectionPastIllnessHx].code = $cs-loinc#11348-0 "Anamnese früherer Krankheiten"
* section[sectionPastIllnessHx].text.status = #empty
* section[sectionPastIllnessHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionPastIllnessHx].entry[pastProblem][+] = Reference(urn:uuid:82301518-66ca-4b4c-821d-087adf643cc4) "Masern (AtApsExampleBundle-Journey-3-illness-history-1)"
* section[sectionPastIllnessHx].entry[pastProblem][+] = Reference(urn:uuid:ce2589a2-a5e5-4520-808f-8118e2863a95) "Windpocken (AtApsExampleBundle-Journey-3-illness-history-2)"

// Social History
* section[sectionSocialHistory].title = "Lebensstil / Soziale Umstände und Verhalten"
* section[sectionSocialHistory].code = $cs-loinc#29762-2 "Sozialanamnese"
* section[sectionSocialHistory].text.status = #empty
* section[sectionSocialHistory].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionSocialHistory].entry[smokingTobaccoUse][0] = Reference(urn:uuid:d0a5bbf1-6d01-4d44-bac5-05f12c98411e) "Raucherstatus (AtApsExampleBundle-Journey-3-social-history-1)"
* section[sectionSocialHistory].entry[alcoholUse][+] = Reference(urn:uuid:9add5c32-1ded-43d6-b163-c3fe13f94985) "Alkoholkonsum (AtApsExampleBundle-Journey-3-social-history-3)"
* section[sectionSocialHistory].entry[+] = Reference(urn:uuid:9add5c32-1ded-43d6-b163-c3fe13f94984) "Körperliche Aktivität (AtApsExampleBundle-Journey-3-social-history-2)"

//***************************************************************************************/

// Patient
Instance: AtApsExampleBundle-Journey-3-patient
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
Instance: AtApsExampleBundle-Journey-3-practitioner
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
Instance: AtApsExampleBundle-Journey-3-problem-5
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
Instance: AtApsExampleBundle-Journey-3-Entlassungsbrief-2024-12
InstanceOf: DocumentReference
Usage: #inline
* status = #current
* type = $cs-loinc#11490-0 "Entlassungsbrief"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* date = "2024-12-08T10:00:00+02:00"
* content.attachment.url = "https://example.org/fhir/Binary/AtApsExampleBundle-Journey-3-Entlassungsbrief-2024-12.pdf"
* content.attachment.contentType = #application/pdf
* content.attachment.title = "Entlassungsbrief AKH Amadeus"

// Provenance
Instance: AtApsExampleBundle-Journey-3-provenance-1
InstanceOf: Provenance
Usage: #inline
* target[0] = Reference(urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde) "Target: AtApsExampleBundle-Journey-3-problem-5 (Arterielle Hypertonie)" //uuid of the condition
* recorded = "2024-12-08T11:00:00+02:00"
* entity[0].role = #source
* entity[0].what = Reference(urn:uuid:1fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc9) "Dokument: Entlassungsbrief AKH Amadeus"
* agent[0].who.display = "AKH Amadeus - Entlassungsmanagement"

Instance: AtApsExampleBundle-Journey-3-problem-17
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#inactive "Inactive"
* verificationStatus = $cs-condition-ver-status#provisional "Provisional"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#2556008 "Parodontalerkrankung"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* stage.assessment = Reference(urn:uuid:f235c566-01aa-457d-ab49-9e422df69863) "AtApsExampleBundle-Journey-3-problem-17-assessment-1"

Instance: AtApsExampleBundle-Journey-3-problem-17-assessment-1
InstanceOf: AtApsObservation
Usage: #inline
* status = #final
* category = $cs-observation-category#exam "Exam"
* code = $cs-sct#1237049003 "Bewertung der Risikofaktoren für Parodontalerkrankungen"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2025-02-08T14:31:30+00:00"
* valueCodeableConcept = $cs-sct#723509005 "Hohes Risiko"

// Problems - Family history
Instance: AtApsExampleBundle-Journey-3-problem-13
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#160303001 "Diabetes mellitus in der Familienanamnese"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"

// Medication Summary

Instance: AtApsExampleBundle-Journey-3-medication-summary-7
InstanceOf: AtApsMedicationStatement
Usage: #inline
* status = #active
* medicationCodeableConcept = $cs-asp-liste#2450888 "RAMIPRIL 1A TBL  5MG"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectivePeriod.start = "2024-12-08T10:31:58+02:00"
* dosage.text = "S:1-0-0-0"

// Allergies and Intolerances

Instance: AtApsExampleBundle-Journey-3-allergy-1
InstanceOf: AtApsAllergyIntolerance
Usage: #inline
* clinicalStatus = $cs-allergyintolerance-clinical#active "Active"
* code = $cs-sct#128488006 "Hausstaub"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"

//
Instance: AtApsExampleBundle-Journey-3-Immunization-1
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

Instance: AtApsExampleBundle-Journey-3-procedure-history-1
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#770606008 "Totalersatz des linken Hüftgelenks"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performedDateTime = "2010"

Instance: AtApsExampleBundle-Journey-3-procedure-history-2
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#80146002 "Appendektomie"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performedDateTime = "2001-06-15"

Instance: AtApsExampleBundle-Journey-3-procedure-history-3
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#73761001 "Koloskopie"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// within the last 10 years
* performedDateTime = "2014-05-17"

// Diagnostische Resultate (Results)
// Specimen

Instance: AtApsExampleBundle-Journey-3-diagnostic-specimen-1
InstanceOf: AtApsSpecimen
Usage: #inline
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* status = $cs-specimen-status#unavailable "Unavailable"
* type = $cs-sct#119297000 "Blutprobe"

Instance: AtApsExampleBundle-Journey-3-diagnostic-specimen-2
InstanceOf: AtApsSpecimen
Usage: #inline
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* status = $cs-specimen-status#available "Available"
* type = $cs-sct#122575003 "Urine specimen"


// Diagnostic Results

Instance: AtApsExampleBundle-Journey-3-diagnostic-result-1
InstanceOf: AtApsObservationResultsLaboratoryPathology
Usage: #inline
* status = #final
// example where all levels of "Laborstruktur" are present
* category[0] = $cs-elga-laborparameterergaenzung#100 "Transfusions-/Transplantationsdiagnostik/Immungenetik"
* category[+] = $cs-elga-laborparameterergaenzung#01850 "Blutgruppenserologie"
* category[+] = $cs-observation-category#laboratory "Laboratory"
* code = $cs-loinc#882-1 "AB0 und Rh-Blutgruppensysteme [Typ] in Blut"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2025-02-13T14:31:30+00:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
* valueCodeableConcept = $cs-sct#278149003 "Blutgruppe A Rh(D) positiv"
* specimen = Reference(urn:uuid:5218bc54-5d55-42fa-aa0c-169b61577ad0) "AtApsExampleBundle-Journey-3-diagnostic-specimen-1"

Instance: AtApsExampleBundle-Journey-3-diagnostic-result-2
InstanceOf: AtApsObservationResultsLaboratoryPathology
Usage: #inline
* status = #final
* category[0] = $cs-elga-laborparameterergaenzung#500 "Klinische Chemie/Proteindiagnostik"
* category[+] = $cs-observation-category#laboratory "Laboratory"
* code = $cs-elga-laborparameterergaenzung#500 "Klinische Chemie/Proteindiagnostik"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2024-02-08T07:56:06+01:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
* hasMember[0] = Reference(urn:uuid:d16dce15-bc5a-48a5-910e-6ac039785a2a) "Cholesterin (AtApsExampleBundle-Journey-3-diagnostic-result-3)"
* hasMember[+] = Reference(urn:uuid:96314fcd-3b0c-4032-8cac-6eb59579d90a) "HDL-Cholesterin (AtApsExampleBundle-Journey-3-diagnostic-result-4)"
* hasMember[+] = Reference(urn:uuid:30c8a990-ea39-4dcb-9e1e-b9ac74afffc9) "Cholesterol.gesamt/Cholesterol in HDL in Serum oder Plasma (AtApsExampleBundle-Journey-3-diagnostic-result-5)"
* hasMember[+] = Reference(urn:uuid:f29ac02d-762e-436e-b40c-667ab89e15f2) "Triglyceride (AtApsExampleBundle-Journey-3-diagnostic-result-6)"
* hasMember[+] = Reference(urn:uuid:28a773ea-38c7-4c77-86c4-7764325756e7) "Gamma-GT (AtApsExampleBundle-Journey-3-diagnostic-result-7)"
* hasMember[+] = Reference(urn:uuid:b675680e-9469-41b1-adc1-093904e3a1d3) "Glucose in Blut (AtApsExampleBundle-Journey-3-diagnostic-result-15)"
* specimen = Reference(urn:uuid:5218bc54-5d55-42fa-aa0c-169b61577ad0) "Blutprobe (AtApsExampleBundle-Journey-3-diagnostic-specimen-1)"

Instance: AtApsExampleBundle-Journey-3-diagnostic-result-3
InstanceOf: AtApsObservationResultsLaboratoryPathology
Usage: #inline
* language = #de-AT
* status = #final
* category[0] = $cs-elga-laborparameterergaenzung#05180 "Klinische Chemie"
* category[+] = $cs-observation-category#laboratory "Laboratory"
* code = $cs-loinc#2093-3 "Cholesterin"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2025-02-13T14:31:30+00:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
* valueQuantity = 180 'mg/dL' "mg/dL"
* specimen = Reference(urn:uuid:5218bc54-5d55-42fa-aa0c-169b61577ad0) "AtApsExampleBundle-Journey-3-diagnostic-specimen-1"

Instance: AtApsExampleBundle-Journey-3-diagnostic-result-4
InstanceOf: AtApsObservationResultsLaboratoryPathology
Usage: #inline
* language = #de-AT
* status = #final
* category[0] = $cs-elga-laborparameterergaenzung#05180 "Klinische Chemie"
* category[+] = $cs-observation-category#laboratory "Laboratory"
* code = $cs-loinc#2085-9 "HDL-Cholesterin"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2025-02-13T14:31:30+00:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
* valueQuantity = 45 'mg/dL' "mg/dL"
* specimen = Reference(urn:uuid:5218bc54-5d55-42fa-aa0c-169b61577ad0) "AtApsExampleBundle-Journey-3-diagnostic-specimen-1"

Instance: AtApsExampleBundle-Journey-3-diagnostic-result-5
InstanceOf: AtApsObservationResultsLaboratoryPathology
Usage: #inline
* status = #final
* category[0] = $cs-elga-laborparameterergaenzung#05180 "Klinische Chemie"
* category[+] = $cs-observation-category#laboratory "Laboratory"
* code = $cs-loinc#9830-1 "Cholesterol.gesamt/Cholesterol in HDL [Massenverhältnis] in Serum oder Plasma"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2025-02-13T14:31:30+00:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
* valueQuantity = 4.0 '{ratio}' "{ratio}"
* specimen = Reference(urn:uuid:5218bc54-5d55-42fa-aa0c-169b61577ad0) "AtApsExampleBundle-Journey-3-diagnostic-specimen-1"

Instance: AtApsExampleBundle-Journey-3-diagnostic-result-6
InstanceOf: AtApsObservationResultsLaboratoryPathology
Usage: #inline
* language = #de-AT
* status = #final
* category[0] = $cs-elga-laborparameterergaenzung#05180 "Klinische Chemie"
* category[+] = $cs-observation-category#laboratory "Laboratory"
* code = $cs-loinc#2571-8 "Triglyceride"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2025-02-13T14:31:30+00:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
* valueQuantity = 130 'mg/dL' "mg/dL"
* specimen = Reference(urn:uuid:5218bc54-5d55-42fa-aa0c-169b61577ad0) "AtApsExampleBundle-Journey-3-diagnostic-specimen-1"

Instance: AtApsExampleBundle-Journey-3-diagnostic-result-7
InstanceOf: AtApsObservationResultsLaboratoryPathology
Usage: #inline
* language = #de-AT
* status = #final
* category[0] = $cs-elga-laborparameterergaenzung#05180 "Klinische Chemie"
* category[+] = $cs-observation-category#laboratory "Laboratory"
* code = $cs-loinc#2324-2 "Gamma-GT"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2025-02-13T14:31:30+00:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
* valueQuantity = 54 'U/L' "U/L"
* specimen = Reference(urn:uuid:5218bc54-5d55-42fa-aa0c-169b61577ad0) "AtApsExampleBundle-Journey-3-diagnostic-specimen-1"

// Instance: AtApsExampleBundle-Journey-3-diagnostic-result-8
// InstanceOf: AtApsObservationResultsLaboratoryPathology
// Usage: #inline
// * status = #final
// * category = $cs-observation-category#laboratory "Laboratory"
// * code = $cs-elga-laborparameterergaenzung#1400 "Urindiagnostik"
// * subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// * effectiveDateTime = "2024-02-08T07:56:06+01:00"
// * performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
// * hasMember[0] = Reference(urn:uuid:24ff8632-0ccd-4279-88b2-325fdd936ecb) "Leukocytes in Urine (AtApsExampleBundle-Journey-3-diagnostic-result-9)"
// * hasMember[+] = Reference(urn:uuid:8c11ad58-94ec-469c-ba4d-bfba9063067d) "Protein in Urine (AtApsExampleBundle-Journey-3-diagnostic-result-10)"
// * hasMember[+] = Reference(urn:uuid:8c7f9e94-b834-474e-818c-bbd6c3ce3e17) "Glucose in Urine (AtApsExampleBundle-Journey-3-diagnostic-result-11)"
// * hasMember[+] = Reference(urn:uuid:e6e05f94-92be-4ae3-bf49-b0b7d4a62b35) "Blood in Urine by Visual (AtApsExampleBundle-Journey-3-diagnostic-result-12)"
// * hasMember[+] = Reference(urn:uuid:33e09da2-5f43-4046-b2eb-cf190031826b) "Nitrite in Urine (AtApsExampleBundle-Journey-3-diagnostic-result-13)"
// * hasMember[+] = Reference(urn:uuid:b675680e-9469-41b1-adc1-093904e3a1d2) "Urobilinogen in Urine (AtApsExampleBundle-Journey-3-diagnostic-result-14)"
// * specimen = Reference(urn:uuid:ee1e26a1-caba-45f7-928e-d93fc1a47da9) "Urine specimen (AtApsExampleBundle-Journey-3-diagnostic-specimen-2)"

// Instance: AtApsExampleBundle-Journey-3-diagnostic-result-9
// InstanceOf: AtApsObservationResultsLaboratoryPathology
// Usage: #inline
// * status = #final
// * category = $cs-observation-category#laboratory "Laboratory"
// * code = $cs-loinc#33052-2 "Leukocytes [Presence] in Urine"
// * subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// * effectiveDateTime = "2025-02-13T14:31:30+00:00"
// * performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
// * valueCodeableConcept = $cs-sct#260415000 "Not detected (qualifier value)"
// * specimen = Reference(urn:uuid:ee1e26a1-caba-45f7-928e-d93fc1a47da9) "Urine specimen (AtApsExampleBundle-Journey-3-diagnostic-specimen-2)"

// Instance: AtApsExampleBundle-Journey-3-diagnostic-result-10
// InstanceOf: AtApsObservationResultsLaboratoryPathology
// Usage: #inline
// * status = #final
// * category = $cs-observation-category#laboratory "Laboratory"
// * code = $cs-loinc#2887-8 "Protein [Presence] in Urine"
// * subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// * effectiveDateTime = "2025-02-13T14:31:30+00:00"
// * performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
// * valueCodeableConcept = $cs-sct#260415000 "Not detected (qualifier value)"
// * specimen = Reference(urn:uuid:ee1e26a1-caba-45f7-928e-d93fc1a47da9) "Urine specimen (AtApsExampleBundle-Journey-3-diagnostic-specimen-2)"

// Instance: AtApsExampleBundle-Journey-3-diagnostic-result-11
// InstanceOf: AtApsObservationResultsLaboratoryPathology
// Usage: #inline
// * status = #final
// * category = $cs-observation-category#laboratory "Laboratory"
// * code = $cs-loinc#2349-9 "Glucose [Presence] in Urine"
// * subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// * effectiveDateTime = "2025-02-13T14:31:30+00:00"
// * performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
// * valueCodeableConcept = $cs-sct#260415000 "Not detected (qualifier value)"
// * specimen = Reference(urn:uuid:ee1e26a1-caba-45f7-928e-d93fc1a47da9) "Urine specimen (AtApsExampleBundle-Journey-3-diagnostic-specimen-2)"

// Instance: AtApsExampleBundle-Journey-3-diagnostic-result-12
// InstanceOf: AtApsObservationResultsLaboratoryPathology
// Usage: #inline
// * status = #final
// * category = $cs-observation-category#laboratory "Laboratory"
// * code = $cs-loinc#53963-5 "Blood [Presence] in Urine by Visual"
// * subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// * effectiveDateTime = "2025-02-13T14:31:30+00:00"
// * performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
// * valueCodeableConcept = $cs-sct#260415000 "Not detected (qualifier value)"
// * specimen = Reference(urn:uuid:ee1e26a1-caba-45f7-928e-d93fc1a47da9) "Urine specimen (AtApsExampleBundle-Journey-3-diagnostic-specimen-2)"

// Instance: AtApsExampleBundle-Journey-3-diagnostic-result-13
// InstanceOf: AtApsObservationResultsLaboratoryPathology
// Usage: #inline
// * status = #final
// * category = $cs-observation-category#laboratory "Laboratory"
// * code = $cs-loinc#32710-6 "Nitrite [Presence] in Urine"
// * subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// * effectiveDateTime = "2025-02-13T14:31:30+00:00"
// * performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
// * valueCodeableConcept = $cs-sct#260415000 "Not detected (qualifier value)"
// * specimen = Reference(urn:uuid:ee1e26a1-caba-45f7-928e-d93fc1a47da9) "Urine specimen (AtApsExampleBundle-Journey-3-diagnostic-specimen-2)"

// Instance: AtApsExampleBundle-Journey-3-diagnostic-result-14
// InstanceOf: AtApsObservationResultsLaboratoryPathology
// Usage: #inline
// * status = #final
// * category = $cs-observation-category#laboratory "Laboratory"
// * code = $cs-loinc#13658-0 "Urobilinogen [Presence] in Urine"
// * subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
// * effectiveDateTime = "2025-02-13T14:31:30+00:00"
// * performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
// * valueCodeableConcept = $cs-sct#260415000 "Not detected (qualifier value)"
// * specimen = Reference(urn:uuid:ee1e26a1-caba-45f7-928e-d93fc1a47da9) "Urine specimen (AtApsExampleBundle-Journey-3-diagnostic-specimen-2)"

Instance: AtApsExampleBundle-Journey-3-diagnostic-result-15
InstanceOf: AtApsObservationResultsLaboratoryPathology
Usage: #inline
* status = #final
* category[0] = $cs-elga-laborparameterergaenzung#05180 "Klinische Chemie"
* category[+] = $cs-observation-category#laboratory "Laboratory"
* code = $cs-loinc#2339-0 "Glucose [Masse/Volumen] in Blut"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2025-02-13T14:31:30+00:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
* valueQuantity = 112 'mg/dL' "mg/dL"
* specimen = Reference(urn:uuid:5218bc54-5d55-42fa-aa0c-169b61577ad0) "AtApsExampleBundle-Journey-3-diagnostic-specimen-1"

// Diagnostic Results - Performer

Instance: AtApsExampleBundle-Journey-3-diagnostic-result-performer-1
InstanceOf: AtApsOrganization
Usage: #inline
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:oid:1.2.40.0.34.99.4613"
* identifier.assigner.display = "Bundesministerium für Gesundheit"
* name = "Amadeus Spital - Labor"
* telecom[0].system = #phone
* telecom[=].value = "+43.1.3453446.0"
* telecom[+].system = #fax
* telecom[=].value = "+43.1.3453446.4674"
* telecom[+].system = #email
* telecom[=].value = "info@amadeusspital.at"
* telecom[+].system = #url
* telecom[=].value = "https://www.amadeusspital.at"
* address.line = "Währinger Gürtel 18-20"
* address.city = "Wien"
* address.postalCode = "1090"
* address.country = "AUT"

// Vitalparameter (Vital Signs)

Instance: AtApsExampleBundle-Journey-3-vital-sign-1
InstanceOf: AtApsObservationVitalSigns
Usage: #inline
* status = #final
* category[VSCat] = $cs-observation-category#vital-signs "Vital Signs"
* code = $cs-loinc#8302-2 "Körpergröße"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2025-02-08T14:31:30+00:00"
* valueQuantity = 173 'cm' "cm"

Instance: AtApsExampleBundle-Journey-3-vital-sign-2
InstanceOf: AtApsObservationVitalSigns
Usage: #inline
* status = #final
* category[VSCat] = $cs-observation-category#vital-signs "Vital Signs"
* code = $cs-loinc#29463-7 "Körpergewicht"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2025-02-08T14:31:30+00:00"
* valueQuantity = 68 'kg' "kg"

Instance: AtApsExampleBundle-Journey-3-vital-sign-3
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

Instance: AtApsExampleBundle-Journey-3-vital-sign-4
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

Instance: AtApsExampleBundle-Journey-3-vital-sign-5
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

Instance: AtApsExampleBundle-Journey-3-illness-history-1
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#resolved "Resolved"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#14189004 "Masern"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* onsetDateTime = "1994-02-08"

Instance: AtApsExampleBundle-Journey-3-illness-history-2
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#resolved "Resolved"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#38907003 "Windpocken"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* onsetDateTime = "1991"

// Lebensstil / Soziale Umstände und Verhalten (Social History)

Instance: AtApsExampleBundle-Journey-3-social-history-1
InstanceOf: AtApsObservationTobaccoUse
Usage: #inline
* status = #final
* code = $cs-loinc#72166-2 "Raucherstatus"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f473) "Dr. Hanna Hausärztin"
* effectiveDateTime = "2024-02-08T08:30:00+01:00"
* valueCodeableConcept = $cs-sct#266919005 "Nie Tabak geraucht"

Instance: AtApsExampleBundle-Journey-3-social-history-2
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

Instance: AtApsExampleBundle-Journey-3-social-history-3
InstanceOf: AtApsObservationAlcoholUse
Usage: #inline
* status = #final
* code = $cs-loinc#74013-4 "Alcoholic drinks per day"
* code.coding.display = "Alkoholische Getränke pro Tag, 1-2 Gläser Wein/Bier"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* performer = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* effectiveDateTime = "2019-07-15"
* valueQuantity = 2 '/d' "wine glasses per day"

Instance: AtApsExampleBundle-Journey-3-deviceUse-Hueftprothese
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

Instance: AtApsExampleBundle-Journey-3-device-Hueftprothese
InstanceOf: AtApsDevice
Usage: #inline
* type = $cs-sct#67270000 "Hüftprothese"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* deviceName.name = "Hüftprothese"
* deviceName.type = #other
* version.value = "Version.value 123456"


Instance: AtApsExampleBundle-Journey-3-author-device
InstanceOf: Device
Usage: #inline
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Maria Musterfrau"
* type = $cs-sct#49062001 "Gerät"
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Dieses Gerät erzeugt ein APS FHIR-Dokument.</p></div>"
* deviceName.name = "APS Generator"
* deviceName.type = #user-friendly-name

Instance: AtApsExampleBundle-Journey-3-custodian
InstanceOf: AtApsOrganization
Usage: #inline
* name = "Muster-Organization"