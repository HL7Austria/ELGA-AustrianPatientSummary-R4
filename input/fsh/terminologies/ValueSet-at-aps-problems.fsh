ValueSet: AtApsProblems
Id: at-aps-problems
Title: "AT APS Problems"
Description: "Dieses Value-Set ist eine Sammlung von möglichen Quellen für die Dokumentation von Problemen/Diagnosen."
* ^meta.profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
* ^status = #active
* ^experimental = false
* ^publisher = "ELGA GmbH"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "https://elga.gv.at"
* ^immutable = false
* ^copyright = "Enthält durch SNOMED International urheberrechtlich geschützte Information. Jede Verwendung von SNOMED CT in Österreich erfordert eine aufrechte Affiliate Lizenz oder eine Sublizenz. Die entsprechende Lizenz ist kostenlos, vorausgesetzt die Verwendung findet nur in Österreich statt und erfüllt die Bedingungen des Affiliate License Agreements. Affiliate Lizenzen können über das [Mitglieder-Lizenzierungs- und Distributions-Service](https://mlds.ihtsdotools.org/#/landing/AT?lang=de) (MLDS) direkt beim jeweiligen NRC beantragt werden."
* include codes from system $cs-icd-10-bmsgpk-2025
* include codes from system $cs-icpc2
* include codes from system $cs-icf
* include codes from system $cs-sct
* include codes from system $cs-lkat-bmsgpk-2025
* include codes from system $cs-loinc
