Instance: AtApsExampleMedication01
InstanceOf: AtApsMedication
Title: "AtApsMedication-Beispiel"
Description: "Medication"
Usage: #example
* code = http://www.whocc.no/atc#C09AA05 "Ramipril"
* code.text = "Ramipril 5mg Kapseln"
* status = #active
* manufacturer = Reference(Organization/HL7ATCoreOrganizationExample01) "Beispiel Pharma GmbH"
* ingredient.itemReference = Reference(Medication/AtApsExampleMedication01) "Ramipril Wirkstoff"
* ingredient.isActive = true
* ingredient.strength.numerator.value = 500
* ingredient.strength.numerator.unit = "mg"
* ingredient.strength.numerator.system = "http://unitsofmeasure.org"
* ingredient.strength.numerator.code = #mg
* ingredient.strength.denominator.value = 1
* ingredient.strength.denominator.unit = "Kapsel"
* ingredient.strength.denominator.system = "http://unitsofmeasure.org"
* ingredient.strength.denominator.code = #1