Profile: AtApsObservationResultsLaboratoryPathology
Parent: AtApsObservation
Id: at-aps-observationresultslaboratorypathology
Title: "AT APS Observation Results Laboratory Pathology"
Description: "Das AT APS-Profil für die Observation-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Observation Results Laboratory Pathology"
* ^extension[$imposeProfile].valueCanonical = Canonical(ObservationResultsLaboratoryPathologyUvIps)
* subject only Reference(AtApsPatient or Group or Device or Location)
* performer only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or CareTeam or AtApsPatient or RelatedPerson)
* specimen only Reference(AtApsSpecimen)
* hasMember only Reference(AtApsObservationResultsLaboratoryPathology)

* value[x] ^slicing.discriminator.type = #type
* value[x] ^slicing.discriminator.path = "$this"
* value[x] ^slicing.rules = #open
* valueString only string
* valueString ^sliceName = "valueString"
* valueQuantity only Quantity
* valueQuantity ^sliceName = "valueQuantity"
* valueCodeableConcept from $vs-results-coded-values-laboratory-pathology-uv-ips (extensible)
* valueCodeableConcept ^sliceName = "valueCodeableConcept"
* valueCodeableConcept ^binding.extension[0].extension[0].url = "purpose"
* valueCodeableConcept ^binding.extension[=].extension[=].valueCode = #candidate
* valueCodeableConcept ^binding.extension[=].extension[+].url = "valueSet"
* valueCodeableConcept ^binding.extension[=].extension[=].valueCanonical = $vs-elga-nachweisergebnis
* valueCodeableConcept ^binding.extension[=].extension[+].url = "documentation"
* valueCodeableConcept ^binding.extension[=].extension[=].valueMarkdown = "An additional binding to the ELGA Valueset \"Nachweisergebnis\" - to include missing values of the IPS ValueSet."
* valueCodeableConcept ^binding.extension[=].extension[+].url = "key"
* valueCodeableConcept ^binding.extension[=].extension[=].valueId = "ProofValue"
* valueCodeableConcept ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"

* code only CodeableConcept-uv-ips
* code from $vs-elga-laborparameter (extensible)
* code ^binding.extension[0].extension[0].url = "purpose"
* code ^binding.extension[=].extension[=].valueCode = #extensible
* code ^binding.extension[=].extension[+].url = "valueSet"
* code ^binding.extension[=].extension[=].valueCanonical = $vs-elga-antibiogramm
* code ^binding.extension[=].extension[+].url = "documentation"
* code ^binding.extension[=].extension[=].valueMarkdown = "Additional binding in case of antibiotic susceptibility testing."
* code ^binding.extension[=].extension[+].url = "key"
* code ^binding.extension[=].extension[=].valueId = "Antibiogram"
* code ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"

* category from $vs-elga-laborstruktur (extensible)
// * category only CodeableConcept-uv-ips
// * category ^slicing.discriminator.type = #pattern
// * category ^slicing.discriminator.path = "$this"
// * category ^slicing.rules = #open
// * category ^definition = "A code that classifies the general type of observation being made."
// * category contains laborstruktur 1..*
// * category[laborstruktur] only CodeableConcept-uv-ips
// * category[laborstruktur] from $vs-elga-laborstruktur
// * category[laborstruktur] ^short = "The way of grouping of the test results into clinically meaningful domains (e.g. hematology study, microbiology study, etc.)"

* interpretation from AtApsObservationInterpretation (extensible)

* component
  * code only CodeableConcept-uv-ips
  * code from $vs-elga-laborparameter (extensible)
  * code ^binding.extension[0].extension[0].url = "purpose"
  * code ^binding.extension[=].extension[=].valueCode = #extensible
  * code ^binding.extension[=].extension[+].url = "valueSet"
  * code ^binding.extension[=].extension[=].valueCanonical = $vs-elga-antibiogramm
  * code ^binding.extension[=].extension[+].url = "documentation"
  * code ^binding.extension[=].extension[=].valueMarkdown = "Additional binding in case of antibiotic susceptibility testing."
  * code ^binding.extension[=].extension[+].url = "key"
  * code ^binding.extension[=].extension[=].valueId = "ComponentAntibiogram"
  * code ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"

  * value[x] ^slicing.discriminator.type = #type
  * value[x] ^slicing.discriminator.path = "$this"
  * value[x] ^slicing.rules = #open
  * valueCodeableConcept from $vs-results-coded-values-laboratory-pathology-uv-ips (extensible)
  * valueCodeableConcept ^binding.extension[0].extension[0].url = "purpose"
  * valueCodeableConcept ^binding.extension[=].extension[=].valueCode = #candidate
  * valueCodeableConcept ^binding.extension[=].extension[+].url = "valueSet"
  * valueCodeableConcept ^binding.extension[=].extension[=].valueCanonical = $vs-elga-nachweisergebnis
  * valueCodeableConcept ^binding.extension[=].extension[+].url = "documentation"
  * valueCodeableConcept ^binding.extension[=].extension[=].valueMarkdown = "An additional binding to the ELGA Valueset \"Nachweisergebnis\" - to include missing values of the IPS ValueSet."
  * valueCodeableConcept ^binding.extension[=].extension[+].url = "key"
  * valueCodeableConcept ^binding.extension[=].extension[=].valueId = "ComponentProofValue"
  * valueCodeableConcept ^binding.extension[=].url = "http://hl7.org/fhir/tools/StructureDefinition/additional-binding"

  * interpretation from AtApsObservationInterpretation (extensible)