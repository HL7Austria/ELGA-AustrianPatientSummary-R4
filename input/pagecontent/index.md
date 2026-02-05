### Einleitung

> Das ist der FHIR® Implementation Guide (IG) für die Austrian Patient Summary (APS). Die Vorgaben beruhen auf dem [HL7® Austria FHIR® Core Implementation Guide (HL7AT Core IG), Version 2.0.0](https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/2.0.0/) und dem HL7® Leitfaden für die [International Patient Summary (IPS), Version 2.0.0](https://hl7.org/fhir/uv/ips/STU2/) und sind kompatibel mit den Vorgaben für die Patient Summary für den grenzüberschreitenden Datenaustausch in der EU (MyHealth@EU Patient Summary Requirements Catalogue).

Die Austrian Patient Summary (APS) ist eine standardisierte, zusammenfassende Kurzakte, die die wesentlichen medizinischen Informationen eines Patienten enthält. Sie dient dazu, Angehörigen von Gesundheitsberufen in Notfall-, Routine- oder grenzüberschreitenden Behandlungssituationen einen schnellen Überblick über den Gesundheitszustand des Patienten zu bieten. Die APS gewährleistet die nationale Implementierbarkeit unter Beibehaltung der semantischen und strukturellen Kompatibilität mit der IPS-Spezifikation.

Eine Patient Summary enthält allgemeine demografische Daten des Patienten (z.B. Name, Geburtsdatum, Geschlecht), eine Zusammenfassung der für die weitere medizinische Behandlung wesentlichen Erkenntnisse und Inhalte aus den Krankenakten des Patienten (z.B. aktuelle medizinische Probleme, Allergien, größere chirurgische Eingriffe, medizinische Implantate) sowie die aktuelle Medikation.

#### Umfang

Die APS ist
- ein minimaler, hochstrukturierter, nicht-vollständiger Datensatz über die verfügbaren Gesundheitsdaten,
- geeignet für die Nutzung durch alle berechtigten Angehörigen der Gesundheitsdienste,
- unabhängig von der aktuellen Situation des Patienten oder der behandelnden Einrichtung,
- geeignet für die grenzüberschreitende Gesundheitsversorgung.

Die APS ist daher keine vollständige Krankenakte, sondern eine Zusammenfassung. "Minimaler und nicht-vollständiger Datensatz" bedeutet, dass nur ein Teil der Krankengeschichte in der APS dokumentiert wird. Sie soll den eigentlichen Gesundheitszustand des Patienten repräsentieren und nicht die gesamte Historie abbilden und ist unabhängig von der medizinischen Fachrichtung oder dem Typ der Gesundheitseinrichtung.
