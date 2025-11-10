### Sektionen der Austrian Patient Summary

Die Austrian Patient Summary (APS) besteht aus folgenden Sektionen (Module):

[![overview](APS_Sections.drawio.png){: style="width: 85%"}](APS_Sections.drawio.png)
<br>

Im Folgenden werden die Inhalte der Sektionen zusammenfassend beschrieben und, sofern österreichspezifische Anpassungen der internationalen Spezifikation (Profile) vorgenommen wurden, kurz begründet.
<br>
<br>

**ADMINISTRATIVE DATEN**

| **Sektion** | **Beschreibung** | **Konformität** | **Profile** |
|---|---|---|---|
| **Patient (Subject)** | Patientendaten, inkl. Angabe von Kontaktpersonenen, Hausarzt bzw. primäre Ansprechpartner. | 1..1 | [AtApsPatient](StructureDefinition-at-aps-patient.html) |
| **Verfasser (Author)** | Automatische Erstellung der Patient Summary durch die Zentrale Anwendung. | 1..* | [AtApsDevice](StructureDefinition-at-aps-device.html) |
| **Rechtlicher Unterzeichner (Attester)** | Person, die die Richtigkeit der Zusammenstellung bestätigt. Darf bei automatischer Erstellung durch ein Device nicht angegeben werden. | 0..* |  |
| **Verwahrer des Dokuments (Custodian)** | Organisation, die die Patient Summary verwaltet (Zentrale Anwendung). | 1..1 | [AtApsOrganization](StructureDefinition-at-aps-organization.html) |

<br>
<br>

**MEDIZINISCHE DATEN**

