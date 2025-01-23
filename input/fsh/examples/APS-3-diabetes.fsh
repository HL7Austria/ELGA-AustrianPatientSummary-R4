Instance: APS-3-diabetes
InstanceOf: AtIpsBundle
Description: "Diabetes Checklist / Leitdokument"
Usage: #example
* identifier.system = "http://system-to-be-defined.com"
* identifier.value = "63fef90a-be11-4ddf-aece-d77da15c4f20"
* type = #document
* timestamp = "2025-01-08T14:01:30+00:00"
// Composition
* entry[0].fullUrl = "urn:uuid:212fdc76-ccc3-40bf-8cdd-82f2ef88bd7b"
* entry[=].resource = example-diab-leitdokument-composition
// Patient
* entry[+].fullUrl = "urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8"
* entry[=].resource = example-diab-leitdokument-patient
// Author
* entry[+].fullUrl = "urn:uuid:75db30ee-7028-486c-929a-c5126837f472"
* entry[=].resource = example-diab-leitdokument-author
// Organisation
* entry[+].fullUrl = "urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6"
* entry[=].resource = example-diab-organization
// Problem List
* entry[+].fullUrl = "urn:uuid:72e85b9d-004d-4104-b166-86d129948bae"
* entry[=].resource = example-diab-leitdokument-problem-1
* entry[+].fullUrl = "urn:uuid:82fa32f6-39d6-4fc9-9624-90a48fd3d3a5"
* entry[=].resource = example-diab-leitdokument-problem-2
* entry[+].fullUrl = "urn:uuid:61db6213-22ab-405a-825a-0ae6905fad1e"
* entry[=].resource = example-diab-leitdokument-problem-3
* entry[+].fullUrl = "urn:uuid:61db6213-22ab-405a-825a-0ae6905fad2e"
* entry[=].resource = example-diab-leitdokument-problem-6
* entry[+].fullUrl = "urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde"
* entry[=].resource = example-diab-leitdokument-problem-5
// Problem List - Family history
* entry[+].fullUrl = "urn:uuid:caa77334-fbfc-4129-a101-1b01c595dd91"
* entry[=].resource = example-diab-leitdokument-problem-14
// Problem List - periodontal disease risk
* entry[+].fullUrl = "urn:uuid:fa46fccb-5c24-4a40-a478-d6da4902ff33"
* entry[=].resource = example-diab-leitdokument-problem-17
* entry[+].fullUrl = "urn:uuid:f235c566-01aa-457d-ab49-9e422df69863"
* entry[=].resource = example-diab-leitdokument-problem-17-assessment-1 //21
// Schulungen
* entry[+].fullUrl = "urn:uuid:39cd75da-2456-46a9-a703-89d8b65ae63b"
* entry[=].resource = example-diab-leitdokument-schulung-1
// Medication Summary
* entry[+].fullUrl = "urn:uuid:acac4c94-a752-4cf5-9a6b-0d84237d5076"
* entry[=].resource = example-diab-leitdokument-medication-summary-1
// Allergies and Intolerances
* entry[+].fullUrl = "urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b"
* entry[=].resource = example-diab-leitdokument-allergy-1
// History of Procedures
* entry[+].fullUrl = "urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a"
* entry[=].resource = example-diab-leitdokument-procedure-history-1
// // Diagnostic Results
* entry[+].fullUrl = "urn:uuid:725bcf71-22e6-473b-a879-49a4b63cd654"
* entry[=].resource = example-diab-leitdokument-diagnostic-result-1
// // Diagnostic Results - Performer
* entry[+].fullUrl = "urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6"
* entry[=].resource = example-diab-leitdokument-diagnostic-result-performer-1
// Vital Signs
* entry[+].fullUrl = "urn:uuid:74c5e186-d765-4c93-a624-c9b0746e8142"
* entry[=].resource = example-diab-leitdokument-vital-sign-1
// Past History of Illness
* entry[+].fullUrl = "urn:uuid:82301518-66ca-4b4c-821d-087adf643cc4"
* entry[=].resource = example-diab-leitdokument-illness-history-1
// Social History
* entry[+].fullUrl = "urn:uuid:d0a5bbf1-6d01-4d44-bac5-05f12c98411e"
* entry[=].resource = example-diab-leitdokument-social-history-1
// Medical Devices 
* entry[+].fullUrl = "urn:uuid:490dab5c-271e-4736-8a6b-5f6f089d0a05"
* entry[=].resource = example-diab-leitdokument-device-use-1
* entry[+].fullUrl = "urn:uuid:a1a80313-a757-4062-b0d7-d04fd2a04602"
* entry[=].resource = example-diab-device

