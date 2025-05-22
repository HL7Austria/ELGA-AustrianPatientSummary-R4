### Einleitung

> Das ist der FHIR® Implementation Guide (IG) für das Austrian Patient Summary (APS). Die Vorgaben beruhen auf dem [HL7® Austria FHIR® Core Implementation Guide (HL7AT Core IG), Version 2.0.0](https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/2.0.0/) und dem HL7® Leitfaden für das [International Patient Summary (IPS), Version 2.0.0-ballot](https://hl7.org/fhir/uv/ips/2024Sep/) und sind kompatibel mit den Vorgaben für das Patient Summary für den grenzüberschreitenden Datenaustausch in der EU (MyHealth@EU Patient Summary Requirements Catalogue).

Das Austrian Patient Summary (APS) ist eine standardisierte, zusammenfassende Kurzakte, die die wesentlichen medizinischen Informationen eines Patienten enthält. Es dient dazu, Angehörigen von Gesundheitsberufen in Notfall-, Routine- oder grenzüberschreitenden Behandlungssituationen einen schnellen Überblick über den Gesundheitszustand des Patienten zu bieten.

Ein Patient Summary enthält allgemeine demografische Daten des Patienten (z.B. Name, Geburtsdatum, Geschlecht), eine Zusammenfassung der für die weitere medizinische Behandlung wesentlichen Erkenntnisse und Inhalte aus den Krankenakten des Patienten (z.B. aktuelle medizinische Probleme, Allergien, größere chirurgische Eingriffe, medizinische Implantate) sowie die aktuelle Medikation.

<div class="note-to-balloters" markdown="1">
**Informationen für den Ballot**

- In der [AT APS Composition](StructureDefinition-at-aps-composition.html) wurde die Reihenfolge der `section`-Elemente festgelegt, wobei weitere `section`-Elemente (`openAtEnd`) angelegt werden dürfen. Ebenso wurde die Reihenfolge der `entry`-Elemente innerhalb der einzelnen `section`-Elemente festgelegt und es dürfen nur die angeführten Profile verwendet werden. Der Grund für diese Entscheidung beruht auf der Annahme, dass dadurch Instanzen schneller validiert werden können.
- Beispiele noch unvollständig weil Unklarheiten ...
</div>

#### Umfang

Das Patient Summary ist
- ein minimaler, hochstrukturierter, nicht-vollständiger Datensatz über die (in ELGA) verfügbaren Gesundheitsdaten,
- geeignet für alle medizinischen Fachrichtungen und Gesundheitseinrichtungen,
- unabhängig von der aktuellen Situation des Patienten,
- für die grenzüberschreitende Gesundheitsversorgung vorgesehen.

Das Patient Summary ist daher keine vollständige Krankenakte, sondern eine Zusammenfassung. "Minimaler und nicht-vollständiger Datensatz" bedeutet, dass nur ein Teil der Krankengeschichte im Patient Summary dokumentiert wird. Es soll den eigentlichen Gesundheitszustand des Patienten repräsentieren und nicht die gesamte Historie abbilden. Es ist unabhängig von der medizinischen Fachrichtung oder dem Typ der Gesundheitseinrichtung.

### Designentscheidung

Das Profil des APS leitet direkt vom [HL7AT Core IG](https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/2.0.0/) ab. Um darüber hinaus die Vorgaben des IPS zu erfüllen, wird auf die [imposeProfile-Extension](https://hl7.org/fhir/extensions/StructureDefinition-structuredefinition-imposeProfile.html) zurückgegriffen. Zusätzlich wurden bei der Erstellung des APS die Vorgaben aus dem Requirements Catalogue im Rahmen von [MyHealth@EU](https://health.ec.europa.eu/ehealth-digital-health-and-care/digital-health-and-care/electronic-cross-border-health-services_en) berücksichtigt. Weitere Erläuterungen finden sich im Kapitel [Hintergrund](background.html).

[![overview](austrian-ips-context.drawio.png){: style="width: 60%"}](austrian-ips-context.drawio.png)
