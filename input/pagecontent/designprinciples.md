#### Kontext und Verwendung von Patient Summary

Die Patient Summary ist eine standardisierte Kurzakte, die die wesentlichen medizinischen Informationen eines Patienten zusammenfasst und eine kohärente Momentaufnahme bietet. Sie ist rein informativ und nicht zur direkten Ausführung oder maschinellen Verarbeitung bestimmt.
Die APS gewährleistet die nationale Implementierbarkeit unter Beibehaltung der semantischen und strukturellen Kompatibilität mit den IPS-Spezifikationen.

#### Patientensicherheit

Ein korrektes Verständnis der Datenelemente der Patient Summary ist entscheidend, damit Behandler fundierte Entscheidungen treffen können und Fehler vermieden werden. Daher sind sicherheitskritische Datenelemente für Ersteller und Nutzer der Patient Summary verpflichtend zu berücksichtigen. 

Elemente, die mit ["Is-modifier" ("?!")](https://hl7.org/fhir/R4/conformance-rules.html#isModifier) oder „SHALL:handle” gekennzeichnet sind, dürfen weder bei der Erstellung noch bei der Weiterverarbeitung oder Anzeige der APS ignoriert werden und sind für menschliche Überprüfung sichtbar (SHOULD:display) zu machen.

Beispiele für sicherheitsrelevante Fälle:
* Eine dokumentierte Allergie (*AllergyIntolerance*), deren Schweregrad (*severity*) als schwer (*severe*) eingestuft ist.
* Eine Diagnose (*Condition*), deren Verifikationsstatus (*verificationStatus*) widerlegt ist (*refuted*), also ausgeschlossen wurde.
* Eine Medikation (*MedicationStatement*), deren Status *stopped* lautet.
* Ein Laborergebnis (*Observation*), dessen Status vorläufig (*preliminary*) ist, also noch nicht validiert wurde.

Die korrekte Übersetzung und Darstellung von Inhalten hat ebenfalls Auswirkungen auf die Patientensicherheit.

#### Structuring Terminology Choices

Die APS wird in diesem Leitfaden als HL7-FHIR-Dokument vom Typ "Bundle" spezifiziert.
Die APS Composition legt fest, dass nur jene Profile verwendet werden dürfen, die vorgesehene Sektionen und Entries enthalten. Eine Ausnahme bilden die Sektionen *Diagnostische Resultate*, *Vitalparameter* und *Lebensstil* mit der slicing.rule „openAtEnd“. 
Erklärung?
Reihenfolge der Sektionen?
TODO:
* Bevorzugte Terminologie SNOMED CD, LOINC, UCUM, ergänzt mit nationalen Value Sets und Mappings ?  Hinweis auf Snomed Lizenzen, Terminologieserver
* Einschränkungen von IPS, AtApsPatient usw wenn noch nicht an anderer Stelle beschrieben

#### Erstellung und Abruf der APS

Folgendes Use Case Diagramm stellt die relevanten Funktionen der Austrian Patient Summary dar.

<div>{% include aps-uml.svg %}</div>
<br clear="all"/>



<br>

##### APS lesen (UC2)




### Designkonventionen

##### Beziehung zu HL7AT Core, IPS und MyHealth@EU

Die APS baut auf dem [HL7® Austria FHIR® Core Implementation Guide (HL7AT Core IG), Version 2.0.0](https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/2.0.0/) und dem HL7® Leitfaden für die [International Patient Summary (IPS), Version 2.0.0](https://hl7.org/fhir/uv/ips/STU2/) auf. 

Nachdem es in FHIR® nicht möglich ist, mehr als eine Basisdefinition für eine StructureDefinition-Ressource anzugeben, wird nach Möglichkeit immer das entsprechende Profil aus dem HL7AT Core IG als Basisdefinition angegeben und das entsprechende Profil aus der IPS mit Hilfe der [`imposeProfile`-Extension](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) eingebunden. Damit kann eine Instanz der APS gegen beide Spezifikationen validiert werden.

<div class="dragon" markdown="1">
Beim Lesen der APS-Profile müssen insofern auch immer die IPS-Profile berücksichtigt werden. So ist das `subject` in der [AT APS Composition](StructureDefinition-at-aps-composition.html) mit `0..1` modelliert. In der [Composition (IPS)](https://hl7.org/fhir/uv/ips/STU2/StructureDefinition-Composition-uv-ips.html) ist das `subject` allerdings mit `1..1` modelliert. Die strengere Regel wird bei der Validierung einer Instanz schlagend.
</div>

Zusätzlich wurden bei der Erstellung der APS die Vorgaben aus dem Requirements Catalogue im Rahmen von [MyHealth@EU](https://health.ec.europa.eu/ehealth-digital-health-and-care/digital-health-and-care/electronic-cross-border-health-services_en) berücksichtigt, insbesondere im Hinblick auf die Erweiterung der verpflichtend zu befüllenden Sektionen. Weitere Erläuterungen finden sich im Kapitel [Hintergrund](background.html).

[![overview](austrian-ips-context.drawio.png){: style="width: 60%"}](austrian-ips-context.drawio.png)

##### FHIR® R4

Aktuell liegt die IPS nur auf Basis von FHIR® R4 vor. Ob und wann die IPS auch in R5 bzw. R6 zur Verfügung steht, ist noch nicht klar. Deshalb wird die APS zurzeit auch nur in FHIR® R4 spezifiziert.

#### Profilierungsansatz

Wie bei der IPS wurde bei der APS folgender Profilierungsansatz gewählt: Anstatt die Ressourcen streng zu beschränken, wurden hauptsächlich die Pflichtelemente des Minimaldatensatzes festgelegt, während anderen offen bleiben.
Dieser Ansatz erleichtert die Wiederverwendung der Profile und erlaubt den schrittweisen Zugriff auf zusätzliche relevante Informationen, um zukünftige Anforderungen und spezifische klinische Anwendungsfälle abzubilden.
* Einschränkungen von IPS, AtApsPatient usw wenn noch nicht an anderer Stelle beschrieben ?

#### Open Slicing

TODO @Gabriel: bitte für die APS anpassen
One of the important and useful capabilities of FHIR profiling is slicing, where multiple sets of constraints for a specific use case can be defined for a resource element or a complex element group (slicing can be used with repeating, type choice or non-repeating elements). Most of the slices specified in this guide are open (i.e. slicing.rules is not closed), which means that it is possible for resource instances with elements that do not match any of the defined slices to still be conformant with the profile as long as they satisfy the remaining profile constraints.

Having this clear is important for correctly understanding the published profiles. For example, the optional section of Social History has open slicing on the entry element allowing for the use of the IPS Tobacco Use profile, the IPS Alcohol Use profile, or any other Observation or DocumentReference. Therefore, while specific IPS profiles are described in this guide, other profiles may also be included as well.

#### Narrativer Text und Übersetzungen

Obwohl strukturierte Daten (FHIR-Resources, Terminologien wie SNOMED CT) in der Patient Summary bevorzugt werden, kann nicht jedes System alle Informationen kodieren oder interpretieren. Daher enthält die Patient Summary Composition die Anforderung, dass jede Sektion einen menschenlesbaren narrativen Text enthalten muss. Dies steht im Einklang mit den Grundsätzen von FHIR-Dokumenten und stellt insbesondere im grenzüberschreitenden Austausch sicher, dass alle relevanten Inhalte weiterhin zugänglich sind (Sicherheits- und Fallback-Funktion). Weiters beitet FHIR Mechanismen zur Unterstützung von mehrsprachigen Übersetzungen über erweiterte Datentypen (z. B. CodeableConcept, Coding).

Gemäß IPS-Standard bestehen derzeit keine Einschränkungen hinsichtlich der Gestaltung narrativer Beschreibungen. Es wird jedoch empfohlen, folgende Punkte zu beachten:
- den Inhalt von Composition.section.text (verpflichtend) nicht in Composition.text duplizieren,
- Verwendung verständlicher, gebräuchlicher Begriffe
- konsistente Reihenfolge der Tabellen (und gegebenenfalls Erläuterung der Reihenfolge)
- Einbindung mehrsprachiger Beschreibungen (mit entsprechenden Tags), wenn möglich
- Berücksichtigung der Aktualität der Informationen in den Beschreibungen via meta.lastUpdated, wenn möglich

Der narrative Text ist auch für den rechtlichen Unterzeichner des Dokuments (Attester) von Bedeutung, da er den präsentierten und prüfbaren Dokumentinhalt darstellt. Da in Österreich die APS automatisch generiert wird, entfällt der Attester.

#### Linking Narrative to Discrete FHIR Resources
TODO ?

#### Medication Lists in the IPS
TODO ?

#### Medicinal Product Identification
TODO ?

#### Datenherkunft

Zum aktuellen Zeitpunkt ist noch nicht abschließend geklärt, aus welchen Quellen bzw. über welche Mechanismen die Informationen in die APS übernommen werden. Insbesondere ist offen, ob bestimmte Angaben über e-Befunde bereitgestellt und diese als Quelldokumente herangezogen werden können. Grundsätzlich soll die Herkunft der Daten jeweils in Meta.source abgelegt werden; die konkrete Formatvorgabe für dieses Feld befindet sich noch in Ausarbeitung. Um zukünftige Anwendungsfälle abdecken zu können, besteht zudem die Möglichkeit, zu einem späteren Zeitpunkt zusätzlich Provenance zu verwenden.

#### Use of Persistent Identifiers in IPS
TODO ?

#### Must Support und Obligations

Die APS folgt den Grundsätzen des IPS-Standards in Bezug auf „Must Support“ und Verpflichtungen:
Ein Element, das als Must Support gekennzeichnet ist, muss von Implementierungen unterstützt werden – d.h. Systeme müssen in der Lage sein, das Element zu erfassen, zu speichern, zu übermitteln und anzuzeigen, sofern entsprechende Informationen verfügbar sind.
Wenn Daten für ein Must Support-Element nicht vorliegen, darf das Element weggelassen oder mit einem geeigneten Data Absent Reason-Code versehen werden. 
Pflichtfelder gemäß FHIR-Definition (cardinality 1..1 oder 1..*) müssen immer befüllt werden.

TODO @Gabriel: Derzeit ist die Must Support Kennzechnung in den Profilen der APS visuell nicht sichtbar.

#### Leere Sektionen und fehlende Daten

Wenn eine verpflichtende Sektion der APS leer bleibt, weile keine relevanten Informationen vorliegen oder verfügbar sind, muss „Composition.section.emptyReason“ befüllt werden, sodass der Grund dafür ersichtlich ist (z.B. "nicht verfügbar" oder "nicht abgefragt"). Nicht verpflichtende Sektionen dürfen bei der Erstellung der Patient Summary weggelassen werden.
Auch mittels Ressourcen können fehlende Informationen dokumentiert werden, z.B. mittels SNOMED Codes, dass keine bekannte Allergie vorliegt.
Das Ziel ist, die Vollständigkeit und Nachvollziehbarkeit der Patient Summary sicherzustellen – auch bei fehlenden Informationen.

#### Optionale Datenelemente mit Must Support/Obligations (cardinality of 0..1 or 0..*)

Verfügt ein Ersteller einer Patient Summary über keine Daten, weil sie entweder nicht vorhanden sind, nicht weitergegeben werden dürfen oder für den Anwendungsbereich nicht relevant sind, kann das entsprechende Datenelement weggelassen werden.

#### Verpflichtende Datenelemente mit Must Support/Obligations (cardinality of 1..1 or 1..*)

Nicht codierte Datenelemente und codierte Datenelemente:
Beispiele siehe https://hl7.org/fhir/uv/ips/Empty-Sections-and-Missing-Data.html#required-data-elements-with-must-supportobligations-cardinality-of-11-or-1

### Privacy and Security Considerations
https://hl7.org/fhir/uv/ips/Privacy-and-Security-Considerations.html


#### Bekannte Probleme

TODO: Würde hier alle offenen Punkte reinnehmen, auch wenn sie vielleicht schon mal wo anders erwähnt wurden
- Angaben zur Herkunft von Informationen: Meta.source vs Provenance
- Inkonsistente Darstellung der APS Profile durch imposeProfile (TODO @Gabriel)
- Deutsche Übersetzungen der APS Profile


#### Zukünftige Entwicklungen