Instance: example-diab-leitdokument-composition
InstanceOf: AtIpsComposition
Usage: #inline
// * language = #de-AT
* status = #final
* type = $loinc#60591-5 "Patient summary Document"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* date = "2024-02-08T14:01:30+00:00"
* author = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "Dr. IV-Ärztin"
* title = "Diabetes Leitdokument"
* attester.mode = #personal
* attester.party = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* attester.party.display = "Validiert von"
* custodian = Reference(urn:uuid:f6266e6a-f63d-4673-b2de-3dff11e619d6)
* extension[countryOfAffiliation].valueString = "AT"
// Problem List
* section[sectionProblems].title = "Problem List"
* section[sectionProblems].code = $loinc#11450-4 "Problem list - Reported"
* section[sectionProblems].text.status = #empty
* section[sectionProblems].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Problem list - Reported</p></div>"
* section[sectionProblems].entry[0] = Reference(urn:uuid:72e85b9d-004d-4104-b166-86d129948bae)
* section[sectionProblems].entry[+] = Reference(urn:uuid:82fa32f6-39d6-4fc9-9624-90a48fd3d3a5)
* section[sectionProblems].entry[+] = Reference(urn:uuid:61db6213-22ab-405a-825a-0ae6905fad1e) 
* section[sectionProblems].entry[+] = Reference(urn:uuid:61db6213-22ab-405a-825a-0ae6905fad2e) 
* section[sectionProblems].entry[+] = Reference(urn:uuid:9d1c0b74-20c1-4603-a95a-71e6a1dc8fde) 
// Problem List - Family history
* section[sectionProblems].entry[+] = Reference(urn:uuid:caa77334-fbfc-4129-a101-1b01c595dd91)
// Problem List - periodontal disease risk
* section[sectionProblems].entry[+] = Reference(urn:uuid:fa46fccb-5c24-4a40-a478-d6da4902ff33)
// Medication Summary
* section[sectionMedications].title = "Medication Summary"
* section[sectionMedications].code = $loinc#10160-0 "History of Medication use Narrative"
* section[sectionMedications].text.status = #empty
* section[sectionMedications].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>History of Medication use Narrative</p></div>"
* section[sectionMedications].entry[0] = Reference(urn:uuid:acac4c94-a752-4cf5-9a6b-0d84237d5076)
// Allergies and Intolerances
* section[sectionAllergies].title = "Allergies and Intolerances"
* section[sectionAllergies].code = $loinc#48765-2 "Allergies and adverse reactions Document"
* section[sectionAllergies].text.status = #empty
* section[sectionAllergies].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Allergies and adverse reactions Document</p></div>"
* section[sectionAllergies].entry = Reference(urn:uuid:768eb9cb-00f3-4ab1-bfc2-ff835cb3b89b)
// History of Procedures
* section[sectionProceduresHx].title = "History of Procedures"
* section[sectionProceduresHx].code = $loinc#47519-4 "History of Procedures Document"
* section[sectionProceduresHx].text.status = #empty
* section[sectionProceduresHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>History of Procedures Document</p></div>"
* section[sectionProceduresHx].entry[0] = Reference(urn:uuid:75c46c35-8f4e-4232-b026-5672c60d076a)
// Medical Devices
* section[sectionMedicalDevices].title = "Medical Devices"
* section[sectionMedicalDevices].code = $loinc#46264-8 "History of medical device use"
* section[sectionMedicalDevices].text.status = #empty
* section[sectionMedicalDevices].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>narrative needs to be generated</p></div>"
* section[sectionMedicalDevices].entry = Reference(urn:uuid:490dab5c-271e-4736-8a6b-5f6f089d0a05)
// Diagnostic Results
* section[sectionResults].title = "Diagnostic Results"
* section[sectionResults].code = $loinc#30954-2 "Relevant diagnostic tests/laboratory data Narrative"
* section[sectionResults].text.status = #empty
* section[sectionResults].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Relevant diagnostic tests/laboratory data Narrative</p></div>"
* section[sectionResults].entry[0] = Reference(urn:uuid:725bcf71-22e6-473b-a879-49a4b63cd654)
//* section[sectionResults].entry[+] = Reference(urn:uuid:aeff2319-2cc2-4fba-9541-7a4de3d20f91)
// Vital Signs
* section[sectionVitalSigns].title = "Vital Signs"
* section[sectionVitalSigns].code = $loinc#8716-3 "Vital signs"
* section[sectionVitalSigns].text.status = #empty
* section[sectionVitalSigns].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Vital signs</p></div>"
* section[sectionVitalSigns].entry[0] = Reference(urn:uuid:74c5e186-d765-4c93-a624-c9b0746e8142)
// Past History of Illness
* section[sectionPastIllnessHx].title = "Past History of Illness"
* section[sectionPastIllnessHx].code = $loinc#11348-0 "History of Past illness Narrative"
* section[sectionPastIllnessHx].text.status = #empty
* section[sectionPastIllnessHx].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>History of Past illness Narrative</p></div>"
* section[sectionPastIllnessHx].entry[0] = Reference(urn:uuid:82301518-66ca-4b4c-821d-087adf643cc4)
// Social History
* section[sectionSocialHistory].title = "Social History"
* section[sectionSocialHistory].code = $loinc#29762-2 "Social history Narrative"
* section[sectionSocialHistory].text.status = #empty
* section[sectionSocialHistory].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Social history Narrative</p></div>"
* section[sectionSocialHistory].entry[0] = Reference(urn:uuid:d0a5bbf1-6d01-4d44-bac5-05f12c98411e)
// Care Plan
* section[sectionPlanOfCare].title = "Plan of Care"
* section[sectionPlanOfCare].code = $loinc#18776-5 "Plan of care note"
* section[sectionPlanOfCare].text.status = #empty
* section[sectionPlanOfCare].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Plan of care note</p></div>"
* section[sectionPlanOfCare].entry[0] = Reference(urn:uuid:39cd75da-2456-46a9-a703-89d8b65ae63b)

Instance: example-diab-leitdokument-patient
InstanceOf: AtIpsPatient
Usage: #inline
* id = "001"
* identifier[socialSecurityNumber].type = $v2-0203#SS "Social Security number"
* identifier[socialSecurityNumber].system = "urn:oid:1.2.40.0.10.1.4.3.1"
* identifier[socialSecurityNumber].value = "0000121150"
* identifier[socialSecurityNumber].assigner.display = "Dachverband der österreichischen Sozialversicherungsträger"
* identifier[localPatientId].type = $v2-0203#PI "Patient internal identifier"
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

Instance: example-diab-leitdokument-author
InstanceOf: AtIpsPractitioner
Usage: #inline
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:oid:1.2.40.0.10.99.1.2.3.4"
* identifier.assigner.display = "Bundesministerium für Gesundheit"
* name.prefix[0] = "Dr."
* name.family = "IV-Ärztin"
* name.given[0] = "Gabriele"

// Problem List

// Diabetes Hauptdiagnose
Instance: example-diab-leitdokument-problem-3
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
//* category[diabetes] = VsIvDiagnosekategorie#73211009 "Diabetes mellitus"
* code = $sct#105401000119101 "Diabetes mellitus due to pancreatic injury (disorder)"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* recordedDate = "2024-02-08T14:01:30+00:00"

// // Diabetes Nebendiagnosen
Instance: example-diab-leitdokument-problem-6
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#280137006 "Diabetisches Fußsyndrom"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* recordedDate = "2021-02-08T14:01:30+00:00"

Instance: example-diab-leitdokument-problem-1
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#700379002 "Chronic kidney disease stage 3B"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: example-diab-leitdokument-problem-2
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#711150003 "Long-term current use of anticoagulant"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: example-diab-leitdokument-problem-5
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#38341003 "Hypertensive disorder"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"


// Problem List - Family history

Instance: example-diab-leitdokument-problem-13
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#160303001 "Family history of diabetes mellitus (situation)"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: example-diab-leitdokument-problem-14
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#312824007 "Family history of cancer of colon"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: example-diab-leitdokument-problem-15
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#134439009 "Family history: premature coronary heart disease"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: example-diab-leitdokument-problem-16
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#active "Active"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#160314003 "FH: Hypercholesterolemia"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

// risk of periodontal disease
Instance: example-diab-leitdokument-problem-17
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#inactive "Inactive"
* verificationStatus = $condition-ver-status#provisional "Provisional"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#2556008 "Periodontal disease (disorder)"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* stage.assessment = Reference(urn:uuid:f235c566-01aa-457d-ab49-9e422df69863)

Instance: example-diab-leitdokument-problem-17-assessment-1
InstanceOf: Observation
Usage: #inline
* status = #final
* category = $observation-category#exam "Exam"
* code = $sct#1237049003 "Evaluation of risk factors for periodontal disease"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6)
* effectiveDateTime = "2024-02-08T08:30:00+01:00"
* valueCodeableConcept = $sct#723509005 "High risk"

// Careplan Schulungen

Instance: example-diab-leitdokument-schulung-1
InstanceOf: CarePlan
Usage: #inline
* id = "example"
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n <p>Schulung zur Verbesserung der Mobilität </p>\n    </div>"
* contained.resourceType = "Condition"
* contained.clinicalStatus = $condition-clinical#active
* contained.verificationStatus = $condition-ver-status#confirmed
* contained.code.text = "Diabetes"
* contained.subject.reference = "urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8"
* contained.subject.display = "Susi Testpatientin" 
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
* activity.outcomeCodeableConcept = $sct#408443003 "Bereitstellung von Patienteninformationen"
// * activity.outcomeReference = Reference(Observation/example) "Patient ist über das Ereignis informiert" // ??
* activity.detail.code.coding[0] = $sct#409063005 "Beratung"
* activity.detail.code.coding[+] = $sct#1293061000168108 "Dient zur Förderung der Gesundheit"
* activity.detail.status = #completed
* activity.detail.statusReason.text = "Der Hausarzt informierte den Patienten über eine Veranstaltung des Herzverbandes zur Förderung der Herzgesundheit."
* activity.detail.doNotPerform = false
* activity.detail.scheduledTiming.repeat.frequency = 1
* activity.detail.scheduledTiming.repeat.period = 1
* activity.detail.scheduledTiming.repeat.periodUnit = #d
* activity.detail.location.display = "Informationsveranstaltung des Herzverbandes"
* activity.detail.performer = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"


// Medication Summary

Instance: example-diab-leitdokument-medication-summary-1
InstanceOf: AtIpsMedicationStatement
Usage: #inline
* status = #active
* medicationCodeableConcept = $asp#2443061 "EBETREXAT TBL 10MG"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* effectivePeriod.start = "2024-02-08T10:31:58+02:00"
// "S:0-0-0-2 / FR"
* dosage.sequence = 1
* dosage.timing.repeat.when = $event-timing#NIGHT "Night"
* dosage.timing.repeat.dayOfWeek = #fri
* dosage.route = $sct#26643006 "Oral use"
* dosage.doseAndRate.doseQuantity.value = 2
* dosage.doseAndRate.doseQuantity.unit = "Tablet"
* dosage.doseAndRate.doseQuantity.system = "https://standardterms.edqm.eu/"
* dosage.doseAndRate.doseQuantity.code = #15054000"


// Allergies and Intolerances

Instance: example-diab-leitdokument-allergy-1
InstanceOf: AtIpsAllergyIntolerance // DiabAllergyIntolerance
Usage: #inline
* clinicalStatus = $allergyintolerance-clinical#active "Active"
* code = $sct#89055006 "Benzylpenicillin Natrium"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
//* text.div = "Das ist eine optionale Beschreibung der Allergie des Arztes." // ??
* asserter = Reference(urn:uuid:75db30ee-7028-486c-929a-c5126837f472) "Dr. IV-Ärztin"



// History of Procedures

Instance: example-diab-leitdokument-procedure-history-1
InstanceOf: AtIpsProcedure
Usage: #inline
* status = #completed
* code = $sct#770606008 "Total replacement of left hip joint"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performedDateTime = "2010"

// Diagnostic Results

Instance: example-diab-leitdokument-diagnostic-result-1
InstanceOf: AtIpsObservationResultsLaboratoryPathology
Usage: #inline
* status = #final
* category = $observation-category#laboratory "Laboratory"
* code = $loinc#882-1 "ABO and Rh group [Type] in Blood"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* effectiveDateTime = "2024-02-08T07:34:06+01:00"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6)
* valueCodeableConcept = $sct#278149003 "Blood group A Rh(D) positive (finding)"

// Diagnostic Results - Performer
Instance: example-diab-leitdokument-diagnostic-result-performer-1
InstanceOf: AtIpsOrganization
Usage: #inline
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:oid:82f802a7-56a9-49b4-a675-95da08f0d7a6"
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

// Vital Signs

Instance: example-diab-leitdokument-vital-sign-1
InstanceOf: AtIpsObservationVitalSigns
Usage: #inline
* status = #final
* language = #de-AT
* category[VSCat] = $observation-category#vital-signs "Vital Signs"
* code = $loinc#8302-2 "Körpergröße"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6)
* effectiveDateTime = "2024-02-08T08:30:00+01:00"
* valueQuantity.value = 173
* valueQuantity.unit = "cm"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #cm


// Past History of Illness

Instance: example-diab-leitdokument-illness-history-1
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#resolved "Resolved"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#161419000 "History of measles"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

Instance: example-diab-leitdokument-illness-history-2
InstanceOf: AtIpsCondition
Usage: #inline
* clinicalStatus = $condition-clinical#resolved "Resolved"
* verificationStatus = $condition-ver-status#confirmed "Confirmed"
* category.coding[0] = $condition-category#problem-list-item "Problem List Item"
* code = $sct#161423008 "History of chickenpox (situation)"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"

// Social History

Instance: example-diab-leitdokument-social-history-1
InstanceOf: AtIpsObservationTobaccoUse
Usage: #inline
* status = #final
* code = $loinc#72166-2 "Tobacco smoking status"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6)
* effectiveDateTime = "2019-07-15"
* valueCodeableConcept = $current-smoking-status#8517006 "Ex-smoker"

Instance: example-diab-leitdokument-social-history-2
InstanceOf: Observation
Usage: #inline
* status = #final
* code = $sct#61686008 "Physical exercise"
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* performer = Reference(urn:uuid:82f802a7-56a9-49b4-a675-95da08f0d7a6)
* effectiveDateTime = "2024-02-08T08:30:00+01:00"
* valueRatio.numerator.value = 2.5
* valueRatio.numerator.unit = "h"
* valueRatio.numerator.system = "http://unitsofmeasure.org"
* valueRatio.numerator.code = #h
* valueRatio.numerator.comparator = #>
* valueRatio.denominator.value = 1
* valueRatio.denominator.unit = "wk"
* valueRatio.denominator.system = "http://unitsofmeasure.org"
* valueRatio.denominator.code = #wk

Instance: example-diab-leitdokument-device-use-1  //todo
InstanceOf: AtIpsDeviceUseStatement
Usage: #inline
* status = #active
* subject = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* device = Reference(urn:uuid:a1a80313-a757-4062-b0d7-d04fd2a04602)
* timingDateTime.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* timingDateTime.extension.valueCode = #unknown

Instance: example-diab-device
InstanceOf: AtIpsDevice
Usage: #inline
* type = $sct#787483001 "No known device use (situation)"
* patient = Reference(urn:uuid:0fed5ebe-ca8f-4ad1-aba4-ddad45bd6cc8) "Susi Testpatientin"
* deviceName.name = "empty"
* deviceName.type = #other
* version.value = "empty"

Instance: example-diab-organization
InstanceOf: AtIpsOrganization
Usage: #inline
* name = "MusterOrganization"