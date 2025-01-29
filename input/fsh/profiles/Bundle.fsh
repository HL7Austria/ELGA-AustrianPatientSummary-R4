Profile: AtIpsBundle
Parent: Bundle
Id: at-ips-bundle
Title: "AT IPS Bundle"
Description: "This AT IPS profile for the Bundle resource is derived from the general Bundle resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Bundle"
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
    Clinicalimpression 0..* and
    Careplan 0..* and
    Consent 0..* and
    Documentreference 0..*

* entry[Composition].resource 1..
* entry[Composition].resource only AtIpsComposition

* entry[Patient].resource 1..
* entry[Patient].resource only AtIpsPatient

* entry[AllergyIntolerance].resource 1..
* entry[AllergyIntolerance].resource only AtIpsAllergyIntolerance

* entry[Condition].resource 1..
* entry[Condition].resource only AtIpsCondition

* entry[Device].resource 1..
* entry[Device].resource only Device // do not use AtIpsDevice here because e.g. no simple Device-author is possible

* entry[DeviceUseStatement].resource 1..
* entry[DeviceUseStatement].resource only AtIpsDeviceUseStatement

* entry[DiagnosticReport].resource 1..
* entry[DiagnosticReport].resource only AtIpsDiagnosticReport

* entry[ImagingStudy].resource 1..
* entry[ImagingStudy].resource only AtIpsImagingStudy

* entry[Immunization].resource 1..
* entry[Immunization].resource only AtIpsImmunization

* entry[Medication].resource 1..
* entry[Medication].resource only AtIpsMedication

* entry[MedicationRequest].resource 1..
* entry[MedicationRequest].resource only AtIpsMedicationRequest

* entry[MedicationStatement].resource 1..
* entry[MedicationStatement].resource only AtIpsMedicationStatement

* entry[Practitioner].resource 1..
* entry[Practitioner].resource only AtIpsPractitioner

* entry[PractitionerRole].resource 1..
* entry[PractitionerRole].resource only AtIpsPractitionerRole

* entry[Procedure].resource 1..
* entry[Procedure].resource only AtIpsProcedure

* entry[Organization].resource 1..
* entry[Organization].resource only AtIpsOrganization

* entry[ObservationPregnancyEdd].resource 1..
* entry[ObservationPregnancyEdd].resource only AtIpsObservationPregnancyEdd

* entry[ObservationPregnancyOutcome].resource 1..
* entry[ObservationPregnancyOutcome].resource only AtIpsObservationPregnancyOutcome

* entry[ObservationPregnancyStatus].resource 1..
* entry[ObservationPregnancyStatus].resource only AtIpsObservationPregnancyStatus

* entry[ObservationAlcoholUse].resource 1..
* entry[ObservationAlcoholUse].resource only AtIpsObservationAlcoholUse

* entry[ObservationTobaccoUse].resource 1..
* entry[ObservationTobaccoUse].resource only AtIpsObservationTobaccoUse

* entry[ObservationResultsLaboratoryPathology].resource 1..
* entry[ObservationResultsLaboratoryPathology].resource only AtIpsObservationResultsLaboratoryPathology

* entry[ObservationResultsRadiology].resource 1..
* entry[ObservationResultsRadiology].resource only AtIpsObservationResultsRadiology

* entry[ObservationVitalSigns].resource 1..
* entry[ObservationVitalSigns].resource only AtIpsObservationVitalSigns

* entry[Specimen].resource 1..
* entry[Specimen].resource only AtIpsSpecimen

* entry[Flag].resource 1..
* entry[Flag].resource only FlagAlertUvIps

* entry[Clinicalimpression].resource 1..
* entry[Clinicalimpression].resource only ClinicalImpression

* entry[Careplan].resource 1..
* entry[Careplan].resource only CarePlan

* entry[Consent].resource 1..
* entry[Consent].resource only Consent

* entry[Documentreference].resource 1..
* entry[Documentreference].resource only DocumentReference