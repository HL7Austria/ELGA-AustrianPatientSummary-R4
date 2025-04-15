### Impressum und Haftungsausschluss

*Medieneigentümer, Herausgeber, Hersteller, Verleger:*<br/>
ELGA GmbH, Treustraße 35-43, Wien, Österreich. Telefon: +43.1.2127050<br/>
Internet: [www.elga.gv.at](https://www.elga.gv.at), Email: [standards@elga.gv.at](mailto:standards@elga.gv.at)<br/>
Geschäftsführer: Mag. Dr. Stefan Sabutsch, Dr. Edith Bulant-Wodak, MBA

*Redaktion, Projektleitung, Koordination:*<br/>
Dr. Emmanuel Helm, [emmanuel.helm@elga.gv.at](mailto:emmanuel.helm@elga.gv.at)

*Abbildungen:* © ELGA GmbH

*Nutzung:* Das Dokument enthält geistiges Eigentum der Health Level Seven® Int. und HL7® Austria, Erdbergweg 7/8, 8052 Graz; [www.hl7.at](https://www.hl7.at).

*Download* unter [fhir.hl7.at](https://fhir.hl7.at)

Die Nutzung ist ohne Lizenz- und Nutzungsgebühren zum Zweck der Erstellung medizinischer Dokumente ausdrücklich erlaubt. Andere Arten der Nutzung und auch auszugsweise Wiedergabe bedürfen der Genehmigung des Medieneigentümers. 

*Haftungsausschluss:* Die Arbeiten für den vorliegenden Leitfaden wurden von den Autoren gemäß dem Stand der Technik und mit größtmöglicher Sorgfalt erbracht und über ein öffentliches Kommentierungsverfahren kontrolliert. Die Nutzung des vorliegenden Leitfadens erfolgt in ausschließlicher Verantwortung der Anwender. Aus der Verwendung des vorliegenden Leitfadens können keinerlei Rechtsansprüche gegen die Autoren, Herausgeber oder Mitwirkenden erhoben und/oder abgeleitet werden. Ein allfälliger Widerspruch zum geltenden Recht ist jedenfalls nicht beabsichtigt und von den Erstellern des Dokumentes nicht gewünscht. 

### Hinweis zur Sprachverwendung

Aus Gründen der Lesbarkeit wird im Text das generische Maskulinum verwendet. Es bezieht sich gleichermaßen auf alle Geschlechter. Der Begriff "Patient" schließt auch Bürgerinnen und Bürger, Kundinnen und Kunden sowie Klientinnen und Klienten ein – unabhängig davon, ob sie aktuell an einem Behandlungs- oder Pflegeprozess teilnehmen.

## Gesetzliche Grundlagen

### Lizenzinformationen

Die von HL7 Austria erarbeiteten Standards und die Bearbeitungen der Standards von HL7 International stellen Werke im Sinne des österreichischen Urheberrechtsgesetzes dar und unterliegen daher urheberrechtlichem Schutz.

HL7 Austria genehmigt die Verwendung dieser Standards für die Zwecke der Erstellung, des Verkaufs und des Betriebs von Computerprogrammen, sofern nicht anders angegeben oder sich die Standards auf andere urheberrechtlich oder lizenzrechtlich geschützte Werke beziehen.

Die vollständige oder teilweise Veröffentlichung der Standards (zum Beispiel in Spezifikationen, Publikationen oder Schulungsunterlagen) ist nur mit einer ausdrücklichen Genehmigung der HL7 Austria gestattet. Mitglieder von HL7 Austria sind berechtigt, die Standards vollständig oder in Auszügen ausschließlich organisationsintern zu publizieren, zu vervielfältigen oder zu verteilen. Die Veröffentlichung eigener Anpassungen der HL7-Spezifikationen (im Sinne von Lokalisierungen) oder eigener Leitfäden erfordert eine formale Vereinbarung mit der HL7 Austria.

HL7® und FHIR® sind die eingetragenen Marken von Health Level Seven International. Die vollständigen Lizenzinformationen finden sich unter [https://hl7.at/nutzungsbedingungen-und-lizenzinformationen/](https://hl7.at/nutzungsbedingungen-und-lizenzinformationen/). Die Lizenzbedingungen von HL7 International finden sich unter [http://www.HL7.org/legal/ippolicy.cfm](http://www.HL7.org/legal/ippolicy.cfm).

### Verbindlichkeit

Die Verbindlichkeit und die Umsetzungsfrist dieses Leitfadens sind im Gesundheitstelematikgesetz 2012, BGBl.I Nr.111/2012 sowie in den darauf fußenden ELGA-Verordnungen geregelt.

Der Leitfaden in seiner jeweils aktuell gültigen Fassung sowie die aktualisierten Terminologien sind vom zuständigen Minister auf [www.gesundheit.gv.at](https://www.gesundheit.gv.at) zu veröffentlichen. Der Zeitplan zur Bereitstellung der Datenaustauschformate wird durch das Gesundheitstelematikgesetz 2012 und darauf basierenden Durchführungsverordnungen durch den zuständigen Bundesminister vorgegeben. Hauptversionen, also Aktualisierungen des Implementierungsleitfadens, welche zusätzliche verpflichtende Konformitätskriterien enthalten ("Mandatory" [M], "Required" [R] und "Fixed" [F]), sind mit ihren Fristen zur Bereitstellung per Verordnung kundzumachen. Andere Aktualisierungen (Nebenversionen) dürfen auch ohne Änderung dieser Verordnung unter www.gesundheit.gv.at veröffentlicht werden.

Die Anwendung dieses Implementierungsleitfadens hat im Einklang mit österreichischem und europäischem Recht, insbesondere mit den relevanten Materiengesetzen (z.B. Ärztegesetz 1998, Apothekenbetriebsordnung 2005, Krankenanstalten- und Kuranstaltengesetz, Gesundheits- und Krankenpflegegesetz, Rezeptpflichtgesetz, Datenschutzgesetz, Gesundheitstelematikgesetz 2012, DSGVO) zu erfolgen. Technische Möglichkeiten können gesetzliche Bestimmungen selbstverständlich nicht verändern, vielmehr sind die technischen Möglichkeiten im Einklang mit den Gesetzen zu nutzen.

Die Einhaltung der gesetzlichen Bestimmungen liegt im Verantwortungsbereich der Ersteller der CDA-Dokumente.

## Autoren und Mitwirkende

Das Redaktionsteam bestand aus folgenden Personen[^1]: 
<table class="wikitable">
<tbody><tr>
<th> Name
</th>
<th> Organisation
</th>
<th> Rolle
</th></tr>
<tr>
<td> Sonja Gradwohl
</td>
<td> ELGA GmbH
</td>
<td> Autorin
</td></tr>
<tr>
<td> Emmanuel Helm
</td>
<td> ELGA GmbH
</td>
<td> Projektleiter, Fachkoordinator
</td></tr>
<tr>
<td> Gabriel Kleinoscheg
</td>
<td> ELGA GmbH, HL7 Austria
</td>
<td> Autor
</td></tr>
<tr>
<td> Andrea Klostermann
</td>
<td> ELGA GmbH
</td>
<td> Autorin
</td></tr>
<tr>
<td> Nikolaus Krondraf 
</td>
<td> ELGA GmbH
</td>
<td> Autor
</td></tr>
</tbody></table>


Teilnehmer der Arbeitsgruppe Austrian Patient Summary[^1]: *TODO*

[^1]: Personen sind in alphabetischer Reihenfolge ohne Titel angegeben.