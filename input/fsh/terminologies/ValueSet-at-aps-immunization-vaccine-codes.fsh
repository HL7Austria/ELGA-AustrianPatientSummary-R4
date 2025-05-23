ValueSet: AtApsImmunizationVaccineCodes
Id: at-aps-immunization-vaccine-codes
Title: "AT APS Immunitzation Vaccine Codes"
Description: "Dieses Value-Set erweitert die in Österreich existierenden Impfstoffe um die Möglichkeit, angeben zu können, dass der verimpfte Impfstoff unbekannt ist."
* ^meta.profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
* ^status = #active
* ^experimental = false
* ^publisher = "ELGA GmbH"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "https://elga.gv.at"
* ^immutable = false
* ^copyright = "Enthält durch SNOMED International urheberrechtlich geschützte Information. Jede Verwendung von SNOMED CT in Österreich erfordert eine aufrechte Affiliate Lizenz oder eine Sublizenz. Die entsprechende Lizenz ist kostenlos, vorausgesetzt die Verwendung findet nur in Österreich statt und erfüllt die Bedingungen des Affiliate License Agreements. Affiliate Lizenzen können über das [Mitglieder-Lizenzierungs- und Distributions-Service](https://mlds.ihtsdotools.org/#/landing/AT?lang=de) (MLDS) direkt beim jeweiligen NRC beantragt werden."
* include codes from valueset $vs-eimpf-impfstoffe
* include codes from system $cs-sct
    where concept is-a #787482006 "No known immunizations (situation)"
