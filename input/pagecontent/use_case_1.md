| **Element** | **Beschreibung** |
|---|---|
| **Akteur** | Zentrale Anwendung Patient Summary |
| **Beschreibung** | Die Inhalte der APS werden automatisch aus den angebundenen Registern (e-Medikation, e-Impfpass, etc.) zusammengeführt und basieren somit auf den aktuellsten verfügbaren Gesundheitsdaten des Patienten. Die APS dient darüber hinaus der Generierung fachspezifischer Dokumente (z. B. für bestimmte Krankheitsbilder wie Diabetes) nach definierten Kriterien und stellt diese für den Abruf bereit. Auf der APS basierende Dokumentenklassen werden in eigenen Implementierungsleitfäden spezifiziert. <br><br>**Hinweis:** Die genaue Beschreibung des Aggregationsprozesses folgt in einer späteren Version der APS-Spezifikation (siehe dazu auch Kapitel *Datenherkunft*) |
| **Auslöser** | Beim Abruf der APS wird automatisch ein Prozess gestartet, der die angebundenen Register auf neue oder geänderte Daten überprüft und die Inhalte in die Patient Summary übernimmt. |
| **Vorbedingungen** | Ein berechtigter Akteur hat lesend auf die APS (UC2) zugegriffen. In den angebundenen Registern liegen Gesundheitsdaten für den betreffenden Patienten vor. |
| **Ergebnis** | Die *Austrian Patient Summary* wurde mit den aktuellsten Gesundheitsinformationen aus den angebundenen Registern aggregiert. |

