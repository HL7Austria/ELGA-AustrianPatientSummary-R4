Das folgende Kapitel soll die wichtigsten Prinzipen der APS zusammenfassen und Unterschiede zur IPS aufzeigen.

TODO: Was soll in dieses Kapitel:
- Auf welche Standards baut die APS auf
- Wie wird die APS erzeugt
- Mögliche Quellen (Dokumente/Anwendungen)
- zum aktuellen Zeitpunkt noch offene Punkte 

******************************

Die APS gewährleistet die nationale Implementierbarkeit unter Beibehaltung der semantischen und strukturellen Kompatibilität mit den IPS-Spezifikationen. Sie ist erweiterbar ausgelegt, um zukünftige Anforderungen, spezifische klinische Anwendungsfälle unter Einhaltung österreichischer Rahmenbedingungen abzubilden. Die nachstehenden Punkte fassen die wesentlichen Designprinzipien der APS zusammen.

### Beziehung zu HL7AT Core, IPS und MyHealth@EU

Die APS baut auf dem [HL7® Austria FHIR® Core Implementation Guide (HL7AT Core IG), Version 2.0.0](https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/2.0.0/) und dem HL7® Leitfaden für die [International Patient Summary (IPS), Version 2.0.0-ballot](https://hl7.org/fhir/uv/ips/2024Sep/) auf.
Nachdem es in FHIR® nicht möglich ist, mehr als eine Basisdefinition für eine StructureDefinition-Ressource anzugeben, wird nach Möglichkeit immer das entsprechende Profil aus dem HL7AT Core IG als Basisdefinition angegeben und das entsprechende Profil aus der IPS mit Hilfe der [`imposeProfile`-Extension](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) eingebunden. Damit kann eine Instanz der APS gegen beide Spezifikationen validiert werden.
Zusätzlich wurden bei der Erstellung der APS die Vorgaben aus dem Requirements Catalogue im Rahmen von [MyHealth@EU](https://health.ec.europa.eu/ehealth-digital-health-and-care/digital-health-and-care/electronic-cross-border-health-services_en) berücksichtigt, insbesondere im Hinblick auf die Erweiterung der verpflichtend zu befüllenden Sektionen. Weitere Erläuterungen finden sich im Kapitel [Hintergrund](background.html).

[![overview](austrian-ips-context.drawio.png){: style="width: 60%"}](austrian-ips-context.drawio.png)

<div class="dragon" markdown="1">

</div>

### FHIR® R4

Aktuell gibt es die IPS nur auf Basis von FHIR® R4. Ob und wann die IPS auch in R5 bzw. R6 zur Verfügung steht, ist noch nicht klar. Deshalb wird die APS zurzeit auch nur in FHIR® R4 spezifiziert.

### Struktur der Patient Summary

Das APS wird in diesem Leitfaden als HL7-FHIR-Dokument vom Typ "Bundle" spezifiziert. TODO: kurze Erklärung

### Verwendete Terminologien

TODO: Bevorzugte Terminologie SNOMED CD, LOINC, UCUM und weitere möglich  ?  Hinweis auf Snomed Lizenzen, Terminologieserver

### Erstellung und Abruf der IPS

Folgendes Use Case Diagramm stellt die relevanten Funktionen der Austrian Patient Summary dar.

<div>{% include aps-uml.svg %}</div>
<br clear="all"/>

#### APS aggregieren (UC1)

| **Element** | **Beschreibung** |
|---|---|
| **Akteur** | Zentrale Anwendung Patient Summary |
| **Beschreibung** | Die Inhalte der APS werden automatisch aus den angebundenen Registern (e-Medikation, e-Impfpass, etc.) zusammengeführt und basieren somit auf den aktuellsten verfügbaren Gesundheitsdaten des Patienten. Die APS dient darüber hinaus der Generierung fachspezifischer Dokumente (z. B. für bestimmte Krankheitsbilder wie Diabetes) nach definierten Kriterien und stellt diese für den Abruf bereit. Auf der APS basierende Dokumentenklassen werden in eigenen Implementierungsleitfäden spezifiziert. <br><br>**Hinweis:** Die genaue Beschreibung des Aggregationsprozesses folgt in einer späteren Version der APS-Spezifikation (siehe dazu auch Kapitel *Datenherkunft*) |
| **Auslöser** | Beim Abruf der APS wird automatisch ein Prozess gestartet, der die angebundenen Register auf neue oder geänderte Daten überprüft und die Inhalte in die Patient Summary übernimmt. |
| **Vorbedingungen** | Ein berechtigter Akteur hat lesend auf die APS (UC2) zugegriffen. In den angebundenen Registern liegen Gesundheitsdaten für den betreffenden Patienten vor. |
| **Ergebnis** | Die *Austrian Patient Summary* wurde mit den aktuellsten Gesundheitsinformationen aus den angebundenen Registern aggregiert. |

<br>

#### APS lesen (UC2)

| **Element** | **Beschreibung** |
|---|---|
| **Akteur** | Gesundheitsdiensteanbieter, Patient:in |
| **Beschreibung** | Ein GDA ruft die aktuellste Version der APS seines Patienten über sein Primärsystem bzw. ein GDA-Portal ab. Der Patient kann via ELGA-Zugangsportal auf seine aktuelle Patient Summary zugreifen. Die Patient Summary bietet in modular aufgebauten Abschnitten (Sektionen) eine strukturierte Zusammenfassung verfügbarer, medizinisch validierter Gesundheitsinformationen aus Registern, die an die Zentrale Anwendung Patient Summary angebunden sind. |
| **Verwendete Anwendungsfälle** | GUC1 Patient Summary generieren |
| **Auslöser** | - Konsultation durch GDA<br> - Informationswunsch durch Patienten<br> - Bedarf für Notfallversorgung, fachärztliche Zweitmeinung, etc. |
| **Vorbedingungen** | Der jeweilige Akteur ist berechtigt auf die Patient Summary zuzugreifen. |
| **Ergebnis** | Die aktuelle Version der Patient Summary wird angezeigt und steht zur Behandlungsunterstützung, Behandlungsplanung oder Informationsweitergabe zur Verfügung. |

### Datenherkunft

Zum aktuellen Zeitpunkt ist noch nicht abschließend geklärt, aus welchen Quellen bzw. über welche Mechanismen die Informationen in die APS übernommen werden. Insbesondere ist offen, ob bestimmte Angaben über e-Befunde bereitgestellt und diese als Quelldokumente herangezogen werden können. Grundsätzlich soll die Herkunft der Daten jeweils in Meta.source abgelegt werden; die konkrete Formatvorgabe für dieses Feld befindet sich noch in Ausarbeitung. Um zukünftige Anwendungsfälle abdecken zu können, besteht zudem die Möglichkeit, zu einem späteren Zeitpunkt zusätzlich Provenance zu verwenden.

### Patient Safety in IPS Context

Patient safety is foundational in healthcare and its importance is even more pronounced in the context of cross-border care information exchange. Understanding specific data elements from IPS profiles is critical to ensuring that clinicians have accurate, timely, and relevant information to make informed decisions. Ignoring or misinterpreting these elements can lead to adverse events.

Elements throughout this IPS guide have [obligations for both Creators and Consumers](./Must-Support-and-Obligations.html) of IPS documents, many of which impact patient safety. Elements flagged with ["Is-modifier" (shown as "?!")](https://hl7.org/fhir/R4/conformance-rules.html#isModifier) or those with a SHALL:handle obligation cannot be safely ignored in patient summary sharing. Implementers that are developing IPS consuming functions, either viewers or services that use the information in the IPS need to pay careful attention to obligations and "Is-modifier" flags. Many IPS documents will not populate the elements, particularly in a testing context, but when these elements are populated, or have unusual values, it is important that the clinical facts they convey are understood. Experience gained from the IPS development process has demonstrated that they are easily missed.

Here are some examples of clinical safety cases where ignoring data may introduce patient risk to downstream care:

- The IPS includes an allergy (AllergyIntolerance) where the reaction "severity" (an element with SHALL:handle obligations) is severe
- The IPS includes an immunization (Immunization) where the "occurenceDateTime" (an element with SHALL:handle obligation) is so old that immunity is no longer conferred 
- The IPS includes a problem (Condition) which the "verificationStatus" (an is-Modifier) is "refuted", meaning that the problem has been ruled out
- The IPS includes a medication (MedicationRequest or MedicationStatus) where the "status" (an is-Modifier) is "stopped"
- The IPS includes a lab result (Observation) where the "status" (an is-Modifier) is "preliminary", meaning this result may be incomplete or unverified

While this specification does not precisely define how downstream consumers should manage these elements, it is often recommended these elements be available for human-review (often shown as an obligation of SHOULD:display). Of course, language translation and presentation of textual narrative also have implications for patient safety as described with the [Design Conventions](./Design-Conventions.html) of the guide. The above highlights on is-Modifier flags and obligations are indicators of some critical elements for safe and effective clinical care.

Ultimately, patient safety benefits from consistent, accurate, and context-aware handling of IPS documents. Creators and consumers of IPS documents should be aware that all data may impact patient safety.
