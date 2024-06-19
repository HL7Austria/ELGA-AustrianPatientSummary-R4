<style>
.stu-note::before {
  white-space: pre;
  content: "AUFGABE\A ";
  background-color: unset;
  color: unset;
  font-weight: bold;
}

.stu-note {
  margin: 5px;
  padding: 10px;
  background-color: #CBE9FD;
  border-left-color: #7F929E;
}
</style>

![hl7at](contest.png){: style="width: 10%"}

Liebe Schüler:innen und Student:innen,

Die [HL7® Austria](https://hl7.at/) lädt mit Unterstützung der [ELGA GmbH](https://www.elga.gv.at/) herzlich dazu ein, am Visualization Contest für das [International Patient Summary (IPS)](https://hl7.org/fhir/uv/ips/) teilzunehmen und euer kreatives Potenzial zu entfalten! Das IPS wird zu einem wichtigen Element der europäischen Gesundheitskommunikation und trägt dazu bei, wesentliche Patientendaten einheitlich und verständlich zu übermitteln.

Das IPS basiert auf dem [HL7® FHIR®](https://hl7.org/fhir/R4/index.html) (Fast Healthcare Interoperability Resources) Standard und nutzt strukturierte Datenformate wie JSON zur Speicherung und Übertragung. Es umfasst wichtige Informationen zu einer Person, wie demografische Daten, medizinische Diagnosen, Medikationspläne, Allergien und vieles mehr, um ein umfassendes Bild zu vermitteln.

Im Rahmen dieses Wettbewerbs stellen wir euch zwei beispielhafte IPS-Datensätze zur Verfügung, die im Zuge des Contests visualisiert werden sollen. Diese Datensätze bieten euch die Möglichkeit, eure Designideen an realistischen Patient:inneninformationen zu testen und umzusetzen.

<div markdown="1" class="stu-note" >
Eure Aufgabe besteht darin, innovative Design-Prototypen für die Visualisierung des IPS zu entwickeln - allein oder als Team! Ihr könnt dabei interaktive Lösungen gestalten, die die Nutzer einbeziehen. Alternativ könnt ihr auch statische Visualisierungen entwerfen, die beispielsweise für den Ausdruck geeignet sind und dennoch die Informationen klar und übersichtlich darstellen. Wichtig ist uns, dass die Informationen übersichtlich dargestellt werden und bei bedarf auch nach Daten gefiltert oder gesucht werden kann. Ebenso solle jede Art von Darstellung unterstützt werden (z.B. Stichwort "responsive"). Sollte eine technische Umsetzung nicht möglich sein, sind wir jedenfalls auch an Mock-ups interessiert. In jedem Fall solltet ihr euer Werk gut dokumentieren, z.B. in einem GitHub/GitLab-Repository, wo ihr auch gleich die Source-Files bereitstellen könnt.

Beispiele des österreichischen Patient Summary (bereitgestellt durch die ELGA GmbH):

- [APS-1-no-problems-medication-allergies](Bundle-APS-1-no-problems-medication-allergies.html) - Minimalbeispiel eines Patienten ohne gesundheitliche Probleme, aktuelle Medikation oder Allergien.
- [APS-2-preventive-medical-checkup](Bundle-APS-2-preventive-medical-checkup.html) - Umfangreiches Beispiel eines Patienten mit zahlreichen Beschwerden, Allergien, früheren Behandlungen, etc. Darüber hinaus wurden mehrere Medikamente verschrieben und Laborwerte erhoben.
</div>

Der Contest erstreckt sich über den Sommer und endet am **31. Oktober 2024**. Eure eingereichten Prototypen werden von einer Fachjury bewertet, die Kreativität, Benutzerfreundlichkeit, Umsetzbarkeit, Ästhetik und die Fähigkeit zur effektiven Kommunikation von Gesundheitsinformationen berücksichtigt.

Die Gewinner:innen werden nicht nur mit einem Preisgeld belohnt, sondern haben auch die Möglichkeit, ihre Entwürfe einer breiten Öffentlichkeit zu präsentieren und einen Beitrag zur Weiterentwicklung der Gesundheitskommunikation zu leisten. Die Gewinner:innen des Wettbewerbs werden mit einem Preisgeld von € 1000,- prämiert und dürfen ihren Design-Prototypen im Rahmen der HL7 Jahrestagung 2025 präsentieren.

Nutzt diese Chance, eure Fähigkeiten im Design und euer Interesse am Gesundheitswesen zu kombinieren und gemeinsam die Zukunft der Patient Summary zu gestalten!

Wir freuen uns auf eure kreativen Ideen und Einsendungen!

Mit freundlichen Grüßen,

HL7® Austria mit Unterstützung der ELGA GmbH

[![hl7at](hl7atlogo.png){: style="width: 10%"}](https://hl7.at/) [![elga](logo.jpg){: style="width: 10%"}](https://www.elga.gv.at/)

### Existierende Visualisierungswerkzeuge

Für das IPS gibt es bereits verschiedene Visualisierungswerkzeuge, die aber allesamt noch nicht optimal sind:

- [https://www.maxmddirect.com/direct/FHIR/ResponseViewer](https://www.maxmddirect.com/direct/FHIR/ResponseViewer)
- [https://ps-ca-renderer.apibox.ca/index.html](https://ps-ca-renderer.apibox.ca/index.html)
- [https://www.ipsviewer.com/](https://www.ipsviewer.com/)
- [https://sandbox.hl7europe.eu/laboratory/web/apps/visualiser/index.html?url=https://sandbox.hl7europe.eu/laboratory/fhir/Bundle/at-f91828ea057b](https://sandbox.hl7europe.eu/laboratory/web/apps/visualiser/index.html?url=https://sandbox.hl7europe.eu/laboratory/fhir/Bundle/at-f91828ea057b) basierend auf [https://github.com/hl7-eu/viz-lab](https://github.com/hl7-eu/viz-lab)
- [https://idmp-viewer.azurewebsites.net/display-product?url=https://sandbox.hl7europe.eu/laboratory/fhir/Bundle/at-f91828ea057b](https://idmp-viewer.azurewebsites.net/display-product?url=https://sandbox.hl7europe.eu/laboratory/fhir/Bundle/at-f91828ea057b) basierend auf [http://www.nprogram.co.uk/](http://www.nprogram.co.uk/)

### Teilnahmebedingungen

- Diese Teilnahmebedingungen gelten für den Wettbewerb "IPS Visualization Contest", organisiert von HL7® Austria mit Unterstützung der ELGA GmbH.
- Der einzureichende Design-Prototyp muss sich mit der Visualisierung des IPS auseinandersetzen.
- Einreichen können einzelne oder Gruppen von Schüler:innen und/oder Student:innen, die aktiv sind oder deren Schul- oder Studienabschluss an einer österreichischen Schule oder Universität nicht länger als ein Jahr zurückliegt.
- Eine Mitgliedschaft bei HL7® Austria wird nicht vorausgesetzt.
- Eine Bewerbung erfolgt auf Deutsch oder Englisch und umfasst folgende Unterlagen:
  - Vorstellung des Design-Prototypen - diese sollte folgendes enthalten:
    - Beschreibung des Design-Prototypen
    - Designvorschläge/Screenshots
    - ggf. Link auf ein GitLab/GitHub-Repository
    - ggf. Link auf einen funktionierenden Prototypen
  - Kurzpräsentation des Design-Prototypen auf 3 Folien (als PDF)
  - Lebenslauf mit stichwortartiger Beschreibung des bisherigen (schulischen oder wissenschaftlichen) Werdegangs der einzelnen Schüler:innen und/oder Student:innen (als PDF)
- Einsendung an [office@hl7.at](mailto:office@hl7.at). Sie erhalten dann eine Rückmeldung, ob Ihre Unterlagen akzeptiert wurden. Nur vollständige Bewerbungen werden akzeptiert.
- Einsendeschluss: 31. Oktober 2024
- Die Gewinner:innen werden bis 31. Dezember 2024 bekannt gegeben.
- Die Gewinner:innen präsentieren ihren Design-Prototyp in einem Kurzvortrag (5 Minuten) anhand der eingereichten Kurzpräsentation im Rahmen der HL7® Jahrestagung 2025. Für sie ist daher die Teilnahme an dieser Veranstaltung kostenlos.
- Etwaige durch die Einreichung anfallende Kosten (wie z.B. Arbeitszeit, Reisekosten, etc.) werden nicht erstattet.
- Die Auswahl des besten Design-Prototypen erfolgt durch eine Jury, die als wissenschaftliches Komitee von der HL7® Austria bestellt wird.
- Das Einlegen von Rechtsmitteln gegen die vom Ausschuss getroffene Auswahl ist ausgeschlossen.
- Mit der Einreichung erklären sich die Teilnehmer ausdrücklich damit einverstanden, dass alle Nutzungs-, Veröffentlichungs- und Weiterentwicklungsrechte an dem eingereichten Design-Prototypen nicht-exklusiv auf die ELGA GmbH übertragen werden. Diese Rechte-Übertragung an die ELGA GmbH erfolgt unwiderruflich und unentgeltlich. Nicht-exklusiv bedeutet in diesem Zusammenhang, dass die Teilnehmer ihre Design-Prototypen unabhängig von der ELGA GmbH auch selbst uneingeschränkt weiterverwenden und verwerten dürfen.
- Für alle Streitigkeiten aus oder im Zusammenhang mit der gegenständlichen Auslobung sowie im Zusammenhang mit Nutzungsrechten an der im Wettbewerb eingereichten Software ist ausnahmslos österreichisches Recht, jedoch unter Ausschluss aller Weiterverweisungen auf ausländisches Recht anzuwenden.
- Für Streitigkeiten aus dieser Auslobung inkl. Nutzungsrechten ist das sachlich zuständige Gericht am Sitz der Ausloberin (HL7 Austria) zuständig.

