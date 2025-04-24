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
    text-align: center;
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

**ADMINISTRATIVE DATEN**

<div class="table-responsive">
    <table><thead>
  <tr>
    <th>Modul</th>
    <th>Beschreibung</th>
    <th>Profile</th>
    <th>Konformität</th>
    <th>Anmerkung / TODOs</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Patient (Subject)</td>
    <td>Patientendaten, inkl. Angabe von Kontaktpersonenen, Hausarzt bzw. primäre Ansprechpartner.</td>
    <td>HL7ATCorePatient</td>
    <td>1..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Verfasser (Author)</td>
    <td>Ersteller der Patient Summary<br>Automatische Erstellung: Gerät (Zentrale Anwendung)<br>Automatische und manuell erstellte Einträge: Device und Person</td>
    <td><br><a href="https://hl7.org/fhir/R4/device.html" target="_blank" rel="noopener noreferrer">Device</a><br>Device, HL7ATCorePractitioner, HL7ATCorePatient</td>
    <td><br>1..* <br>1..*</td>
    <td><br>1..1 Analog zu Kompl. Immunisierungsst.<br>? als mögliche spätere Variante (z.B. Patient Story: Patient, <br>Persistenzkennzeichnung durch den GDA)</td>
  </tr>
  <tr>
    <td>Rechtlicher Unterzeichner (Attester)</td>
    <td>Person, die die Richtigkeit der Zusammenstellung bestätigt <br>Automatische Erstellung<br>Automatisch und manuell erstellte Einträge: ?</td>
    <td><br>-<br>HL7ATCorePractitioner </td>
    <td><br>0..*<br>1..1 ?</td>
    <td><br>NP Analog zu Kompl. Immunisierungsst.<br>Patient Story durch den Patienten,<br>Persistenzkennzeichnung von Befunden durch den GDA</td>
  </tr>
  <tr>
    <td>Verwahrer des Dokuments (Custodian)</td>
    <td>Organisation, die das Patient Summary verwaltet (Zentrale Anwendung)</td>
    <td>HL7ATCoreOrganization </td>
    <td>1..1</td>
    <td></td>
  </tr>
</tbody></table>
</div>

<br>

**MEDIZINISCHE DATEN**

