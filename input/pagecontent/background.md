### Umfeld

Die Relevanz der Austrian Patient Summary (APS) lässt sich durch die zahlreichen Projekte und Initiativen in ihrem Umfeld erklären. Die folgende Grafik stellt die wichtigsten Einflussgrößen auf der APS dar, wobei jene, die von der AG Integrierte Versorgung mit Austrian Patient Summary bei der Erstellung dieses Leitfadens berücksichtigt worden sind, farblich hervorgehoben wurden.

<div>{% include aps-environment.svg %}</div>
<br clear="all"/>

Beginnend mit HL7® und dem existierenden Standard zur International Patient Summary (IPS) bildet diese die wichtigste Grundlage für die APS. Zuletzt wurde im Rahmen von HL7EU auch an einer europäischen Version der Patient Summary gearbeitet, der European Patient Summary (EPS). Ziel der EPS ist, nationale (europäische) Initiativen zu harmonisieren und als Grundlage für das European EHR eXchange Format (EEHRxF) zu dienen.

Auf Ebene der EU gibt es im Rahmen vom grenzüberschreitenden Datenaustausch (MyHealth@EU) eine Spezifikation auf Basis von HL7® CDA®, die von einigen EU-Ländern produktiv eingesetzt wird. Die Grundlage für diese Spezifikation bilden zunächst die Guideline on Patient Summary vom eHealth Network sowie der davon abgeleitete Anforderungskatalog für MyHealth@EU.

Zusätzlich ist mit 26. März 2025 die Verordnung zum Europäischen Gesundheitsdatenraum (European Health Data Space, EHDS) in Kraft getreten. Ein zentrales Element dieser Verordnung ist die Definition der Prioritären Kategorien personenbezogener elektronischer Gesundheitsdaten für die Primärnutzung. Darunter fällt unter anderem die sogenannte Patientenkurzakte (= Patient Summary). Im Rahmen des mit der Verordnung verknüpften Projekts Extended Electronic Health Record (Xt-EHR) soll neben anderen Aufgaben auch die EU-weite Spezifikation für das EEHRxF erarbeitet werden, wobei hier eng mit HL7EU zusammengearbeitet wird.

In Österreich haben vor allem nationale Projekte (z.B. zur Umsetzung des EHDS oder zur Integrierten Versorgung) sowie die bestehenden CDA® oder FHIR® Implementierungsleitfäden Einfluss auf die Spezifikation der APS.

#### Fokus auf IPS

In Österreich hat man sich darauf geeinigt, dass die IPS die Grundlage für die APS bilden soll. Die Gründe dafür sind vielseitig. Zunächst gibt es für die IPS sowohl eine [FHIR®](https://build.fhir.org/ig/HL7/fhir-ips/index.html)- als auch eine [CDA®](https://art-decor.org/art-decor/decor-project--hl7ips-)-Spezifikation, was eine mögliche Konvertierung zwischen den beiden Formaten entsprechend erleichtert. Dem gegenüber steht die Spezifikation der [Patient Summary im Kontext von MyHealth@EU](https://art-decor.ehdsi.eu/art-decor/decor-templates--epsos-?section=templates&id=1.3.6.1.4.1.12559.11.10.1.3.1.1.3), die auf CDA® basiert und die innerhalb der EU eine größere Bedeutung hat als die IPS. Wann im Rahmen von MyHealth@EU auf FHIR® umgestellt wird, ist zurzeit noch nicht absehbar. Trotzdem zeichnet sich mit dem EHDS FHIR® ab. Das Projekt Xt-EHR befasst sich in Zusammenarbeit mit HL7EU unter anderem mit der Spezifikation der EPS, die ihrerseits auf die IPS aufbaut. Gleichzeitig wird in Xt-EHR auch die Konvergenz zur IPS beschrieben, weshalb langfristig davon auszugehen ist, dass die IPS im Grunde auch im europäischen Kontext eine zentrale Rolle spielen wird.

### Designentscheidung

#### IPS vor EPS

Die APS baut auf dem [HL7® Austria FHIR® Core Implementation Guide (HL7AT Core IG), Version 2.0.0](https://fhir.hl7.at/HL7-AT-FHIR-Core-R5/2.0.0/) und dem HL7® Leitfaden für die [International Patient Summary (IPS), Version 2.0.0-ballot](https://hl7.org/fhir/uv/ips/2024Sep/) auf. Nachdem es in FHIR® allerdings nicht möglich ist, mehr als eine Basisdefinition für eine StructureDefinition-Ressource anzugeben, wird nach Möglichkeit immer das entsprechende Profil aus dem HL7AT Core IG als Basisdefinition angegeben und das entsprechende Profil aus der IPS mit Hilfe der [`imposeProfile`-Extension](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) eingebunden. Damit kann eine Instanz der APS gegen beide Spezifikationen validiert werden.

<div class="dragon" markdown="1">
Beim Lesen der APS-Profile müssen insofern auch immer die IPS-Profile berücksichtigt werden. So ist das `subject` in der [AT APS Composition](StructureDefinition-at-aps-composition.html) mit `0..1` modelliert. In der [Composition (IPS)](https://hl7.org/fhir/uv/ips/2024Sep/StructureDefinition-Composition-uv-ips.html) ist das `subject` allerdings mit `1..1` modelliert. Die strengere Regel wird bei der Validierung einer Instanz schlagend.
</div>

#### FHIR® R4

Aktuell gibt es die IPS nur auf Basis von FHIR® R4. Ob und wann die IPS auch in R5 bzw. R6 zur Verfügung steht, ist noch nicht klar. Deshalb wird die APS zurzeit auch nur in FHIR® R4 spezifiziert.