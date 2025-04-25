### Module der Austrian Patient Summary

Die Austrian Patient Summary (APS) besteht aus folgenden Abschnitten (Modulen):


[![overview](APS_Sections.drawio.png){: style="width: 60%"}](APS_Sections.drawio.png)
<br>

Im Folgenden werden die Inhalte der Module zusammenfassend beschrieben und, sofern österreichspezifische Anpassungen der internationalen Spezifikation (Profile) vorgenommen wurden, kurz begründet. (TODO)
<br>
<br>

**ADMINISTRATIVE DATEN**

| **Modul** | **Beschreibung** | **Konformität** | **Profile** | **Anmerkung / TODO** |
|---|---|---|---|---|
| **Patient (Subject)** | Patientendaten, inkl. Angabe von Kontaktpersonenen, Hausarzt bzw. primäre Ansprechpartner. | 1..1 | [HL7ATCorePatient](StructureDefinition-at-aps-patient.html) |  |
| **Verfasser (Author)** | Automatische Erstellung der Patient Summary durch die Zentrale Anwendung | 1..* | [Device](https://hl7.org/fhir/R4/device.html) | 1..1 analog zu Kompl. Immunisierungsst. Prüfen: auch zutreffend für evt. zukünft. mixed Erstellung: z.B. Patient Story erstellt durch Patienten oder Persistenzkennzeichnung von Dokumenten, PS-Kuratierung durch GDA? |
| **Rechtlicher Unterzeichner (StructureDefinition-attester)** | Person, die die Richtigkeit der Zusammenstellung bestätigt. Entfällt bei automatischer Erstellung. | 0..* |  | 0..0 NP analog zu Kompl. Immunisierungsst. Prüfen: zukünft. mixed Erstellung beachten? |
| **Verwahrer des Dokuments (Custodian)** | Organisation, die das Patient Summary verwaltet (Zentrale Anwendung) | 1..1 | [HL7ATCoreOrganization](StructureDefinition-at-aps-organization.html) |  |

<br>
<br>

**MEDIZINISCHE DATEN**

| **Modul** | **Beschreibung** | **Konformität** | **AT APS Profile** | **IPS Profile Anmerkung / TODO** |
|---|---|---|---|---|
| **Medikationsliste (Medication Summary)** | Der Abschnitt enthält eine Beschreibung der aktuell relevanten Medikamente des Patienten bzw. liefert Information über das Nichtvorhandensein. | 1..1 | [AtApsMedication](StructureDefinition-at-aps-medication.html) [AtApsMedicationRequest](StructureDefinition-at-aps-medicationrequest.html) [AtApsMedicationStatement](StructureDefinition-at-aps-medicationstatement.html) | MedicationStatement MedicationRequest MedicationAdministration MedicationDispense DocumentReference Wieso wird AtApsMedication nicht in der Composition verwendet? |
| **Allergien und Intoleranzen (Allergies and Intolerances)** | In dem Abschnitt werden die relevanten Allergien oder Unverträglichkeiten des Patienten dokumentiert, wobei die Art der Reaktion (z.B. Ausschlag, Anaphylaxie usw.), vorzugsweise die auslösenden Stoffe, sowie optional die Kritikalität und die Bestimmtheit der Allergie beschrieben werden. Zumindest sollten die derzeit aktiven und alle relevanten früheren Allergien und Nebenwirkungen aufgeführt werden. Liegen keine Informationen über Allergien vor oder sind keine Allergien bekannt, sollte dies in diesem Abschnitt deutlich dokumentiert werden. | 1..1 | [AtApsAllergyIntolerance](StructureDefinition-at-aps-allergyintolerance.html) | AllergyIntolerance DocumentReference |
| **Gesundheitsprobleme und Risiken (Problems)** | Der Abschnitt listet und beschreibt klinische Probleme oder Erkrankungen (kodierte Diagnosen), die derzeit für den Patienten relevant sind bzw. liefert Information über das Nichtvorhandensein. | 1..1 | [AtApsCondition](StructureDefinition-at-aps-condition.html) | Condition DocumentReference |
| **Impfungen (Immunization)** | Der Abschnitt beschreibt den aktuellen Impfstatus eines Patienten und die dazugehörige Impfhistorie. | 0..1 | [AtApsImmunization](StructureDefinition-at-aps-immunization.html) | Immunization or DocumentReference |
| **Eingriffe und Therapien (History of Procedures)** | Der Abschnitt enthält eine Beschreibung früherer Eingriffe und Therapien. Darunter fallen zum Beispiel invasive diagnostische Verfahren, z.B. Herzkatheteruntersuchung; therapeutische Verfahren: z.B. Dialyse; chirurgische Eingriffe: z.B. Appendektomie. Außerdem können hier auch Teilnahmen an Schulungen oder Beratungen dokumentiert werden. | 1..1 | [AtApsProcedure](StructureDefinition-at-aps-procedure.html) | Procedure or DocumentReference Warum werden absolvierte Schulungen nicht im Careplan (Status completed) dokumentiert? |
| **Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)** | Der Abschnitt über Medical Devices enthält Informationen und kodierte Einträge, die den Gebrauch von Medizinprodukten in der Krankengeschichte beschreiben, z.B. Insulinpumpen oder Herzschrittmacher. | 1..1 | [AtApsDeviceUseStatement](StructureDefinition-at-aps-deviceusestatement.html) | DeviceUseStatement or DocumentReference |
| **Diagnostische Resultate (Results)** | Der Abschnitt fasst Untersuchungsergebnisse zusammen, die am Patienten erhoben oder anhand von biologischen In-vitro-Proben erstellt wurden. Dabei kann es sich um Laborergebnisse, Ergebnisse der anatomischen Pathologie oder um radiologische Ergebnisse handeln. | 0..1 | [AtApsObservationResultsLaboratoryPathology](StructureDefinition-at-aps-observationresultslaboratorypathology.html) [AtApsObservationResultsRadiology](StructureDefinition-at-aps-observationresultsradiology.html) [AtApsDiagnosticReport](StructureDefinition-at-aps-diagnosticreport.html) | Observation or DiagnosticReport or DocumentReference |
| **Vitalparameter (Vital Signs)** | Der Abschnitt umfasst Informationen wie Blutdruck, Körpertemperatur, Herzfrequenz, Atemfrequenz, Größe, Gewicht, Body-Mass-Index, Kopfumfang oder Pulsoximetrie. Insbesondere können auffällige Vitalparameter oder körperliche Befunde wie der letzte, maximale und/oder minimale Werte, der Ausgangswert oder relevante Trends angegeben werden. | 0..1 | [AtApsObservationVitalSigns](StructureDefinition-at-aps-observationvitalsigns.html) | Observation or DocumentReference |
| **Vergangene Gesundheitsprobleme und Risiken (History of Past Illness)** | Der Abschnitt enthält eine Beschreibung der historischen klinischen Probleme oder Erkrankungen, die für die Patientin oder den Patienten in der Vergangenheit diagnostiziert wurden. | 0..1 | [AtApsCondition](StructureDefinition-at-aps-observationvitalsigns.html) | Condition or DocumentReference Titel: Krankengeschichte? oder "Risiken" entfern? |
| **Schwangerschaftshistorie (History of Pregnancy)** | Dieser Abschnitt ermöglicht die Dokumentation eines Schwangerschaftsstatus inkl. geplantem Entbindungstermin und eine kurze Zusammenfassung von vergangenen Schwangerschaften. | 0..1 | [AtApsObservationPregnancyStatus](StructureDefinition-at-aps-observationpregnancystatus.html) [AtApsObservationPregnancyOutcome](StructureDefinition-at-aps-observationpregnancyoutcome.html) [AtApsObservationPregnancyEdd](StructureDefinition-at-aps-observationpregnancyedd.html) | Observation or DocumentReference |
| **Lebensstil / Soziale Umstände und Verhalten (Social History)** | Dieser Abschnitt dokumentiert den aktuellen Lebensstil einer Person, z.B. den Raucherstatus und Informationen zum Alkoholkonsum. | 0..1 | [AtApsObservationTobaccoUse](StructureDefinition-at-aps-observationtobaccouse.html) [AtApsObservationAlcoholUse](StructureDefinition-at-aps-observationalcoholuse.html) | Observation or DocumentReference Titel? |
| **Beeinträchtigungen (Functional Status)** | Dieser Abschnitt enthält eine Beschreibung der Mobilität bzw. Fähigkeit der Patientin oder des Patienten, Handlungen des täglichen Lebens auszuführen, einschließlich möglicher Bedürfnisse. Hier könnte auch die Pflegestufe dokumentiert werden. | 0..1 | [AtApsCondition](StructureDefinition-at-aps-condition.html) | Condition or ClinicalImpression or DocumentReference |
| **Behandlungsplan (Plan of Care)** | Dieser Abschnitt enthält den Behandlungsplan inkl. Vorschlägen, Zielen und Anordnungen zur Kontrolle oder Verbesserung des Zustands des Patienten, zur Planung der nächsten empfohlenen oder vereinbarten Untersuchungen, Kontrolltermine und Schulungen. Durchgeführte Maßnahmen wie Untersuchungen oder Schulungen können im Abschnitt History of Procedures dokumentiert werden.| 0..1 |  | [CarePlan](https://hl7.org/fhir/R4/careplan.html) |
| **Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)** | Dieser Abschnitt kann aktuelle Verfügungen von Patienten beinhalten. | 0..1 |  | [Consent](https://hl7.org/fhir/R4/consent.html) or DocumentReference |
| **Warnungen (Alerts)** | Dieser Abschnitt ermöglicht Warnmeldungen, wenn bestimmte Umstände (z.B. Grenzwerte werden für einen gewissen Zeitraum überschritten, wie Blutdruck, Gewicht, subjektives Befinden) eintreten. | 0..1 |  | Flag or DocumentReference [FlagAlertUvIps](https://hl7.org/fhir/uv/ips/2024Sep/StructureDefinition-Flag-alert-uv-ips.html) |
| **Patientenbericht (Patient Story)** | Der Abschnitt enthält narrativen Text sowie optionale Ressourcen, die zum Ausdruck bringen, was für den Patienten wichtig ist. Dazu können Bedürfnisse, Stärken, Werte, Bedenken und Präferenzen für andere, die Unterstützung und Pflege anbieten, gehören. | 0..1 |  |  |

<br>
<br>

### Anwendungsfallbeschreibung

<div>{% include aps-uml.svg %}</div>
<br clear="all"/>

#### UC1 APS aggregieren

##### Akteure

- Gesundheitsdiensteanbieter (GDA)
- Patient

##### Beschreibung

Die Inhalte der APS werden automatisch aus den angebundenen Registern zusammengeführt und basieren somit auf den aktuellsten vorhandenen Gesundheitsdaten des Patienten. Das APS dient im Weiteren dazu, nach festgelegten Kriterien fachspezifische Dokumente (wie z.B. ein Leitdokument für Diabetes) zu generieren und für den Abruf zur Verfügung zu stellen. Auf dem APS basierende Dokumentenklassen werden in eigenen Implementierungsleitfäden spezifiziert.

##### Auslöser

Bei Abruf des Patient Summary wird automatisch ein Prozess gestartet, der die angebundenen Register auf neue oder aktualisierte Daten überprüft und diese Inhalte in das Patient Summary übernimmt.

##### Vorbedingungen

Ein berechtigter Akteur hat lesenend auf das Patient Summary (UC2) zugegriffen.

##### Ergebnis

Das Patient Summary wurde mit den aktuellsten Gesundheitsinformatinen aus allen verfügbaren Registern aggregiert.

<br>

#### UC2 APS lesen

##### Akteure

- Gesundheitsdiensteanbieter (GDA)
- Patient

##### Beschreibung

Ein GDA ruft die aktuellste Version des Patient Summary seines Patienten über sein Primärsystem bzw. ein GDA-Portal ab. Der Patient kann via ELGA-Zugangsportal auf sein aktuelles Patient Summary zugreifen. Das Patient Summary bietet in modular aufgebauten Abschnitten eine strukturierte Zusammenfassung verfügbarer, medizinisch validierter Gesundheitsinformationen aus Registern, die an die Zentrale Anwendung Patient Summary angebunden sind.

##### Verwendete Anwendungsfälle

- UC1 Patient Summary generieren

##### Auslöser

- Konsultation durch GDA
- Informationswunsch durch Patienten
- Bedarf für Notfallversorgung, fachärztliche Zweitmeinung, etc.

##### Vorbedingungen

Der jeweilige Akteur ist berechtigt auf das Patient Summary zuzugreifen.

##### Ergebnis

Die aktuelle Version des Patient Summary wird angezeigt und steht zur Behandlungsunterstützung, Behandlungsplanung oder Informationsweitergabe zur Verfügung.