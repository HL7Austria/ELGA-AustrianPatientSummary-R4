Profile: AtApsAllergyIntolerance
Parent: AllergyIntolerance
Id: at-aps-allergyintolerance
Title: "AT APS AllergyIntolerance"
Description: "This AT APS profile for the AllergyIntolerance resource is derived from the general AllergyIntolerance resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS AllergyIntolerance"
* ^extension[$imposeProfile].valueCanonical = Canonical(AllergyIntoleranceUvIps)
* patient only Reference(AtApsPatient)
* code from $allergy-intolerance (extensible)
* reaction.manifestation from $allergy-reaction (extensible)
