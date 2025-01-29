ValueSet: AtIpsLaboratoryPathologyCategory
Id: at-ips-laboratory-pathology-category
Title: "AT IPS Laboratory/Pathology Category"
Description: "This value set combines the FHIR observation category and the ELGA specific laboratory report structure."
* ^meta.profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
* ^status = #active
* ^experimental = false
* ^publisher = "ELGA GmbH"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "https://elga.gv.at"
* ^immutable = false
* include codes from valueset $laboratory-structure
* include codes from valueset http://hl7.org/fhir/ValueSet/observation-category