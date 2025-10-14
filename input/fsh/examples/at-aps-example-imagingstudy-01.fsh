Alias: $DCM = http://dicom.nema.org/resources/ontology/DCM

Instance: AtApsExampleImagingStudy01
InstanceOf: AtApsImagingStudy
Title: "AtApsImagingStudy-Beispiel"
Description: "Imaging Study"
Usage: #example
* identifier.system = "urn:dicom:uid"
* identifier.value = "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430045"
* status = #available
* subject = Reference(Patient/HL7ATCorePatientExample01) "Max Mustermann"
* started = "2011-01-01T11:01:20+03:00"
* numberOfSeries = 1
* numberOfInstances = 1
* series.uid = "2.16.124.113543.6003.2588828330.45298.17418.2723805630"
* series.number = 3
* series.modality = $DCM#CT
* series.description = "CT Surview 180"
* series.numberOfInstances = 1
* series.bodySite = $cs-sct#67734004 "Upper Trunk Structure"
* series.instance.uid = "2.16.124.113543.6003.189642796.63084.16748.2599092903"
* series.instance.sopClass = urn:ietf:rfc:3986#urn:oid:1.2.840.10008.5.1.4.1.1.2
* series.instance.number = 1