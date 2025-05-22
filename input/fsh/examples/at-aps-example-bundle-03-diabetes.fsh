Instance: AtApsExample03Diabetes
InstanceOf: AtApsBundle
Title: "AtApsBundle-Beispiel 3"
Description: "Diabetes Checklist / Leitdokument"
Usage: #example
* identifier.system = "http://system-to-be-defined.com"
* identifier.value = "63fef90a-be11-4ddf-aece-d77da15c4f20"
* type = #document
* timestamp = "2025-01-08T14:01:30+00:00"
// Composition
* entry[0].fullUrl = "urn:uuid:212fdc76-ccc3-40bf-8cdd-82f2ef88bd7b"
* entry[=].resource = AtApsExample03Diabetes-composition
// Patient
* entry[+].fullUrl = "urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8"
* entry[=].resource = AtApsExample03Diabetes-patient
// Author
* entry[+].fullUrl = "urn:uuid:75db30ee-7028-486c-929a-c5126837f472"
* entry[=].resource = AtApsExample03Diabetes-author
// Organisation
* entry[+].fullUrl = "urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6"
* entry[=].resource = AtApsExample03Diabetes-organization
// Problem List
* entry[+].fullUrl = "urn:uuid:72e85b9d-004d-4104-b166-86d129948bae"
* entry[=].resource = AtApsExample03Diabetes-problem-1
* entry[+].fullUrl = "urn:uuid:82fa32f6-39d6-4fc9-9624-90a48fd3d3a5"
* entry[=].resource = AtApsExample03Diabetes-problem-2
* entry[+].fullUrl = "urn:uuid:61db6213-22ab-405a-825a-0ae6905fad1e"
* entry[=].resource = AtApsExample03Diabetes-problem-3
* entry[+].fullUrl = "urn:uuid:61db6213-22ab-405a-825a-0ae6905fad2e"
* entry[=].resource = AtApsExample03Diabetes-problem-6
* entry[+].fullUrl = "urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde"
* entry[=].resource = AtApsExample03Diabetes-problem-5
// Problem List - Family history
* entry[+].fullUrl = "urn:uuid:caa77334-fbfc-4129-a101-1b01c595dd91"
* entry[=].resource = AtApsExample03Diabetes-problem-14
// Problem List - periodontal disease risk
* entry[+].fullUrl = "urn:uuid:fa46fccb-5c24-4a40-a478-d6da4902ff33"
* entry[=].resource = AtApsExample03Diabetes-problem-17
* entry[+].fullUrl = "urn:uuid:f235c566-01aa-457d-ab49-9e422df69863"
* entry[=].resource = AtApsExample03Diabetes-problem-17-assessment-1 //21
// Schulungen
* entry[+].fullUrl = "urn:uuid:39cd75da-2456-46a9-a703-89d8b65ae63b"
* entry[=].resource = AtApsExample03Diabetes-schulung-1
// Medication Summary
* entry[+].fullUrl = "urn:uuid:acac4c94-a752-4cf5-9a6b-0d84237d5076"
* entry[=].resource = AtApsExample03Diabetes-medication-summary-1
// Allergies and Intolerances
* entry[+].fullUrl = "urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b"
* entry[=].resource = AtApsExample03Diabetes-allergy-1
// History of Procedures
* entry[+].fullUrl = "urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a"
* entry[=].resource = AtApsExample03Diabetes-procedure-history-1
// // Diagnostic Results
* entry[+].fullUrl = "urn:uuid:725bcf71-22e6-473b-a879-49a4b63cd654"
* entry[=].resource = AtApsExample03Diabetes-diagnostic-result-1
// // Diagnostic Results - Performer
* entry[+].fullUrl = "urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6"
* entry[=].resource = AtApsExample03Diabetes-diagnostic-result-performer-1
// // Diagnostic Results - Specimen
* entry[+].fullUrl = "urn:uuid:e3567418-073e-4fd7-af4e-5fd7ee4785f7"
* entry[=].resource = AtApsExample03Diabetes-diagnostic-specimen-1
// Vital Signs
* entry[+].fullUrl = "urn:uuid:74c5e186-d765-4c93-a624-c9b0746e8142"
* entry[=].resource = AtApsExample03Diabetes-vital-sign-1
// Past History of Illness
* entry[+].fullUrl = "urn:uuid:82301518-66ca-4b4c-821d-087adf643cc4"
* entry[=].resource = AtApsExample03Diabetes-illness-history-1
// Social History
* entry[+].fullUrl = "urn:uuid:d0a5bbf1-6d01-4d44-bac5-05f12c98411e"
* entry[=].resource = AtApsExample03Diabetes-social-history-1