| **Sektion** | **Beschreibung** | **Konformität** | **AT APS Profile** |
|---|---|---|---|
| **Medikationsliste (Medication Summary)** | Diese Sektion enthält eine Beschreibung der aktuell relevanten Medikamente des Patienten bzw. liefert Information über das Nichtvorhandensein. | 1..1 | [AtApsMedication](StructureDefinition-at-aps-medication.html)  <br>[AtApsMedicationadministration](StructureDefinition-at-aps-medicationadministration.html) <br> [AtApsMedicationdispense](StructureDefinition-at-aps-medicationdispense.html)  <br>[AtApsMedicationRequest](StructureDefinition-at-aps-medicationrequest.html) <br>[AtApsMedicationStatement](StructureDefinition-at-aps-medicationstatement.html) |
| **Allergien und Intoleranzen (Allergies and Intolerances)** | In dieser Sektion werden die relevanten Allergien oder Unverträglichkeiten des Patienten dokumentiert, wobei die Art der Reaktion (z.B. Ausschlag, Anaphylaxie usw.), vorzugsweise die auslösenden Stoffe, sowie optional die Kritikalität und die Bestimmtheit der Allergie beschrieben werden. Zumindest sollten die derzeit aktiven und alle relevanten früheren Allergien und Nebenwirkungen aufgeführt werden. Liegen keine Informationen über Allergien vor oder sind keine Allergien bekannt, sollte dies ebenfalls dokumentiert werden. | 1..1 | [AtApsAllergyIntolerance](StructureDefinition-at-aps-allergyintolerance.html) |
| **Gesundheitsprobleme und Risiken (Problems)** | Diese Sektion listet und beschreibt klinische Probleme oder Erkrankungen (kodierte Diagnosen), die derzeit für den Patienten relevant sind bzw. liefert Information über das Nichtvorhandensein. | 1..1 | [AtApsCondition](StructureDefinition-at-aps-condition.html) |
| **Eingriffe und Therapien (History of Procedures)** | Diese Sektion enthält eine Beschreibung früherer Eingriffe und Therapien. Darunter fallen zum Beispiel invasive diagnostische Verfahren (z.B. Herzkatheteruntersuchung), therapeutische Verfahren (z.B. Dialyse) und chirurgische Eingriffe (z.B. Appendektomie). Außerdem können hier auch Teilnahmen an Schulungen oder Beratungen dokumentiert werden. | 1..1 | [AtApsProcedure](StructureDefinition-at-aps-procedure.html) |
| **Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)** | Diese Sektion enthält Informationen und kodierte Einträge, die den Gebrauch von Medizinprodukten in der Krankengeschichte beschreiben, z.B. Insulinpumpen oder Herzschrittmacher. | 1..1 | [AtApsDeviceUseStatement](StructureDefinition-at-aps-deviceusestatement.html) <br> [AtApsDevice](StructureDefinition-at-aps-device.html)|
| **Impfungen (Immunization)** | Die Sektion beschreibt den aktuellen Impfstatus eines Patienten und die dazugehörige Impfhistorie. | 0..1 | [AtApsImmunization](StructureDefinition-at-aps-immunization.html) |
| **Diagnostische Resultate (Results)** | Die Sektion fasst Untersuchungsergebnisse zusammen, die am Patienten erhoben oder anhand von biologischen In-vitro-Proben erstellt wurden. Dabei kann es sich um Laborergebnisse, Ergebnisse der anatomischen Pathologie oder um radiologische Ergebnisse handeln. | 0..1 | [AtApsObservationResultsLaboratoryPathology](StructureDefinition-at-aps-observationresultslaboratorypathology.html) <br>[AtApsObservationResultsRadiology](StructureDefinition-at-aps-observationresultsradiology.html) <br>[AtApsDiagnosticReport](StructureDefinition-at-aps-diagnosticreport.html) |
| **Vitalparameter (Vital Signs)** | Die Sektion umfasst Informationen wie Blutdruck, Körpertemperatur, Herzfrequenz, Atemfrequenz, Größe, Gewicht, Body-Mass-Index, Kopfumfang oder Pulsoximetrie. Insbesondere können auffällige Vitalparameter oder körperliche Befunde wie der letzte, maximale und/oder minimale Wert, der Ausgangswert oder relevante Trends angegeben werden. | 0..1 | [AtApsObservationVitalSigns](StructureDefinition-at-aps-observationvitalsigns.html) |
| **Vergangene Gesundheitsprobleme und Risiken (History of Past Illness)** | Die Sektion enthält eine Beschreibung der historischen klinischen Probleme oder Erkrankungen, die für die Patientin oder den Patienten in der Vergangenheit diagnostiziert wurden. | 0..1 | [AtApsCondition](StructureDefinition-at-aps-observationvitalsigns.html) |
| **Beeinträchtigungen (Functional Status)** | Diese Sektion enthält eine Beschreibung der Mobilität bzw. Fähigkeit der Patientin oder des Patienten, Handlungen des täglichen Lebens auszuführen, einschließlich möglicher Bedürfnisse. Hier könnte auch die Pflegestufe dokumentiert werden. | 0..1 | [AtApsCondition](StructureDefinition-at-aps-condition.html) |
| **Behandlungsplan (Plan of Care)** | Die Sektion enthält den Behandlungsplan inkl. Vorschlägen, Zielen und Anordnungen zur Kontrolle oder Verbesserung des Zustands des Patienten, zur Planung der nächsten empfohlenen oder vereinbarten Untersuchungen, Kontrolltermine und Schulungen. Durchgeführte Maßnahmen wie Untersuchungen oder Schulungen können in der Sektion "History of Procedures" dokumentiert werden.| 0..1 | [AtApsCareplan](StructureDefinition-at-aps-careplan.html) <br>  |
| **Lebensstil / Soziale Umstände und Verhalten (Social History)** | Diese Sektion dokumentiert den aktuellen Lebensstil einer Person, z.B. den Raucherstatus und Informationen zum Alkoholkonsum. | 0..1 | [AtApsObservation](StructureDefinition-at-aps-observation.html) <br>[AtApsObservationTobaccoUse](StructureDefinition-at-aps-observationtobaccouse.html) <br>[AtApsObservationAlcoholUse](StructureDefinition-at-aps-observationalcoholuse.html) |
| **Schwangerschaftshistorie (History of Pregnancy)** | Die Sektion ermöglicht die Dokumentation eines Schwangerschaftsstatus inkl. geplantem Entbindungstermin und eine kurze Zusammenfassung von vergangenen Schwangerschaften. | 0..1 | [AtApsObservationPregnancyStatus](StructureDefinition-at-aps-observationpregnancystatus.html) <br>[AtApsObservationPregnancyOutcome](StructureDefinition-at-aps-observationpregnancyoutcome.html) [AtApsObservationPregnancyEdd](StructureDefinition-at-aps-observationpregnancyedd.html) |
| **Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)** | Die Sektion kann aktuelle Verfügungen von Patienten beinhalten. | 0..1 | [AtApsCconsent](StructureDefinition-at-aps-consent.html) <br> |
| **Warnungen (Alerts)** | Die Sektion ermöglicht Warnmeldungen, wenn bestimmte Umstände eintreten (z.B. wenn Grenzwerte für Blutdruck, Gewicht oder subjektives Befinden einen gewissen Zeitraum überschritten werden). | 0..1 | [AtApsFlagalert](StructureDefinition-at-aps-flagalert.html) <br> |
| **Patientenbericht (Patient Story)** | Die Sektion enthält narrativen Text sowie optionale Ressourcen, die zum Ausdruck bringen, was für den Patienten wichtig ist. Dazu können Bedürfnisse, Stärken, Werte, Bedenken und Präferenzen gehören, die für Personen relevant sind, die Unterstützung und Pflege anbieten. | 0..1 |  |

