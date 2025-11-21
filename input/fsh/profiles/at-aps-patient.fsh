Profile: AtApsPatient
Parent: HL7ATCorePatient
Id: at-aps-patient
Title: "AT APS Patient"
Description: """Patientendaten, inkl. Angabe von Kontaktpersonen, Hausarzt bzw. primäre Ansprechpartner.

Um die Vorgaben aus dem Umfeld von MyHealth@EU zu erfüllen, muss ein Vor- und Nachname angegeben werden.

Das AT APS-Profil für die Patient-Ressource ist vom entsprechenden Profil aus dem HL7® Austria FHIR® Core IG abgeleitet und stellt zusätzlich die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird. 
Deshalb ist die Angabe des Geburtsdatums erforderlich."""
* ^status = #active
* . ^short = "AT APS Patient"
* ^extension[$imposeProfile].valueCanonical = Canonical(PatientUvIps)
* name.family 1..1
* name.given 1..*
* birthDate 1..1
* identifier[localPatientId] 1..1