Profile: AtApsSpecimen
Parent: Specimen
Id: at-aps-specimen
Title: "AT APS Specimen"
Description: "This AT APS profile for the Specimen resource is derived from the general Specimen resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* ^status = #active
* . ^short = "AT APS Specimen"
* ^extension[$imposeProfile].valueCanonical = Canonical(SpecimenUvIps)
* subject only Reference(AtApsPatient)
* type from $elga-probenmaterial (extensible)
* type ^binding.extension[0].extension[0].url = "purpose"
* type ^binding.extension[=].extension[=].valueCode = #candidate
* type ^binding.extension[=].extension[+].url = "valueSet"
* type ^binding.extension[=].extension[=].valueCanonical = $elga-specimentype
* type ^binding.extension[=].extension[+].url = "documentation"
* type ^binding.extension[=].extension[=].valueMarkdown = "An additional binding to the ELGA Valueset \"Specimentype\" - retained for backward compatibility."
* type ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"
* collection.bodySite ^binding.strength = #extensible   // Europe Laboratory Report has an additional bodySite - this might be not relevant vor the IPS/APS: https://hl7.eu/fhir/laboratory/StructureDefinition-Specimen-eu-lab.html

* condition ^slicing.discriminator.type = #pattern
* condition ^slicing.discriminator.path = "$this"
* condition ^slicing.rules = #open
* condition contains insufficientsample 0..1
* condition[insufficientsample] = $sct#281268007 "Insufficient sample (finding)"