<br>
<br>
<br>

### Anwendungsfallbeschreibung

Folgendes Use Case Diagramm stellt die im Kontext Implementierungsleitfaden relevanten Funktionen der Austrian Patient Summary dar.

<div>{% include aps-uml.svg %}</div>
<br clear="all"/>

#### APS aggregieren (UC1)

**Akteure**

- Zentrale Anwendung Patient Summary

**Beschreibung**

Die Inhalte der APS werden automatisch aus den angebundenen Registern (e-Medikation, e-Impfpass, etc.) zusammengeführt und basieren somit auf den aktuellsten vorhandenen Gesundheitsdaten des Patienten. Die APS dient im Weiteren dazu, nach festgelegten Kriterien fachspezifische Dokumente (wie z.B. ein Leitdokument für Diabetes) zu generieren und für den Abruf zur Verfügung zu stellen. Auf der APS basierende Dokumentenklassen werden in eigenen Implementierungsleitfäden spezifiziert.

<blockquote>
    <p>
        <b>Note:</b> Wie die Aggregation genauer erfolgt, kann zum aktuellen Zeitpunkt noch nicht beschrieben werden und wird in einer späteren Version der APS ergänzt.
    </p>
</blockquote>

**Auslöser**

Bei Abruf der APS wird automatisch ein Prozess gestartet, der die angebundenen Register auf neue oder aktualisierte Daten überprüft und diese Inhalte in die Patient Summary übernimmt.

**Vorbedingungen**

Ein berechtigter Akteur hat lesend auf die APS (UC2) zugegriffen. In den angebundenen Registern liegen Daten für den Patienten vor.

**Ergebnis**

Die Austrian Patient Summary wurde mit den aktuellsten Gesundheitsinformationen der angebundenen Register aggregiert.

<br>

#### APS lesen (UC2)

**Akteure**

- Gesundheitsdiensteanbieter (GDA)
- Patient

**Beschreibung**

Ein GDA ruft die aktuellste Version der APS seines Patienten über sein Primärsystem bzw. ein GDA-Portal ab. Der Patient kann via ELGA-Zugangsportal auf seine aktuelle Patient Summary zugreifen. Die Patient Summary bietet in modular aufgebauten Abschnitten (Sektionen) eine strukturierte Zusammenfassung verfügbarer, medizinisch validierter Gesundheitsinformationen aus Registern, die an die Zentrale Anwendung Patient Summary angebunden sind.

**Verwendete Anwendungsfälle**

- UC1 Patient Summary generieren

**Auslöser**

- Konsultation durch GDA
- Informationswunsch durch Patienten
- Bedarf für Notfallversorgung, fachärztliche Zweitmeinung, etc.

**Vorbedingungen**

Der jeweilige Akteur ist berechtigt auf die Patient Summary zuzugreifen.

**Ergebnis**

Die aktuelle Version der Patient Summary wird angezeigt und steht zur Behandlungsunterstützung, Behandlungsplanung oder Informationsweitergabe zur Verfügung.

<br>
<br>

### Patient Journey

Das folgende Anwendungsbeispiel veranschaulicht potenzielle Einsatzszenarien für die International Patient Summary Dokument. Es dient dazu, beispielhaft die zum jeweiligen Zeitpunkt entstehenden Dokumente im Kontext der APS zu demonstrieren.

