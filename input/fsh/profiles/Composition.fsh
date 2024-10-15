
Profile: AtIpsComposition
Parent: Composition
Id: at-ips-composition
Title: "AT IPS Composition"
Description: "This AT IPS profile for the Composition resource is derived from the general Composition resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Composition"
* ^extension[$imposeProfile].valueCanonical = Canonical(CompositionUvIps)
* subject only Reference(AtIpsPatient)
* relatesTo.target[x] only Identifier or Reference(Composition or AtIpsComposition)

* section ^slicing.discriminator.type = #pattern
* section ^slicing.discriminator.path = "code"
* section ^slicing.rules = #open
* section ^slicing.ordered = false

* section contains
    sectionMedications 1..1 and
    sectionAllergies 1..1 and
    sectionProblems 1..1 and
    sectionProceduresHx 0..1 and
    sectionImmunizations 0..1 and
    sectionMedicalDevices 0..1 and
    sectionResults 0..1 and
    sectionVitalSigns 0..1 and
    sectionPastIllnessHx 0..1 and
    sectionFunctionalStatus 0..1 and
    sectionPlanOfCare 0..1 and
    sectionSocialHistory 0..1 and
    sectionPregnancyHx 0..1 and
    sectionAdvanceDirectives 0..1 and
    sectionAlerts 0..1 and
    sectionPatientStory 0..1

// ------ Required sections ------ //

* section[sectionMedications].code = $loinc#10160-0
* section[sectionMedications].entry ^slicing.discriminator[0].type = #profile
* section[sectionMedications].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionMedications].entry ^slicing.rules = #open
* section[sectionMedications].entry 1..
* section[sectionMedications].entry only Reference (MedicationStatement or MedicationRequest or MedicationAdministration or MedicationDispense or DocumentReference)
* section[sectionMedications].entry contains
    medicationStatement 0..* and
    medicationRequest 0..*
* section[sectionMedications].entry[medicationStatement] only Reference(AtIpsMedicationStatement)
* section[sectionMedications].entry[medicationRequest] only Reference(AtIpsMedicationRequest)

* section[sectionAllergies].code = $loinc#48765-2
* section[sectionAllergies].entry ^slicing.discriminator[0].type = #profile
* section[sectionAllergies].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionAllergies].entry ^slicing.rules = #open
* section[sectionAllergies].entry 1..
* section[sectionAllergies].entry only Reference (AllergyIntolerance or DocumentReference)
* section[sectionAllergies].entry contains
    allergyOrIntolerance 1..*
* section[sectionAllergies].entry[allergyOrIntolerance] only Reference(AtIpsAllergyIntolerance)

* section[sectionProblems].code = $loinc#11450-4
* section[sectionProblems].entry ^slicing.discriminator[0].type = #profile
* section[sectionProblems].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionProblems].entry ^slicing.rules = #open
* section[sectionProblems].entry 1..
* section[sectionProblems].entry only Reference(Condition or DocumentReference)
* section[sectionProblems].entry contains
    problem 1..*
* section[sectionProblems].entry[problem] only Reference(AtIpsCondition)

// ------ Recommended sections ------ //

* section[sectionProceduresHx].code = $loinc#47519-4
* section[sectionProceduresHx].entry ^slicing.discriminator[0].type = #profile
* section[sectionProceduresHx].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionProceduresHx].entry ^slicing.rules = #open
* section[sectionProceduresHx].entry 1..
* section[sectionProceduresHx].entry only Reference(Procedure or DocumentReference)
* section[sectionProceduresHx].entry contains
    procedure 1..*
* section[sectionProceduresHx].entry[procedure] only Reference(AtIpsProcedure)

* section[sectionImmunizations].code = $loinc#11369-6
* section[sectionImmunizations].entry ^slicing.discriminator[0].type = #profile
* section[sectionImmunizations].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionImmunizations].entry ^slicing.rules = #open
* section[sectionImmunizations].entry 1..
* section[sectionImmunizations].entry only Reference(Immunization or DocumentReference)
* section[sectionImmunizations].entry contains
    immunization 1..*
* section[sectionImmunizations].entry[immunization] only Reference(AtIpsImmunization)

* section[sectionMedicalDevices].code = $loinc#46264-8
* section[sectionMedicalDevices].entry ^slicing.discriminator[0].type = #profile
* section[sectionMedicalDevices].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionMedicalDevices].entry ^slicing.rules = #open
* section[sectionMedicalDevices].entry 1..
* section[sectionMedicalDevices].entry only Reference(DeviceUseStatement or DocumentReference)
* section[sectionMedicalDevices].entry contains
    deviceStatement 1..*
* section[sectionMedicalDevices].entry[deviceStatement] only Reference(AtIpsDeviceUseStatement)

* section[sectionResults].code = $loinc#30954-2
* section[sectionResults].entry ^slicing.discriminator[0].type = #type
* section[sectionResults].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionResults].entry ^slicing.discriminator[+].type = #profile
* section[sectionResults].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionResults].entry ^slicing.rules = #open
* section[sectionResults].entry 1..
* section[sectionResults].entry only Reference(Observation or DiagnosticReport or DocumentReference)
* section[sectionResults].entry contains
    resultsObservationLaboratoryPathology 0..* and
    resultsObservationRadiology 0..* and
    resultsDiagnosticReport 0..*
