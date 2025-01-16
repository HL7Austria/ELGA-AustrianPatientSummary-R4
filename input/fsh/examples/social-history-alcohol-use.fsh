Instance: alcohol-use-example
InstanceOf: AtIpsObservationAlcoholUse
Description: "Social History - Alkohol Beispiel"
Usage: #example
* status = #final
* code = $loinc#74013-4 "Alcoholic drinks per day"
* subject = Reference(patient-01)
* effectiveDateTime = "2024-09-20"
* valueQuantity = 2 '/d' "wine glasses per day"