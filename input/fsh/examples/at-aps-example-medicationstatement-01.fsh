Instance: AtApsExampleMedicationStatement01
InstanceOf: AtApsMedicationStatement
Title: "AtApsMedicationStatement-Beispiel"
Description: "Medication Statement"
Usage: #example
* status = #active
* medicationReference = Reference(Medication/AtApsExampleMedication01) "Ramipril 5mg Kapseln"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* effectivePeriod.start = "2024-10-01"
* effectivePeriod.end = "2025-03-31"
* informationSource = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"
* reasonCode = $cs-sct#59621000 "Hypertonie"
* reasonCode.text = "Hypertonie"
* dosage.text = "1 Kapsel täglich morgens"
* dosage.route = $cs-sct#26643006 "Oral use"
* dosage.doseAndRate.doseQuantity = 5 'mg' "mg"