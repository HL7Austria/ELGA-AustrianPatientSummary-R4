Instance: procedure-01
InstanceOf: AtApsProcedure
Title: "Procedure - Surgical Placement of Coronary Stent"
Description: "Procedure - Surgical Placement of Coronary Stent"
Usage: #example
* id = "001"
* status = #completed
* category = $sct#387713003 "Surgical procedure"
* code.coding[0] = $sct#36969009 "Placement of stent in coronary artery"
* code.coding[+] = $sct#233258006 "Balloon angioplasty of artery"
* code.text = "Previous balloon angioplasty on mid-LAD stenosis with STENT Implantation"
* subject = Reference(Patient/002) "Maria Musterfrau"
* performedPeriod.extension.url = "http://hl7.org/fhir/StructureDefinition/data-absent-reason"
* performedPeriod.extension.valueCode = #unknown