* section[sectionResults].entry[resultsObservationLaboratoryPathology] only Reference(AtIpsObservationResultsLaboratoryPathology)
* section[sectionResults].entry[resultsObservationRadiology] only Reference(AtIpsObservationResultsRadiology)
* section[sectionResults].entry[resultsDiagnosticReport] only Reference(AtIpsDiagnosticReport)

// ------ Optional sections ------ //

* section[sectionVitalSigns].code = $loinc#8716-3
* section[sectionVitalSigns].entry ^slicing.discriminator[0].type = #profile
* section[sectionVitalSigns].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionVitalSigns].entry ^slicing.rules = #open
* section[sectionVitalSigns].entry only Reference(Observation or DocumentReference)
* section[sectionVitalSigns].entry contains
    vitalSign 0..*
* section[sectionVitalSigns].entry[vitalSign] only Reference(AtIpsObservationVitalSigns)

* section[sectionPastIllnessHx].code = $loinc#11348-0
* section[sectionPastIllnessHx].entry ^slicing.discriminator[0].type = #profile
* section[sectionPastIllnessHx].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionPastIllnessHx].entry ^slicing.rules = #open
* section[sectionPastIllnessHx].entry 1..
* section[sectionPastIllnessHx].entry only Reference(Condition or DocumentReference)
* section[sectionPastIllnessHx].entry contains
    pastProblem 1..*
* section[sectionPastIllnessHx].entry[pastProblem] only Reference(AtIpsCondition)

* section[sectionFunctionalStatus].code = $loinc#47420-5
* section[sectionFunctionalStatus].entry ^slicing.discriminator[0].type = #profile
* section[sectionFunctionalStatus].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionFunctionalStatus].entry ^slicing.rules = #open
* section[sectionFunctionalStatus].entry only Reference(Condition or ClinicalImpression or DocumentReference)
* section[sectionFunctionalStatus].entry contains
    disability 0..* and
    functionalAssessment 0..*
* section[sectionFunctionalStatus].entry[disability] only Reference(AtIpsCondition)
* section[sectionFunctionalStatus].entry[functionalAssessment] only Reference(ClinicalImpression)

* section[sectionPlanOfCare].code = $loinc#18776-5
* section[sectionPlanOfCare].entry ^slicing.discriminator[0].type = #profile
* section[sectionPlanOfCare].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionPlanOfCare].entry ^slicing.rules = #open
* section[sectionPlanOfCare].entry only Reference(CarePlan or DocumentReference)
* section[sectionPlanOfCare].entry contains
    carePlan 0..*
* section[sectionPlanOfCare].entry[carePlan] only Reference(CarePlan)

* section[sectionSocialHistory].code = $loinc#29762-2
* section[sectionSocialHistory].entry ^slicing.discriminator[0].type = #profile
* section[sectionSocialHistory].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionSocialHistory].entry ^slicing.rules = #open
* section[sectionSocialHistory].entry only Reference(Observation or DocumentReference)
* section[sectionSocialHistory].entry contains
    smokingTobaccoUse 0..1 and
    alcoholUse 0..1
* section[sectionSocialHistory].entry[smokingTobaccoUse] only Reference(AtIpsObservationTobaccoUse)
* section[sectionSocialHistory].entry[alcoholUse] only Reference(AtIpsObservationAlcoholUse)

* section[sectionPregnancyHx].code = $loinc#10162-6
* section[sectionPregnancyHx].entry ^slicing.discriminator[0].type = #profile
* section[sectionPregnancyHx].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionPregnancyHx].entry ^slicing.rules = #open
* section[sectionPregnancyHx].entry only Reference(Observation or DocumentReference)
* section[sectionPregnancyHx].entry contains
    pregnancyStatus 0..* and
    pregnancyOutcomeSummary 0..*
* section[sectionPregnancyHx].entry[pregnancyStatus] only Reference(AtIpsObservationPregnancyStatus)
* section[sectionPregnancyHx].entry[pregnancyOutcomeSummary] only Reference(AtIpsObservationPregnancyOutcome)

* section[sectionAdvanceDirectives].code = $loinc#42348-3
* section[sectionAdvanceDirectives].entry ^slicing.discriminator[0].type = #profile
* section[sectionAdvanceDirectives].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionAdvanceDirectives].entry ^slicing.rules = #open
* section[sectionAdvanceDirectives].entry only Reference(Consent or DocumentReference)
* section[sectionAdvanceDirectives].entry contains
    advanceDirectivesConsent 0..*
* section[sectionAdvanceDirectives].entry[advanceDirectivesConsent] only Reference(Consent)

* section[sectionAlerts].code = $loinc#104605-1
* section[sectionAlerts].entry ^slicing.discriminator[0].type = #profile
* section[sectionAlerts].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionAlerts].entry ^slicing.rules = #open
* section[sectionAlerts].entry only Reference(Flag or DocumentReference)
* section[sectionAlerts].entry contains alertsFlag 0..*
* section[sectionAlerts].entry[alertsFlag] only Reference(FlagAlertUvIps)

* section[sectionPatientStory].code = $loinc#81338-6
