Profile: AtApsConsent
Parent: Consent
Id: at-aps-consent
Title: "AT APS Consent"
Description: "Das AT APS-Profil für die Consent-Ressource berücksichtigt die österreichischen Vorgaben (z.B. Patient)."
* ^status = #active
* . ^short = "AT APS Consent"
* patient only Reference(AtApsPatient)
* performer only Reference(AtApsOrganization or AtApsPatient or AtApsPractitioner or RelatedPerson or AtApsPractitionerRole)
* organization only Reference(AtApsOrganization)
* verification.verifiedWith only Reference(AtApsPatient or RelatedPerson)
* provision.actor.reference only Reference(AtApsDevice or Group or CareTeam or AtApsOrganization or AtApsPatient or AtApsPractitioner or RelatedPerson or AtApsPractitionerRole)
* source[x] only Reference(AtApsConsent or AtApsDocumentReference or Contract or QuestionnaireResponse) or Attachment