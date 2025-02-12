Profile: AtApsObservationResultsLaboratoryPathology
Parent: Observation
Id: at-aps-observationresultslaboratorypathology
Title: "AT APS Observation Results Laboratory Pathology"
Description: "This AT APS profile for the Observation resource is derived from the \"AtApsObservationResults\" profile and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS Observation Results Laboratory Pathology"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationResultsLaboratoryPathologyUvIps)
* subject only Reference(AtApsPatient or Group or Device or Location)
* performer only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or CareTeam or AtApsPatient or RelatedPerson)
* specimen only Reference(AtApsSpecimen)
* hasMember only Reference(AtApsObservationResultsLaboratoryPathology)
* valueCodeableConcept ^binding.extension[0].extension[0].url = "purpose"
* valueCodeableConcept ^binding.extension[=].extension[=].valueCode = #extensible
* valueCodeableConcept ^binding.extension[=].extension[+].url = "valueSet"
* valueCodeableConcept ^binding.extension[=].extension[=].valueCanonical = "https://termgit.elga.gv.at/ValueSet/elga-nachweisergebnis"
* valueCodeableConcept ^binding.extension[=].extension[+].url = "documentation"
* valueCodeableConcept ^binding.extension[=].extension[=].valueMarkdown = "An additional binding to the ELGA Valueset \"Nachweisergebnis\" - to include missing values of the IPS ValueSet."
* valueCodeableConcept ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"

* code only CodeableConcept-uv-ips
* code from $laboratory-code (preferred)
* code ^binding.extension[0].extension[0].url = "purpose"
* code ^binding.extension[=].extension[=].valueCode = #preferred
* code ^binding.extension[=].extension[+].url = "valueSet"
* code ^binding.extension[=].extension[=].valueCanonical = $laboratory-antibiogramm-code
* code ^binding.extension[=].extension[+].url = "documentation"
* code ^binding.extension[=].extension[=].valueMarkdown = "Additional preferred binding in case of antibiotic susceptibility testing."
* code ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"

* category only CodeableConcept-uv-ips
* category ^slicing.discriminator.type = #pattern
* category ^slicing.discriminator.path = "$this"
* category ^slicing.rules = #open
* category ^definition = "A code that classifies the general type of observation being made."
* category contains laborstruktur 1..*
* category[laborstruktur] only CodeableConcept-uv-ips
* category[laborstruktur] from $laboratory-structure
* category[laborstruktur] ^short = "The way of grouping of the test results into clinically meaningful domains (e.g. hematology study, microbiology study, etc.)"

* interpretation from $laboratory-interpretation (extensible)