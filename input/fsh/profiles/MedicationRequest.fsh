Profile: AtIpsMedicationRequest
Parent: MedicationRequest
Id: at-ips-medicationrequest
Title: "AT IPS MedicationRequest"
Description: "This AT IPS profile for the MedicationRequest resource is derived from the general MedicationRequest resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS MedicationRequest"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(MedicationRequestIPS)
* medication[x] only CodeableConcept or Reference(AtIpsMedication)
* subject only Reference(AtIpsPatient)
