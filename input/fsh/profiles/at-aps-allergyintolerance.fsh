Profile: AtApsAllergyIntolerance
Parent: AllergyIntolerance
Id: at-aps-allergyintolerance
Title: "AT APS AllergyIntolerance"
Description: "Das AT APS-Profil für die AllergyIntolerance-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS AllergyIntolerance"
* ^extension[$imposeProfile].valueCanonical = Canonical(AllergyIntoleranceUvIps)
* patient only Reference(AtApsPatient)
* code from $vs-elga-allergyorintoleranceagent (extensible)
* reaction.manifestation from $vs-elga-allergyreaction (extensible)