<div class="table-responsive">
    <table><thead>
  <tr>
    <th>Modul</th>
    <th>Beschreibung</th>
    <th>Profile</th>
    <th>Konformität</th>
    <th>Anmerkung / TODO</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Medikationsliste (Medication Summary)</td>
    <td>Der Abschnitt enthält eine Beschreibung der aktuell relevanten Medikamente des Patienten bzw. liefert Information über das Nichtvorhandensein.</td>
    <td></td>
    <td>1..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Allergien und Intoleranzen (Allergies and Intolerances)</td>
    <td>In dem Abschnitt werden die relevanten Allergien oder Unverträglichkeiten des Patienten dokumentiert, wobei die Art der Reaktion (z.B. Ausschlag, Anaphylaxie usw.), vorzugsweise die auslösenden Stoffe, sowie optional die Kritikalität und die Bestimmtheit der Allergie beschrieben werden. Zumindest sollten die derzeit aktiven und alle relevanten früheren Allergien und Nebenwirkungen aufgeführt werden. Liegen keine Informationen über Allergien vor oder sind keine Allergien bekannt, sollte dies in diesem Abschnitt deutlich dokumentiert werden.</td>
    <td></td>
    <td>1..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Gesundheitsprobleme und Risiken (Problems)</td>
    <td>Der Abschnitt listet und beschreibt klinische Probleme oder Erkrankungen (kodierte Diagnosen), die derzeit für den Patienten relevant sind bzw. liefert Information über das Nichtvorhandensein.</td>
    <td></td>
    <td>1..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Impfungen (Immunization)</td>
    <td>Der Abschnitt beschreibt den aktuellen Impfstatus eines Patienten und die dazugehörige Impfhistorie.</td>
    <td></td>
    <td>0..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Eingriffe und Therapien (History of Procedures)</td>
    <td>Der Abschnitt enthält eine Beschreibung früherer Eingriffe und Therapien. Darunter fallen zum Beispiel invasive diagnostische Verfahren, z.B. Herzkatheteruntersuchung; therapeutische Verfahren: z.B. Dialyse; chirurgische Eingriffe: z.B. Appendektomie. Außerdem können hier auch Teilnahmen an Schulungen oder Beratungen dokumentiert werden.</td>
    <td></td>
    <td>1..1</td>
    <td>Warum werden absolvierte Schulungen nicht im Careplan (Status completed)  dokumentiert?</td>
  </tr>
  <tr>
    <td>Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)</td>
    <td>Der Abschnitt über Medical Devices enthält Informationen und kodierte Einträge, die den Gebrauch von Medizinprodukten in der Krankengeschichte beschreiben, z.B. Insulinpumpen oder Herzschrittmacher.</td>
    <td></td>
    <td>1..1</td>
    <td>ad Krankengeschichte: korrekten Titel des Abschnittes verwenden</td>
  </tr>
  <tr>
    <td>Diagnostische Resultate (Results)</td>
    <td>Der Abschnitt fasst Untersuchungsergebnisse zusammen, die am Patienten erhoben oder anhand von biologischen In-vitro-Proben erstellt wurden. Dabei kann es sich um Laborergebnisse, Ergebnisse der anatomischen Pathologie oder um radiologische Ergebnisse handeln.</td>
    <td></td>
    <td>0..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Vitalparameter (Vital Signs)</td>
    <td>Der Abschnitt umfasst Informationen wie Blutdruck, Körpertemperatur, Herzfrequenz, Atemfrequenz, Größe, Gewicht, Body-Mass-Index, Kopfumfang oder Pulsoximetrie. Insbesondere können auffällige Vitalparameter oder körperliche Befunde wie der letzte, maximale und/oder minimale Werte, der Ausgangswert oder relevante Trends angegeben werden.</td>
    <td></td>
    <td>0..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Vergangene Gesundheitsprobleme und Risiken (History of Past Illness)</td>
    <td>Der Abschnitt enthält eine Beschreibung der historischen klinischen Probleme oder Erkrankungen, die für die Patientin oder den Patienten in der Vergangenheit diagnostiziert wurden.</td>
    <td></td>
    <td>0..1</td>
    <td>Titel: Krankengeschichte? oder "Risiken" entfern?</td>
  </tr>
  <tr>
    <td>Schwangerschaftshistorie (History of Pregnancy)</td>
    <td>Dieser Abschnitt ermöglicht die Dokumentation eines Schwangerschaftsstatus inkl. geplantem Entbindungstermin und eine kurze Zusammenfassung von vergangenen Schwangerschaften.</td>
    <td></td>
    <td>0..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Lebensstil / Soziale Umstände und Verhalten (Social History)</td>
    <td>Dieser Abschnitt dokumentiert den aktuellen Lebensstil einer Person, z.B. den Raucherstatus und Informationen zum Alkoholkonsum.</td>
    <td></td>
    <td>0..1</td>
    <td>Titel?</td>
  </tr>
  <tr>
    <td>Beeinträchtigungen (Functional Status)</td>
    <td>Dieser Abschnitt enthält eine Beschreibung der Mobilität bzw. Fähigkeit der Patientin oder des Patienten, Handlungen des täglichen Lebens auszuführen, einschließlich möglicher Bedürfnisse. Hier könnte auch die Pflegestufe dokumentiert werden.</td>
    <td></td>
    <td>0..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Behandlungsplan (Plan of Care)</td>
    <td>Dieser Abschnitt enthält den Behandlungsplan inkl. Vorschlägen, Zielen und Anordnungen zur Überwachung, Verfolgung oder Verbesserung des Zustands des Patienten. Die einzelnen Untersuchungen, Schulungen etc. können im Abschnitt History of Procedures dokumentiert werden.</td>
    <td></td>
    <td>0..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)</td>
    <td>Dieser Abschnitt kann aktuelle Verfügungen von Patienten beinhalten.</td>
    <td></td>
    <td>0..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Warnungen (Alerts)</td>
    <td>Dieser Abschnitt enthält Warnmeldungen. Sie sollen auf potenzielle Bedenken und Gefahren hinweisen.</td>
    <td></td>
    <td>0..1</td>
    <td></td>
  </tr>
  <tr>
    <td>Patientenbericht (Patient Story)</td>
    <td>Der Abschnitt enthält narrativen Text sowie optionale Ressourcen, die zum Ausdruck bringen, was für den Patienten wichtig ist. Dazu können Bedürfnisse, Stärken, Werte, Bedenken und Präferenzen für andere, die Unterstützung und Pflege anbieten, gehören. </td>
    <td></td>
    <td>0..1</td>
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