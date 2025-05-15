Profile: AtApsObservationVitalSigns
Parent: AtApsObservation
Id: at-aps-observationvitalsigns
Title: "AT APS Observation Vital Signs"
Description: "Das AT APS-Profil für die Abbildung der Vitalparameter ist abgeleitet vom allgemeinen [\"Vital Signs\"-Profil](http://hl7.org/fhir/StructureDefinition/vitalsigns) und berücksichtigt die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets)."
* ^status = #active
* . ^short = "AT APS Observation Vital Signs"
* subject only Reference(AtApsPatient)
