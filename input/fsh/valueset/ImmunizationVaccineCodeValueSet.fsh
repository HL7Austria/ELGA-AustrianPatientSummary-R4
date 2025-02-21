ValueSet: AtApsImmunizationVaccineCodes
Id: at-aps-immunization-vaccine-codes
Title: "AT APS Immunitzation Vaccine Codes"
Description: "This value set extends the existing vaccine codes from ELGA GmbH."
* ^meta.profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
* ^status = #active
* ^experimental = true
* ^publisher = "ELGA GmbH"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "https://elga.gv.at"
* ^immutable = false
* ^copyright = "This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement"
* include codes from valueset $eimpf-impfstoffe
* include codes from system http://snomed.info/sct
    where concept is-a #787482006 "No known immunizations (situation)"
