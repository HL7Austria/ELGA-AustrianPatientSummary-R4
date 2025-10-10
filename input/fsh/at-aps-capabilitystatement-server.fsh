Instance: at-aps-capabilitystatement-server
InstanceOf: CapabilityStatement
Title: "AT APS CapabilityStatement (Server)"
Usage: #definition
* url = "https://fhir.hl7.at/elga/aps/r4/CapabilityStatement/at-aps-capabilitystatement-server"
* name = "AtApsCapabilityStatementServer"
* status = #active
* experimental = false
* date = "2025-04-28T13:30:00+01:00"
* publisher = "ELGA GmbH"
* contact.telecom.system = #url
* contact.telecom.value = "https://elga.gv.at"
* description = "Dieser Abschnitt beschreibt die erwarteten Fähigkeiten eines FHIR®-Servers, der die Austrian Patient Summary (APS) unterstützt. Die Liste gibt relevante FHIR®-Profile und -Operationen für diesen Zweck wieder."
* kind = #requirements
* fhirVersion = #4.0.1
* format[0] = #application/fhir+xml
* format[+] = #xml
* format[+] = #application/fhir+json
* format[+] = #json
* rest.mode = #server

* rest.resource[0].type = #Bundle
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #SHALL
* rest.resource[=].profile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-bundle"

* rest.resource[+].type = #Composition
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #SHALL
* rest.resource[=].profile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-composition"

* rest.resource[+].type = #Patient
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #SHALL
* rest.resource[=].profile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-patient"
* rest.resource[=].operation.extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].operation.extension.valueCode = #SHOULD
* rest.resource[=].operation.name = "summary"
* rest.resource[=].operation.definition = "http://hl7.org/fhir/uv/ips/OperationDefinition/summary"
* rest.resource[=].operation.documentation = "Operation zum Abrufen einer APS"

* rest.resource[+].type = #AllergyIntolerance
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #SHOULD
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-allergyintolerance"

* rest.resource[+].type = #Condition
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #SHOULD
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-condition"

* rest.resource[+].type = #MedicationRequest
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #SHOULD
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-medicationrequest"
* rest.resource[=].documentation = "Some systems may only support AT APS MedicationRequest or AT APS MedicationStatement."

* rest.resource[+].type = #MedicationStatement
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #SHOULD
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-medicationstatement"
* rest.resource[=].documentation = "Some systems may only support AT APS MedicationRequest or AT APS MedicationStatement."

* rest.resource[+].type = #CarePlan
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY

* rest.resource[+].type = #ClinicalImpression
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY

* rest.resource[+].type = #Consent
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY

* rest.resource[+].type = #Device
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-device"

* rest.resource[+].type = #DeviceUseStatement
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-deviceusestatement"

* rest.resource[+].type = #DiagnosticReport
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-diagnosticreport"

* rest.resource[=].type = #DocumentReference
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].operation.extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].operation.extension.valueCode = #MAY
* rest.resource[=].operation.name = "docref"
* rest.resource[=].operation.definition = "http://hl7.org/fhir/uv/ipa/OperationDefinition/docref"

// no changes made by the APS
* rest.resource[+].type = #Flag
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "http://hl7.org/fhir/uv/ips/StructureDefinition/Flag-alert-uv-ips"

* rest.resource[+].type = #ImagingStudy
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-imagingstudy"

* rest.resource[+].type = #Immunization
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-immunization"

* rest.resource[+].type = #Medication
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-medication"

* rest.resource[+].type = #MedicationAdministration
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY

* rest.resource[+].type = #MedicationDispense
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY

* rest.resource[+].type = #Observation
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile[0] = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-observationpregnancyedd"
* rest.resource[=].supportedProfile[+] = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-observationpregnancyoutcome"
* rest.resource[=].supportedProfile[+] = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-observationpregnancystatus"
* rest.resource[=].supportedProfile[+] = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-observationalcoholuse"
* rest.resource[=].supportedProfile[+] = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-observationtobaccouse"
* rest.resource[=].supportedProfile[+] = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-observationresultslaboratorypathology"
* rest.resource[=].supportedProfile[+] = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-observationresultsradiology"
* rest.resource[=].supportedProfile[+] = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-observationvitalsigns"

* rest.resource[+].type = #Organization
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-organization"

* rest.resource[+].type = #Practitioner
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-practitioner"

* rest.resource[+].type = #PractitionerRole
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-practitionerrole"

* rest.resource[+].type = #Procedure
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-procedure"

* rest.resource[+].type = #RelatedPerson
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY

* rest.resource[+].type = #Specimen
* rest.resource[=].extension.url = "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation"
* rest.resource[=].extension.valueCode = #MAY
* rest.resource[=].supportedProfile = "https://fhir.hl7.at/elga/aps/r4/StructureDefinition/at-aps-specimen"
