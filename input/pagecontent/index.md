### Einleitung

> Das ist der FHIR® Implementation Guide (IG) für das Austrian Patient Summary (APS). Die Vorgaben beruhen auf dem [HL7® Austria FHIR® Core Implementation Guide (HL7AT Core IG), Version 2.0.0](https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/2.0.0/) und dem HL7® Leitfaden für das [International Patient Summary (IPS), Version 2.0.0-ballot](https://hl7.org/fhir/uv/ips/2024Sep/) und sind kompatibel mit den Vorgaben für das Patient Summary für den grenzüberschreitenden Datenaustausch in der EU (MyHealth@EU Patient Summary Requirements Catalogue).

Das Austrian Patient Summary (APS) ist eine standardisierte, zusammenfassende Kurzakte die wesentlichen medizinischen Informationen eines Patienten enthält. Es dient dazu, Angehörigen von Gesundheitsberufen in Notfall-, Routine- oder grenzüberschreitenden Behandlungssituationen einen schnellen Überblick über den Gesundheitszustand des Patienten zu bieten.

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
