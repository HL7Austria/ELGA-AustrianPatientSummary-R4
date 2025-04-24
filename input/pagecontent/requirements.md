<style>
  .table-responsive {
    display: block;
    width: 100%;
    overflow-x: auto;
  }

  .table-responsive > table {
    width: 100%;
    border-collapse: collapse;
  }

  .table-responsive th {
    text-align: left;
    font-weight: bold;
  }

  .table-responsive td:first-child,
  .table-responsive th:first-child {
    font-weight: bold;
  }
</style>

### Module der Austrian Patient Summary

Die Austrian Patient Summary (APS) besteht aus folgenden Modulen:


[![overview](APS_Sections.drawio.png){: style="width: 60%"}](APS_Sections.drawio.png)
<br>

Im Folgenden werden die Inhalte der Module zusammenfassend beschrieben und, sofern österreichspezifische Anpassungen der internationalen Spezifikation (Profile) vorgenommen wurden, kurz begründet. (TODO)
<br>
<br>

**ADMINISTRATIVE DATEN**

<div class="table-responsive">
    <table><table><thead>
  <tr>
    <th>Modul</th>
    <th>Beschreibung</th>
    <th>Konformität</th>
    <th>Profile</th>
    <th>Anmerkung / TODOs</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Patient (Subject)</td>
    <td>Patientendaten, inkl. Angabe von Kontaktpersonenen, Hausarzt bzw. primäre Ansprechpartner.</td>
    <td>1..1</td>
    <td>HL7ATCorePatient</td>
    <td></td>
  </tr>
  <tr>
    <td>Verfasser (Author)</td>
    <td>Automatische Erstellung der Patient Summary durch die Zentrale Anwendung</td>
    <td>1..* </td>
    <td><a href="https://hl7.org/fhir/R4/device.html" target="_blank" rel="noopener noreferrer">Device</a></td>
    <td>1..1 analog zu Kompl. Immunisierungsst.<br>Prüfen: auch zutreffend für evt. zukünft. mixed Erstellung: z.B. Patient Story erstellt durch Patienten oder <br>Persistenzkennzeichnung von Dokumenten, PS-Kuratierung durch GDA?</td>
  </tr>
  <tr>
    <td>Rechtlicher Unterzeichner (Attester)</td>
    <td>Person, die die Richtigkeit der Zusammenstellung bestätigt. Entfällt bei automatischer Erstellung.</td>
    <td>0..*</td>
    <td></td>
    <td>0..0 NP analog zu Kompl. Immunisierungsst.<br>Prüfen: zukünft. mixed Erstellung beachten?</td>
  </tr>
  <tr>
    <td>Verwahrer des Dokuments (Custodian)</td>
    <td>Organisation, die das Patient Summary verwaltet (Zentrale Anwendung)</td>
    <td>1..1</td>
    <td>HL7ATCoreOrganization </td>
    <td></td>
  </tr>
</tbody></table>
</div>

<br>
<br>

**MEDIZINISCHE DATEN**

