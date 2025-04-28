Profile: AtApsMedicationRequest
Parent: MedicationRequest
Id: at-aps-medicationrequest
Title: "AT APS MedicationRequest"
Description: "Das AT APS-Profil für die MedicationRequest-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS MedicationRequest"
* ^extension[$imposeProfile].valueCanonical = Canonical(MedicationRequestIPS)
* medication[x] only CodeableConcept or Reference(AtApsMedication)
* subject only Reference(AtApsPatient)
