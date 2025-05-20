Profile: AtApsObservationVitalSigns
Parent: AtApsObservation
Id: at-aps-observationvitalsigns
Title: "AT APS Observation Vital Signs"
Description: "Das AT APS-Profil für die Abbildung der Vitalparameter ist abgeleitet vom allgemeinen [\"Vital Signs\"-Profil](http://hl7.org/fhir/StructureDefinition/vitalsigns) und berücksichtigt die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets)."
* ^status = #active
* . ^short = "AT APS Observation Vital Signs"
* ^extension[$imposeProfile].valueCanonical = Canonical(http://hl7.org/fhir/StructureDefinition/vitalsigns)
* category ..* MS
* category only CodeableConcept
* category ^slicing.discriminator[0].type = #value
* category ^slicing.discriminator[=].path = "coding.code"
* category ^slicing.discriminator[+].type = #value
* category ^slicing.discriminator[=].path = "coding.system"
* category ^slicing.ordered = false
* category ^slicing.rules = #open
* category contains VSCat 1..1 MS
* category[VSCat] only CodeableConcept
* category[VSCat].coding 1..* MS
* category[VSCat].coding only Coding
* category[VSCat].coding.system 1..1 MS
* category[VSCat].coding.system only uri
* category[VSCat].coding.system = $cs-observation-category (exactly)
* category[VSCat].coding.code 1..1 MS
* category[VSCat].coding.code only code
* category[VSCat].coding.code = #vital-signs (exactly)
* subject only Reference(AtApsPatient)
