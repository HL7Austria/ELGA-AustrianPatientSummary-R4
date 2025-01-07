Profile: AtIpsImmunization
Parent: Immunization
Id: at-ips-immunization
Title: "AT IPS Immunization"
Description: "This AT IPS profile for the Immunization resource is derived from the general Immunization resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS Immunization"
* ^extension[$imposeProfile].valueCanonical = Canonical(ImmunizationUvIps)
* patient only Reference(AtIpsPatient)
* extension contains ImmunizationBasedOn named basedOn 0..1
* vaccineCode from AtIpsImmunizationVacineCodes (extensible)
* route from $immunization-route (extensible)
* protocolApplied.targetDisease 1..*
* protocolApplied.targetDisease from $immunization-target-disease (extensible)

Extension:      ImmunizationBasedOn
Id:             immunization-basedOn
Title:          "Immunization basedOn"
Description:    "Authority that the immunization event is based on"
* value[x] only Reference(CarePlan or MedicationRequest or ServiceRequest or ImmunizationRecommendation)
* value[x] ^short = "Authority that the immunization event is based on"
* value[x] 1..1

ValueSet: AtIpsImmunizationVacineCodes
Id: at-ips-immunization-vacine-codes
Title: "AT IPS Immunitzation Vacine Codes"
Description: "This value set extens the existing vaccine codes from ELGA GmbH."
* ^meta.profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
* ^status = #active
* ^experimental = false
* ^publisher = "ELGA GmbH"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "https://elga.gv.at"
* ^immutable = false
* include codes from valueset https://termgit.elga.gv.at/ValueSet/eimpf-immunizationtarget
* include codes from system http://snomed.info/sct
    where concept descendent-of #787482006 "No known immunizations"
* include codes from system http://snomed.info/sct
    where concept = #787859002 "Vaccine product (medicinal product)"