Instance: AtApsExample03Diabetes-composition
InstanceOf: AtApsComposition
Usage: #inline
// * language = #de-AT
* status = #final
* type = $cs-loinc#60591-5 "Patient summary"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* date = "2024-02-08T14:01:30+00:00"
* author = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "Dr. IV-Ärztin"
* title = "Diabetes Leitdokument"
* custodian = Reference(urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6) "Muster-Organisation"
* extension[countryOfAffiliation].valueString = "AT"
// Medication Summary
* section[sectionMedications].title = "Medikationsliste"
* section[sectionMedications].code = $cs-loinc#10160-0 "Medikationsanamnese"
* section[sectionMedications].text.status = #empty
* section[sectionMedications].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionMedications].entry[medicationStatement][0] = Reference(urn:uuid:acac4c94-a752-4cf5-9a6b-0d84237d5076) "AtApsExample03Diabetes-medication-summary-1"
// Allergies and Intolerances
* section[sectionAllergies].title = "Allergien und Intoleranzen"
* section[sectionAllergies].code = $cs-loinc#48765-2 "Allergien und unerwünschte Wirkungen"
* section[sectionAllergies].text.status = #empty
* section[sectionAllergies].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionAllergies].entry[allergyOrIntolerance][0] = Reference(urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b) "AtApsExample03Diabetes-allergy-1"
// Problem List
* section[sectionProblems].title = "Gesundheitsprobleme und Risiken"
* section[sectionProblems].code = $cs-loinc#11450-4 "Problemliste"
* section[sectionProblems].text.status = #empty
* section[sectionProblems].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionProblems].entry[problem][0] = Reference(urn:uuid:72e85b9d-004d-4104-b166-86d129948bae) "AtApsExample03Diabetes-problem-1"
* section[sectionProblems].entry[problem][+] = Reference(urn:uuid:82fa32f6-39d6-4fc9-9624-90a48fd3d3a5) "AtApsExample03Diabetes-problem-2"
* section[sectionProblems].entry[problem][+] = Reference(urn:uuid:61db6213-22ab-405a-825a-0ae6905fad1e) "AtApsExample03Diabetes-problem-3"
* section[sectionProblems].entry[problem][+] = Reference(urn:uuid:61db6213-22ab-405a-825a-0ae6905fad2e) "AtApsExample03Diabetes-problem-6"
* section[sectionProblems].entry[problem][+] = Reference(urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde) "AtApsExample03Diabetes-problem-5"
// Problem List - Family history
* section[sectionProblems].entry[problem][+] = Reference(urn:uuid:caa77334-fbfc-4129-a101-1b01c595dd91) "AtApsExample03Diabetes-problem-14"
// Problem List - periodontal disease risk
* section[sectionProblems].entry[problem][+] = Reference(urn:uuid:fa46fccb-5c24-4a40-a478-d6da4902ff33) "AtApsExample03Diabetes-problem-17"
// History of Procedures
* section[sectionProceduresHx].title = "Eingriffe und Therapien"
* section[sectionProceduresHx].code = $cs-loinc#47519-4 "Anamnese der Prozeduren oder Maßnahmen"
* section[sectionProceduresHx].text.status = #empty
* section[sectionProceduresHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionProceduresHx].entry[procedure][0] = Reference(urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a) "AtApsExample03Diabetes-procedure-history-1"
// Medical Devices
* section[sectionMedicalDevices].title = "Implantate, medizinische Geräte und Heilbehelfe"
* section[sectionMedicalDevices].code = $cs-loinc#46264-8 "Anamnese zum Einsatz von Medizinprodukten"
* section[sectionMedicalDevices].text.status = #empty
* section[sectionMedicalDevices].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionMedicalDevices].emptyReason = $cs-list-empty-reason#nilknown
// Diagnostic Results
* section[sectionResults].title = "Diagnostische Resultate"
* section[sectionResults].code = $cs-loinc#30954-2 "Relevante diagnostische Tests und/oder Labordaten"
* section[sectionResults].text.status = #empty
* section[sectionResults].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionResults].entry[resultsObservationLaboratoryPathology][0] = Reference(urn:uuid:725bcf71-22e6-473b-a879-49a4b63cd654) "AtApsExample03Diabetes-diagnostic-result-1"
//* section[sectionResults].entry[+] = Reference(urn:uuid:aeff2319-2cc2-4fba-9541-7a4de3d20f91)
// Vital Signs
* section[sectionVitalSigns].title = "Vitalparameter"
* section[sectionVitalSigns].code = $cs-loinc#8716-3 "Vitalparameter"
* section[sectionVitalSigns].text.status = #empty
* section[sectionVitalSigns].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionVitalSigns].entry[vitalSign][0] = Reference(urn:uuid:74c5e186-d765-4c93-a624-c9b0746e8142) "AtApsExample03Diabetes-vital-sign-1"
// Past History of Illness
* section[sectionPastIllnessHx].title = "Vergangene Gesundheitsprobleme und Risiken"
* section[sectionPastIllnessHx].code = $cs-loinc#11348-0 "Vergangene Gesundheitsprobleme und Risiken"
* section[sectionPastIllnessHx].text.status = #empty
* section[sectionPastIllnessHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionPastIllnessHx].entry[pastProblem][0] = Reference(urn:uuid:82301518-66ca-4b4c-821d-087adf643cc4) "AtApsExample03Diabetes-illness-history-1"
// Care Plan
* section[sectionPlanOfCare].title = "Behandlungsplan"
* section[sectionPlanOfCare].code = $cs-loinc#18776-5 "Behandlungsplan - Notiz"
* section[sectionPlanOfCare].text.status = #empty
* section[sectionPlanOfCare].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionPlanOfCare].entry[carePlan][0] = Reference(urn:uuid:39cd75da-2456-46a9-a703-89d8b65ae63b) "AtApsExample03Diabetes-schulung-1"
// Social History
* section[sectionSocialHistory].title = "Lebensstil / Soziale Umstände und Verhalten"
* section[sectionSocialHistory].code = $cs-loinc#29762-2 "Sozialanamnese"
* section[sectionSocialHistory].text.status = #empty
* section[sectionSocialHistory].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Narrativer Text muss generiert werden.</p></div>"
* section[sectionSocialHistory].entry[smokingTobaccoUse][0] = Reference(urn:uuid:d0a5bbf1-6d01-4d44-bac5-05f12c98411e) "AtApsExample03Diabetes-social-history-1"

