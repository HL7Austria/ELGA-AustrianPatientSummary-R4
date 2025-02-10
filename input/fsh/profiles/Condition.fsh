Profile: AtApsCondition
Parent: Condition
Id: at-aps-condition
Title: "AT APS Condition"
Description: "This AT APS profile for the Condition resource is derived from the general Condition resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS Condition"
* ^extension[$imposeProfile].valueCanonical = Canonical(ConditionUvIps)
* subject only Reference(AtApsPatient)
* category from $condition-category-vs (extensible)
* severity from $condition-severity-vs (extensible)
* code from AtApsConditionCodeSystems (extensible)
* bodySite ^binding.strength = #extensible