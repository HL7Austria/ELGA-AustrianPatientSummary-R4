### Einleitung

> Das ist der FHIR® Implementation Guide (IG) für das Austrian Patient Summary (APS). Die Vorgaben beruhen auf dem [HL7® Austria FHIR® Core Implementation Guide (HL7AT Core IG), Version 2.0.0](https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/2.0.0/) und dem HL7® Leitfaden für das [International Patient Summary (IPS), Version 2.0.0-ballot](https://hl7.org/fhir/uv/ips/2024Sep/), und sind auch kompatibel mit den Vorgaben für das Patient Summary für den grenzüberschreitenden Datenaustausch in der EU (MyHealth@EU Patient Summary Requirements Catalogue).

Ein Patient Summary ist eine standardisierte Zusammenfassung von grundlegenden medizinischen Informationen zu einem Patienten, um Angehörigen von Gesundheitsberufen einen schnellen Überblick über die wesentlichen Fakten zum Gesundheitszustand des Patienten zu verschaffen.

Das Patient Summary soll zur sicheren und zuverlässigen Gesundheitsversorgung beitragen, sowohl im Fall von unerwarteten oder ungeplanten Behandlungen (Unfall, Notfall), als auch bei geplanten Behandlungen, im Rahmen von organisationsübergreifenden Behandlungspfaden und bei der grenzüberschreitenden Gesundheitsversorgung.

Ein Patient Summary enthält allgemeine demografische Daten des Patienten (z.B. Name, Geburtsdatum, Geschlecht), eine Zusammenfassung der für die weitere medizinische Behandlung wesentlichen Erkenntnisse und Inhalte aus den Krankenakten des Patienten (z.B. aktuelle medizinische Probleme, Allergien, größere chirurgische Eingriffe, medizinische Implantate) sowie die aktuelle Medikation.

Ziel des Patient Summary ist es
- dem GDA einen schnellen Überblick über die (in ELGA) verfügbaren Informationen zu einem Patienten zu ermöglichen;
- die wesentlichen Gesundheitsinformationen eines Patienten eindeutig und hochstrukturiert vorliegen zu haben und in andere Sprachen übersetzbar zu machen.

#### Umfang

Das Patient Summary ist
- ein minimaler und nicht-vollständiger Datensatz,
- geeignet für alle medizinischen Fachrichtungen und Gesundheitseinrichtungen,
- unabhängig von der aktuellen Situation des Patienten,
- für die grenzüberschreitende Gesundheitsversorgung vorgesehen.

Das Patient Summary ist daher keine vollständige Krankenakte, sondern eine Zusammenfassung. "Minimaler und nicht-vollständiger Datensatz" bedeutet, dass nur ein Teil der Krankengeschichte im Patient Summary dokumentiert wird. Es soll den eigentlichen Gesundheitszustand des Patienten repräsentieren und nicht die gesamte Historie abbilden. Es ist unabhängig von der medizinischen Fachrichtung oder dem Typ der Gesundheitseinrichtung.

### Designentscheidung

Das Profil des APS leitet direkt vom [HL7AT Core IG](https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/2.0.0/) ab. Um darüber hinaus die Vorgaben des IPS zu erfüllen, wird auf die [imposeProfile-Extension](https://hl7.org/fhir/extensions/StructureDefinition-structuredefinition-imposeProfile.html) zurückgegriffen. Zusätzlich wurden bei der Erstellung des APS die Vorgaben aus dem Requirements Catalogue im Rahmen von [MyHealth@EU](https://health.ec.europa.eu/ehealth-digital-health-and-care/digital-health-and-care/electronic-cross-border-health-services_en) berücksichtigt.

[![overview](austrian-ips-context.drawio.png){: style="width: 60%"}](austrian-ips-context.drawio.png)

### Abhängigkeiten zu anderen Implementierungsleitfäden

{% include dependency-table.xhtml %}

### Cross Version Analyse

{% include cross-version-analysis.xhtml %}

### Globale Profile

{% include globals-table.xhtml %}

### Lizenz und rechtliche Bedingungen
HL7®, HEALTH LEVEL SEVEN® und FHIR® sind Marken im Besitz von Health Level Seven International, eingetragen beim United States Patent and Trademark Office.

Dieser Implementierungsleitfaden enthält und verweist auf geistiges Eigentum, das Dritten gehört („Third Party IP“). Mit der Annahme dieser Lizenzbedingungen werden keine Rechte in Bezug auf das geistige Eigentum Dritter gewährt. Der Lizenznehmer ist allein dafür verantwortlich, alle erforderlichen Lizenzen oder Genehmigungen für die Nutzung des geistigen Eigentums Dritter in Verbindung mit der Spezifikation oder auf andere Weise zu ermitteln und einzuholen.

#### IP-Statements

{% include ip-statements.xhtml %}