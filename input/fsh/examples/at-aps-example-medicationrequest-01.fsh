Instance: AtApsExampleMedicationRequest01
InstanceOf: AtApsMedicationRequest
Title: "AtApsMedicationRequest-Beispiel"
Description: "Medication Request"
Usage: #example
* status = #active
* intent = #order
* medicationReference = Reference(Medication/APS-Medication-Example01) "Ramipril 5mg Kapseln"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* authoredOn = "2024-10-14T10:00:00+01:00"
* requester = Reference(Practitioner/HL7ATCorePractitionerExample01) "Dr. Melanie Musterärztin"
* reasonCode = $cs-sct#59621000 "Hypertonie"
* reasonCode.text = "Hypertonie"
* dosageInstruction.text = "1 Kapsel täglich morgens"
* dosageInstruction.timing.repeat.frequency = 1
* dosageInstruction.timing.repeat.period = 1
* dosageInstruction.timing.repeat.periodUnit = #d
* dosageInstruction.route = $cs-route-codes#PO "Oral"
* dosageInstruction.doseAndRate.doseQuantity = 5 'mg' "mg"
* dispenseRequest.quantity = 30 '{Capsule}' "Kapseln"
* dispenseRequest.expectedSupplyDuration = 30 'd' "Tage"