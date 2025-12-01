Instance: AtApsExampleMedicationAdministration01
InstanceOf: AtApsMedicationAdministration
Title: "AtApsMedicationAdministration-Beispiel"
Description: "Medication Administration"
Usage: #example
* status = #completed
* medicationReference = Reference(Medication/AtApsExampleMedication01) "Ramipril 5mg Kapseln"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* effectiveDateTime = "2024-10-15T08:00:00+01:00"
* performer.actor = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"
* reasonCode = $cs-sct#59621000 "Hypertonie"
* reasonCode.text = "Hypertonie"
* dosage.text = "1 Kapsel täglich morgens"
* dosage.route = $cs-sct#26643006 "Oral use"
* dosage.dose = 5 'mg' "mg"