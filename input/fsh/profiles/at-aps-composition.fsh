Profile: AtApsComposition
Parent: Composition
Id: at-aps-composition
Title: "AT APS Composition"
Description: "Das AT APS-Profil für die Composition-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS Composition"
* ^extension[$imposeProfile].valueCanonical = Canonical(CompositionUvIps)

* obeys aps-comp-1

* subject only Reference(AtApsPatient)
* subject ^short = "The person the Austrian Patient Summary is about."
* subject ^definition = "Patientendaten, inkl. Angabe von Kontaktpersonen, Hausarzt bzw. primäre Ansprechpartner."

* author only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsDevice or AtApsPatient or RelatedPerson or AtApsOrganization)
* author ^short = "Autor der Austrian Patient Summary"
* author ^definition = "Autor der Austrian Patient Summary. Ggf. Angabe eines Devices z.B. bei automatischer Erstellung der Patient Summary durch die zentrale Anwendung."
* attester.party only Reference(AtApsPatient or RelatedPerson or AtApsPractitioner or AtApsPractitionerRole or AtApsOrganization)
* attester ^short = "Person, die die Richtigkeit der Zusammenstellung bestätigt."
* attester ^definition = "Person, die die Richtigkeit der Zusammenstellung bestätigt. Darf bei automatischer Erstellung durch ein Device nicht angegeben werden."
* custodian 1..1 
* custodian only Reference(AtApsOrganization)
* custodian ^short = "Organisation, die die Patient Summary verwaltet (z.b. zentrale Anwendung)."
* custodian ^definition = "Organisation, die die Patient Summary verwaltet (z.B. zentrale Anwendung)."
* relatesTo.target[x] only Identifier or Reference(AtApsComposition)

* section.author only Reference(AtApsPractitioner or AtApsPractitionerRole or AtApsDevice or AtApsPatient or RelatedPerson or AtApsOrganization)

* section ^slicing.discriminator.type = #pattern
* section ^slicing.discriminator.path = "code"
* section ^slicing.rules = #open
* section ^slicing.ordered = false

* section contains
    sectionMedications 1..1 and
    sectionAllergies 1..1 and
    sectionProblems 1..1 and
    sectionProceduresHx 1..1 and
    sectionMedicalDevices 1..1 and
    sectionImmunizations 0..1 and
    sectionResults 0..1 and
    sectionVitalSigns 0..1 and
    sectionPastIllnessHx 0..1 and
    sectionFunctionalStatus 0..1 and
    sectionPlanOfCare 0..1 and
    sectionSocialHistory 0..1 and
    sectionPregnancyHx 0..1 and
    sectionAdvanceDirectives 0..1 and
    sectionAlerts 0..1 and
    sectionPatientStory 0..1

// ------ Required sections ------ //

* section[sectionMedications] ^short = "Medikationsliste (Medication Summary)"
* section[sectionMedications] ^definition = "Diese Sektion enthält eine Beschreibung der aktuell relevanten Medikamente des Patienten bzw. liefert Information über das Nichtvorhandensein. Dabei werden nur rezeptpflichtige Medikamente und wechselwirkungsrelevante OTCs berücksichtigt."
* section[sectionMedications].code = $cs-loinc#10160-0
* section[sectionMedications].entry ^slicing.discriminator[0].type = #profile
* section[sectionMedications].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionMedications].entry ^slicing.rules = #open
* section[sectionMedications].entry ^slicing.ordered = false
* section[sectionMedications].entry only Reference (AtApsMedicationStatement or AtApsMedicationRequest or AtApsMedicationAdministration or AtApsMedicationDispense or AtApsDocumentReference)
* section[sectionMedications].entry contains
    medicationStatement 0..* and
    medicationRequest 0..* and
    medicationAdministration 0..* and
    medicationDispense 0..* and
    document 0..*
* section[sectionMedications].entry[medicationStatement] only Reference(AtApsMedicationStatement)
* section[sectionMedications].entry[medicationRequest] only Reference(AtApsMedicationRequest)
* section[sectionMedications].entry[medicationAdministration] only Reference(AtApsMedicationAdministration)
* section[sectionMedications].entry[medicationDispense] only Reference(AtApsMedicationDispense)
* section[sectionMedications].entry[document] only Reference(AtApsDocumentReference)

