Profile: AtApsFlagAlert
Parent: Flag
Id: at-aps-flagalert
Title: "AT APS Flag Alert"
Description: "Das AT APS-Profil für die Flag-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Flag Alert"
* ^extension[$imposeProfile].valueCanonical = Canonical(FlagAlertUvIps)
* subject only Reference(AtApsPatient or Location or Group or AtApsOrganization or AtApsPractitioner or PlanDefinition or AtApsMedication or AtApsProcedure)