Instance: AtApsExampleCareplan01
InstanceOf: AtApsCarePlan
Title: "AtApsCarePlan-Beispiel"
Description: "Care Plan"
Usage: #example
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n<p>A simple care plan to indicate a patient taking their weight once a day because of obesity.</p>\n</div>"
* contained = p1
* identifier.value = "12345"
* instantiatesUri = "http://example.org/protocol-for-obesity"
* basedOn.display = "Management of Type 2 Diabetes"
* replaces.display = "Plan from urgent care clinic"
* partOf.display = "Overall wellness plan"
* status = #active
* intent = #plan
* category.text = "Weight management plan"
* description = "Manage obesity and weight loss"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* encounter = Reference(Encounter/home)
* period.end = "2017-06-01"
* created = "2016-01-01"
* author = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* careTeam = Reference(CareTeam/example)
* addresses = Reference(p1) "obesity"
* goal = Reference(Goal/example)
* activity.outcomeCodeableConcept = $cs-sct#161832001 "Progressive weight loss"
* activity.outcomeReference = Reference(Observation/example) "Weight Measured"

Instance: p1
InstanceOf: Condition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active
* verificationStatus = $cs-condition-ver-status#confirmed
* code.text = "Obesity"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"