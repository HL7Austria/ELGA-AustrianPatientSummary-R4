Instance: immunization-vaccine-unknown
InstanceOf: AtIpsImmunization
Description: "Immunisierung mit unbekannten Impfstoff"
Usage: #example
* language = #de-AT
* status = #completed
* vaccineCode.coding[0] = $sct#787859002 "Vaccine product (medicinal product)"
* patient = Reference(Patient/002) "Maria Musterfrau"
* occurrenceDateTime = "1998-06-04T00:00:00+02:00"
* protocolApplied.targetDisease[0] = $immunization-target-disease#36989005 "Mumps"
* protocolApplied.targetDisease[1] = $immunization-target-disease#14189004 "Masern"
* protocolApplied.doseNumberString = "unknown"