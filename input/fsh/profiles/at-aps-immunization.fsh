Profile: AtApsImmunization
Parent: Immunization
Id: at-aps-immunization
Title: "AT APS Immunization"
Description: "Das AT APS-Profil für die Immunization-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Immunization"
* ^extension[$imposeProfile].valueCanonical = Canonical(ImmunizationUvIps)
* patient only Reference(AtApsPatient)
* extension contains AtApsExtImmunizationBasedOn named basedOn 0..1

* vaccineCode from AtApsImmunizationVaccineCodes (extensible)
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
