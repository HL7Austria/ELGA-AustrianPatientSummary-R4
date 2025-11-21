Die Austrian Patient Summary (APS) enthält neben administrativen Inhalten Strukturen, um verschiedene medizinische Inhalte zu dokumentieren.

{% include APS_Sections.md %}

Die medizinischen Inhalte werden weiters in drei Kategorien gegliedert, die die einzelnen Sektionen der APS enthalten.
- **Required**: Sektionen in dieser Kategorie müssen jedenfalls in der APS enthalten sein. Enthalten diese Sektionen keine Referenz auf eine Ressource in `Composition.section.entry`, `Composition.section.emptyReason` muss befüllt werden.
- **Recommended**: Die Angabe von Sektionen dieser Kategorie ist empfohlen. Sollte keine Information für die jeweilige Sektion vorhanden sein, können diese Sektionen entfallen.
- **Optional**: Sektionen dieser Kategorie können in der APS angegeben werden. Sollte keine Information für die jeweilige Sektion vorhanden sein, können diese Sektionen entfallen.

Im Unterschied zur [International Patient Summary (IPS)](https://hl7.org/fhir/uv/ips/STU2/Structure-of-the-International-Patient-Summary.html) sind in der APS auch die Sektionen "Eingriffe und Therapien (History of Procedures)" und "Implantate, medizinische Geräte und Heilbehelfe (Medical Devices)" in der Kategorie "Required" zu finden, um den Anforderungen von MyHealth@EU gerecht zu werden.