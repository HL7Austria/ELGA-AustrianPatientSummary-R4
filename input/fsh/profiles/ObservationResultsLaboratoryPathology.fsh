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
* valueCodeableConcept ^binding.strength = #extensible
* valueCodeableConcept ^binding.extension[0].extension[0].url = "purpose"
* valueCodeableConcept ^binding.extension[=].extension[=].valueCode = #extensible
* valueCodeableConcept ^binding.extension[=].extension[+].url = "valueSet"
* valueCodeableConcept ^binding.extension[=].extension[=].valueCanonical = "https://termgit.elga.gv.at/ValueSet/elga-nachweisergebnis"
* valueCodeableConcept ^binding.extension[=].extension[+].url = "documentation"
* valueCodeableConcept ^binding.extension[=].extension[=].valueMarkdown = "An additional binding to the ELGA Valueset \"Nachweisergebnis\" - to include missing values of the IPS ValueSet."
* valueCodeableConcept ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"
* code from AtApsLaboratoryPathologyCodes (extensible)
* interpretation from $laboratory-interpretation (extensible)
* category from AtApsLaboratoryPathologyCategory (extensible)