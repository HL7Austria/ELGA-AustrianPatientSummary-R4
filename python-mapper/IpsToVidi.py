from asyncio import ensure_future

from pyscript import window
import micropip
import pyodide

async def setup():
    # Install your module that depends on lxml
    await micropip.install('lxml')
    #await micropip.install('malac-hd')

    # here goes the original code
    import time
    import json
    from datetime import datetime
    import dateutil.parser
    import r4
    import vidi as malac_vidi
    import utils
    import fhirpath



    description_text = "This has been compiled by the MApping LAnguage compiler for Health Data, short MaLaC-HD. See arguments for more details."
    one_timestamp = datetime.now()
    fhirpath_utils = fhirpath.FHIRPathUtils(r4)
    shared_vars = {}


    def transform(source_path, target_path):
        start = time.time()
        print('+++++++ Transformation from '+source_path+' to '+target_path+' started +++++++')

        if source_path.endswith('.xml'):
            bundi = r4.parse(source_path, silence=True)
        elif source_path.endswith('.json'):
            with open(source_path, 'r', newline='', encoding='utf-8') as f:
                bundi = utils.parse_json(r4, json.load(f))
        else:
            raise BaseException('Unknown source file ending: ' + source_path)
        vidi = malac_vidi.vidi()
        groot(bundi, vidi)
        with open(target_path, 'w', newline='', encoding='utf-8') as f:
            if target_path.endswith('.xml'):
                f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                vidi.export(f, 0, namespacedef_='xmlns="http://hl7.org/fhir" xmlns:v3="urn:hl7-org:v3"')
            elif target_path.endswith('.json'):
                json.dump(vidi.exportJson(), f)
            else:
                raise BaseException('Unknown target file ending')

        print('altogether in '+str(round(time.time()-start,3))+' seconds.')
        print('+++++++ Transformation from '+source_path+' to '+target_path+' ended  +++++++')

    def transform_web(source):
        start = time.time()
        print('+++++++ Transformation started +++++++')
        bundi = utils.parse_json(r4, json.loads(source)) # r4.parseJson(source, silence=True)
        vidi = malac_vidi.vidi()
        groot(bundi, vidi)
        print('altogether in '+str(round(time.time()-start,3))+' seconds.')
        print('+++++++ Transformation ended  +++++++')
        return json.dumps(vidi.exportJson())


    def groot(bundi, vidi):
        for entry in bundi.entry or []:
            med = entry.resource
            if med:
                med = unpack_container(med)
                if isinstance(med, r4.MedicationStatement):
                    med_effper = med.effectivePeriod
                    if med_effper:
                        if fhirpath.single((fhirpath_utils.bool_or(fhirpath_utils.bool_not([bool([v2 for v1 in [med_effper] for v2 in fhirpath_utils.get(v1,'end')])]), fhirpath_utils.compare([v5 for v4 in [med_effper] for v5 in fhirpath_utils.get(v4,'end')], '>=', [one_timestamp.date()])))):
                            vcmd = malac_vidi.v_current_medication_dataType()
                            if vidi.v_current_medication_data is not None:
                                vcmd = vidi.v_current_medication_data
                            else:
                                vidi.v_current_medication_data = vcmd
                            data = malac_vidi.dataType()
                            vcmd.data.append(data)
                            medication_data(med, data)
            med = entry.resource
            if med:
                med = unpack_container(med)
                if isinstance(med, r4.MedicationStatement):
                    med_effper = med.effectivePeriod
                    if med_effper:
                        if fhirpath.single((fhirpath_utils.bool_or(fhirpath_utils.bool_not([bool([v2 for v1 in [med_effper] for v2 in fhirpath_utils.get(v1,'end')])]), fhirpath_utils.compare([v5 for v4 in [med_effper] for v5 in fhirpath_utils.get(v4,'end')], '>=', [one_timestamp.date()])))):
                            icmd = malac_vidi.i_current_medication_dataType()
                            if vidi.i_current_medication_data is not None:
                                icmd = vidi.i_current_medication_data
                            else:
                                vidi.i_current_medication_data = icmd
                            data = malac_vidi.dataType1()
                            icmd.data.append(data)
                            i_medication_data(med, data)
            med = entry.resource
            if med:
                med = unpack_container(med)
                if isinstance(med, r4.MedicationStatement):
                    med_effper = med.effectivePeriod
                    if med_effper:
                        if fhirpath.single((fhirpath_utils.compare([v2 for v1 in [med_effper] for v2 in fhirpath_utils.get(v1,'end')], '<', [one_timestamp.date()]))):
                            vpmd = malac_vidi.v_past_medication_dataType()
                            if vidi.v_past_medication_data is not None:
                                vpmd = vidi.v_past_medication_data
                            else:
                                vidi.v_past_medication_data = vpmd
                            data = malac_vidi.dataType2()
                            vpmd.data.append(data)
                            medication_data(med, data)
            med = entry.resource
            if med:
                med = unpack_container(med)
                if isinstance(med, r4.MedicationStatement):
                    med_effper = med.effectivePeriod
                    if med_effper:
                        if fhirpath.single((fhirpath_utils.compare([v2 for v1 in [med_effper] for v2 in fhirpath_utils.get(v1,'end')], '<', [one_timestamp.date()]))):
                            ipmd = malac_vidi.i_past_medication_dataType()
                            if vidi.i_past_medication_data is not None:
                                ipmd = vidi.i_past_medication_data
                            else:
                                vidi.i_past_medication_data = ipmd
                            data = malac_vidi.dataType3()
                            ipmd.data.append(data)
                            i_medication_data(med, data)
            allin = entry.resource
            if allin:
                allin = unpack_container(allin)
                if isinstance(allin, r4.AllergyIntolerance):
                    vad = malac_vidi.v_allergies_dataType()
                    if vidi.v_allergies_data is not None:
                        vad = vidi.v_allergies_data
                    else:
                        vidi.v_allergies_data = vad
                    data = malac_vidi.dataType4()
                    vad.data.append(data)
                    problems_data(allin, data)
            allin = entry.resource
            if allin:
                allin = unpack_container(allin)
                if isinstance(allin, r4.AllergyIntolerance):
                    iad = malac_vidi.i_allergies_dataType()
                    if vidi.i_allergies_data is not None:
                        iad = vidi.i_allergies_data
                    else:
                        vidi.i_allergies_data = iad
                    data = malac_vidi.dataType5()
                    iad.data.append(data)
                    i_problems_data(allin, data)
            condi = entry.resource
            if condi:
                condi = unpack_container(condi)
                if isinstance(condi, r4.Condition):
                    if fhirpath.single((fhirpath_utils.bool_and(fhirpath_utils.bool_and(fhirpath_utils.bool_not([v8 for v7 in [v6 for v5 in [v4 for v3 in [v2 for v1 in [condi] for v2 in fhirpath_utils.get(v1,'code')] for v4 in fhirpath_utils.get(v3,'coding')] for v6 in fhirpath_utils.get(v5,'display')] for v8 in fhirpath_utils.startswith(v7, ['FH:'])]), fhirpath_utils.bool_not([v16 for v15 in [v14 for v13 in [v12 for v11 in [v10 for v9 in [condi] for v10 in fhirpath_utils.get(v9,'code')] for v12 in fhirpath_utils.get(v11,'coding')] for v14 in fhirpath_utils.get(v13,'display')] for v16 in fhirpath_utils.startswith(v15, ['Family history'])])), fhirpath_utils.equals([v22 for v21 in [v20 for v19 in [v18 for v17 in [condi] for v18 in fhirpath_utils.get(v17,'clinicalStatus')] for v20 in fhirpath_utils.get(v19,'coding')] for v22 in fhirpath_utils.get(v21,'code')], '==', ['active'])))):
                        vcpd = malac_vidi.v_current_problems_dataType()
                        if vidi.v_current_problems_data is not None:
                            vcpd = vidi.v_current_problems_data
                        else:
                            vidi.v_current_problems_data = vcpd
                        data = malac_vidi.dataType6()
                        vcpd.data.append(data)
                        problems_data(condi, data)
            condi = entry.resource
            if condi:
                condi = unpack_container(condi)
                if isinstance(condi, r4.Condition):
                    if fhirpath.single((fhirpath_utils.bool_and(fhirpath_utils.bool_and(fhirpath_utils.bool_not([v8 for v7 in [v6 for v5 in [v4 for v3 in [v2 for v1 in [condi] for v2 in fhirpath_utils.get(v1,'code')] for v4 in fhirpath_utils.get(v3,'coding')] for v6 in fhirpath_utils.get(v5,'display')] for v8 in fhirpath_utils.startswith(v7, ['FH:'])]), fhirpath_utils.bool_not([v16 for v15 in [v14 for v13 in [v12 for v11 in [v10 for v9 in [condi] for v10 in fhirpath_utils.get(v9,'code')] for v12 in fhirpath_utils.get(v11,'coding')] for v14 in fhirpath_utils.get(v13,'display')] for v16 in fhirpath_utils.startswith(v15, ['Family history'])])), fhirpath_utils.equals([v22 for v21 in [v20 for v19 in [v18 for v17 in [condi] for v18 in fhirpath_utils.get(v17,'clinicalStatus')] for v20 in fhirpath_utils.get(v19,'coding')] for v22 in fhirpath_utils.get(v21,'code')], '==', ['active'])))):
                        icpd = malac_vidi.i_current_problems_dataType()
                        if vidi.i_current_problems_data is not None:
                            icpd = vidi.i_current_problems_data
                        else:
                            vidi.i_current_problems_data = icpd
                        data = malac_vidi.dataType7()
                        icpd.data.append(data)
                        i_problems_data(condi, data)
            condi = entry.resource
            if condi:
                condi = unpack_container(condi)
                if isinstance(condi, r4.Condition):
                    if fhirpath.single((fhirpath_utils.bool_and(fhirpath_utils.bool_and(fhirpath_utils.bool_not([v8 for v7 in [v6 for v5 in [v4 for v3 in [v2 for v1 in [condi] for v2 in fhirpath_utils.get(v1,'code')] for v4 in fhirpath_utils.get(v3,'coding')] for v6 in fhirpath_utils.get(v5,'display')] for v8 in fhirpath_utils.startswith(v7, ['FH:'])]), fhirpath_utils.bool_not([v16 for v15 in [v14 for v13 in [v12 for v11 in [v10 for v9 in [condi] for v10 in fhirpath_utils.get(v9,'code')] for v12 in fhirpath_utils.get(v11,'coding')] for v14 in fhirpath_utils.get(v13,'display')] for v16 in fhirpath_utils.startswith(v15, ['Family history'])])), fhirpath_utils.equals([v22 for v21 in [v20 for v19 in [v18 for v17 in [condi] for v18 in fhirpath_utils.get(v17,'clinicalStatus')] for v20 in fhirpath_utils.get(v19,'coding')] for v22 in fhirpath_utils.get(v21,'code')], '!=', ['active'])))):
                        vppd = malac_vidi.v_past_problems_dataType()
                        if vidi.v_past_problems_data is not None:
                            vppd = vidi.v_past_problems_data
                        else:
                            vidi.v_past_problems_data = vppd
                        data = malac_vidi.dataType8()
                        vppd.data.append(data)
                        problems_data(condi, data)
            condi = entry.resource
            if condi:
                condi = unpack_container(condi)
                if isinstance(condi, r4.Condition):
                    if fhirpath.single((fhirpath_utils.bool_and(fhirpath_utils.bool_and(fhirpath_utils.bool_not([v8 for v7 in [v6 for v5 in [v4 for v3 in [v2 for v1 in [condi] for v2 in fhirpath_utils.get(v1,'code')] for v4 in fhirpath_utils.get(v3,'coding')] for v6 in fhirpath_utils.get(v5,'display')] for v8 in fhirpath_utils.startswith(v7, ['FH:'])]), fhirpath_utils.bool_not([v16 for v15 in [v14 for v13 in [v12 for v11 in [v10 for v9 in [condi] for v10 in fhirpath_utils.get(v9,'code')] for v12 in fhirpath_utils.get(v11,'coding')] for v14 in fhirpath_utils.get(v13,'display')] for v16 in fhirpath_utils.startswith(v15, ['Family history'])])), fhirpath_utils.equals([v22 for v21 in [v20 for v19 in [v18 for v17 in [condi] for v18 in fhirpath_utils.get(v17,'clinicalStatus')] for v20 in fhirpath_utils.get(v19,'coding')] for v22 in fhirpath_utils.get(v21,'code')], '!=', ['active'])))):
                        ippd = malac_vidi.i_past_problems_dataType()
                        if vidi.i_past_problems_data is not None:
                            ippd = vidi.i_past_problems_data
                        else:
                            vidi.i_past_problems_data = ippd
                        data = malac_vidi.dataType10()
                        ippd.data.append(data)
                        i_problems_data(condi, data)
            condi = entry.resource
            if condi:
                condi = unpack_container(condi)
                if isinstance(condi, r4.Condition):
                    if fhirpath.single((fhirpath_utils.bool_or([v8 for v7 in [v6 for v5 in [v4 for v3 in [v2 for v1 in [condi] for v2 in fhirpath_utils.get(v1,'code')] for v4 in fhirpath_utils.get(v3,'coding')] for v6 in fhirpath_utils.get(v5,'display')] for v8 in fhirpath_utils.startswith(v7, ['FH:'])], [v16 for v15 in [v14 for v13 in [v12 for v11 in [v10 for v9 in [condi] for v10 in fhirpath_utils.get(v9,'code')] for v12 in fhirpath_utils.get(v11,'coding')] for v14 in fhirpath_utils.get(v13,'display')] for v16 in fhirpath_utils.startswith(v15, ['Family history'])]))):
                        vfpd = malac_vidi.v_family_problems_dataType()
                        if vidi.v_family_problems_data is not None:
                            vfpd = vidi.v_family_problems_data
                        else:
                            vidi.v_family_problems_data = vfpd
                        data = malac_vidi.dataType11()
                        vfpd.data.append(data)
                        problems_data(condi, data)
            condi = entry.resource
            if condi:
                condi = unpack_container(condi)
                if isinstance(condi, r4.Condition):
                    if fhirpath.single((fhirpath_utils.bool_or([v8 for v7 in [v6 for v5 in [v4 for v3 in [v2 for v1 in [condi] for v2 in fhirpath_utils.get(v1,'code')] for v4 in fhirpath_utils.get(v3,'coding')] for v6 in fhirpath_utils.get(v5,'display')] for v8 in fhirpath_utils.startswith(v7, ['FH:'])], [v16 for v15 in [v14 for v13 in [v12 for v11 in [v10 for v9 in [condi] for v10 in fhirpath_utils.get(v9,'code')] for v12 in fhirpath_utils.get(v11,'coding')] for v14 in fhirpath_utils.get(v13,'display')] for v16 in fhirpath_utils.startswith(v15, ['Family history'])]))):
                        ifpd = malac_vidi.i_family_problems_dataType()
                        if vidi.i_family_problems_data is not None:
                            ifpd = vidi.i_family_problems_data
                        else:
                            vidi.i_family_problems_data = ifpd
                        data = malac_vidi.dataType13()
                        ifpd.data.append(data)
                        i_problems_data(condi, data)
            proc = entry.resource
            if proc:
                proc = unpack_container(proc)
                if isinstance(proc, r4.Procedure):
                    vpd = malac_vidi.v_procedures_dataType()
                    if vidi.v_procedures_data is not None:
                        vpd = vidi.v_procedures_data
                    else:
                        vidi.v_procedures_data = vpd
                    data = malac_vidi.dataType14()
                    vpd.data.append(data)
                    procedures_data(proc, data)
            proc = entry.resource
            if proc:
                proc = unpack_container(proc)
                if isinstance(proc, r4.Procedure):
                    ipd = malac_vidi.i_procedures_dataType()
                    if vidi.i_procedures_data is not None:
                        ipd = vidi.i_procedures_data
                    else:
                        vidi.i_procedures_data = ipd
                    data = malac_vidi.dataType16()
                    ipd.data.append(data)
                    i_procedures_data(proc, data)

    def medication_data(med, data):
        med_code = med.medicationCodeableConcept
        if med_code:
            for med_code_coding in med_code.coding or []:
                med_code_coding_display = med_code_coding.display
                if med_code_coding_display:
                    data.name = med_code_coding_display.value
        for med_dose in med.dosage or []:
            med_dose_text = med_dose.text
            if med_dose_text:
                data.dosis = med_dose_text.value

    def i_medication_data(med, data):
        medication_data(med, data)
        med_effper = med.effectivePeriod
        if med_effper:
            med_effper_start = med_effper.start
            if med_effper_start:
                data.beginn = fhirpath.single(fhirpath_utils.toString([dateutil.parser.parse(str(med_effper_start.value))]))
        med_status = med.status
        if med_status:
            data.status = med_status.value
        med_code = med.medicationCodeableConcept
        if med_code:
            for med_code_coding in med_code.coding or []:
                med_code_coding_code = med_code_coding.code
                if med_code_coding_code:
                    data.code = med_code_coding_code.value
                med_code_coding_system = med_code_coding.system
                if med_code_coding_system:
                    data.codeSystem = med_code_coding_system

    def problems_data(condi, data):
        condi_code = condi.code
        if condi_code:
            for condi_code_coding in condi_code.coding or []:
                condi_code_coding_display = condi_code_coding.display
                if condi_code_coding_display:
                    data.diagnose = condi_code_coding_display.value

    def i_problems_data(condi, data):
        problems_data(condi, data)
        condi_code = condi.code
        if condi_code:
            for condi_code_coding in condi_code.coding or []:
                condi_code_coding_code = condi_code_coding.code
                if condi_code_coding_code:
                    data.code = condi_code_coding_code.value
                condi_code_coding_cs = condi_code_coding.system
                if condi_code_coding_cs:
                    data.codesystem = condi_code_coding_cs.value
        condi_clinstat = condi.clinicalStatus
        if condi_clinstat:
            for condi_clinstat_codi in condi_clinstat.coding or []:
                condi_clinstat_codi_disp = condi_clinstat_codi.display
                if condi_clinstat_codi_disp:
                    data.status = condi_clinstat_codi_disp.value
        condi_veristat = condi.verificationStatus
        if condi_veristat:
            for condi_veristat_codi in condi_veristat.coding or []:
                condi_veristat_codi_disp = condi_veristat_codi.display
                if condi_veristat_codi_disp:
                    data.status = condi_veristat_codi_disp.value

    def procedures_data(proc, data):
        problems_data(proc, data)
        proc_performedDateTime = proc.performedDateTime
        if proc_performedDateTime:
            data.zeitpunkt = fhirpath.single([v2 for v1 in fhirpath_utils.toString([dateutil.parser.parse(str(proc_performedDateTime.value))]) for v2 in fhirpath_utils.substring(v1,[0],[4])])

    def i_procedures_data(proc, data):
        procedures_data(proc, data)
        proc_code = proc.code
        if proc_code:
            for proc_code_coding in proc_code.coding or []:
                proc_code_coding_code = proc_code_coding.code
                if proc_code_coding_code:
                    data.code = proc_code_coding_code.value
                proc_code_coding_cs = proc_code_coding.system
                if proc_code_coding_cs:
                    data.codesystem = proc_code_coding_cs.value
        proc_status = proc.status
        if proc_status:
            data.status = proc_status.value

    def unpack_container(resource_container):
        if resource_container.Account is not None:
            return resource_container.Account
        if resource_container.ActivityDefinition is not None:
            return resource_container.ActivityDefinition
        if resource_container.AdministrableProductDefinition is not None:
            return resource_container.AdministrableProductDefinition
        if resource_container.AdverseEvent is not None:
            return resource_container.AdverseEvent
        if resource_container.AllergyIntolerance is not None:
            return resource_container.AllergyIntolerance
        if resource_container.Appointment is not None:
            return resource_container.Appointment
        if resource_container.AppointmentResponse is not None:
            return resource_container.AppointmentResponse
        if resource_container.AuditEvent is not None:
            return resource_container.AuditEvent
        if resource_container.Basic is not None:
            return resource_container.Basic
        if resource_container.Binary is not None:
            return resource_container.Binary
        if resource_container.BiologicallyDerivedProduct is not None:
            return resource_container.BiologicallyDerivedProduct
        if resource_container.BodyStructure is not None:
            return resource_container.BodyStructure
        if resource_container.Bundle is not None:
            return resource_container.Bundle
        if resource_container.CapabilityStatement is not None:
            return resource_container.CapabilityStatement
        if resource_container.CarePlan is not None:
            return resource_container.CarePlan
        if resource_container.CareTeam is not None:
            return resource_container.CareTeam
        if resource_container.CatalogEntry is not None:
            return resource_container.CatalogEntry
        if resource_container.ChargeItem is not None:
            return resource_container.ChargeItem
        if resource_container.ChargeItemDefinition is not None:
            return resource_container.ChargeItemDefinition
        if resource_container.Citation is not None:
            return resource_container.Citation
        if resource_container.Claim is not None:
            return resource_container.Claim
        if resource_container.ClaimResponse is not None:
            return resource_container.ClaimResponse
        if resource_container.ClinicalImpression is not None:
            return resource_container.ClinicalImpression
        if resource_container.ClinicalUseDefinition is not None:
            return resource_container.ClinicalUseDefinition
        if resource_container.CodeSystem is not None:
            return resource_container.CodeSystem
        if resource_container.Communication is not None:
            return resource_container.Communication
        if resource_container.CommunicationRequest is not None:
            return resource_container.CommunicationRequest
        if resource_container.CompartmentDefinition is not None:
            return resource_container.CompartmentDefinition
        if resource_container.Composition is not None:
            return resource_container.Composition
        if resource_container.ConceptMap is not None:
            return resource_container.ConceptMap
        if resource_container.Condition is not None:
            return resource_container.Condition
        if resource_container.Consent is not None:
            return resource_container.Consent
        if resource_container.Contract is not None:
            return resource_container.Contract
        if resource_container.Coverage is not None:
            return resource_container.Coverage
        if resource_container.CoverageEligibilityRequest is not None:
            return resource_container.CoverageEligibilityRequest
        if resource_container.CoverageEligibilityResponse is not None:
            return resource_container.CoverageEligibilityResponse
        if resource_container.DetectedIssue is not None:
            return resource_container.DetectedIssue
        if resource_container.Device is not None:
            return resource_container.Device
        if resource_container.DeviceDefinition is not None:
            return resource_container.DeviceDefinition
        if resource_container.DeviceMetric is not None:
            return resource_container.DeviceMetric
        if resource_container.DeviceRequest is not None:
            return resource_container.DeviceRequest
        if resource_container.DeviceUseStatement is not None:
            return resource_container.DeviceUseStatement
        if resource_container.DiagnosticReport is not None:
            return resource_container.DiagnosticReport
        if resource_container.DocumentManifest is not None:
            return resource_container.DocumentManifest
        if resource_container.DocumentReference is not None:
            return resource_container.DocumentReference
        if resource_container.Encounter is not None:
            return resource_container.Encounter
        if resource_container.Endpoint is not None:
            return resource_container.Endpoint
        if resource_container.EnrollmentRequest is not None:
            return resource_container.EnrollmentRequest
        if resource_container.EnrollmentResponse is not None:
            return resource_container.EnrollmentResponse
        if resource_container.EpisodeOfCare is not None:
            return resource_container.EpisodeOfCare
        if resource_container.EventDefinition is not None:
            return resource_container.EventDefinition
        if resource_container.Evidence is not None:
            return resource_container.Evidence
        if resource_container.EvidenceReport is not None:
            return resource_container.EvidenceReport
        if resource_container.EvidenceVariable is not None:
            return resource_container.EvidenceVariable
        if resource_container.ExampleScenario is not None:
            return resource_container.ExampleScenario
        if resource_container.ExplanationOfBenefit is not None:
            return resource_container.ExplanationOfBenefit
        if resource_container.FamilyMemberHistory is not None:
            return resource_container.FamilyMemberHistory
        if resource_container.Flag is not None:
            return resource_container.Flag
        if resource_container.Goal is not None:
            return resource_container.Goal
        if resource_container.GraphDefinition is not None:
            return resource_container.GraphDefinition
        if resource_container.Group is not None:
            return resource_container.Group
        if resource_container.GuidanceResponse is not None:
            return resource_container.GuidanceResponse
        if resource_container.HealthcareService is not None:
            return resource_container.HealthcareService
        if resource_container.ImagingStudy is not None:
            return resource_container.ImagingStudy
        if resource_container.Immunization is not None:
            return resource_container.Immunization
        if resource_container.ImmunizationEvaluation is not None:
            return resource_container.ImmunizationEvaluation
        if resource_container.ImmunizationRecommendation is not None:
            return resource_container.ImmunizationRecommendation
        if resource_container.ImplementationGuide is not None:
            return resource_container.ImplementationGuide
        if resource_container.Ingredient is not None:
            return resource_container.Ingredient
        if resource_container.InsurancePlan is not None:
            return resource_container.InsurancePlan
        if resource_container.Invoice is not None:
            return resource_container.Invoice
        if resource_container.Library is not None:
            return resource_container.Library
        if resource_container.Linkage is not None:
            return resource_container.Linkage
        if resource_container.List is not None:
            return resource_container.List
        if resource_container.Location is not None:
            return resource_container.Location
        if resource_container.ManufacturedItemDefinition is not None:
            return resource_container.ManufacturedItemDefinition
        if resource_container.Measure is not None:
            return resource_container.Measure
        if resource_container.MeasureReport is not None:
            return resource_container.MeasureReport
        if resource_container.Media is not None:
            return resource_container.Media
        if resource_container.Medication is not None:
            return resource_container.Medication
        if resource_container.MedicationAdministration is not None:
            return resource_container.MedicationAdministration
        if resource_container.MedicationDispense is not None:
            return resource_container.MedicationDispense
        if resource_container.MedicationKnowledge is not None:
            return resource_container.MedicationKnowledge
        if resource_container.MedicationRequest is not None:
            return resource_container.MedicationRequest
        if resource_container.MedicationStatement is not None:
            return resource_container.MedicationStatement
        if resource_container.MedicinalProductDefinition is not None:
            return resource_container.MedicinalProductDefinition
        if resource_container.MessageDefinition is not None:
            return resource_container.MessageDefinition
        if resource_container.MessageHeader is not None:
            return resource_container.MessageHeader
        if resource_container.MolecularSequence is not None:
            return resource_container.MolecularSequence
        if resource_container.NamingSystem is not None:
            return resource_container.NamingSystem
        if resource_container.NutritionOrder is not None:
            return resource_container.NutritionOrder
        if resource_container.NutritionProduct is not None:
            return resource_container.NutritionProduct
        if resource_container.Observation is not None:
            return resource_container.Observation
        if resource_container.ObservationDefinition is not None:
            return resource_container.ObservationDefinition
        if resource_container.OperationDefinition is not None:
            return resource_container.OperationDefinition
        if resource_container.OperationOutcome is not None:
            return resource_container.OperationOutcome
        if resource_container.Organization is not None:
            return resource_container.Organization
        if resource_container.OrganizationAffiliation is not None:
            return resource_container.OrganizationAffiliation
        if resource_container.PackagedProductDefinition is not None:
            return resource_container.PackagedProductDefinition
        if resource_container.Patient is not None:
            return resource_container.Patient
        if resource_container.PaymentNotice is not None:
            return resource_container.PaymentNotice
        if resource_container.PaymentReconciliation is not None:
            return resource_container.PaymentReconciliation
        if resource_container.Person is not None:
            return resource_container.Person
        if resource_container.PlanDefinition is not None:
            return resource_container.PlanDefinition
        if resource_container.Practitioner is not None:
            return resource_container.Practitioner
        if resource_container.PractitionerRole is not None:
            return resource_container.PractitionerRole
        if resource_container.Procedure is not None:
            return resource_container.Procedure
        if resource_container.Provenance is not None:
            return resource_container.Provenance
        if resource_container.Questionnaire is not None:
            return resource_container.Questionnaire
        if resource_container.QuestionnaireResponse is not None:
            return resource_container.QuestionnaireResponse
        if resource_container.RegulatedAuthorization is not None:
            return resource_container.RegulatedAuthorization
        if resource_container.RelatedPerson is not None:
            return resource_container.RelatedPerson
        if resource_container.RequestGroup is not None:
            return resource_container.RequestGroup
        if resource_container.ResearchDefinition is not None:
            return resource_container.ResearchDefinition
        if resource_container.ResearchElementDefinition is not None:
            return resource_container.ResearchElementDefinition
        if resource_container.ResearchStudy is not None:
            return resource_container.ResearchStudy
        if resource_container.ResearchSubject is not None:
            return resource_container.ResearchSubject
        if resource_container.RiskAssessment is not None:
            return resource_container.RiskAssessment
        if resource_container.Schedule is not None:
            return resource_container.Schedule
        if resource_container.SearchParameter is not None:
            return resource_container.SearchParameter
        if resource_container.ServiceRequest is not None:
            return resource_container.ServiceRequest
        if resource_container.Slot is not None:
            return resource_container.Slot
        if resource_container.Specimen is not None:
            return resource_container.Specimen
        if resource_container.SpecimenDefinition is not None:
            return resource_container.SpecimenDefinition
        if resource_container.StructureDefinition is not None:
            return resource_container.StructureDefinition
        if resource_container.StructureMap is not None:
            return resource_container.StructureMap
        if resource_container.Subscription is not None:
            return resource_container.Subscription
        if resource_container.SubscriptionStatus is not None:
            return resource_container.SubscriptionStatus
        if resource_container.SubscriptionTopic is not None:
            return resource_container.SubscriptionTopic
        if resource_container.Substance is not None:
            return resource_container.Substance
        if resource_container.SubstanceDefinition is not None:
            return resource_container.SubstanceDefinition
        if resource_container.SupplyDelivery is not None:
            return resource_container.SupplyDelivery
        if resource_container.SupplyRequest is not None:
            return resource_container.SupplyRequest
        if resource_container.Task is not None:
            return resource_container.Task
        if resource_container.TerminologyCapabilities is not None:
            return resource_container.TerminologyCapabilities
        if resource_container.TestReport is not None:
            return resource_container.TestReport
        if resource_container.TestScript is not None:
            return resource_container.TestScript
        if resource_container.ValueSet is not None:
            return resource_container.ValueSet
        if resource_container.VerificationResult is not None:
            return resource_container.VerificationResult
        if resource_container.VisionPrescription is not None:
            return resource_container.VisionPrescription
        if resource_container.Parameters is not None:
            return resource_container.Parameters
        return None

    window.transform = transform_web


# Run the main function
ensure_future(setup())