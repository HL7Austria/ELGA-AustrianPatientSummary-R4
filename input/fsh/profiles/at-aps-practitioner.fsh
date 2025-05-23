Profile: AtApsPractitioner
Parent: HL7ATCorePractitioner
Id: at-aps-practitioner
Title: "AT APS Practitioner"
Description: "Das AT APS-Profil für die Practitioner-Ressource ist vom entsprechenden Profil aus dem HL7® Austria FHIR® Core IG abgeleitet und stellt zusätzlich die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Practitioner"
* ^extension[$imposeProfile].valueCanonical = Canonical(PractitionerUvIps)
