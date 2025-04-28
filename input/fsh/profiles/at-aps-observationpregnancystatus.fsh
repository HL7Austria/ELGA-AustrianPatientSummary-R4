Profile: AtApsObservationPregnancyStatus
Parent: Observation
Id: at-aps-observationpregnancystatus
Title: "AT APS Observation Pregnancy Status"
Description: "Das AT APS-Profil für die Observation-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Observation Pregnancy Status"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationPregnancyStatusUvIps)
* subject only Reference(AtApsPatient)
* hasMember only Reference(AtApsObservationPregnancyEdd)
* valueCodeableConcept from $vs-elga-pregnancystatus (extensible)
