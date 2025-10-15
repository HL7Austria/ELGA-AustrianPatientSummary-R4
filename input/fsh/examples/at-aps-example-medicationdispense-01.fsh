Instance: AtApsExampleMedicationDispense01
InstanceOf: AtApsMedicationDispense
Title: "AtApsMedicationDispense-Beispiel"
Description: "Medication Dispense"
Usage: #example
* status = #completed
* medicationReference = Reference(Medication/APS-Medication-Example01) "Ramipril 5mg Kapseln"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* performer.actor = Reference(Organization/HL7ATCoreOrganizationExample01) "Apotheke zum Heiligen Rezept"
* authorizingPrescription = Reference(MedicationRequest/APS-MedicationRequest-Example01) "Verordnung Ramipril"
* whenHandedOver = "2024-10-15T09:30:00+01:00"
* quantity = 30 '{Capsule}' "Kapseln"
* daysSupply = 30 'd' "Tage"
* dosageInstruction.text = "1 Kapsel täglich morgens"
* dosageInstruction.timing.repeat.frequency = 1
* dosageInstruction.timing.repeat.period = 1
* dosageInstruction.timing.repeat.periodUnit = #d
* dosageInstruction.route = $cs-route-codes#PO "Oral"