* section[sectionAllergies] ^short = "Allergien und Intoleranzen (Allergies and Intolerances)"
* section[sectionAllergies] ^definition = "In dieser Sektion werden die relevanten Allergien oder Unverträglichkeiten des Patienten dokumentiert, wobei die Art der Reaktion (z.B. Ausschlag, Anaphylaxie usw.), vorzugsweise die auslösenden Stoffe, sowie optional die Kritikalität und die Bestimmtheit der Allergie beschrieben werden. Zumindest sollten die derzeit aktiven und alle relevanten früheren Allergien und Nebenwirkungen aufgeführt werden. Liegen keine Informationen über Allergien vor oder sind keine Allergien bekannt, sollte dies ebenfalls dokumentiert werden."
* section[sectionAllergies].code = $cs-loinc#48765-2
* section[sectionAllergies].entry ^slicing.discriminator[0].type = #profile
* section[sectionAllergies].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionAllergies].entry ^slicing.rules = #open
* section[sectionAllergies].entry ^slicing.ordered = false
* section[sectionAllergies].entry only Reference (AtApsAllergyIntolerance or AtApsDocumentReference)
* section[sectionAllergies].entry contains
    allergyOrIntolerance 0..* and
    document 0..*
* section[sectionAllergies].entry[allergyOrIntolerance] only Reference(AtApsAllergyIntolerance)
* section[sectionAllergies].entry[document] only Reference(AtApsDocumentReference)

* section[sectionProblems] ^short = "Gesundheitsprobleme und Risiken (Problems)"
* section[sectionProblems] ^definition = "Diese Sektion listet und beschreibt klinische Probleme oder Erkrankungen (kodierte Diagnosen), die derzeit für den Patienten relevant sind bzw. liefert Information über das Nichtvorhandensein."
* section[sectionProblems].code = $cs-loinc#11450-4
* section[sectionProblems].entry ^slicing.discriminator[0].type = #profile
* section[sectionProblems].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionProblems].entry ^slicing.rules = #open
* section[sectionProblems].entry ^slicing.ordered = false
* section[sectionProblems].entry only Reference(AtApsCondition or AtApsDocumentReference)
* section[sectionProblems].entry contains
    problem 0..* and
    document 0..*
* section[sectionProblems].entry[problem] only Reference(AtApsCondition)
* section[sectionProblems].entry[document] only Reference(AtApsDocumentReference)

// ------ Recommended sections ------ //

* section[sectionProceduresHx] ^short = "Eingriffe und Therapien (History of Procedures)"
* section[sectionProceduresHx] ^definition = "Diese Sektion enthält eine Beschreibung früherer Eingriffe und Therapien. Darunter fallen zum Beispiel invasive diagnostische Verfahren (z.B. Herzkatheteruntersuchung), therapeutische Verfahren (z.B. Dialyse) und chirurgische Eingriffe (z.B. Appendektomie). Befunde und Dokumentation von z.B. im Rahmen von Disease-Management-Programmen durchgeführten Schulungen und Beratungen werden ebenfalls in dieser Sektion aufgenommen. Die Dokumentation der Information kann am Beispiel der Integrierten Versorgung z.B. der Fallkoordinator übernehmen."
* section[sectionProceduresHx] obeys ips-comp-1
* section[sectionProceduresHx].code = $cs-loinc#47519-4
* section[sectionProceduresHx].entry ^slicing.discriminator[0].type = #profile
* section[sectionProceduresHx].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionProceduresHx].entry ^slicing.rules = #open
* section[sectionProceduresHx].entry ^slicing.ordered = false
* section[sectionProceduresHx].entry only Reference(AtApsProcedure or AtApsDocumentReference)
* section[sectionProceduresHx].entry contains
    procedure 0..* and
    document 0..*
* section[sectionProceduresHx].entry[procedure] only Reference(AtApsProcedure)
* section[sectionProceduresHx].entry[document] only Reference(AtApsDocumentReference)

* section[sectionImmunizations] ^short = "Impfungen (Immunizations)"
* section[sectionImmunizations] ^definition = "Die Sektion beschreibt den aktuellen Impfstatus des Patienten und die dazugehörige Impfhistorie."
* section[sectionImmunizations].code = $cs-loinc#11369-6
* section[sectionImmunizations].entry ^slicing.discriminator[0].type = #profile
* section[sectionImmunizations].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionImmunizations].entry ^slicing.rules = #open
* section[sectionImmunizations].entry ^slicing.ordered = false
* section[sectionImmunizations].entry only Reference(AtApsImmunization or AtApsDocumentReference)
* section[sectionImmunizations].entry contains
    immunization 0..* and
    document 0..*
* section[sectionImmunizations].entry[immunization] only Reference(AtApsImmunization)
* section[sectionImmunizations].entry[document] only Reference(AtApsDocumentReference)

