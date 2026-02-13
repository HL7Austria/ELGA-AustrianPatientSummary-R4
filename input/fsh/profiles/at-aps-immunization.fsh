Profile: AtApsImmunization
Parent: Immunization
Id: at-aps-immunization
Title: "AT APS Immunization"
Description: "Das AT APS-Profil für die Immunization-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Immunization"
* ^extension[$imposeProfile].valueCanonical = Canonical(ImmunizationUvIps)
* patient only Reference(AtApsPatient)

* extension contains http://hl7.org/fhir/5.0/StructureDefinition/extension-Immunization.basedOn named ImmunizationBasedOnR5 0..*

* extension[ImmunizationBasedOnR5]
  * ^short = "Authority that the immunization event is based on"
  * ^definition = "This extension implements the R5 basedOn element. A plan, order or recommendation fulfilled in whole or in part by this immunization."
  *  valueReference 1..1
  *  valueReference only Reference(AtApsCarePlan or AtApsMedicationRequest or ServiceRequest or ImmunizationRecommendation)

* manufacturer only Reference(AtApsOrganization)
* performer.actor only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization)
* reasonReference only Reference(AtApsCondition or AtApsObservation or AtApsDiagnosticReport)
* reaction.detail only Reference(AtApsObservation)
* protocolApplied.authority only Reference(AtApsOrganization)

* vaccineCode from $vs-at-aps-immunization-vaccine-codes (extensible)
* vaccineCode ^binding.extension[0].extension[0].url = "purpose"
* vaccineCode ^binding.extension[=].extension[=].valueCode = #candidate
* vaccineCode ^binding.extension[=].extension[+].url = "valueSet"
* vaccineCode ^binding.extension[=].extension[=].valueCanonical = $vs-eimpf-historischeimpfstoffe
* vaccineCode ^binding.extension[=].extension[+].url = "key"
* vaccineCode ^binding.extension[=].extension[=].valueId = "HistoricVaccines"
* vaccineCode ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"

* route from $vs-eimpf-medikationartanwendung (extensible)
* protocolApplied 1..*
* protocolApplied.targetDisease 1..*
* protocolApplied.targetDisease from $vs-eimpf-immunizationtarget (extensible)
