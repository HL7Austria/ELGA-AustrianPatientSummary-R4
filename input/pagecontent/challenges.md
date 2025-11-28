
### Lesen des IGs mit imposeProfile

- multiple Vererbung

<div class="dragon" markdown="1">
Beim Lesen der APS-Profile müssen insofern auch immer die IPS-Profile berücksichtigt werden. So ist das `subject` in der [AT APS Composition](StructureDefinition-at-aps-composition.html) mit `0..1` modelliert. In der [Composition (IPS)](https://hl7.org/fhir/uv/ips/STU2/StructureDefinition-Composition-uv-ips.html) ist das `subject` allerdings mit `1..1` modelliert. Die strengere Regel wird bei der Validierung einer Instanz schlagend.
</div>

- Aufwärtskompatibilität CarePlan -> Extensions
- Deutsche Übersetzung der APS-Profile