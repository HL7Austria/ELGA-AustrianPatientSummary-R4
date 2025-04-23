ValueSet: AtApsObservationInterpretation
Id: at-aps-observationinterpretation
Title: "AT APS ObservationInterpretation"
Description: "This value set extends the existing value set from ELGA GmbH."
* ^meta.profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
* ^status = #active
* ^experimental = false
* ^publisher = "ELGA GmbH"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "https://elga.gv.at"
* ^immutable = false
* include codes from valueset $vs-observation-interpretation
* include codes from system $cs-elga-ergaenzungsliste
* include codes from system $cs-rast-klassen