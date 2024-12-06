Profile: AtIpsImagingStudy
Parent: ImagingStudy
Id: at-ips-imagingstudy
Title: "AT IPS ImagingStudy"
Description: "This AT IPS profile for the ImagingStudy resource is derived from the general ImagingStudy resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT IPS ImagingStudy"
* ^extension[AtIpsImposeProfile].valueCanonical = Canonical(ImagingStudyUvIps)
* subject only Reference(AtIpsPatient)
