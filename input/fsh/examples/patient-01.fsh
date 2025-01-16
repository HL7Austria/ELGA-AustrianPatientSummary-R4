Instance: patient-01
InstanceOf: AtIpsPatient
Description: "Patient - Female Minimal Marie Musterfrau"
Usage: #example
* id = "001"
* identifier[localPatientId].type = $v2-0203#PI "Patient internal identifier"
* identifier[localPatientId].system = "urn:oid:1.2.3.4.5"
* identifier[localPatientId].value = "0001"
* identifier[localPatientId].assigner.display = "Ein GDA in Österreich"
* name.family = "Musterfrau"
* name.given[0] = "Maria"
* gender = #female
* birthDate = "1998-04-17"