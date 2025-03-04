Profile: AtApsImmunization
Parent: Immunization
Id: at-aps-immunization
Title: "AT APS Immunization"
Description: "This AT APS profile for the Immunization resource is derived from the general Immunization resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* ^status = #active
* . ^short = "AT APS Immunization"
* ^extension[$imposeProfile].valueCanonical = Canonical(ImmunizationUvIps)
* patient only Reference(AtApsPatient)
* extension contains ImmunizationBasedOn named basedOn 0..1

* vaccineCode from AtApsImmunizationVaccineCodes (extensible)
* vaccineCode ^binding.extension[0].extension[0].url = "purpose"
* vaccineCode ^binding.extension[=].extension[=].valueCode = #candidate
* vaccineCode ^binding.extension[=].extension[+].url = "valueSet"
* vaccineCode ^binding.extension[=].extension[=].valueCanonical = $eimpf-historischeimpfstoffe
* vaccineCode ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"

* route from $immunization-route (extensible)
* protocolApplied 1..*
* protocolApplied.targetDisease 1..*
* protocolApplied.targetDisease from $vs-eimpf-immunizationtarget (extensible)

Extension:      ImmunizationBasedOn
Id:             immunization-basedOn
Title:          "Immunization basedOn"
Description:    "Authority that the immunization event is based on"
Context:        AtApsImmunization

* value[x] only Reference(CarePlan or MedicationRequest or ServiceRequest or ImmunizationRecommendation)
* value[x] ^short = "Authority that the immunization event is based on"
* value[x] 1..1
