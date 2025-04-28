Profile: AtApsPractitionerRole
Parent: HL7ATCorePractitionerRole
Id: at-aps-practitionerrole
Title: "AT APS PractitionerRole"
Description: "Das AT APS-Profil für die PractitionerRole-Ressource ist vom entsprechenden Profil aus dem HL7® Austria FHIR® Core IG abgeleitet und stellt zusätzlich die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "At APS PractitionerRole"
* ^extension[$imposeProfile].valueCanonical = Canonical(PractitionerRoleUvIps)
* practitioner only Reference(AtApsPractitioner)
* organization only Reference(AtApsOrganization)
