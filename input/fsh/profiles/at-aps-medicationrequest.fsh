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
* reported[x] only Reference(AtApsPatient or AtApsPractitioner or AtApsPractitionerRole or RelatedPerson or AtApsOrganization)
* requester only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or AtApsPatient or RelatedPerson or AtApsDevice)
* performer only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization or AtApsPatient or AtApsDevice or RelatedPerson or CareTeam)
* recorder only Reference(AtApsPractitioner or AtApsPractitionerRole)
* reasonReference only Reference(AtApsCondition or AtApsObservation)
* basedOn only Reference(AtApsCarePlan or AtApsMedicationRequest or ServiceRequest or ImmunizationRecommendation)
* dispenseRequest.performer only Reference(AtApsOrganization)
* priorPrescription only Reference(AtApsMedicationRequest)