Instance: AtApsExampleMedication01
InstanceOf: AtApsMedication
Title: "AtApsMedication-Beispiel"
Description: "Medication"
Usage: #example
* code = http://www.whocc.no/atc#C09AA05 "Ramipril"
* code.text = "Ramipril 5mg Kapseln"
* status = #active
* manufacturer = Reference(Organization/HL7ATCoreOrganizationExample01) "Beispiel Pharma GmbH"
* ingredient.itemReference = Reference(Medication/AT-APS-Medication-Ingredient-Ramipril) "Ramipril Wirkstoff"
* ingredient.isActive = true
* ingredient.strength.numerator = 5 'mg' "mg"
* ingredient.strength.denominator = 1 'capsule' "Kapsel"