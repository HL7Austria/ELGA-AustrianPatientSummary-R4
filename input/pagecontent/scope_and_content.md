Die Austrian Patient Summary (APS) besteht aus folgenden Sektionen:
<br><br>
{% include APS_Sections.md %}
<br>

**Begriffsdefintion**<br>
**Required**: Ein als Required gekennzeichnetes Element ist ein Pflichtfeld und muss vorhanden sein. In FHIR wird diese Verpflichtung durch die Kardinalität festgelegt, typischerweise 1..1 oder 1..\*.<br>
**Recommended**: Elemente mit diesem Status sind dringend empfohlen, aber nicht verpflichtend. Sie sollen befüllt werden, sofern Informationen verfügbar sind. In FHIR-Profilen wird dies typischerweise durch Must Support oder erläuternde Kommentare kenntlich gemacht. Systeme müssen das Element verarbeiten können, sind jedoch nicht verpflichtet, es stets bereitzustellen.<br>
**Optional**: Ein als Optional gekennzeichnetes Element kann verwendet werden, ist jedoch nicht verpflichtend. In FHIR wird dies meist durch die Kardinalität 0..1 oder 0..\* abgebildet.<br>

Im Folgenden werden die Inhalte der einzelnen Sektionen zusammenfassend beschrieben. Sofern im Vergleich zur internationalen Spezifikation österreichspezifische Anpassungen (Profile) vorgenommen wurden, werden diese angeführt und begründet.