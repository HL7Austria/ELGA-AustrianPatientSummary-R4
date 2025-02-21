Profile: AtApsImagingStudy
Parent: ImagingStudy
Id: at-aps-imagingstudy
Title: "AT APS ImagingStudy"
Description: "This AT APS profile for the ImagingStudy resource is derived from the general ImagingStudy resource in absence of a corresponding profile in the HL7® Austria FHIR® Core implementation guide and also ensures IPS conformity via the IPS profile referenced by the so-called [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile) extension."
* . ^short = "AT APS ImagingStudy"
* ^extension[$imposeProfile].valueCanonical = Canonical(ImagingStudyUvIps)
* subject only Reference(AtApsPatient)