* section[sectionMedicalDevices] ^short = "Implantate, medizinische Geräte (Medical Devices)"
* section[sectionMedicalDevices] ^definition = "Diese Sektion enthält Informationen und kodierte Einträge, die den Gebrauch von Medizinprodukten in der Krankengeschichte beschreiben, z.B. Insulinpumpen oder Herzschrittmacher."
* section[sectionMedicalDevices] obeys ips-comp-1
* section[sectionMedicalDevices].code = $cs-loinc#46264-8
* section[sectionMedicalDevices].entry ^slicing.discriminator[0].type = #profile
* section[sectionMedicalDevices].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionMedicalDevices].entry ^slicing.rules = #open
* section[sectionMedicalDevices].entry ^slicing.ordered = false
* section[sectionMedicalDevices].entry only Reference(AtApsDeviceUseStatement or AtApsDocumentReference)
* section[sectionMedicalDevices].entry contains
    deviceStatement 0..* and
    document 0..*
* section[sectionMedicalDevices].entry[deviceStatement] only Reference(AtApsDeviceUseStatement)
* section[sectionMedicalDevices].entry[document] only Reference(AtApsDocumentReference)

* section[sectionResults] ^short = "Diagnostische Resultate (Results)"
* section[sectionResults] ^definition = "Die Sektion fasst Untersuchungsergebnisse zusammen, die am Patienten erhoben oder anhand von biologischen In-vitro-Proben erstellt wurden. Dabei kann es sich um Laborergebnisse, Ergebnisse der anatomischen Pathologie oder um radiologische Ergebnisse handeln."
* section[sectionResults].code = $cs-loinc#30954-2
* section[sectionResults].entry ^slicing.discriminator[0].type = #type
* section[sectionResults].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionResults].entry ^slicing.discriminator[+].type = #profile
* section[sectionResults].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionResults].entry ^slicing.rules = #open
* section[sectionResults].entry ^slicing.ordered = false
* section[sectionResults].entry only Reference(AtApsObservation or AtApsDiagnosticReport or AtApsDocumentReference)
* section[sectionResults].entry contains
    resultsObservationLaboratoryPathology 0..* and
    resultsObservationRadiology 0..* and
    resultsDiagnosticReport 0..* and
    document 0..*
* section[sectionResults].entry[resultsObservationLaboratoryPathology] only Reference(AtApsObservationResultsLaboratoryPathology)
* section[sectionResults].entry[resultsObservationRadiology] only Reference(AtApsObservationResultsRadiology)
* section[sectionResults].entry[resultsDiagnosticReport] only Reference(AtApsDiagnosticReport)
* section[sectionResults].entry[document] only Reference(AtApsDocumentReference)

// ------ Optional sections ------ //

* section[sectionVitalSigns] ^short = "Vitalparameter (Vital Signs)"
* section[sectionVitalSigns] ^definition = "Die Sektion umfasst Informationen wie Blutdruck, Körpertemperatur, Herzfrequenz, Atemfrequenz, Größe, Gewicht, Body-Mass-Index, Kopfumfang oder Pulsoximetrie. Insbesondere können auffällige Vitalparameter oder körperliche Befunde wie der letzte, maximale und/oder minimale Wert, der Ausgangswert oder relevante Trends angegeben werden."
* section[sectionVitalSigns].code = $cs-loinc#8716-3
* section[sectionVitalSigns].entry ^slicing.discriminator[0].type = #profile
* section[sectionVitalSigns].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionVitalSigns].entry ^slicing.rules = #open
* section[sectionVitalSigns].entry ^slicing.ordered = false
* section[sectionVitalSigns].entry only Reference(AtApsObservation or AtApsDocumentReference)
* section[sectionVitalSigns].entry contains
    vitalSign 0..* and
    document 0..*
* section[sectionVitalSigns].entry[vitalSign] only Reference(AtApsObservationVitalSigns)
* section[sectionVitalSigns].entry[document] only Reference(AtApsDocumentReference)

* section[sectionPastIllnessHx] ^short = "Vergangene Gesundheitsprobleme und Risiken (History of Past Illness)"
* section[sectionPastIllnessHx] ^definition = "Die Sektion enthält eine Beschreibung der historischen klinischen Probleme oder Erkrankungen, die für die Patientin oder den Patienten in der Vergangenheit diagnostiziert wurden."
* section[sectionPastIllnessHx].code = $cs-loinc#11348-0
* section[sectionPastIllnessHx].entry ^slicing.discriminator[0].type = #profile
* section[sectionPastIllnessHx].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionPastIllnessHx].entry ^slicing.rules = #open
* section[sectionPastIllnessHx].entry ^slicing.ordered = false
* section[sectionPastIllnessHx].entry only Reference(AtApsCondition or AtApsDocumentReference)
* section[sectionPastIllnessHx].entry contains
    pastProblem 0..* and
    document 0..*
