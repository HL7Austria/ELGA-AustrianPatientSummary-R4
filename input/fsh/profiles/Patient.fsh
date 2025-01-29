Profile: AtIpsPatient
Parent: HL7ATCorePatient
Id: at-ips-patient
Title: "AT IPS Patient"
Description: "This AT IPS profile for the Patient resource is derived from the corresponding HL7® Austria FHIR® Core profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Patient"
* ^extension[$imposeProfile].valueCanonical = Canonical(PatientUvIps)
* name.family 1..1
* name.given 1..*
* birthDate 1..1
* identifier[localPatientId] 1..1