Instance: AtApsExample03Diabetes-patient
InstanceOf: AtApsPatient
Usage: #inline
* id = "001"
* identifier[socialSecurityNumber].type = $cs-v2-0203#SS "Social Security number"
* identifier[socialSecurityNumber].system = "urn:oid:1.2.40.0.10.1.4.3.1"
* identifier[socialSecurityNumber].value = "0000121150"
* identifier[socialSecurityNumber].assigner.display = "Dachverband der österreichischen Sozialversicherungsträger"
* identifier[localPatientId].type = $cs-v2-0203#PI "Patient internal identifier"
* identifier[localPatientId].system = "urn:oid:1.2.3.4.5"
* identifier[localPatientId].value = "0002"
* identifier[localPatientId].assigner.display = "Ein GDA in Österreich"
* name.family = "Testpatientin"
* name.given[0] = "Susi"
* gender = #female // 1..1 in AT Core
* birthDate = "1950-11-12" // 1..1 in IPS
* address.line = "Am Schulweg 5"
* address.use = #home
* address.city = "Hainfeld"
* address.postalCode = "3100"
* address.country = "AUT"

Instance: AtApsExample03Diabetes-author
InstanceOf: AtApsPractitioner
Usage: #inline
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:oid:1.2.40.0.10.99.1.2.3.4"
* identifier.assigner.display = "Bundesministerium für Gesundheit"
* name.prefix[0] = "Dr."
* name.family = "IV-Ärztin"
* name.given[0] = "Gabriele"

// Problem List

// Diabetes Hauptdiagnose
Instance: AtApsExample03Diabetes-problem-3
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
//* category[diabetes] = VsIvDiagnosekategorie#73211009 "Diabetes mellitus"
* code = $cs-sct#105401000119101 "Diabetes mellitus aufgrund einer Verletzung der Bauchspeicheldrüse"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* recordedDate = "2024-02-08T14:01:30+00:00"

