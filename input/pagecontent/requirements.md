**MOVE TO SCOPE AND CONTENT**

### Sektionen der Austrian Patient Summary

Die Austrian Patient Summary (APS) besteht aus folgenden Sektionen:
<br><br>
[![overview](APS_Sections.drawio.png){: style="width: 75%"}](APS_Sections.drawio.png)
<br>

**Begriffsdefintion**<br>
**Required**: Ein als Required gekennzeichnetes Element ist ein Pflichtfeld und muss vorhanden sein. In FHIR wird diese Verpflichtung durch die Kardinalität festgelegt, typischerweise 1..1 oder 1..\*.<br>
**Recommended**: Elemente mit diesem Status sind dringend empfohlen, aber nicht verpflichtend. Sie sollen befüllt werden, sofern Informationen verfügbar sind. In FHIR-Profilen wird dies typischerweise durch Must Support oder erläuternde Kommentare kenntlich gemacht. Systeme müssen das Element verarbeiten können, sind jedoch nicht verpflichtet, es stets bereitzustellen.<br>
**Optional**: Ein als Optional gekennzeichnetes Element kann verwendet werden, ist jedoch nicht verpflichtend. In FHIR wird dies meist durch die Kardinalität 0..1 oder 0..\* abgebildet.<br>

Im Folgenden werden die Inhalte der einzelnen Sektionen zusammenfassend beschrieben. Sofern im Vergleich zur internationalen Spezifikation österreichspezifische Anpassungen (Profile) vorgenommen wurden, werden diese angeführt und begründet.
<br>
<br>

**INTEGRATE INTO COMPOSITION**

**ADMINISTRATIVE DATEN**

| **Sektion** | **Beschreibung** | **Konformität** | **Profile** |
|---|---|---|---|
| **Patient (Subject)** | Patientendaten, inkl. Angabe von Kontaktpersonen, Hausarzt bzw. primäre Ansprechpartner. | 1..1 | [AtApsPatient](StructureDefinition-at-aps-patient.html) |
| **Verfasser (Author)** | Autor der Patient Summary. Bei Angabe eines Devices z.B. automatische Erstellung der Patient Summary durch die Zentrale Anwendung. | 1..* | [AtApsPractitioner](StructureDefinition-at-aps-practitioner.html), [AtApsPractitionerRole](StructureDefinition-at-aps-practitionerrole.html), [AtApsDevice](StructureDefinition-at-aps-device.html) |
| **Rechtlicher Unterzeichner (Attester)** | Person, die die Richtigkeit der Zusammenstellung bestätigt. Darf bei automatischer Erstellung durch ein Device nicht angegeben werden. | 0..* | [AtApsPractitioner](StructureDefinition-at-aps-practitioner.html), [AtApsPractitionerRole](StructureDefinition-at-aps-practitionerrole.html) |
| **Verwahrer des Dokuments (Custodian)** | Organisation, die die Patient Summary verwaltet (Zentrale Anwendung). | 1..1 | [AtApsOrganization](StructureDefinition-at-aps-organization.html) |

<br>
<br>

**INTEGRATE INTO COMPOSITION**

**MEDIZINISCHE DATEN**

