Instance: AtApsExampleClinicalImpression01
InstanceOf: AtApsClinicalImpression
Title: "AtApsClinicalImpression-Beispiel"
Description: "Clinical Impression"
Usage: #example
* identifier.value = "12345"
* status = #completed
* description = "This 26 yo male patient is brought into ER by ambulance after being involved in a motor vehicle accident"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* encounter = Reference(Encounter/example)
* effectivePeriod.start = "2014-12-06T20:00:00+11:00"
* effectivePeriod.end = "2014-12-06T22:33:00+11:00"
* date = "2014-12-06T22:33:00+11:00"
* assessor = Reference(Practitioner/HL7ATCorePractitionerExample01) "Melanie Musterärztin"
* problem.display = "MVA"
* investigation.code.text = "Initial Examination"
* investigation.item[0].display = "deep laceration of the scalp (left temporo-occipital)"
* investigation.item[+].display = "decreased level of consciousness"
* investigation.item[+].display = "disoriented to time and place"
* investigation.item[+].display = "restless"
* summary = "provisional diagnoses of laceration of head and traumatic brain injury (TBI)"
* finding.itemCodeableConcept = http://hl7.org/fhir/sid/icd-9#850.0