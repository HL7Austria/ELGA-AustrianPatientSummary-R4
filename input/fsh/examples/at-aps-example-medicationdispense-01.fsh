Instance: AtApsExampleMedicationDispense01
InstanceOf: AtApsMedicationDispense
Title: "AtApsMedicationDispense-Beispiel"
Description: "Medication Dispense"
Usage: #example
* status = #completed
* medicationReference = Reference(Medication/AtApsExampleMedication01) "Ramipril 5mg Kapseln"
* subject = Reference(Patient/at-aps-example-patient-01) "Maria Musterfrau"
* performer.actor = Reference(Organization/AtApsExampleOrganization01) "Amadeus Spital"
* authorizingPrescription = Reference(MedicationRequest/AtApsExampleMedicationRequest01) "Verordnung Ramipril"
* whenHandedOver = "2024-10-15T09:30:00+01:00"
* quantity.value = 30
* quantity.unit = "Kapseln"
* daysSupply = 30 'd' "Tage"
* dosageInstruction.text = "1 Kapsel täglich morgens"
* dosageInstruction.timing.repeat.frequency = 1
* dosageInstruction.timing.repeat.period = 1
* dosageInstruction.timing.repeat.periodUnit = #d
* dosageInstruction.route = $cs-sct#26643006 "Oral use"