| **Sektion** | **Beschreibung** | **Konformität** | **AT APS Profile** |
|---|---|---|---|
| **Medikationsliste (Medication Summary)** | Diese Sektion enthält eine Beschreibung der aktuell relevanten Medikamente des Patienten bzw. liefert Information über das Nichtvorhandensein. | 1..1 | [AtApsMedication](StructureDefinition-at-aps-medication.html)  <br>[AtApsMedicationadministration](StructureDefinition-at-aps-medicationadministration.html) <br> [AtApsMedicationdispense](StructureDefinition-at-aps-medicationdispense.html)  <br>[AtApsMedicationRequest](StructureDefinition-at-aps-medicationrequest.html) <br>[AtApsMedicationStatement](StructureDefinition-at-aps-medicationstatement.html) |
| **Allergien und Intoleranzen (Allergies and Intolerances)** | In dieser Sektion werden die relevanten Allergien oder Unverträglichkeiten des Patienten dokumentiert, wobei die Art der Reaktion (z.B. Ausschlag, Anaphylaxie usw.), vorzugsweise die auslösenden Stoffe, sowie optional die Kritikalität und die Bestimmtheit der Allergie beschrieben werden. Zumindest sollten die derzeit aktiven und alle relevanten früheren Allergien und Nebenwirkungen aufgeführt werden. Liegen keine Informationen über Allergien vor oder sind keine Allergien bekannt, sollte dies ebenfalls dokumentiert werden. | 1..1 | [AtApsAllergyIntolerance](StructureDefinition-at-aps-allergyintolerance.html) |
| **Gesundheitsprobleme und Risiken (Problems)** | Diese Sektion listet und beschreibt klinische Probleme oder Erkrankungen (kodierte Diagnosen), die derzeit für den Patienten relevant sind bzw. liefert Information über das Nichtvorhandensein. | 1..1 | [AtApsCondition](StructureDefinition-at-aps-condition.html) |
| **Eingriffe und Therapien (History of Procedures)** | Diese Sektion enthält eine Beschreibung früherer Eingriffe und Therapien. Darunter fallen zum Beispiel invasive diagnostische Verfahren (z.B. Herzkatheteruntersuchung), therapeutische Verfahren (z.B. Dialyse) und chirurgische Eingriffe (z.B. Appendektomie). Befunde und Dokumentation von z.B. im Rahmen von Disease-Management-Programmen durchgeführten Schulungen und Beratungen werden ebenfalls in dieser Sektion aufgenommen. Die Dokumentation der Information kann am Beispiel der Integrierten Versorgung z.B. der Fallkoordinator übernehmen. | 1..1 | [AtApsProcedure](StructureDefinition-at-aps-procedure.html) |
| **Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)** | Diese Sektion enthält Informationen und kodierte Einträge, die den Gebrauch von Medizinprodukten in der Krankengeschichte beschreiben, z.B. Insulinpumpen oder Herzschrittmacher. | 1..1 | [AtApsDeviceUseStatement](StructureDefinition-at-aps-deviceusestatement.html) <br> [AtApsDevice](StructureDefinition-at-aps-device.html)|
| **Impfungen (Immunization)** | Die Sektion beschreibt den aktuellen Impfstatus des Patienten und die dazugehörige Impfhistorie. | 0..1 | [AtApsImmunization](StructureDefinition-at-aps-immunization.html) |
| **Diagnostische Resultate (Results)** | Die Sektion fasst Untersuchungsergebnisse zusammen, die am Patienten erhoben oder anhand von biologischen In-vitro-Proben erstellt wurden. Dabei kann es sich um Laborergebnisse, Ergebnisse der anatomischen Pathologie oder um radiologische Ergebnisse handeln. | 0..1 | [AtApsObservationResultsLaboratoryPathology](StructureDefinition-at-aps-observationresultslaboratorypathology.html) <br>[AtApsObservationResultsRadiology](StructureDefinition-at-aps-observationresultsradiology.html) <br>[AtApsDiagnosticReport](StructureDefinition-at-aps-diagnosticreport.html) |
| **Vitalparameter (Vital Signs)** | Die Sektion umfasst Informationen wie Blutdruck, Körpertemperatur, Herzfrequenz, Atemfrequenz, Größe, Gewicht, Body-Mass-Index, Kopfumfang oder Pulsoximetrie. Insbesondere können auffällige Vitalparameter oder körperliche Befunde wie der letzte, maximale und/oder minimale Wert, der Ausgangswert oder relevante Trends angegeben werden. | 0..1 | [AtApsObservationVitalSigns](StructureDefinition-at-aps-observationvitalsigns.html) |
| **Vergangene Gesundheitsprobleme und Risiken (History of Past Illness)** | Die Sektion enthält eine Beschreibung der historischen klinischen Probleme oder Erkrankungen, die für die Patientin oder den Patienten in der Vergangenheit diagnostiziert wurden. | 0..1 | [AtApsCondition](StructureDefinition-at-aps-observationvitalsigns.html) |
| **Beeinträchtigungen (Functional Status)** | Diese Sektion enthält eine Beschreibung der Mobilität bzw. Fähigkeit der Patientin oder des Patienten, Handlungen des täglichen Lebens auszuführen, einschließlich möglicher Bedürfnisse. Hier könnte auch die Pflegestufe dokumentiert werden. | 0..1 | [AtApsCondition](StructureDefinition-at-aps-condition.html) |
| **Behandlungsplan (Plan of Care)** | Die Sektion enthält den Behandlungsplan inkl. Vorschlägen, Zielen und Anordnungen zur Kontrolle oder Verbesserung des Zustands des Patienten, zur Planung der nächsten empfohlenen oder vereinbarten Untersuchungen, Kontrolltermine und Schulungen. Durchgeführte Maßnahmen wie Untersuchungen oder Schulungen können in der Sektion "History of Procedures" dokumentiert werden.| 0..1 | [AtApsCareplan](StructureDefinition-at-aps-careplan.html) <br>  |
| **Lebensstil / Soziale Umstände und Verhalten (Social History)** | Diese Sektion erfasst den aktuellen Lebensstil einer Person. Angaben zum Rauchverhalten sowie zum Alkoholkonsum werden in den hierfür vorgesehenen spezifischen Ressourcen abgebildet. Weitere relevante Aspekte, wie z.B. körperliche Aktivität, Ernährungsgewohnheiten oder sonstige Verhaltensweisen, werden mithilfe der AtApsObservation-Ressource dokumentiert. | 0..1 | [AtApsObservation](StructureDefinition-at-aps-observation.html) <br>[AtApsObservationTobaccoUse](StructureDefinition-at-aps-observationtobaccouse.html) <br>[AtApsObservationAlcoholUse](StructureDefinition-at-aps-observationalcoholuse.html) |
| **Schwangerschaftshistorie (History of Pregnancy)** | Die Sektion ermöglicht die Dokumentation eines Schwangerschaftsstatus inkl. geplantem Entbindungstermin und eine kurze Zusammenfassung von vergangenen Schwangerschaften. | 0..1 | [AtApsObservationPregnancyStatus](StructureDefinition-at-aps-observationpregnancystatus.html) <br>[AtApsObservationPregnancyOutcome](StructureDefinition-at-aps-observationpregnancyoutcome.html) [AtApsObservationPregnancyEdd](StructureDefinition-at-aps-observationpregnancyedd.html) |
| **Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)** | Die Sektion kann aktuelle Verfügungen von Patienten beinhalten. | 0..1 | [AtApsConsent](StructureDefinition-at-aps-consent.html) <br> |
| **Warnungen (Alerts)** | Die Sektion ermöglicht Warnmeldungen, wenn bestimmte Umstände eintreten (z.B. wenn Grenzwerte für Blutdruck, Gewicht oder subjektives Befinden einen gewissen Zeitraum überschritten werden). | 0..1 | [AtApsFlagalert](StructureDefinition-at-aps-flagalert.html) <br> |
| **Patientenbericht (Patient Story)** | Die Sektion enthält narrativen Text sowie optionale Ressourcen, die zum Ausdruck bringen, was für den Patienten wichtig ist. Dazu können Bedürfnisse, Stärken, Werte, Bedenken und Präferenzen gehören, die für Personen relevant sind, die Unterstützung und Pflege anbieten. | 0..1 |  |