#### *Beispiel*

**1. Arztbesuch**

Frau [Maria Musterfrau](Patient-at-aps-example-patient-01.html), geboren am 17. April 1989, nimmt am 8. Februar 2025 bei ihrer neuen Ärztin [Dr. Hanna Hausärztin](Practitioner-at-aps-example-practitioner-01.html) eine Vorsorgeuntersuchung in Anspruch. Diese ruft die aktuelle [APS (Journey-1)](Bundle-AtApsExampleBundle-Journey-1.html) ihrer Patientin ab, um eine Zusammenfassung bereits dokumentierter Erkrankungen und Befunde einsehen zu können:

- Die [Medikationsliste](Bundle-AtApsExampleBundle-Journey-1.html#medikationsliste) zeigt Dr. Hausärztin, die in der zentralen Anwendung e-Medikation verfügbaren Medikationsdaten der Patientin an. Dieser wurden vor ca. 2 Monaten nach einem Krankenhausaufenthalt aufgrund von zu hohem Blutdruck Ramipril (5 mg) verordnet.

- Um sich das genauer anzusehen, kann Dr. Hausärztin in der Sektion [Gesundheitsprobleme und Risiken](Bundle-AtApsExampleBundle-Journey-1.html#gesundheitsprobleme-und-risiken) unter der dort angeführten "Arteriellen Hypertonie" das zugrundeliegende Quelldokument, nämlich den Entlassungsbrief aus dem AKH Amadeus einsehen. Weiters ist in dieser Sektion ersichtlich, dass eine familiäre Vorbelastung bezüglich Diabetes mellitus vorliegt.

- In der Sektion [Vergangene Gesundheitsprobleme und Risiken](Bundle-AtApsExampleBundle-Journey-1.html#vergangene-gesundheitsprobleme-und-risiken) sieht Dr. Hausärztin eine in der Kindheit durchgemachte Windpocken-Erkrankung.

- Aus der Sektion [Allergien und Intoleranzen](Bundle-AtApsExampleBundle-Journey-1.html#allergien-und-intoleranzen) geht eine Hausstaubmilbenallergie hervor.

- Die Sektion [Eingriffe und Therapien](Bundle-AtApsExampleBundle-Journey-1.html#eingriffe-und-therapien) gibt Auskunft darüber, dass bei Frau Musterfrau im Jahr 2010 das Hüftgelenk ersetzt werden musste und sie daher links ein Hüftimplantat trägt, wie im Abschnitt [Implantate, medizinische Geräte und Heilbehelfe](Bundle-AtApsExampleBundle-Journey-1.html#implantate-medizinische-geräte-und-heilbehelfe) hervorgeht. Weiters ersichtlich ist eine Bilddarmentferung (2015) und eine durchgeführte Koloskopie (2012).

- Bei der Kontrolle der eingetragenen [Impfungen](Bundle-AtApsExampleBundle-Journey-1.html#impfungen) sieht Dr. Hausärztin, dass am 8. Jänner eine Diphtherie-Pertussis-Poliomyelitis-Tetanus-Impfung durchgeführt wurde.

Im Anschluss untersucht Dr. Hausärztin die Patientin und misst Körpergröße und -gewicht, Blutdruck und Puls (*Vitalparameter*) und erhebt den Raucherstauts, Alkoholkonsum und körperliche Aktivität (*Lebensstil*) der Patientin und dokumentiert dies in einem neuen Befund.
Bei der Untersuchung wird eine Parodontalerkrankung diagnostiziert.

Zuletzt veranlasst Dr. Hausärztin eine Labordiagnostik und empfiehlt einen Zahnarztbesuch.

Dr. Hausärztin speichert ihren soeben erstellten Befund und kontrolliert die automatisch von der zentralen Anwendung aktualisierte [APS (Journey-2)](Bundle-AtApsExampleBundle-Journey-2.html) durch erneute Abfrage.

**2. Arztbesuch**

Dr. Hausarzt bespricht die Laborergebnisse, die am 13. Februar eingetroffen sind, mit der Patientin. Die Ergebnisse sind in der APS in der Sektion [Diagnostische Resultate (Journey-3)](Bundle-AtApsExampleBundle-Journey-3.html#diagnostische-resultate) ersichtlich.
