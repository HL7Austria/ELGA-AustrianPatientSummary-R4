Instance: AtApsExampleImmunization01Unknown
InstanceOf: AtApsImmunization
Title: "AtApsImmunization-Beispiel"
Description: "Immunisierung mit unbekanntem Impfstoff"
Usage: #example
* id = "at-aps-example-immunization-01-unknown"
* language = #de-AT
* status = #completed
* vaccineCode.coding[0] = $cs-sct#787482006 "Unbekannte Immunisierungen"
* patient = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* occurrenceDateTime = "1998-06-04T00:00:00+02:00"
* protocolApplied.targetDisease[0] = $cs-sct#836499004 "Masern-Mumps Impfstoffkombination"
* protocolApplied.doseNumberString = "unknown"