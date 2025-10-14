Instance: AtApsExampleCareplan01
InstanceOf: AtApsCarePlan
Title: "AtApsCarePlan-Beispiel"
Description: "Care Plan"
Usage: #example
* text.status = #additional
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n<p>Ein einfacher Pflegeplan, der angibt, dass ein Patient aufgrund von Adipositas einmal täglich sein Gewicht messen soll.</p>\n</div>"
* contained = p1
* identifier.value = "12345"
* instantiatesUri = "http://example.org/protocol-for-obesity"
* basedOn.display = "Behandlung von Typ-2-Diabetes"
* replaces.display = "Plan der Klinik"
* partOf.display = "Allgemeiner Wellnessplan"
* status = #active
* intent = #plan
* category.text = "Gewichtsmanagementplan"
* description = "Übergewicht und Gewichtsverlust managen"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* encounter = Reference(Encounter/home)
* period.end = "2017-06-01"
* created = "2016-01-01"
* author = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* careTeam = Reference(CareTeam/example)
* addresses = Reference(p1) "obesity"
* goal = Reference(Goal/example)
* activity.outcomeCodeableConcept = $cs-sct#161832001 "Progressive weight loss"
* activity.outcomeReference = Reference(Observation/example) "Gewicht gemessen"

Instance: p1
InstanceOf: Condition
Usage: #inline
* clinicalStatus = $cs-condition-clinical#active
* verificationStatus = $cs-condition-ver-status#confirmed
* code.text = "Obesity"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"