Instance: AtApsExamplePractitionerRole01
InstanceOf: AtApsPractitionerRole
Title: "Patient Journey Practitioner"
Description: "Beispiel eines behandelnden Arztes und seiner Organisation"
Usage: #example
* practitioner = Reference(Practitioner/at-aps-example-practitioner-01) "Hanna Hausärztin"
* organization = Reference(Organization/AtApsExampleOrganization01) "Amadeus Spital"
* code = $cs-elga-gtelvogdarollen#1000 "Ärztin/Arzt"
* specialty = $cs-sct#419192003 "Internal medicine"