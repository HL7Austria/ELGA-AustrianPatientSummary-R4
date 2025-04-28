Profile: AtApsPatient
Parent: HL7ATCorePatient
Id: at-aps-patient
Title: "AT APS Patient"
Description: "Das AT APS-Profil für die Patient-Ressource ist vom entsprechenden Profil aus dem HL7® Austria FHIR® Core IG abgeleitet und stellt zusätzlich die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Patient"
* ^extension[$imposeProfile].valueCanonical = Canonical(PatientUvIps)
* name.family 1..1
* name.given 1..*
* birthDate 1..1
* identifier[localPatientId] 1..1