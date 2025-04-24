Instance: AtApsExampleImmunization01Unknown
InstanceOf: AtApsImmunization
Title: "AtApsImmunization-Beispiel"
Description: "Immunisierung mit unbekanntem Impfstoff"
Usage: #example
* id = "at-aps-example-immunization-01-unknown"
* language = #de-AT
* status = #completed
* vaccineCode.coding[0] = $sct#787482006 "Unbekannte Immunissierungen"
* patient = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* occurrenceDateTime = "1998-06-04T00:00:00+02:00"
* protocolApplied.targetDisease[0] = $sct#10021000234102 "Masern und Mumps Impfstoffprodukt"
* protocolApplied.doseNumberString = "unknown"