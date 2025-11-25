Die Relevanz der Austrian Patient Summary (APS) lässt sich durch zahlreiche aktuelle Projekte und Initiativen beschreiben, die in dem Paper **["Towards the Austrian Patient Summary: Standards and Cross-Border Integration"](https://ebooks.iospress.nl/ISBN/978-1-64368-592-2)** beschrieben werden.

Hervorzuheben sind in diesem Zusammenhang die [FHIR®-Spezifikation der International Patient Summary (IPS)](https://hl7.org/fhir/uv/ips/STU2/) sowie der [MyHealth@EU Requirements Catalogue für die Patient Summary](https://webgate.ec.europa.eu/fpfis/wikis/x/4uHzN) ([EU-Login](https://trusted-digital-identity.europa.eu/index_en) erforderlich), die direkten Einfluss auf die vorliegende Spezifikation der APS hatten. 

<blockquote class="stu-note" markdown="1">
- Die Arbeiten rund um die [European Patient Summary (EPS) von HL7EU](https://build.fhir.org/ig/hl7-eu/eps/) sind noch nicht abgeschlossen und können somit noch nicht berücksichtigt werden.
- Aktuell gibt es noch keine Information darüber, wie die Spezifikation für das European EHR eXchange Format (EEHRxF) im Rahmen vom Europäischen Gesundheitsdatenraum (European Health Data Space, EHDS) aussehen wird.

Sobald entsprechende Informationen vorliegen, wird es zu einer Aktualisierung der APS kommen.
</blockquote>

### Fokus auf IPS

In Österreich hat man sich darauf geeinigt, dass die IPS die Grundlage für die APS bilden soll. Die Gründe dafür sind vielseitig. Zunächst gibt es für die IPS sowohl eine [FHIR®](https://hl7.org/fhir/uv/ips/STU2/)- als auch eine [CDA®](https://art-decor.org/art-decor/decor-project--hl7ips-)-Spezifikation, was eine mögliche Konvertierung zwischen den beiden Formaten entsprechend erleichtert. Dem gegenüber steht die Spezifikation der [Patient Summary im Kontext von MyHealth@EU](https://art-decor.ehdsi.eu/art-decor/decor-templates--epsos-?section=templates&id=1.3.6.1.4.1.12559.11.10.1.3.1.1.3), die auf CDA® basiert und die innerhalb der EU eine größere Bedeutung hat als die IPS.

Mit dem EHDS zeichnet sich allerdings generell FHIR® ab. Das Projekt Xt-EHR befasst sich in Zusammenarbeit mit HL7EU unter anderem mit der Spezifikation der EPS, die ihrerseits auf die IPS aufbaut. Gleichzeitig wird in Xt-EHR auch die Konvergenz zur IPS beschrieben, weshalb langfristig davon auszugehen ist, dass die IPS im Grunde auch im europäischen Kontext eine zentrale Rolle spielen wird. Ebenso soll die Patient Summary im Rahmen von MyHealth@EU bis März 2029 auf FHIR® umgestellt werden.

### Vergleich IPS and MyHealth@EU PS

<table class="tg"><thead>
  <tr>
    <th class="tg-0pky">IPS</th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">MyHealth@EU</th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">APS</th>
    <th class="tg-0lax"></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Patient</td>
    <td class="tg-0pky">required</td>
    <td class="tg-0pky">Patient</td>
    <td class="tg-0pky">required</td>
    <td class="tg-0pky">Patient</td>
    <td class="tg-0lax">required</td>
  </tr>
  <tr>
    <td class="tg-0pky">Author</td>
    <td class="tg-0pky">required</td>
    <td class="tg-0pky">Author</td>
    <td class="tg-0pky">required</td>
    <td class="tg-0pky">Verfasser</td>
    <td class="tg-0lax">required</td>
  </tr>
  <tr>
    <td class="tg-0pky">Attester</td>
    <td class="tg-0pky">optional</td>
    <td class="tg-0pky">Attester</td>
    <td class="tg-0pky">optional</td>
    <td class="tg-0pky">Attester</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax">Custodian</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Custodian</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Custodian</td>
    <td class="tg-0lax">required</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Problems</td>
    <td class="tg-0lax">required</td>
    <td class="tg-0lax">List of current problems/diagnosis</td>
    <td class="tg-0lax">required</td>
    <td class="tg-0lax">Gesundheitsprobleme und Risiken</td>
    <td class="tg-0lax">required</td>
  </tr>
  <tr>
    <td class="tg-0lax">Allergies and Intolerances</td>
    <td class="tg-0lax">required</td>
    <td class="tg-0lax">Allergies and Intolerances</td>
    <td class="tg-0lax">required</td>
    <td class="tg-0lax">Allergien und Intoleranzen</td>
    <td class="tg-0lax">required</td>
  </tr>
  <tr>
    <td class="tg-0lax">Medication Summary</td>
    <td class="tg-0lax">required</td>
    <td class="tg-0lax">Medication Summary</td>
    <td class="tg-0lax">required</td>
    <td class="tg-0lax">Medikationsliste</td>
    <td class="tg-0lax">required</td>
  </tr>
  <tr>
    <td class="tg-0lax">Immunizations</td>
    <td class="tg-0lax">recommended</td>
    <td class="tg-0lax">Vaccinations</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Impfungen</td>
    <td class="tg-0lax">recommended</td>
  </tr>
  <tr>
    <td class="tg-0lax">Results</td>
    <td class="tg-0lax">recommended</td>
    <td class="tg-0lax">Results</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Diagnostische Resultate</td>
    <td class="tg-0lax">recommended</td>
  </tr>
  <tr>
    <td class="tg-0lax">History of Procedures</td>
    <td class="tg-0lax">recommended</td>
    <td class="tg-0lax">Procedures</td>
    <td class="tg-0lax">required</td>
    <td class="tg-0lax">Eingriffe und Therapien</td>
    <td class="tg-0lax">required</td>
  </tr>
  <tr>
    <td class="tg-0lax">Medical Devices</td>
    <td class="tg-0lax">recommended</td>
    <td class="tg-0lax">Medical Devices</td>
    <td class="tg-0lax">required</td>
    <td class="tg-0lax">Implantate, medizinische Geräte und Heilbehelfe</td>
    <td class="tg-0lax">required</td>
  </tr>
  <tr>
    <td class="tg-0lax">Advance Directives</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Advance Directives</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Willenserklärungen und andere juridische Dokumente</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax">Functional Status</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Functional Status</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Beeinträchtigungen</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax">History of Pregnancy</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Pregnancy History</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Schwangerschaftshistorie</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax">Plan of Care</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Plan of Care</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Behandlungsplan</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax">Vital Signs</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Vitalparameter</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax">Alerts</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Medical alert information (other alerts not included in allergies)</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Warnungen</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax">History of Past Problems</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">List of resolved, closed or inactive problems</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Vergangene Gesundheitsprobleme und Risiken</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax">Patient Story</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Patientenbericht</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Medical History</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax">Social History</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Social History</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax">Lebensstil / Soziale Umstände und Verhalten</td>
    <td class="tg-0lax">optional</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Travel History</td>
    <td class="tg-0lax">optional</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
</tbody></table>