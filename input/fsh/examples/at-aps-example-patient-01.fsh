Instance: AtApsExamplePatient01
InstanceOf: AtApsPatient
Title: "AtApsPatient-Beispiel"
Description: "Mimimalbeispiel einer Patientin"
Usage: #example
* id = "at-aps-example-patient-01"
* identifier[socialSecurityNumber].type = $cs-v2-0203#SS "Social Security number"
* identifier[socialSecurityNumber].system = "urn:oid:1.2.40.0.10.1.4.3.1"
* identifier[socialSecurityNumber].value = "0000121150"
* identifier[socialSecurityNumber].assigner.display = "Dachverband der österreichischen Sozialversicherungsträger"
* identifier[localPatientId].type = $cs-v2-0203#PI "Patient internal identifier"
* identifier[localPatientId].system = "urn:oid:1.2.3.4.5"
* identifier[localPatientId].value = "0001"
* identifier[localPatientId].assigner.display = "Ein GDA in Österreich"
* name.family = "Musterfrau"
* name.given[0] = "Maria"
* gender = #female
* birthDate = "1998-04-17"
* address.line = "Am Schulweg 5"
* address.use = #home
* address.city = "Hainfeld"
* address.postalCode = "3100"
* address.country = "AUT"