Profile: AtApsOrganization
Parent: HL7ATCoreOrganization
Id: at-aps-organization
Title: "AT APS Organization"
Description: "Das AT APS-Profil für die Organization-Ressource ist vom entsprechenden Profil aus dem HL7® Austria FHIR® Core IG abgeleitet und stellt zusätzlich die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Organization"
* ^extension[$imposeProfile].valueCanonical = Canonical(OrganizationUvIps)
* identifier[GDA-OID].assigner only Reference(AtApsOrganization)
* identifier[VPNR].assigner only Reference(AtApsOrganization)
* identifier[VKZ].assigner only Reference(AtApsOrganization)
* identifier[KANR].assigner only Reference(AtApsOrganization)
* partOf only Reference(AtApsOrganization)