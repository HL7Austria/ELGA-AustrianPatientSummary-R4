Profile: AtApsCarePlan
Parent: CarePlan
Id: at-aps-careplan
Title: "AT APS CarePlan"
Description: "Das AT APS-Profil für die CarePlan-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient)."
* ^status = #active
* . ^short = "AT APS CarePlan"
* subject only Reference(AtApsPatient or Group)