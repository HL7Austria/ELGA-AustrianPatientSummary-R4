
Profile: AtApsComposition
Parent: Composition
Id: at-aps-composition
Title: "AT APS Composition"
Description: "This AT APS profile for the Composition resource is derived from the general Composition resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS Composition"
* ^extension[$imposeProfile].valueCanonical = Canonical(CompositionUvIps)
* subject only Reference(AtApsPatient)
* relatesTo.target[x] only Identifier or Reference(Composition or AtApsComposition)
* custodian 1..1
* extension contains CountryOfAffiliation named countryOfAffiliation 1..1
* extension[countryOfAffiliation] ^short = "Country of affiliation of the patient. (e.g. can be ISO 3166 2 or 3 letter code)"

* section ^slicing.discriminator.type = #pattern
* section ^slicing.discriminator.path = "code"
* section ^slicing.rules = #open
* section ^slicing.ordered = false

* section contains
    sectionMedications 1..1 and
    sectionAllergies 1..1 and
    sectionProblems 1..1 and
    sectionProceduresHx 1..1 and
    sectionMedicalDevices 1..1 and
    sectionImmunizations 0..1 and
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
* section[sectionMedications].entry only Reference (MedicationStatement or MedicationRequest or MedicationAdministration or MedicationDispense or DocumentReference)
* section[sectionMedications].entry contains
    medicationStatement 0..* and
    medicationRequest 0..*
* section[sectionMedications].entry[medicationStatement] only Reference(AtApsMedicationStatement)
* section[sectionMedications].entry[medicationRequest] only Reference(AtApsMedicationRequest)

* section[sectionAllergies].code = $loinc#48765-2
* section[sectionAllergies].entry ^slicing.discriminator[0].type = #profile
* section[sectionAllergies].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionAllergies].entry ^slicing.rules = #open
* section[sectionAllergies].entry only Reference (AllergyIntolerance or DocumentReference)
* section[sectionAllergies].entry contains
    allergyOrIntolerance 0..*
* section[sectionAllergies].entry[allergyOrIntolerance] only Reference(AtApsAllergyIntolerance)

* section[sectionProblems].code = $loinc#11450-4
* section[sectionProblems].entry ^slicing.discriminator[0].type = #profile
* section[sectionProblems].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionProblems].entry ^slicing.rules = #open
* section[sectionProblems].entry only Reference(Condition or DocumentReference)
* section[sectionProblems].entry contains
    problem 0..*
* section[sectionProblems].entry[problem] only Reference(AtApsCondition)

// ------ Recommended sections ------ //

* section[sectionProceduresHx] obeys ips-comp-1
* section[sectionProceduresHx].code = $loinc#47519-4
* section[sectionProceduresHx].entry ^slicing.discriminator[0].type = #profile
* section[sectionProceduresHx].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionProceduresHx].entry ^slicing.rules = #open
* section[sectionProceduresHx].entry only Reference(Procedure or DocumentReference)
* section[sectionProceduresHx].entry contains
    procedure 0..*
* section[sectionProceduresHx].entry[procedure] only Reference(AtApsProcedure)

* section[sectionImmunizations].code = $loinc#11369-6
* section[sectionImmunizations].entry ^slicing.discriminator[0].type = #profile
* section[sectionImmunizations].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionImmunizations].entry ^slicing.rules = #open
* section[sectionImmunizations].entry only Reference(Immunization or DocumentReference)
* section[sectionImmunizations].entry contains
    immunization 0..*
* section[sectionImmunizations].entry[immunization] only Reference(AtApsImmunization)

* section[sectionMedicalDevices] obeys ips-comp-1
* section[sectionMedicalDevices].code = $loinc#46264-8
* section[sectionMedicalDevices].entry ^slicing.discriminator[0].type = #profile
* section[sectionMedicalDevices].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionMedicalDevices].entry ^slicing.rules = #open
* section[sectionMedicalDevices].entry only Reference(DeviceUseStatement or DocumentReference)
* section[sectionMedicalDevices].entry contains
    deviceStatement 0..*
* section[sectionMedicalDevices].entry[deviceStatement] only Reference(AtApsDeviceUseStatement)

