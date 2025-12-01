Instance: AtApsExampleSpecimen01
InstanceOf: AtApsSpecimen
Title: "AtApsSpecimen-Beispiel"
Description: "Specimen"
Usage: #example
* identifier.system = "https://elga.gv.at/specimen-id"
* identifier.value = "SPC-2025-0001"
* status = #available
* type = $cs-sct#119376003 "Tissue specimen"
* type.text = "Gewebeprobe"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* receivedTime = "2025-06-20T10:00:00+02:00"
* collection.collector = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"
* collection.collectedDateTime = "2025-06-19T15:00:00+02:00"
* collection.bodySite = $cs-sct#76752008 "Breast structure (body structure)"
* collection.bodySite.text = "Brustgewebe"
* collection.method = $cs-sct#104210008 "Biopsy - action"
* collection.method.text = "Biopsie"
* collection.quantity = 2 '{pieces}' "pieces"
* condition = $cs-sct#281268007 "Insufficient sample (finding)"
* condition.text = "Unzureichende Probe für Analyse"