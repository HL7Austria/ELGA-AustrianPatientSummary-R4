Instance: AtApsExampleOrganization01
InstanceOf: AtApsOrganization
Title: "AtApsExampleOrganization01-Beispiel"
Description: "Organization"
Usage: #example
* identifier[0].system = "urn:ietf:rfc:3986"
* identifier[=].value = "urn:oid:1.2.40.0.34.99.4613.3"
* identifier[=].assigner.display = "Bundesministerium für Gesundheit"
* identifier[+].system = "urn:oid:1.2.40.0.34.4.10"
* identifier[=].value = "K101+"
* identifier[=].assigner.display = "Österreichisches Bundesministerium für Gesundheit"
* identifier[+].system = "urn:oid:1.2.40.0.10.1.4.3.2"
* identifier[=].value = "123456789"
* identifier[=].assigner.display = "Dachverband der österreichischen Sozialversicherungsträger"
* type = $cs-elga-gtelvogdarollen#300 "Allgemeine Krankenanstalt"
* name = "Amadeus Spital"
* address.use = #work
* address.type = #both
* address.line = "Mozartgasse 1-7 Haupteingang"
* address.line.extension[0].url = "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-streetName"
* address.line.extension[=].valueString = "Mozartgasse"
* address.line.extension[+].url = "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber"
* address.line.extension[=].valueString = "1-7"
* address.line.extension[+].url = "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-additionalLocator"
* address.line.extension[=].valueString = "Haupteingang"
* address.line.extension[+].url = "http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-ext-address-additionalInformation"
* address.line.extension[=].valueString = "Barrierefreier Zugang"
* address.city = "St. Wolfgang"
* address.state = "Salzburg"
* address.postalCode = "5350"
* address.country = "AUT"
* contact.telecom[0].system = #email
* contact.telecom[=].value = "info@amadeusspital.at"
* contact.telecom[=].use = #work
* contact.telecom[+].system = #phone
* contact.telecom[=].value = "+43.6138.3453446.0"
* contact.telecom[=].use = #home
