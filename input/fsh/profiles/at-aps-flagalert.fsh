Profile: AtApsFlagAlert
Parent: Flag
Id: at-aps-flagalert
Title: "AT APS Flag Alert"
Description: "TODO"
* ^status = #active
* . ^short = "AT APS Flag Alert"
* ^extension[$imposeProfile].valueCanonical = Canonical(FlagAlertUvIps)
* subject only Reference(AtApsPatient or Location or Group or Organization or Practitioner or PlanDefinition or Medication or Procedure)