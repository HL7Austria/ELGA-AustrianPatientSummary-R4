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
* subject only Reference(AtApsPatient or Group)
* author only Reference(AtApsPatient or AtApsPractitioner or AtApsPractitionerRole or Device or RelatedPerson or AtApsOrganization or CareTeam)
* contributor only Reference(AtApsPatient or AtApsPractitioner or AtApsPractitionerRole or Device or RelatedPerson or AtApsOrganization or CareTeam)
* activity.detail 0..0