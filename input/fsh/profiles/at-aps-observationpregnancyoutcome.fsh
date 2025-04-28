Profile: AtApsObservationPregnancyOutcome
Parent: Observation
Id: at-aps-observationpregnancyoutcome
Title: "AT APS Observation Pregnancy Outcome"
Description: "Das AT APS-Profil für die Observation-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Observation Pregnancy Outcome"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationPregnancyOutcomeUvIps)
* subject only Reference(AtApsPatient)