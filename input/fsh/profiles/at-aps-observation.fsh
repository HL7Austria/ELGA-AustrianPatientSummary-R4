Profile: AtApsObservation
Parent: Observation
Id: at-aps-observation
Title: "AT APS Observation"
Description: "TODO"
* ^status = #active
* . ^short = "At APS Observation"
* category ^slicing.discriminator.type = #value
* category ^slicing.discriminator.path = "coding.code"
* category ^slicing.rules = #open
* category contains VSCat 0..1