* section[sectionResults].code = $loinc#30954-2
* section[sectionResults].entry ^slicing.discriminator[0].type = #type
* section[sectionResults].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionResults].entry ^slicing.discriminator[+].type = #profile
* section[sectionResults].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionResults].entry ^slicing.rules = #open
* section[sectionResults].entry only Reference(Observation or DiagnosticReport or DocumentReference)
* section[sectionResults].entry contains
    resultsObservationLaboratoryPathology 0..* and
    resultsObservationRadiology 0..* and
    resultsDiagnosticReport 0..*
* section[sectionResults].entry[resultsObservationLaboratoryPathology] only Reference(AtApsObservationResultsLaboratoryPathology)
* section[sectionResults].entry[resultsObservationRadiology] only Reference(AtApsObservationResultsRadiology)
* section[sectionResults].entry[resultsDiagnosticReport] only Reference(AtApsDiagnosticReport)

// ------ Optional sections ------ //

* section[sectionVitalSigns].code = $loinc#8716-3
* section[sectionVitalSigns].entry ^slicing.discriminator[0].type = #profile
* section[sectionVitalSigns].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionVitalSigns].entry ^slicing.rules = #open
* section[sectionVitalSigns].entry only Reference(Observation or DocumentReference)
* section[sectionVitalSigns].entry contains
    vitalSign 0..*
* section[sectionVitalSigns].entry[vitalSign] only Reference(AtApsObservationVitalSigns)

* section[sectionPastIllnessHx].code = $loinc#11348-0
* section[sectionPastIllnessHx].entry ^slicing.discriminator[0].type = #profile
* section[sectionPastIllnessHx].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionPastIllnessHx].entry ^slicing.rules = #open
* section[sectionPastIllnessHx].entry only Reference(Condition or DocumentReference)
* section[sectionPastIllnessHx].entry contains
    pastProblem 0..*
* section[sectionPastIllnessHx].entry[pastProblem] only Reference(AtApsCondition)

* section[sectionFunctionalStatus].code = $loinc#47420-5
* section[sectionFunctionalStatus].entry ^slicing.discriminator[0].type = #profile
* section[sectionFunctionalStatus].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionFunctionalStatus].entry ^slicing.rules = #open
* section[sectionFunctionalStatus].entry only Reference(Condition or ClinicalImpression or DocumentReference)
* section[sectionFunctionalStatus].entry contains
    disability 0..* and
    functionalAssessment 0..*
* section[sectionFunctionalStatus].entry[disability] only Reference(AtApsCondition)
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
* section[sectionSocialHistory].entry[smokingTobaccoUse] only Reference(AtApsObservationTobaccoUse)
* section[sectionSocialHistory].entry[alcoholUse] only Reference(AtApsObservationAlcoholUse)

* section[sectionPregnancyHx].code = $loinc#10162-6
* section[sectionPregnancyHx].entry ^slicing.discriminator[0].type = #profile
* section[sectionPregnancyHx].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionPregnancyHx].entry ^slicing.rules = #open
* section[sectionPregnancyHx].entry only Reference(Observation or DocumentReference)
* section[sectionPregnancyHx].entry contains
    pregnancyStatus 0..* and
    pregnancyOutcomeSummary 0..*
* section[sectionPregnancyHx].entry[pregnancyStatus] only Reference(AtApsObservationPregnancyStatus)
* section[sectionPregnancyHx].entry[pregnancyOutcomeSummary] only Reference(AtApsObservationPregnancyOutcome)

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
* section[sectionAlerts].entry contains
    alertsFlag 0..*
* section[sectionAlerts].entry[alertsFlag] only Reference(FlagAlertUvIps)

* section[sectionPatientStory].code = $loinc#81338-6

Extension:      CountryOfAffiliation
Id:             country-of-affiliation
Title:          "Country of Affiliation element"
Description:    "Add the element for Country of Affiliation"

* value[x] only string
* value[x] ^short = "The country of affiliation of the patient. (e.g. can be ISO 3166 2 or 3 letter code)"
* value[x] 1..1

Invariant: ips-comp-1
Description: "Either section.entry or emptyReason are present"
Expression: "(entry.reference.exists() or emptyReason.exists())"
Severity: #error