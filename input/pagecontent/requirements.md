### Module der Austrian Patient Summary

Die Austrian Patient Summary (APS) besteht aus folgenden Modulen:


[![overview](APS_Sections.drawio.png){: style="width: 60%"}](APS_Sections.drawio.png)


Im Folgenden werden die Inhalte der Module zusammenfassend beschrieben und, sofern österreichspezifische Anpassungen der internationalen Spezifikation (Profile) vorgenommen wurden, kurz begründet. (TODO)

**Administrative Daten**
- Patient (Subject): Patientendaten, inkl. Angabe von Kontaktpersonenen, Hausarzt bzw. primäre Ansprechpartner.
- Verfasser (Author): Person oder Gerät, welche/s das Patient Summary erstellt hat.
- Rechtlicher Unterzeichner (Attester): Person, die die Richtigkeit der Zusammenstellung bestätigt.
- Verwahrer des Dokuments (Custodian): Organisation, die das Patient Summary verwaltet.

**Medikationsliste (Medication Summary)**
Der Abschnitt Medication Summary enthält eine Beschreibung der aktuell relevanten Medikamente des Patienten bzw. liefert Information über das Nichtvorhandensein.

**Allergien und Intoleranzen (Allergies and Intolerances)**
Im Abschnitt Allergies and Intolerances werden die relevanten Allergien oder Unverträglichkeiten des Patienten dokumentiert, wobei die Art der Reaktion (z.B. Ausschlag, Anaphylaxie usw.), vorzugsweise die auslösenden Stoffe, sowie optional die Kritikalität und die Bestimmtheit der Allergie beschrieben werden. Zumindest sollten die derzeit aktiven und alle relevanten früheren Allergien und Nebenwirkungen aufgeführt werden. Liegen keine Informationen über Allergien vor oder sind keine Allergien bekannt, sollte dies in diesem Abschnitt deutlich dokumentiert werden.

**Gesundheitsprobleme und Risiken (Problems)** 
Der Abschnitt Problems listet und beschreibt klinische Probleme oder Erkrankungen (kodierte Diagnosen), die derzeit für den Patienten relevant sind oder bzw. liefert Information über das Nichtvorhandensein.

**Impfungen (Immunization)**
Der Abschnitt Immunization beschreibt den aktuellen Impfstatus einer Patientin oder eines Patienten und die dazugehörige Impfhistorie.

**Eingriffe und Therapien (History of Procedures)**
History of Procedures enthält eine Beschreibung früherer Eingriffe und Therapien. Darunter fallen zum Beispiel invasive diagnostische Verfahren, z. B. Herzkatheteruntersuchung; therapeutische Verfahren: z. B. Dialyse; chirurgische Eingriffe: z. B. Appendektomie. Außerdem können hier auch Teilnahmen an Schulungen oder Beratungen dokumentiert werden.

**Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)**
Der Abschnitt über Medical Devices enthält Informationen und kodierte Einträge, die den Gebrauch von Medizinprodukten in der Krankengeschichte beschreiben, z.B. Insulinpumpen oder Herzschrittmacher.

**Diagnostische Resultate (Results)**
Diagnostic Results fasst Untersuchungsergebnisse zusammen, die an der Patientin oder am Patienten erhoben oder anhand von biologischen In-vitro-Proben erstellt wurden. Dabei kann es sich um Laborergebnisse, Ergebnisse der anatomischen Pathologie oder um radiologische Ergebnisse handeln.

**Vitalparameter (Vital Signs)**
Vital Signs umfasst Informationen wie Blutdruck, Körpertemperatur, Herzfrequenz, Atemfrequenz, Größe, Gewicht, Body-Mass-Index, Kopfumfang oder Pulsoximetrie. Insbesondere können auffällige Vitalparameter oder körperliche Befunde wie der letzte, maximale und/oder minimale Werte, der Ausgangswert oder relevante Trends angegeben werden.

**Vergangene Gesundheitsprobleme und Risiken (History of  Past Illness)**
Der Abschnitt History of  Past Illness enthält eine Beschreibung der historischen klinischen Probleme oder Erkrankungen, die für die Patientin oder den Patienten in der Vergangenheit diagnostiziert wurden.

**Schwangerschaftshistorie (History of Pregnancy)** 
History of Pregnancy liefert, falls vorhanden, einen Schwangerschaftsstatus inkl. geplantem Entbindungstermin und eine kurze Zusammenfassung von vergangenen Schwangerschaften.

**Lebensstil / Soziale Umstände und Verhalten (Social History)**
Social History dokumentiert den aktuellen Lebensstil einer Person, z.B. den Raucherstatus und Informationen zum Alkoholkonsum.

**Beeinträchtigungen (Functional Status)**
Functional Status enthält eine Beschreibung der Mobilität bzw. Fähigkeit der Patientin oder des Patienten, Handlungen des täglichen Lebens auszuführen, einschließlich möglicher Bedürfnisse. Hier könnte auch die Pflegestufe dokumentiert werden.

**Behandlungsplan (Plan of Care)**
Der Plan of Care enthält den Behandlungsplan inkl. Vorschlägen, Zielen und Anordnungen und kann im Sinne einer "Versorgungscheckliste" aufgebaut werden, wobei die einzelnen Untersuchungen, Schulungen etc. dann Schritt für Schritt im Abschnitt History of Procedures dokumentiert und damit "abgehakt" werden können.

**Willenserklärungen und andere juridische Dokumente (AdvanceDirectives)**
Advance Directives kann aktuelle Verfügungen von Patientinnen und Patienten beinhalten.


### Anwendungsfallbeschreibung

<div>{% include aps-uml.svg %}</div>
<br clear="all"/>

#### UC1 Patient Summary aktualisieren/erstellen
Basierend neuer Dokumentation in den angebundenen Registern wird die APS automatische aktualisiert. Die Information der APS dient im Weiteren dazu, fachspezifische Dokumente (wie z.B. ein Leitdokument für Diabetes) zu generieren und für den Abruf zur Verfügung zu stellen.

#### UC2 Patient Summary lesen
TODO

### Generierung der APS
Zusammenspiel mit CDA

#### Beteiligte Akteure und Rollen
TODO