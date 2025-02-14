Profile: AtApsObservationVitalSigns
Parent: http://hl7.org/fhir/StructureDefinition/vitalsigns
Id: at-aps-observationvitalsigns
Title: "AT APS Observation Vital Signs"
Description: "This AT APS profile for the Observation resource is derived from the general vital signs profile."
* . ^short = "AT APS Observation Vital Signs"
* subject only Reference(AtApsPatient)
* code from $vs-elga-vitalparameterarten (extensible)
* component.code from $vs-elga-vitalparameterarten (extensible)
