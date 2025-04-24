### Module der Austrian Patient Summary

Die Austrian Patient Summary (APS) besteht aus folgenden Modulen:


[![overview](APS_Sections.drawio.png){: style="width: 60%"}](APS_Sections.drawio.png)
<br>

Im Folgenden werden die Inhalte der Module zusammenfassend beschrieben und, sofern österreichspezifische Anpassungen der internationalen Spezifikation (Profile) vorgenommen wurden, kurz begründet. (TODO)
<br>
<br>

**ADMINISTRATIVE DATEN**

| **Modul** | **Beschreibung** | **Konformität** | **Profile** | **Anmerkung / TODO** |
|---|---|---|---|---|
| **Patient (Subject)** | Patientendaten, inkl. Angabe von Kontaktpersonenen, Hausarzt bzw. primäre Ansprechpartner. | 1..1 | HL7ATCorePatient |  |
| **Verfasser (Author)** | Automatische Erstellung der Patient Summary durch die Zentrale Anwendung | 1..* | Device | 1..1 analog zu Kompl. Immunisierungsst. Prüfen: auch zutreffend für evt. zukünft. mixed Erstellung: z.B. Patient Story erstellt durch Patienten oder Persistenzkennzeichnung von Dokumenten, PS-Kuratierung durch GDA? |
| **Rechtlicher Unterzeichner (Attester)** | Person, die die Richtigkeit der Zusammenstellung bestätigt. Entfällt bei automatischer Erstellung. | 0..* |  | 0..0 NP analog zu Kompl. Immunisierungsst. Prüfen: zukünft. mixed Erstellung beachten? |
| **Verwahrer des Dokuments (Custodian)** | Organisation, die das Patient Summary verwaltet (Zentrale Anwendung) | 1..1 | HL7ATCoreOrganization |  |

<br>
<br>

**MEDIZINISCHE DATEN**

