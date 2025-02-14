ValueSet: AtApsAllergyOrIntoleranceAgent
Id: at-aps-allergyorintoleranceagent
Title: "AT APS Allergy or Intolerance Agent"
Description: "This value set extends the existing value set from ELGA GmbH."
* ^meta.profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
* ^status = #active
* ^experimental = true
* ^publisher = "ELGA GmbH"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "https://elga.gv.at"
* ^immutable = false
* ^copyright = "This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement"
* include codes from valueset $allergy-intolerance
* include codes from system http://snomed.info/sct
    where concept is-a #716186003 "No known allergy (situation)"
