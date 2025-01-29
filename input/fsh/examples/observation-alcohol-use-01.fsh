Instance: alcohol-use-01
InstanceOf: AtIpsObservationAlcoholUse
Description: "Social History - Alkohol Beispiel"
Usage: #example
* status = #final
* id = "001"
* code = $loinc#74013-4 "Alcoholic drinks per day"
* subject = Reference(Patient/002) "Maria Musterfrau"
* performer = Reference(Patient/002) "Maria Musterfrau"
* effectiveDateTime = "2024-09-20"
* valueQuantity = 2 '/d' "wine glasses per day"