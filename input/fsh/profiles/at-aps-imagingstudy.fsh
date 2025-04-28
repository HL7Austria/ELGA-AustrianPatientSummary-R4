Profile: AtApsImagingStudy
Parent: ImagingStudy
Id: at-aps-imagingstudy
Title: "AT APS ImagingStudy"
Description: "Das AT APS-Profil für die ImagingStudy-Ressource berücksichtigt zum einen die österreichischen Vorgaben (z.B. Patient und zu verwendende Value-Sets) und stellt andererseits die Konformität gegenüber dem IPS-Profil sicher, indem die so genannte [`imposeProfile`](http://hl7.org/fhir/StructureDefinition/structuredefinition-imposeProfile)-Erweiterung verwendet wird."
* ^status = #active
* . ^short = "AT APS ImagingStudy"
* ^extension[$imposeProfile].valueCanonical = Canonical(ImagingStudyUvIps)
* subject only Reference(AtApsPatient)
