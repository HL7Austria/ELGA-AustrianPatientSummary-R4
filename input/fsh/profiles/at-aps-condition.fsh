Profile: AtApsCondition
Parent: Condition
Id: at-aps-condition
Title: "AT APS Condition"
Description: "Das AT APS-Profil für die Condition-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Condition"
* ^extension[$imposeProfile].valueCanonical = Canonical(ConditionUvIps)
* subject only Reference(AtApsPatient)

* category from $vs-problem-type-uv-ips (extensible)
* category ^binding.extension[0].extension[0].url = "purpose"
* category ^binding.extension[=].extension[=].valueCode = #candidate
* category ^binding.extension[=].extension[+].url = "valueSet"
* category ^binding.extension[=].extension[=].valueCanonical = $vs-elga-problemarten
* category ^binding.extension[=].extension[+].url = "key"
* category ^binding.extension[=].extension[=].valueId = "ElgaProblemType"
* category ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"

* severity from $vs-elga-problemseverity (extensible)
* code from ProblemsUvIps (extensible)
* bodySite ^binding.strength = #extensible
* recorder only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsPatient or RelatedPerson)
* asserter only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsPatient or RelatedPerson)
* stage.assessment only Reference(AtApsClinicalImpression or AtApsDiagnosticReport or AtApsObservation)
