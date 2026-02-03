Profile: AtApsImmunizationRecommendation
Parent: ImmunizationRecommendation
Id: at-aps-immunizationrecommendation
Title: "AT APS Immunization"
Description: "Das AT APS-Profil für die ImmunizationRecommendation-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets)."
* ^status = #active
* . ^short = "AT APS Immunization"
* patient only Reference(AtApsPatient)

* authority only Reference(AtApsOrganization)

* recommendation.forecastStatus from $vs-eimpf-specialcasevaccination (extensible)
* recommendation.supportingImmunization only Reference(AtApsImmunization or ImmunizationEvaluation)