<br>
<br>
<br>

**MOVE TO USE CASE 1**

### Anwendungsfallbeschreibung - Patient Journey

Das folgende Anwendungsbeispiel beschreibt den primären Einsatzfall der Austrian Patient Summary und zeigt, wie die zu einem bestimmten Zeitpunkt verfügbaren Informationen im Rahmen der APS dargestellt werden.

Da derzeit noch nicht abschließend festgelegt ist, welche Dokumente und Systeme als Datenquellen für die APS herangezogen werden, werden im Folgenden bestimmte Annahmen getroffen. So könnten relevante Informationen beispielsweise aus Laborbefunden oder Ambulanzbefunden extrahiert werden.

*Beispiel*

**1. Arztbesuch**

Frau [Maria Musterfrau](Patient-at-aps-example-patient-01.html), geboren am 17. April 1989, nimmt am 8. Februar 2025 bei ihrer neuen Ärztin [Dr. Hanna Hausärztin](Practitioner-at-aps-example-practitioner-01.html) eine Vorsorgeuntersuchung in Anspruch. Diese ruft die aktuelle [APS (Journey-1)](Bundle-AtApsExampleBundle-Journey-1.html) ihrer Patientin ab, um eine Zusammenfassung bereits dokumentierter Erkrankungen und Befunde einsehen zu können:

- Die [Medikationsliste](Bundle-AtApsExampleBundle-Journey-1.html#medikationsliste) zeigt Dr. Hausärztin, die in der zentralen Anwendung e-Medikation verfügbaren Medikationsdaten der Patientin an. Dieser wurden vor ca. 2 Monaten nach einem Krankenhausaufenthalt aufgrund von zu hohem Blutdruck Ramipril (5 mg) verordnet.

- Um sich das genauer anzusehen, kann Dr. Hausärztin in der Sektion [Gesundheitsprobleme und Risiken](Bundle-AtApsExampleBundle-Journey-1.html#gesundheitsprobleme-und-risiken) unter der dort angeführten "Arteriellen Hypertonie" das zugrundeliegende Quelldokument, nämlich den Entlassungsbrief aus dem AKH Amadeus einsehen. Weiters ist in dieser Sektion ersichtlich, dass eine familiäre Vorbelastung bezüglich Diabetes mellitus vorliegt.

- In der Sektion [Vergangene Gesundheitsprobleme und Risiken](Bundle-AtApsExampleBundle-Journey-1.html#vergangene-gesundheitsprobleme-und-risiken) sieht Dr. Hausärztin eine in der Kindheit durchgemachte Windpocken-Erkrankung, basierend auf einem referenzierten Ambulanzbefund.

- Aus der Sektion [Allergien und Intoleranzen](Bundle-AtApsExampleBundle-Journey-1.html#allergien-und-intoleranzen) geht eine Hausstaubmilbenallergie hervor.

- Die Sektion [Eingriffe und Therapien](Bundle-AtApsExampleBundle-Journey-1.html#eingriffe-und-therapien) gibt Auskunft darüber, dass bei Frau Musterfrau im Jahr 2010 das Hüftgelenk ersetzt werden musste und sie daher links ein Hüftimplantat trägt, wie im Abschnitt [Implantate, medizinische Geräte und Heilbehelfe](Bundle-AtApsExampleBundle-Journey-1.html#implantate-medizinische-geräte-und-heilbehelfe) hervorgeht. Weiters ersichtlich ist eine Blinddarmentfernung (2015) und eine durchgeführte Koloskopie (2012).

- Bei der Kontrolle der eingetragenen [Impfungen](Bundle-AtApsExampleBundle-Journey-1.html#impfungen) sieht Dr. Hausärztin, dass am 8. Jänner eine Diphtherie-Pertussis-Poliomyelitis-Tetanus-Impfung durchgeführt wurde.

Im Anschluss untersucht Dr. Hausärztin die Patientin und misst Körpergröße und -gewicht, Blutdruck und Puls (*Vitalparameter*) und erhebt den Raucherstauts, Alkoholkonsum und körperliche Aktivität (*Lebensstil*) der Patientin und dokumentiert dies in einem neuen Befund.
Bei der Untersuchung wird eine Parodontalerkrankung diagnostiziert.

Zuletzt veranlasst Dr. Hausärztin eine Labordiagnostik und empfiehlt einen Zahnarztbesuch.

Dr. Hausärztin speichert ihren soeben erstellten Befund und kontrolliert die automatisch von der zentralen Anwendung aktualisierte [APS (Journey-2)](Bundle-AtApsExampleBundle-Journey-2.html) durch erneute Abfrage.

**2. Arztbesuch**

Dr. Hausarzt bespricht die Laborergebnisse, die am 13. Februar eingetroffen sind, mit der Patientin. Die Ergebnisse sind in der APS in der Sektion [Diagnostische Resultate (Journey-3)](Bundle-AtApsExampleBundle-Journey-3.html#diagnostische-resultate) ersichtlich.