| **Modul** | **Beschreibung** | **Konformität** | **AT APS Profile** | **IPS Profile Anmerkung / TODO** |
|---|---|---|---|---|
| **Medikationsliste (Medication Summary)** | Der Abschnitt enthält eine Beschreibung der aktuell relevanten Medikamente des Patienten bzw. liefert Information über das Nichtvorhandensein. | 1..1 | AtApsMedication AtApsMedicationRequest AtApsMedicationStatement | MedicationStatement MedicationRequest MedicationAdministration MedicationDispense DocumentReference Wieso wird AtApsMedication nicht in der Composition verwendet? |
| **Allergien und Intoleranzen (Allergies and Intolerances)** | In dem Abschnitt werden die relevanten Allergien oder Unverträglichkeiten des Patienten dokumentiert, wobei die Art der Reaktion (z.B. Ausschlag, Anaphylaxie usw.), vorzugsweise die auslösenden Stoffe, sowie optional die Kritikalität und die Bestimmtheit der Allergie beschrieben werden. Zumindest sollten die derzeit aktiven und alle relevanten früheren Allergien und Nebenwirkungen aufgeführt werden. Liegen keine Informationen über Allergien vor oder sind keine Allergien bekannt, sollte dies in diesem Abschnitt deutlich dokumentiert werden. | 1..1 | AtApsAllergyIntolerance | AllergyIntolerance DocumentReference |
| **Gesundheitsprobleme und Risiken (Problems)** | Der Abschnitt listet und beschreibt klinische Probleme oder Erkrankungen (kodierte Diagnosen), die derzeit für den Patienten relevant sind bzw. liefert Information über das Nichtvorhandensein. | 1..1 | AtApsCondition | Condition DocumentReference |
| **Impfungen (Immunization)** | Der Abschnitt beschreibt den aktuellen Impfstatus eines Patienten und die dazugehörige Impfhistorie. | 0..1 | AtApsImmunization | Immunization or DocumentReference |
| **Eingriffe und Therapien (History of Procedures)** | Der Abschnitt enthält eine Beschreibung früherer Eingriffe und Therapien. Darunter fallen zum Beispiel invasive diagnostische Verfahren, z.B. Herzkatheteruntersuchung; therapeutische Verfahren: z.B. Dialyse; chirurgische Eingriffe: z.B. Appendektomie. Außerdem können hier auch Teilnahmen an Schulungen oder Beratungen dokumentiert werden. | 1..1 | AtApsProcedure | Procedure or DocumentReference Warum werden absolvierte Schulungen nicht im Careplan (Status completed) dokumentiert? |
| **Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)** | Der Abschnitt über Medical Devices enthält Informationen und kodierte Einträge, die den Gebrauch von Medizinprodukten in der Krankengeschichte beschreiben, z.B. Insulinpumpen oder Herzschrittmacher. | 1..1 | AtApsDeviceUseStatement | DeviceUseStatement or DocumentReference |
| **Diagnostische Resultate (Results)** | Der Abschnitt fasst Untersuchungsergebnisse zusammen, die am Patienten erhoben oder anhand von biologischen In-vitro-Proben erstellt wurden. Dabei kann es sich um Laborergebnisse, Ergebnisse der anatomischen Pathologie oder um radiologische Ergebnisse handeln. | 0..1 | AtApsObservationResultsLaboratoryPathology AtApsObservationResultsRadiology AtApsDiagnosticReport | Observation or DiagnosticReport or DocumentReference |
| **Vitalparameter (Vital Signs)** | Der Abschnitt umfasst Informationen wie Blutdruck, Körpertemperatur, Herzfrequenz, Atemfrequenz, Größe, Gewicht, Body-Mass-Index, Kopfumfang oder Pulsoximetrie. Insbesondere können auffällige Vitalparameter oder körperliche Befunde wie der letzte, maximale und/oder minimale Werte, der Ausgangswert oder relevante Trends angegeben werden. | 0..1 | AtApsObservationVitalSigns | Observation or DocumentReference |
| **Vergangene Gesundheitsprobleme und Risiken (History of Past Illness)** | Der Abschnitt enthält eine Beschreibung der historischen klinischen Probleme oder Erkrankungen, die für die Patientin oder den Patienten in der Vergangenheit diagnostiziert wurden. | 0..1 | AtApsCondition | Condition or DocumentReference Titel: Krankengeschichte? oder "Risiken" entfern? |
| **Schwangerschaftshistorie (History of Pregnancy)** | Dieser Abschnitt ermöglicht die Dokumentation eines Schwangerschaftsstatus inkl. geplantem Entbindungstermin und eine kurze Zusammenfassung von vergangenen Schwangerschaften. | 0..1 | AtApsObservationPregnancyStatus AtApsObservationPregnancyOutcome | Observation or DocumentReference) |
| **Lebensstil / Soziale Umstände und Verhalten (Social History)** | Dieser Abschnitt dokumentiert den aktuellen Lebensstil einer Person, z.B. den Raucherstatus und Informationen zum Alkoholkonsum. | 0..1 | AtApsObservationPregnancyOutcome | Observation or DocumentReference Titel? |
| **Beeinträchtigungen (Functional Status)** | Dieser Abschnitt enthält eine Beschreibung der Mobilität bzw. Fähigkeit der Patientin oder des Patienten, Handlungen des täglichen Lebens auszuführen, einschließlich möglicher Bedürfnisse. Hier könnte auch die Pflegestufe dokumentiert werden. | 0..1 | AtApsObservationAlcoholUse | Condition or ClinicalImpression or DocumentReference |
| **Behandlungsplan (Plan of Care)** | Dieser Abschnitt enthält den Behandlungsplan inkl. Vorschlägen, Zielen und Anordnungen zur Überwachung, Verfolgung oder Verbesserung des Zustands des Patienten. Die einzelnen Untersuchungen, Schulungen etc. können im Abschnitt History of Procedures dokumentiert werden. | 0..1 |  | CarePlan |
| **Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)** | Dieser Abschnitt kann aktuelle Verfügungen von Patienten beinhalten. | 0..1 |  | Consent or DocumentReference |
| **Warnungen (Alerts)** | Dieser Abschnitt enthält Warnmeldungen. Sie sollen auf potenzielle Bedenken und Gefahren hinweisen. | 0..1 |  | Flag or DocumentReference FlagAlertUvIps |
| **Patientenbericht (Patient Story)** | Der Abschnitt enthält narrativen Text sowie optionale Ressourcen, die zum Ausdruck bringen, was für den Patienten wichtig ist. Dazu können Bedürfnisse, Stärken, Werte, Bedenken und Präferenzen für andere, die Unterstützung und Pflege anbieten, gehören. | 0..1 |  |  |


### Anwendungsfallbeschreibung

<div>{% include aps-uml.svg %}</div>
<br clear="all"/>

#### UC1 Patient Summary aktualisieren/erstellen
Basierend neuer Dokumentation in den angebundenen Registern wird die APS automatische aktualisiert, sobald ein lesender Zugriff auf die APS stattfindet. Die Information der APS dient im Weiteren dazu, fachspezifische Dokumente (wie z.B. ein Leitdokument für Diabetes) zu generieren und für den Abruf zur Verfügung zu stellen.

#### UC2 Patient Summary lesen

Umfasst: 
- Behandlungsplan: Einsicht, Kontrolle und Planung der nächsten empfohlenen oder vereinbarten Termine,  Kontrolltermine und Untersuchungen.
- Gesamtübersicht aller erfassten Daten und deren Bearbeitungen einsehen.
- Lebensstil: Einsicht und Kontrolle der vereinbarten Ziele (z.B. Rauchen, Bewegung, Alkohol).
- Hilfsgeräte/Apps erfassen und Behandlungsdaten manuell oder automatisiert speichern.
- Messwerte beobachten und im Anlassfall Rückmeldungen von einem Arzt erhalten (z.B. Grenzwerte werden für einen gewissen Zeitraum überschritten, wie Blutdruck, Gewicht, subjektives Befinden).

TODO


#### Beteiligte Akteure und Rollen
TODO


### Generierung der APS
Zusammenspiel mit CDA