// // Diabetes Nebendiagnosen
Instance: AtApsExample03Diabetes-problem-6
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#280137006 "Diabetischer Fuß"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* recordedDate = "2021-02-08T14:01:30+00:00"

Instance: AtApsExample03Diabetes-problem-1
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#700379002 "CKD - Chronische Niereninsuffizienz Grad 3B"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: AtApsExample03Diabetes-problem-2
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#711150003 "Langfristige Einnahme von Antikoagulantien"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: AtApsExample03Diabetes-problem-5
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#38341003 "Arterielle Hypertonie"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"


// Problem List - Family history

Instance: AtApsExample03Diabetes-problem-13
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#160303001 "Diabetes mellitus in der Familienanamnese"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: AtApsExample03Diabetes-problem-14
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#312824007 "Familienanamnese: Kolonkarzinom"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: AtApsExample03Diabetes-problem-15
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#134439009 "Familienanamnese: vorzeitige koronare Herzkrankheit"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: AtApsExample03Diabetes-problem-16
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active "Active"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#160314003 "Hypercholesterinämie in der Familienanamnese"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

// risk of periodontal disease
Instance: AtApsExample03Diabetes-problem-17
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#inactive "Inactive"
* verificationStatus = $cs-condition-ver-status#provisional "Provisional"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#2556008 "Parodontalerkrankung"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* stage.assessment = Reference(urn:uuid:f235c566-01aa-457d-ab49-9e422df69863) "AtApsExample03Diabetes-problem-17-assessment-1"

Instance: AtApsExample03Diabetes-problem-17-assessment-1
InstanceOf: Observation
Usage: #inline
* status = #final
* category = $cs-observation-category#exam "Exam"
* code = $cs-sct#1237049003 "Bewertung der Risikofaktoren für Parodontalerkrankungen"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "Dr. IV-Ärztin"
* effectiveDateTime = "2024-02-08T08:30:00+01:00"
* valueCodeableConcept = $cs-sct#723509005 "Hohes Risiko"

// Careplan Schulungen

Instance: AtApsExample03Diabetes-schulung-1
InstanceOf: CarePlan
Usage: #inline
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Schulung zur Verbesserung der Mobilität </p></div>"
* identifier.value = "12345"
* instantiatesUri = "http://example.org/protocol-for-heart-association-event"
* basedOn.display = "Schulungen für Diabetespatienten"
* replaces.display = "Plan"
* partOf.display = "Plan"
* status = #active
* intent = #plan
* category.text = "Plan zur Patientenschulung"
* title = "Spezialschulung für Diabetespatienten mit Retinophatie"
* description = "Information über eine Veranstaltung des Diabetes"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* period.end = "2024-04-12"
* created = "2024-03-29"
* author = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "Dr. IV-Ärztin"
* addresses = Reference(urn:uuid:61db6213-22ab-405a-825a-0ae6905fad1e) "AtApsExample03Diabetes-problem-3"
* activity.outcomeCodeableConcept = $cs-sct#408443003 "Allgemeines Verfahren"
// * activity.outcomeReference = Reference(Observation/example) "Patient ist über das Ereignis informiert" // ??
* activity.detail.code.coding[0] = $cs-sct#409063005 "Beratung"
* activity.detail.code.coding[+] = $cs-sct#1293061000168108 "Dienst für Gesundheitsförderung"
* activity.detail.status = #completed
* activity.detail.statusReason.text = "Der Hausarzt informierte den Patienten über eine Veranstaltung des Herzverbandes zur Förderung der Herzgesundheit."
* activity.detail.doNotPerform = false
* activity.detail.scheduledTiming.repeat.frequency = 1
* activity.detail.scheduledTiming.repeat.period = 1
* activity.detail.scheduledTiming.repeat.periodUnit = #d
* activity.detail.location.display = "Informationsveranstaltung des Herzverbandes"
* activity.detail.performer = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"


// Medication Summary

Instance: AtApsExample03Diabetes-medication-summary-1
InstanceOf: AtApsMedicationStatement
Usage: #inline
* status = #active
* medicationCodeableConcept = $cs-asp-liste#2443061 "EBETREXAT TBL 10MG"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* effectivePeriod.start = "2024-02-08T10:31:58+02:00"
// "S:0-0-0-2 / FR"
* dosage.sequence = 1
* dosage.timing.repeat.when = $cs-event-timing#NIGHT "Night"
* dosage.timing.repeat.dayOfWeek = #fri
* dosage.route = $cs-sct#26643006 "Oraler Verabreichungsweg"
* dosage.doseAndRate.doseQuantity = 2 $cs-elga-medikationmengenart#{TAB} "Tablet"

