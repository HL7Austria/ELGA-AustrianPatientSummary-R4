Instance: AtApsExampleMedicationStatement01
InstanceOf: AtApsMedicationStatement
Title: "AtApsMedicationStatement-Beispiel"
Description: "Medication Statement"
Usage: #example
* status = #active
* medicationReference = Reference(Medication/AtApsExampleMedication01) "Ramipril 5mg Kapseln"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* effectivePeriod.start = "2024-10-01"
* effectivePeriod.end = "2025-03-31"
* informationSource = Reference(Practitioner/HL7ATCorePractitionerExample01) "Dr. Melanie Musterärztin"
* reasonCode = $cs-sct#59621000 "Hypertonie"
* reasonCode.text = "Hypertonie"
* dosage.text = "1 Kapsel täglich morgens"
* dosage.route = $cs-sct#26643006 "Oral use"
* dosage.doseAndRate.doseQuantity = 5 'mg' "mg"