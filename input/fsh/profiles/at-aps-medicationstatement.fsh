Profile: AtApsMedicationStatement
Parent: MedicationStatement
Id: at-aps-medicationstatement
Title: "AT APS MedicationStatement"
Description: "Das AT APS-Profil für die MedicationStatement-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS MedicationStatement"
* ^extension[$imposeProfile].valueCanonical = Canonical(MedicationStatementIPS)
* medication[x] only CodeableConcept or Reference(AtApsMedication)
* subject only Reference(AtApsPatient)
* basedOn only Reference(AtApsMedicationRequest or AtApsCarePlan or ServiceRequest)
* partOf only Reference(AtApsMedicationAdministration or AtApsMedicationDispense or AtApsMedicationStatement or AtApsProcedure or AtApsObservation)
* informationSource only Reference(AtApsPatient or AtApsPractitioner or AtApsPractitionerRole or RelatedPerson or AtApsOrganization)
* reasonReference only Reference(AtApsCondition or AtApsObservation or AtApsDiagnosticReport)