Profile: AtApsCarePlan
Parent: CarePlan
Id: at-aps-careplan
Title: "AT APS CarePlan"
Description: "Das AT APS-Profil für die CarePlan-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient)."
* ^status = #active
* . ^short = "AT APS CarePlan"
* instantiatesCanonical 0..0
* instantiatesUri 0..0
* extension contains
    http://hl7.org/fhir/StructureDefinition/workflow-shallComplyWith named shallComplyWith 0..* and
    http://hl7.org/fhir/StructureDefinition/workflow-adheresTo named adheresTo 0..*
* basedOn only Reference(AtApsCarePlan)
* replaces only Reference(AtApsCarePlan)
* partOf only Reference(AtApsCarePlan)
* subject only Reference(AtApsPatient or Group)
* author only Reference(AtApsPatient or AtApsPractitioner or AtApsPractitionerRole or Device or RelatedPerson or AtApsOrganization or CareTeam)
* contributor only Reference(AtApsPatient or AtApsPractitioner or AtApsPractitionerRole or Device or RelatedPerson or AtApsOrganization or CareTeam)
* addresses only Reference(AtApsCondition)
* activity.reference only Reference(Appointment or CommunicationRequest or DeviceRequest or AtApsMedicationRequest or NutritionOrder or Task or ServiceRequest or VisionPrescription or RequestGroup)
* activity.detail 0..0