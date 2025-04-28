Profile: AtApsObservationTobaccoUse
Parent: Observation
Id: at-aps-observationtobaccouse
Title: "AT APS Observation Tobacco Use"
Description: "Das AT APS-Profil für die Observation-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Observation Tobacco Use"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationTobaccoUseUvIps)
* subject only Reference(AtApsPatient)
* valueCodeableConcept from $vs-elga-currentsmokingstatus (extensible)
