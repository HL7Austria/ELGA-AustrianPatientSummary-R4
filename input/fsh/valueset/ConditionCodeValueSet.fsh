ValueSet: AtApsProblems
Id: at-aps-problems
Title: "AT APS Problems"
Description: "This value set collects the different code systems which are used for the AT APS Condition code."
* ^meta.profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
* ^status = #active
* ^experimental = true
* ^publisher = "ELGA GmbH"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "https://elga.gv.at"
* ^immutable = false
* ^copyright = """
This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement
This material contains content from LOINC (http://loinc.org). LOINC is copyright © 1995-2020, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the license at http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief Institute, Inc
"""
* include codes from system $cs-icd-10-bmsgpk-2025
* include codes from system $cs-icpc2
* include codes from system $cs-icf
* include codes from system $sct
* include codes from system $cs-lkat-bmsgpk-2025
* include codes from system $loinc
* include codes from system $sct
    where concept is-a #160245001 "No current problems or disability"