<div class="table-responsive">
    <table><thead>
  <tr>
    <th>Modul</th>
    <th>Beschreibung</th>
    <th>Konformität</th>
    <th>AT APS Profile</th>
    <th>IPS Profile Anmerkung / TODO</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Medikationsliste (Medication Summary)</td>
    <td>Der Abschnitt enthält eine Beschreibung der aktuell relevanten Medikamente des Patienten bzw. liefert Information über das Nichtvorhandensein.</td>
    <td>1..1</td>
    <td>AtApsMedication<br>AtApsMedicationRequest<br>AtApsMedicationStatement</td>
    <td>MedicationStatement<br>MedicationRequest MedicationAdministration MedicationDispense<br>DocumentReference<br><br>Wieso wird AtApsMedication nicht in der Composition verwendet?</td>
  </tr>
  <tr>
    <td>Allergien und Intoleranzen (Allergies and Intolerances)</td>
    <td>In dem Abschnitt werden die relevanten Allergien oder Unverträglichkeiten des Patienten dokumentiert, wobei die Art der Reaktion (z.B. Ausschlag, Anaphylaxie usw.), vorzugsweise die auslösenden Stoffe, sowie optional die Kritikalität und die Bestimmtheit der Allergie beschrieben werden. Zumindest sollten die derzeit aktiven und alle relevanten früheren Allergien und Nebenwirkungen aufgeführt werden. Liegen keine Informationen über Allergien vor oder sind keine Allergien bekannt, sollte dies in diesem Abschnitt deutlich dokumentiert werden.</td>
    <td>1..1</td>
    <td>AtApsAllergyIntolerance</td>
    <td>AllergyIntolerance<br>DocumentReference</td>
  </tr>
  <tr>
    <td>Gesundheitsprobleme und Risiken (Problems)</td>
    <td>Der Abschnitt listet und beschreibt klinische Probleme oder Erkrankungen (kodierte Diagnosen), die derzeit für den Patienten relevant sind bzw. liefert Information über das Nichtvorhandensein.</td>
    <td>1..1</td>
    <td>AtApsCondition</td>
    <td>Condition<br>DocumentReference</td>
  </tr>
  <tr>
    <td>Impfungen (Immunization)</td>
    <td>Der Abschnitt beschreibt den aktuellen Impfstatus eines Patienten und die dazugehörige Impfhistorie.</td>
    <td>0..1</td>
    <td>AtApsImmunization</td>
    <td>Immunization or DocumentReference</td>
  </tr>
  <tr>
    <td>Eingriffe und Therapien (History of Procedures)</td>
    <td>Der Abschnitt enthält eine Beschreibung früherer Eingriffe und Therapien. Darunter fallen zum Beispiel invasive diagnostische Verfahren, z.B. Herzkatheteruntersuchung; therapeutische Verfahren: z.B. Dialyse; chirurgische Eingriffe: z.B. Appendektomie. Außerdem können hier auch Teilnahmen an Schulungen oder Beratungen dokumentiert werden.</td>
    <td>1..1</td>
    <td>AtApsProcedure</td>
    <td>Procedure or DocumentReference<br><br>Warum werden absolvierte Schulungen nicht im Careplan (Status completed)  dokumentiert?</td>
  </tr>
  <tr>
    <td>Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)</td>
    <td>Der Abschnitt über Medical Devices enthält Informationen und kodierte Einträge, die den Gebrauch von Medizinprodukten in der Krankengeschichte beschreiben, z.B. Insulinpumpen oder Herzschrittmacher.</td>
    <td>1..1</td>
    <td>AtApsDeviceUseStatement</td>
    <td>DeviceUseStatement or DocumentReference</td>
  </tr>
  <tr>
    <td>Diagnostische Resultate (Results)</td>
    <td>Der Abschnitt fasst Untersuchungsergebnisse zusammen, die am Patienten erhoben oder anhand von biologischen In-vitro-Proben erstellt wurden. Dabei kann es sich um Laborergebnisse, Ergebnisse der anatomischen Pathologie oder um radiologische Ergebnisse handeln.</td>
    <td>0..1</td>
    <td>AtApsObservationResultsLaboratoryPathology<br>AtApsObservationResultsRadiology<br>AtApsDiagnosticReport</td>
    <td>Observation or DiagnosticReport or DocumentReference</td>
  </tr>
  <tr>
    <td>Vitalparameter (Vital Signs)</td>
    <td>Der Abschnitt umfasst Informationen wie Blutdruck, Körpertemperatur, Herzfrequenz, Atemfrequenz, Größe, Gewicht, Body-Mass-Index, Kopfumfang oder Pulsoximetrie. Insbesondere können auffällige Vitalparameter oder körperliche Befunde wie der letzte, maximale und/oder minimale Werte, der Ausgangswert oder relevante Trends angegeben werden.</td>
    <td>0..1</td>
    <td>AtApsObservationVitalSigns</td>
    <td>Observation or DocumentReference</td>
  </tr>
  <tr>
    <td>Vergangene Gesundheitsprobleme und Risiken (History of Past Illness)</td>
    <td>Der Abschnitt enthält eine Beschreibung der historischen klinischen Probleme oder Erkrankungen, die für die Patientin oder den Patienten in der Vergangenheit diagnostiziert wurden.</td>
    <td>0..1</td>
    <td>AtApsCondition</td>
    <td>Condition or DocumentReference<br><br>Titel: Krankengeschichte? oder "Risiken" entfern?<br></td>
  </tr>
  <tr>
    <td>Schwangerschaftshistorie (History of Pregnancy)</td>
    <td>Dieser Abschnitt ermöglicht die Dokumentation eines Schwangerschaftsstatus inkl. geplantem Entbindungstermin und eine kurze Zusammenfassung von vergangenen Schwangerschaften.</td>
    <td>0..1</td>
    <td>AtApsObservationPregnancyStatus<br>AtApsObservationPregnancyOutcome</td>
    <td>Observation or DocumentReference)</td>
  </tr>
  <tr>
    <td>Lebensstil / Soziale Umstände und Verhalten (Social History)</td>
    <td>Dieser Abschnitt dokumentiert den aktuellen Lebensstil einer Person, z.B. den Raucherstatus und Informationen zum Alkoholkonsum.</td>
    <td>0..1</td>
    <td>AtApsObservationPregnancyOutcome</td>
    <td>Observation or DocumentReference<br><br>Titel?</td>
  </tr>
  <tr>
    <td>Beeinträchtigungen (Functional Status)</td>
    <td>Dieser Abschnitt enthält eine Beschreibung der Mobilität bzw. Fähigkeit der Patientin oder des Patienten, Handlungen des täglichen Lebens auszuführen, einschließlich möglicher Bedürfnisse. Hier könnte auch die Pflegestufe dokumentiert werden.</td>
    <td>0..1</td>
    <td>AtApsObservationAlcoholUse</td>
    <td>Condition or ClinicalImpression or DocumentReference</td>
  </tr>
  <tr>
    <td>Behandlungsplan (Plan of Care)</td>
    <td>Dieser Abschnitt enthält den Behandlungsplan inkl. Vorschlägen, Zielen und Anordnungen zur Überwachung, Verfolgung oder Verbesserung des Zustands des Patienten. Die einzelnen Untersuchungen, Schulungen etc. können im Abschnitt History of Procedures dokumentiert werden.</td>
    <td>0..1</td>
    <td></td>
    <td>CarePlan</td>
  </tr>
  <tr>
    <td>Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)</td>
    <td>Dieser Abschnitt kann aktuelle Verfügungen von Patienten beinhalten.</td>
    <td>0..1</td>
    <td></td>
    <td>Consent or DocumentReference</td>
  </tr>
  <tr>
    <td>Warnungen (Alerts)</td>
    <td>Dieser Abschnitt enthält Warnmeldungen. Sie sollen auf potenzielle Bedenken und Gefahren hinweisen.</td>
    <td>0..1</td>
    <td></td>
    <td>Flag or DocumentReference<br>FlagAlertUvIps</td>
  </tr>
  <tr>
    <td>Patientenbericht (Patient Story)</td>
    <td>Der Abschnitt enthält narrativen Text sowie optionale Ressourcen, die zum Ausdruck bringen, was für den Patienten wichtig ist. Dazu können Bedürfnisse, Stärken, Werte, Bedenken und Präferenzen für andere, die Unterstützung und Pflege anbieten, gehören. </td>
    <td>0..1</td>
    <td></td>
    <td></td>
  </tr>
</tbody></table>
</div>


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