Instance: AtApsExampleMedicationRequest01
InstanceOf: AtApsMedicationRequest
Title: "AtApsMedicationRequest-Beispiel"
Description: "Medication Request"
Usage: #example
* status = #active
* intent = #order
* medicationReference = Reference(Medication/AtApsExampleMedication01) "Ramipril 5mg Kapseln"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* authoredOn = "2024-10-14T10:00:00+01:00"
* requester = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"
* reasonCode = $cs-sct#59621000 "Hypertonie"
* reasonCode.text = "Hypertonie"
* dosageInstruction.text = "1 Kapsel täglich morgens"
* dosageInstruction.timing.repeat.frequency = 1
* dosageInstruction.timing.repeat.period = 1
* dosageInstruction.timing.repeat.periodUnit = #d
* dosageInstruction.route = $cs-sct#26643006 "Oral use"
* dosageInstruction.doseAndRate.doseQuantity = 5 'mg' "mg"
* dispenseRequest.quantity.value = 30
* dispenseRequest.quantity.unit = "Kapseln"
* dispenseRequest.expectedSupplyDuration = 30 'd' "Tage"