// Allergies and Intolerances

Instance: AtApsExample03Diabetes-allergy-1
InstanceOf: AtApsAllergyIntolerance // DiabAllergyIntolerance
Usage: #inline
* clinicalStatus = $cs-allergyintolerance-clinical#active "Active"
* code = $cs-sct#89055006 "Benzylpenicillin-Natrium"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
//* text.div = "Das ist eine optionale Beschreibung der Allergie des Arztes." // ??
* asserter = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "Dr. IV-Ärztin"



// History of Procedures

Instance: AtApsExample03Diabetes-procedure-history-1
InstanceOf: AtApsProcedure
Usage: #inline
* status = #completed
* code = $cs-sct#770606008 "Totalersatz des linken Hüftgelenks"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performedDateTime = "2010"

// Diagnostic Results

Instance: AtApsExample03Diabetes-diagnostic-result-1
InstanceOf: AtApsObservationResultsLaboratoryPathology
Usage: #inline
* status = #final
* category[0] = $cs-observation-category#laboratory "Laboratory"
* category[+] = $cs-elga-laborparameterergaenzung#300 "Hämatologie"
* code = $cs-loinc#882-1 "AB0 und Rh-Blutgruppensysteme [Typ] in Blut"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* effectiveDateTime = "2024-02-08T07:34:06+01:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6) "Amadeus Spital - Labor"
* valueCodeableConcept = $cs-sct#278149003 "Blutgruppe A Rh(D) positiv"
* specimen = Reference(urn:uuid:e3567418-073e-4fd7-af4e-5fd7ee4785f7) "AtApsExample03Diabetes-diagnostic-specimen-1"

// Diagnostic Results - Performer
Instance: AtApsExample03Diabetes-diagnostic-result-performer-1
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

// Diagnostic Results - Specimen

Instance: AtApsExample03Diabetes-diagnostic-specimen-1
InstanceOf: AtApsSpecimen
Usage: #inline
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* status = $cs-specimen-status#unavailable "Unavailable"
* type = $cs-sct#119297000 "Blutprobe"

// Vital Signs

Instance: AtApsExample03Diabetes-vital-sign-1
InstanceOf: AtApsObservationVitalSigns
Usage: #inline
* status = #final
* language = #de-AT
* category[VSCat] = $cs-observation-category#vital-signs "Vital Signs"
* code = $cs-loinc#8302-2 "Körpergröße"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "Dr. IV-Ärztin"
* effectiveDateTime = "2024-02-08T08:30:00+01:00"
* valueQuantity = 173 'cm' "cm"


// Past History of Illness

Instance: AtApsExample03Diabetes-illness-history-1
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#resolved "Resolved"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#161419000 "Zustand nach Masern"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: AtApsExample03Diabetes-illness-history-2
InstanceOf: AtApsCondition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#resolved "Resolved"
* verificationStatus = $cs-condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $cs-condition-category#problem-list-item "Problem List Item"
* code = $cs-sct#161423008 "Zustand nach Windpocken"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

// Social History

Instance: AtApsExample03Diabetes-social-history-1
InstanceOf: AtApsObservationTobaccoUse
Usage: #inline
* status = #final
* code = $cs-loinc#72166-2 "Raucherstatus"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "Dr. IV-Ärztin"
* effectiveDateTime = "2019-07-15"
* valueCodeableConcept = $cs-sct#8517006 "Ehemalig rauchende Person"

Instance: AtApsExample03Diabetes-social-history-2
InstanceOf: Observation
Usage: #inline
* status = #final
* code = $cs-sct#61686008 "Körperliche Aktivität"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performer = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "Dr. IV-Ärztin"
* effectiveDateTime = "2024-02-08T08:30:00+01:00"
* valueRatio.numerator = 2.5 'h' "h"
* valueRatio.numerator.comparator = #>
* valueRatio.denominator = 1 'wk' "wk"

Instance: AtApsExample03Diabetes-organization
InstanceOf: AtApsOrganization
Usage: #inline
* name = "Muster-Organization"