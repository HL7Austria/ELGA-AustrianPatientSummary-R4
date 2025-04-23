Extension: AtApsExtImmunizationBasedOn
Id: at-aps-ext-immunization-basedOn
Title: "Immunization basedOn"
Description: "Authority that the immunization event is based on"
Context: AtApsImmunization

* value[x] only Reference(CarePlan or MedicationRequest or ServiceRequest or ImmunizationRecommendation)
* value[x] ^short = "Authority that the immunization event is based on"
* value[x] 1..1