Profile: AtApsBundle
Parent: Bundle
Id: at-aps-bundle
Title: "AT APS Bundle"
Description: "This AT APS profile for the Bundle resource is derived from the general Bundle resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS Bundle"
* ^extension[$imposeProfile].valueCanonical = Canonical(BundleUvIps)

* entry ^slicing.discriminator[0].type = #profile
* entry ^slicing.discriminator[=].path = "resource"
* entry ^slicing.discriminator[+].type = #type
* entry ^slicing.discriminator[=].path = "resource"
* entry ^slicing.rules = #open
* entry ^slicing.ordered = false

* entry contains
    Composition 1..1 and
    Patient 1..1 and
    AllergyIntolerance 0..* and
    Condition 0..* and
    Device 0..* and
    DeviceUseStatement 0..* and
    DiagnosticReport 0..* and
    ImagingStudy 0..* and
    Immunization 0..* and
    Medication 0..* and
    MedicationRequest 0..* and
    MedicationStatement 0..* and
    Practitioner 0..* and
    PractitionerRole 0..* and
    Procedure 0..* and
    Organization 0..* and
    ObservationPregnancyEdd 0..* and
    ObservationPregnancyOutcome 0..* and
    ObservationPregnancyStatus 0..* and
    ObservationAlcoholUse 0..* and
    ObservationTobaccoUse 0..* and
    ObservationResultsLaboratoryPathology 0..* and
    ObservationResultsRadiology 0..* and
    ObservationVitalSigns 0..* and
    Specimen 0..* and
    Flag 0..* and
    ClinicalImpression 0..* and
    CarePlan 0..* and
    Consent 0..* and
    DocumentReference 0..*

* entry[Composition].resource 1..
* entry[Composition].resource only AtApsComposition

* entry[Patient].resource 1..
* entry[Patient].resource only AtApsPatient

* entry[AllergyIntolerance].resource 1..
* entry[AllergyIntolerance].resource only AtApsAllergyIntolerance

* entry[Condition].resource 1..
* entry[Condition].resource only AtApsCondition

* entry[Device].resource 1..
* entry[Device].resource only Device // do not use AtApsDevice here because e.g. no simple Device-author is possible

* entry[DeviceUseStatement].resource 1..
* entry[DeviceUseStatement].resource only AtApsDeviceUseStatement

* entry[DiagnosticReport].resource 1..
* entry[DiagnosticReport].resource only AtApsDiagnosticReport

* entry[ImagingStudy].resource 1..
* entry[ImagingStudy].resource only AtApsImagingStudy

* entry[Immunization].resource 1..
* entry[Immunization].resource only AtApsImmunization

* entry[Medication].resource 1..
* entry[Medication].resource only AtApsMedication

* entry[MedicationRequest].resource 1..
* entry[MedicationRequest].resource only AtApsMedicationRequest

* entry[MedicationStatement].resource 1..
* entry[MedicationStatement].resource only AtApsMedicationStatement

* entry[Practitioner].resource 1..
* entry[Practitioner].resource only AtApsPractitioner

* entry[PractitionerRole].resource 1..
* entry[PractitionerRole].resource only AtApsPractitionerRole

* entry[Procedure].resource 1..
* entry[Procedure].resource only AtApsProcedure

* entry[Organization].resource 1..
* entry[Organization].resource only AtApsOrganization

* entry[ObservationPregnancyEdd].resource 1..
* entry[ObservationPregnancyEdd].resource only AtApsObservationPregnancyEdd

* entry[ObservationPregnancyOutcome].resource 1..
* entry[ObservationPregnancyOutcome].resource only AtApsObservationPregnancyOutcome

* entry[ObservationPregnancyStatus].resource 1..
* entry[ObservationPregnancyStatus].resource only AtApsObservationPregnancyStatus

* entry[ObservationAlcoholUse].resource 1..
* entry[ObservationAlcoholUse].resource only AtApsObservationAlcoholUse

* entry[ObservationTobaccoUse].resource 1..
* entry[ObservationTobaccoUse].resource only AtApsObservationTobaccoUse

* entry[ObservationResultsLaboratoryPathology].resource 1..
* entry[ObservationResultsLaboratoryPathology].resource only AtApsObservationResultsLaboratoryPathology

* entry[ObservationResultsRadiology].resource 1..
* entry[ObservationResultsRadiology].resource only AtApsObservationResultsRadiology

* entry[ObservationVitalSigns].resource 1..
* entry[ObservationVitalSigns].resource only AtApsObservationVitalSigns

* entry[Specimen].resource 1..
* entry[Specimen].resource only AtApsSpecimen

* entry[Flag].resource 1..
* entry[Flag].resource only FlagAlertUvIps

* entry[ClinicalImpression].resource 1..
* entry[ClinicalImpression].resource only ClinicalImpression

* entry[CarePlan].resource 1..
* entry[CarePlan].resource only CarePlan

* entry[Consent].resource 1..
* entry[Consent].resource only Consent

* entry[DocumentReference].resource 1..
* entry[DocumentReference].resource only DocumentReference