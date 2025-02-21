Profile: AtApsPatient
Parent: HL7ATCorePatient
Id: at-aps-patient
Title: "AT APS Patient"
Description: "This AT APS profile for the Patient resource is derived from the corresponding HL7® Austria FHIR® Core profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS Patient"
* ^extension[$imposeProfile].valueCanonical = Canonical(PatientUvIps)
* name.family 1..1
* name.given 1..*
* birthDate 1..1
* identifier[localPatientId] 1..1