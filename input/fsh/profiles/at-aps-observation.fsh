Profile: AtApsObservation
Parent: Observation
Id: at-aps-observation
Title: "AT APS Observation"
Description: "Das AT APS-Profil für die Observation-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient)."
* ^status = #active
* . ^short = "AT APS Observation"
* subject only Reference(AtApsPatient or Group or Device or Location)