* section[sectionPastIllnessHx].entry[pastProblem] only Reference(AtApsCondition)
* section[sectionPastIllnessHx].entry[document] only Reference(AtApsDocumentReference)

* section[sectionFunctionalStatus] ^short = "Beeinträchtigungen (Functional Status)"
* section[sectionFunctionalStatus] ^definition = "Diese Sektion enthält eine Beschreibung der Mobilität bzw. Fähigkeit der Patientin oder des Patienten, Handlungen des täglichen Lebens auszuführen, einschließlich möglicher Bedürfnisse. Hier könnte auch die Pflegestufe dokumentiert werden."
* section[sectionFunctionalStatus].code = $cs-loinc#47420-5
* section[sectionFunctionalStatus].entry ^slicing.discriminator[0].type = #profile
* section[sectionFunctionalStatus].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionFunctionalStatus].entry ^slicing.rules = #open
* section[sectionFunctionalStatus].entry ^slicing.ordered = false
* section[sectionFunctionalStatus].entry only Reference(AtApsCondition or AtApsClinicalImpression or AtApsDocumentReference)
* section[sectionFunctionalStatus].entry contains
    disability 0..* and
    functionalAssessment 0..* and
    document 0..*
* section[sectionFunctionalStatus].entry[disability] only Reference(AtApsCondition)
* section[sectionFunctionalStatus].entry[functionalAssessment] only Reference(AtApsClinicalImpression)
* section[sectionFunctionalStatus].entry[document] only Reference(AtApsDocumentReference)

* section[sectionPlanOfCare] ^short = "Behandlungsplan (Plan of Care)"
* section[sectionPlanOfCare] ^definition = "Die Sektion enthält den Behandlungsplan inkl. Vorschlägen, Zielen und Anordnungen zur Kontrolle oder Verbesserung des Zustands des Patienten, zur Planung der nächsten empfohlenen oder vereinbarten Untersuchungen, Kontrolltermine und Schulungen. Durchgeführte Maßnahmen wie Untersuchungen oder Schulungen können in der Sektion \"History of Procedures\" dokumentiert werden."
* section[sectionPlanOfCare].code = $cs-loinc#18776-5
* section[sectionPlanOfCare].entry ^slicing.discriminator[0].type = #profile
* section[sectionPlanOfCare].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionPlanOfCare].entry ^slicing.rules = #open
* section[sectionPlanOfCare].entry ^slicing.ordered = false
* section[sectionPlanOfCare].entry only Reference(AtApsCarePlan or AtApsImmunizationRecommendation or AtApsDocumentReference)
* section[sectionPlanOfCare].entry contains
    carePlan 0..* and
    immunizationRecommendation 0..* and
    document 0..*
* section[sectionPlanOfCare].entry[carePlan] only Reference(AtApsCarePlan)
* section[sectionPlanOfCare].entry[immunizationRecommendation] only Reference(AtApsImmunizationRecommendation)
* section[sectionPlanOfCare].entry[document] only Reference(AtApsDocumentReference)

* section[sectionSocialHistory] ^short = "Lebensstil / Soziale Umstände und Verhalten (Social History)"
* section[sectionSocialHistory] ^definition = "Diese Sektion erfasst den aktuellen Lebensstil einer Person. Angaben zum Rauchverhalten sowie zum Alkoholkonsum werden in den hierfür vorgesehenen spezifischen Ressourcen abgebildet. Weitere relevante Aspekte, wie z.B. körperliche Aktivität, Ernährungsgewohnheiten oder sonstige Verhaltensweisen, werden mithilfe der AtApsObservation-Ressource dokumentiert."
* section[sectionSocialHistory].code = $cs-loinc#29762-2
* section[sectionSocialHistory].entry ^slicing.discriminator[0].type = #profile
* section[sectionSocialHistory].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionSocialHistory].entry ^slicing.rules = #open
* section[sectionSocialHistory].entry ^slicing.ordered = false
* section[sectionSocialHistory].entry only Reference(AtApsObservation or AtApsDocumentReference)
* section[sectionSocialHistory].entry contains
    smokingTobaccoUse 0..1 and
    alcoholUse 0..1 and
    document 0..*
* section[sectionSocialHistory].entry[smokingTobaccoUse] only Reference(AtApsObservationTobaccoUse)
* section[sectionSocialHistory].entry[alcoholUse] only Reference(AtApsObservationAlcoholUse)
* section[sectionSocialHistory].entry[document] only Reference(AtApsDocumentReference)

