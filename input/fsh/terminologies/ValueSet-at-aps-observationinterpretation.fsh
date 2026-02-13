ValueSet: AtApsObservationInterpretation
Id: at-aps-observationinterpretation
Title: "AT APS ObservationInterpretation"
Description: "Dieses Value-Set bildet die in Österreich gebräuchlichen Interpretationen von Untersuchungsergebnissen ab."
* ^meta.profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
* ^url = "https://termgit.elga.gv.at/ValueSet/at-aps-observationinterpretation"
* ^version = "1.0.0+20260213"
* ^status = #active
* ^experimental = false
* ^date = "2026-02-13"
* ^publisher = "ELGA GmbH"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "https://elga.gv.at"
* ^immutable = false
* include codes from valueset $vs-observation-interpretation
* include codes from system $cs-elga-ergaenzungsliste
* include codes from system $cs-rast-klassen