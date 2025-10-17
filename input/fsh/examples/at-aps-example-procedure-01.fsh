Instance: AtApsExampleProcedure01
InstanceOf: AtApsProcedure
Title: "AtApsProcedure-Beispiel"
Description: "Chirurgische Platzierung eines Koronarstents"
Usage: #example
* id = "at-aps-example-procedure-01"
* status = #completed
* category = $cs-sct#387713003 "Chirurgische Prozedur"
* code.coding[0] = $cs-sct#36969009 "Einsetzen eines Stents in Koronararterie"
* code.coding[+] = $cs-sct#233258006 "Durchleuchtungsgeführte Angioplastie einer Arterie mit Kontrastmittel"
* code.text = "Vorherige Ballonangioplastie bei mittlerer LAD-Stenose mit STENT-Implantation"
* subject = Reference(Patient/HL7ATCorePatientExample01) "Maria Mustermann"
* performedPeriod.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* performedPeriod.extension.valueCode = #unknown