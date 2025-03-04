Instance: immunization-vaccine-unknown
InstanceOf: AtApsImmunization
Description: "Immunisierung mit unbekannten Impfstoff"
Usage: #example
* language = #de-AT
* status = #completed
* vaccineCode.coding[0] = $sct#787482006 "No known immunizations"
* patient = Reference(Patient/002) "Maria Musterfrau"
* occurrenceDateTime = "1998-06-04T00:00:00+02:00"
* protocolApplied.targetDisease[0] = $sct-auszug#836499004 "Masern-Mumps Impfstoffkombination"
* protocolApplied.doseNumberString = "unknown"