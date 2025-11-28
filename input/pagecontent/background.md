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

<style type="text/css">
  .ps th {
    border: 1px solid !important;
    font-weight: bold;
    text-align: center;
  }
  .ps .required {
    background-color: #D9AFA4;
  }
  .ps .recommended {
    background-color: #FAEBBD;
  }
  .ps .optional {
    background-color: #BBD3B4;
  }
  .ps .border-left {
    border-left: 1px solid !important;
  }
  .ps .border-right {
    border-right: 1px solid !important;
  }
  .ps .border-bottom {
    border-bottom: 1px solid !important;
  }
</style>
<table class="ps">
  <tr>
    <th colspan="2">IPS</th>
    <th colspan="2">MyHealth@EU Requirements Catalogue</th>
    <th colspan="2">APS</th>
    <th rowspan="2">Kommentar</th>
  </tr>
  <tr>
    <th colspan="6">Administrative Inhalte</th>
  </tr>
  <tr>
    <td class="border-left">Patient</td>
    <td class="required">required</td>
    <td class="border-left">Patient</td>
    <td class="required">required</td>
    <td class="border-left">Patient</td>
    <td class="required">required</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Author</td>
    <td class="required">required</td>
    <td class="border-left">Author</td>
    <td class="required">required</td>
    <td class="border-left">Verfasser</td>
    <td class="required">required</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Attester</td>
    <td class="optional">optional</td>
    <td class="border-left">Attester</td>
    <td class="optional">optional</td>
    <td class="border-left">Attester</td>
    <td class="optional">optional</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left border-bottom">Custodian</td>
    <td class="optional border-bottom">optional</td>
    <td class="border-left border-bottom">Custodian</td>
    <td class="required border-bottom">required</td>
    <td class="border-left border-bottom">Custodian</td>
    <td class="required border-bottom">required</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <th colspan="6">Medizinische Inhalte</th>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Problems</td>
    <td class="required">required</td>
    <td class="border-left">List of current problems/diagnosis</td>
    <td class="required">required</td>
    <td class="border-left">Gesundheitsprobleme und Risiken</td>
    <td class="required">required</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Allergies and Intolerances</td>
    <td class="required">required</td>
    <td class="border-left">Allergies and Intolerances</td>
    <td class="required">required</td>
    <td class="border-left">Allergien und Intoleranzen</td>
    <td class="required">required</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Medication Summary</td>
    <td class="required">required</td>
    <td class="border-left">Medication Summary</td>
    <td class="required">required</td>
    <td class="border-left">Medikationsliste</td>
    <td class="required">required</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Immunizations</td>
    <td class="recommended">recommended</td>
    <td class="border-left">Vaccinations</td>
    <td class="optional">optional</td>
    <td class="border-left">Impfungen</td>
    <td class="recommended">recommended</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Results</td>
    <td class="recommended">recommended</td>
    <td class="border-left">Results</td>
    <td class="optional">optional</td>
    <td class="border-left">Diagnostische Resultate</td>
    <td class="recommended">recommended</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">History of Procedures</td>
    <td class="recommended">recommended</td>
    <td class="border-left">Procedures</td>
    <td class="required">required</td>
    <td class="border-left">Eingriffe und Therapien</td>
    <td class="required">required</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Medical Devices</td>
    <td class="recommended">recommended</td>
    <td class="border-left">Medical Devices</td>
    <td class="required">required</td>
    <td class="border-left">Implantate, medizinische Geräte und Heilbehelfe</td>
    <td class="required">required</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Advance Directives</td>
    <td class="optional">optional</td>
    <td class="border-left">Advance Directives</td>
    <td class="optional">optional</td>
    <td class="border-left">Willenserklärungen und andere juridische Dokumente</td>
    <td class="optional">optional</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Functional Status</td>
    <td class="optional">optional</td>
    <td class="border-left">Functional Status</td>
    <td class="optional">optional</td>
    <td class="border-left">Beeinträchtigungen</td>
    <td class="optional">optional</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">History of Pregnancy</td>
    <td class="optional">optional</td>
    <td class="border-left">Pregnancy History</td>
    <td class="optional">optional</td>
    <td class="border-left">Schwangerschaftshistorie</td>
    <td class="optional">optional</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Plan of Care</td>
    <td class="optional">optional</td>
    <td class="border-left">Plan of Care</td>
    <td class="optional">optional</td>
    <td class="border-left">Behandlungsplan</td>
    <td class="optional">optional</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Vital Signs</td>
    <td class="optional">optional</td>
    <td class="border-left"></td>
    <td></td>
    <td class="border-left">Vitalparameter</td>
    <td class="optional">optional</td>
    <td class="border-left border-right">Die Vitalparameter werden in einer eigenen Sektion geführt.<br>In einer zukünftigen Version der APS könnten diese in der Sektion<br>"Diagnostische Resultate" aufgenommen werden.</td>
  </tr>
  <tr>
    <td class="border-left">Alerts</td>
    <td class="optional">optional</td>
    <td class="border-left">Medical alert information (other alerts not included in allergies)</td>
    <td class="optional">optional</td>
    <td class="border-left">Warnungen</td>
    <td class="optional">optional</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">History of Past Problems</td>
    <td class="optional">optional</td>
    <td class="border-left">List of resolved, closed or inactive problems</td>
    <td class="optional">optional</td>
    <td class="border-left">Vergangene Gesundheitsprobleme und Risiken</td>
    <td class="optional">optional</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left">Patient Story</td>
    <td class="optional">optional</td>
    <td class="border-left"></td>
    <td></td>
    <td class="border-left">Patientenbericht</td>
    <td class="optional">optional</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left"></td>
    <td></td>
    <td class="border-left">Medical History</td>
    <td class="optional">optional</td>
    <td class="border-left"></td>
    <td></td>
    <td class="border-left border-right">Aktuell keine Entsprechung in der APS.</td>
  </tr>
  <tr>
    <td class="border-left">Social History</td>
    <td class="optional">optional</td>
    <td class="border-left">Social History</td>
    <td class="optional">optional</td>
    <td class="border-left">Lebensstil / Soziale Umstände und Verhalten</td>
    <td class="optional">optional</td>
    <td class="border-left border-right"></td>
  </tr>
  <tr>
    <td class="border-left border-bottom"></td>
    <td class="border-bottom"></td>
    <td class="border-left border-bottom">Travel History</td>
    <td class="optional border-bottom">optional</td>
    <td class="border-left border-bottom"></td>
    <td class="border-bottom"></td>
    <td class="border-left border-right border-bottom">Aktuell keine Entsprechung in der APS.</td>
  </tr>
</table>