* section[sectionPregnancyHx] ^short = "Schwangerschaftshistorie (History of Pregnancy)"
* section[sectionPregnancyHx] ^definition = "Die Sektion ermöglicht die Dokumentation eines Schwangerschaftsstatus inkl. geplantem Entbindungstermin und eine kurze Zusammenfassung von vergangenen Schwangerschaften."
* section[sectionPregnancyHx].code = $cs-loinc#10162-6
* section[sectionPregnancyHx].entry ^slicing.discriminator[0].type = #profile
* section[sectionPregnancyHx].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionPregnancyHx].entry ^slicing.rules = #open
* section[sectionPregnancyHx].entry ^slicing.ordered = false
* section[sectionPregnancyHx].entry only Reference(AtApsObservationPregnancyStatus or AtApsObservationPregnancyOutcome or AtApsDocumentReference)
* section[sectionPregnancyHx].entry contains
    pregnancyStatus 0..* and
    pregnancyOutcomeSummary 0..* and
    document 0..*
* section[sectionPregnancyHx].entry[pregnancyStatus] only Reference(AtApsObservationPregnancyStatus)
* section[sectionPregnancyHx].entry[pregnancyOutcomeSummary] only Reference(AtApsObservationPregnancyOutcome)
* section[sectionPregnancyHx].entry[document] only Reference(AtApsDocumentReference)

* section[sectionAdvanceDirectives] ^short = "Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)"
* section[sectionAdvanceDirectives] ^definition = "Die Sektion kann aktuelle Verfügungen von Patienten beinhalten."
* section[sectionAdvanceDirectives].code = $cs-loinc#42348-3
* section[sectionAdvanceDirectives].entry ^slicing.discriminator[0].type = #profile
* section[sectionAdvanceDirectives].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionAdvanceDirectives].entry ^slicing.rules = #open
* section[sectionAdvanceDirectives].entry ^slicing.ordered = false
* section[sectionAdvanceDirectives].entry only Reference(AtApsConsent or AtApsDocumentReference)
* section[sectionAdvanceDirectives].entry contains
    advanceDirectivesConsent 0..* and
    document 0..*
* section[sectionAdvanceDirectives].entry[advanceDirectivesConsent] only Reference(AtApsConsent)
* section[sectionAdvanceDirectives].entry[document] only Reference(AtApsDocumentReference)

* section[sectionAlerts] ^short = "Warnungen (Alerts)"
* section[sectionAlerts] ^definition = "Die Sektion ermöglicht Warnmeldungen, wenn bestimmte Umstände eintreten (z.B. wenn Grenzwerte für Blutdruck, Gewicht oder subjektives Befinden einen gewissen Zeitraum überschritten werden)."
* section[sectionAlerts].code = $cs-loinc#104605-1
* section[sectionAlerts].entry ^slicing.discriminator[0].type = #profile
* section[sectionAlerts].entry ^slicing.discriminator[=].path = "resolve()"
* section[sectionAlerts].entry ^slicing.rules = #open
* section[sectionAlerts].entry ^slicing.ordered = false
* section[sectionAlerts].entry only Reference(AtApsFlagAlert or AtApsDocumentReference)
* section[sectionAlerts].entry contains
    alertsFlag 0..* and
    document 0..*
* section[sectionAlerts].entry[alertsFlag] only Reference(AtApsFlagAlert)
* section[sectionAlerts].entry[document] only Reference(AtApsDocumentReference)

* section[sectionPatientStory] ^short = "Patientenbericht (Patient Story)"
* section[sectionPatientStory] ^definition = "Die Sektion enthält narrativen Text sowie optionale Ressourcen, die zum Ausdruck bringen, was für den Patienten wichtig ist. Dazu können Bedürfnisse, Stärken, Werte, Bedenken und Präferenzen gehören, die für Personen relevant sind, die Unterstützung und Pflege anbieten."
* section[sectionPatientStory].code = $cs-loinc#81338-6


Invariant: ips-comp-1
Description: "Either section.entry or emptyReason are present"
Expression: "(entry.reference.exists() or emptyReason.exists())"
Severity: #error

// Either the number of Author-Devices and all Author-Entries is different (i.e. there is at least one non-Device-author)
// OR
// (if the number of Author-Devices equals the number of all Author-Entries (i.e. all authors are devices)) the number of attesters is zero
Invariant: aps-comp-1
Description: "For automatically generated APS an attester is not allowed"
Expression: "(author.resolve().ofType(Device).count() != author.count() or attester.count() = 0)"
Severity: #error