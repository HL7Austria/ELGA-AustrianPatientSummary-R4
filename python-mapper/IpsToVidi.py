
import argparse
import time as sys_time
import json
from datetime import datetime, time as datetime_time
import date as dateutil
from html import escape as html_escape
import r4
import vidi as malac_vidi
import utils
import fhirpath

description_text = "This has been compiled by the MApping LAnguage compiler for Health Data, short MaLaC-HD. See arguments for more details."
one_timestamp = datetime.now()
fhirpath_utils = fhirpath.FHIRPathUtils(r4)
shared_vars = {}

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description_text)
    parser.add_argument(
       '-s', '--source', help='the source file path', required=True
    )
    parser.add_argument(
       '-t', '--target', help='the target file path the result will be written to', required=True
    )
    return parser

def transform(source_path, target_path):
    start = sys_time.time()
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
            json.dump(vidi.exportJson(), f, indent=4)
        else:
            raise BaseException('Unknown target file ending')

    print('altogether in '+str(round(sys_time.time()-start,3))+' seconds.')
    print('+++++++ Transformation from '+source_path+' to '+target_path+' ended  +++++++')

def groot(bundi, vidi):
    for entry in bundi.entry or []:
        author = unpack_container(entry.resource)
        if author is not None:
            if type(author) is r4.Practitioner:
                if vidi.author is None:
                    vidi.author = malac_vidi.authorType()
                vauthor = vidi.author
                authorToVidi(author, vauthor)
        patient = unpack_container(entry.resource)
        if patient is not None:
            if type(patient) is r4.Patient:
                if vidi.subject is None:
                    vidi.subject = malac_vidi.subjectType()
                vsubject = vidi.subject
                patientToVidi(patient, vsubject)
        med = unpack_container(entry.resource)
        if med is not None:
            if type(med) is r4.MedicationStatement:
                med_effper = med.effectivePeriod
                if med_effper is not None:
                    if fhirpath.single(fhirpath_utils.bool_or([(med_effper.end is None)], fhirpath_utils.compare(fhirpath_utils.get(med_effper,'end'), '>=', [one_timestamp.date()]))):
                        if vidi.v_current_medication_data is None:
                            vidi.v_current_medication_data = malac_vidi.v_current_medication_dataType()
                        vcmd = vidi.v_current_medication_data
                        data = malac_vidi.dataType()
                        vcmd.data.append(data)
                        medication_data(med, data)
        med = unpack_container(entry.resource)
        if med is not None:
            if type(med) is r4.MedicationStatement:
                med_effper = med.effectivePeriod
                if med_effper is not None:
                    if fhirpath.single(fhirpath_utils.bool_or([(med_effper.end is None)], fhirpath_utils.compare(fhirpath_utils.get(med_effper,'end'), '>=', [one_timestamp.date()]))):
                        if vidi.i_current_medication_data is None:
                            vidi.i_current_medication_data = malac_vidi.i_current_medication_dataType()
                        icmd = vidi.i_current_medication_data
                        data = malac_vidi.dataType1()
                        icmd.data.append(data)
                        i_medication_data(med, data)
        med = unpack_container(entry.resource)
        if med is not None:
            if type(med) is r4.MedicationStatement:
                med_effper = med.effectivePeriod
                if med_effper is not None:
                    if fhirpath.single(fhirpath_utils.compare(fhirpath_utils.get(med_effper,'end'), '<', [one_timestamp.date()])):
                        if vidi.v_past_medication_data is None:
                            vidi.v_past_medication_data = malac_vidi.v_past_medication_dataType()
                        vpmd = vidi.v_past_medication_data
                        data = malac_vidi.dataType2()
                        vpmd.data.append(data)
                        medication_data(med, data)
        med = unpack_container(entry.resource)
        if med is not None:
            if type(med) is r4.MedicationStatement:
                med_effper = med.effectivePeriod
                if med_effper is not None:
                    if fhirpath.single(fhirpath_utils.compare(fhirpath_utils.get(med_effper,'end'), '<', [one_timestamp.date()])):
                        if vidi.i_past_medication_data is None:
                            vidi.i_past_medication_data = malac_vidi.i_past_medication_dataType()
                        ipmd = vidi.i_past_medication_data
                        data = malac_vidi.dataType3()
                        ipmd.data.append(data)
                        i_medication_data(med, data)
        allin = unpack_container(entry.resource)
        if allin is not None:
            if type(allin) is r4.AllergyIntolerance:
                if vidi.v_allergies_data is None:
                    vidi.v_allergies_data = malac_vidi.v_allergies_dataType()
                vad = vidi.v_allergies_data
                data = malac_vidi.dataType4()
                vad.data.append(data)
                problems_data(allin, data)
        allin = unpack_container(entry.resource)
        if allin is not None:
            if type(allin) is r4.AllergyIntolerance:
                if vidi.i_allergies_data is None:
                    vidi.i_allergies_data = malac_vidi.i_allergies_dataType()
                iad = vidi.i_allergies_data
                data = malac_vidi.dataType5()
                iad.data.append(data)
                i_problems_data(allin, data)
        condi = unpack_container(entry.resource)
        if condi is not None:
            if type(condi) is r4.Condition:
                if fhirpath.single(fhirpath_utils.bool_and(fhirpath_utils.bool_not([v2 for v1 in fhirpath_utils.get(condi,'code','coding','display') for v2 in fhirpath_utils.startswith(v1, ['FH:'])]), fhirpath_utils.bool_not([v4 for v3 in fhirpath_utils.get(condi,'code','coding','display') for v4 in fhirpath_utils.startswith(v3, ['Family history'])]), fhirpath_utils.equals(fhirpath_utils.get(condi,'clinicalStatus','coding','code'), '==', ['active']))):
                    if vidi.v_current_problems_data is None:
                        vidi.v_current_problems_data = malac_vidi.v_current_problems_dataType()
                    vcpd = vidi.v_current_problems_data
                    data = malac_vidi.dataType6()
                    vcpd.data.append(data)
                    problems_data(condi, data)
        condi = unpack_container(entry.resource)
        if condi is not None:
            if type(condi) is r4.Condition:
                if fhirpath.single(fhirpath_utils.bool_and(fhirpath_utils.bool_not([v2 for v1 in fhirpath_utils.get(condi,'code','coding','display') for v2 in fhirpath_utils.startswith(v1, ['FH:'])]), fhirpath_utils.bool_not([v4 for v3 in fhirpath_utils.get(condi,'code','coding','display') for v4 in fhirpath_utils.startswith(v3, ['Family history'])]), fhirpath_utils.equals(fhirpath_utils.get(condi,'clinicalStatus','coding','code'), '==', ['active']))):
                    if vidi.i_current_problems_data is None:
                        vidi.i_current_problems_data = malac_vidi.i_current_problems_dataType()
                    icpd = vidi.i_current_problems_data
                    data = malac_vidi.dataType7()
                    icpd.data.append(data)
                    i_problems_data(condi, data)
        condi = unpack_container(entry.resource)
        if condi is not None:
            if type(condi) is r4.Condition:
                if fhirpath.single(fhirpath_utils.bool_and(fhirpath_utils.bool_not([v2 for v1 in fhirpath_utils.get(condi,'code','coding','display') for v2 in fhirpath_utils.startswith(v1, ['FH:'])]), fhirpath_utils.bool_not([v4 for v3 in fhirpath_utils.get(condi,'code','coding','display') for v4 in fhirpath_utils.startswith(v3, ['Family history'])]), fhirpath_utils.equals(fhirpath_utils.get(condi,'clinicalStatus','coding','code'), '!=', ['active']))):
                    if vidi.v_past_problems_data is None:
                        vidi.v_past_problems_data = malac_vidi.v_past_problems_dataType()
                    vppd = vidi.v_past_problems_data
                    data = malac_vidi.dataType8()
                    vppd.data.append(data)
                    problems_data(condi, data)
        condi = unpack_container(entry.resource)
        if condi is not None:
            if type(condi) is r4.Condition:
                if fhirpath.single(fhirpath_utils.bool_and(fhirpath_utils.bool_not([v2 for v1 in fhirpath_utils.get(condi,'code','coding','display') for v2 in fhirpath_utils.startswith(v1, ['FH:'])]), fhirpath_utils.bool_not([v4 for v3 in fhirpath_utils.get(condi,'code','coding','display') for v4 in fhirpath_utils.startswith(v3, ['Family history'])]), fhirpath_utils.equals(fhirpath_utils.get(condi,'clinicalStatus','coding','code'), '!=', ['active']))):
                    if vidi.i_past_problems_data is None:
                        vidi.i_past_problems_data = malac_vidi.i_past_problems_dataType()
                    ippd = vidi.i_past_problems_data
                    data = malac_vidi.dataType10()
                    ippd.data.append(data)
                    i_problems_data(condi, data)
        condi = unpack_container(entry.resource)
        if condi is not None:
            if type(condi) is r4.Condition:
                if fhirpath.single(fhirpath_utils.bool_or([v2 for v1 in fhirpath_utils.get(condi,'code','coding','display') for v2 in fhirpath_utils.startswith(v1, ['FH:'])], [v4 for v3 in fhirpath_utils.get(condi,'code','coding','display') for v4 in fhirpath_utils.startswith(v3, ['Family history'])])):
                    if vidi.v_family_problems_data is None:
                        vidi.v_family_problems_data = malac_vidi.v_family_problems_dataType()
                    vfpd = vidi.v_family_problems_data
                    data = malac_vidi.dataType11()
                    vfpd.data.append(data)
                    problems_data(condi, data)
        condi = unpack_container(entry.resource)
        if condi is not None:
            if type(condi) is r4.Condition:
                if fhirpath.single(fhirpath_utils.bool_or([v2 for v1 in fhirpath_utils.get(condi,'code','coding','display') for v2 in fhirpath_utils.startswith(v1, ['FH:'])], [v4 for v3 in fhirpath_utils.get(condi,'code','coding','display') for v4 in fhirpath_utils.startswith(v3, ['Family history'])])):
                    if vidi.i_family_problems_data is None:
                        vidi.i_family_problems_data = malac_vidi.i_family_problems_dataType()
                    ifpd = vidi.i_family_problems_data
                    data = malac_vidi.dataType13()
                    ifpd.data.append(data)
                    i_problems_data(condi, data)
        proc = unpack_container(entry.resource)
        if proc is not None:
            if type(proc) is r4.Procedure:
                if vidi.v_procedures_data is None:
                    vidi.v_procedures_data = malac_vidi.v_procedures_dataType()
                vpd = vidi.v_procedures_data
                data = malac_vidi.dataType14()
                vpd.data.append(data)
                procedures_data(proc, data)
        proc = unpack_container(entry.resource)
        if proc is not None:
            if type(proc) is r4.Procedure:
                if vidi.i_procedures_data is None:
                    vidi.i_procedures_data = malac_vidi.i_procedures_dataType()
                ipd = vidi.i_procedures_data
                data = malac_vidi.dataType16()
                ipd.data.append(data)
                i_procedures_data(proc, data)
        immunization = unpack_container(entry.resource)
        if immunization is not None:
            if type(immunization) is r4.Immunization:
                if vidi.i_immunizations_data is None:
                    vidi.i_immunizations_data = malac_vidi.i_immunizations_dataType()
                iid = vidi.i_immunizations_data
                data = malac_vidi.dataType17()
                iid.data.append(data)
                i_immunizations_data(immunization, data)
        careplan = unpack_container(entry.resource)
        if careplan is not None:
            if type(careplan) is r4.CarePlan:
                if vidi.i_careplan_data is None:
                    vidi.i_careplan_data = malac_vidi.i_careplan_dataType()
                icd = vidi.i_careplan_data
                data = malac_vidi.dataType22()
                icd.data.append(data)
                i_careplan_data(careplan, data)
        task = unpack_container(entry.resource)
        if task is not None:
            if type(task) is r4.Task:
                if vidi.i_tasks_data is None:
                    vidi.i_tasks_data = malac_vidi.i_tasks_dataType()
                itd = vidi.i_tasks_data
                data = malac_vidi.dataType23()
                itd.data.append(data)
                i_tasks_data(task, data)
        goal = unpack_container(entry.resource)
        if goal is not None:
            if type(goal) is r4.Goal:
                if vidi.i_goals_data is None:
                    vidi.i_goals_data = malac_vidi.i_goals_dataType()
                igd = vidi.i_goals_data
                data = malac_vidi.dataType24()
                igd.data.append(data)
                i_goals_data(goal, data)

def patientToVidi(patient, vsubject):
    for identifier in patient.identifier or []:
        if getattr(identifier.system, 'value', None) == 'urn:oid:1.2.40.0.10.1.4.3.1':
            vsubject.svnr = fhirpath.single(fhirpath_utils.get(identifier,'value','value'))
    for name in patient.name or []:
        for given in name.given or []:
            for v1 in fhirpath_utils.get(given,'value'):
                vsubject.given.append(v1)
        family = name.family
        if family is not None:
            vsubject.family = fhirpath.single(fhirpath_utils.get(family,'value'))
    gender = patient.gender
    if gender is not None:
        vsubject.gender = str(fhirpath.single(fhirpath_utils.get(gender,'value')))
    birthDate = patient.birthDate
    if birthDate is not None:
        vsubject.birthDate = fhirpath.single(fhirpath_utils.toString([birthDate]))
    for address in patient.address or []:
        vaddress = malac_vidi.addressType()
        vsubject.address.append(vaddress)
        for line in address.line or []:
            for v1 in fhirpath_utils.get(line,'value'):
                vaddress.line.append(v1)
        city = address.city
        if city is not None:
            vaddress.city = fhirpath.single(fhirpath_utils.get(city,'value'))
        postalCode = address.postalCode
        if postalCode is not None:
            vaddress.postalCode = fhirpath.single(fhirpath_utils.get(postalCode,'value'))

def authorToVidi(author, vauthor):
    for name in author.name or []:
        for fhir_prefix in name.prefix or []:
            for v1 in fhirpath_utils.get(fhir_prefix,'value'):
                vauthor.prefix.append(v1)
        for given in name.given or []:
            for v1 in fhirpath_utils.get(given,'value'):
                vauthor.given.append(v1)
        family = name.family
        if family is not None:
            vauthor.family = fhirpath.single(fhirpath_utils.get(family,'value'))

def medication_data(med, data):
    med_code = med.medicationCodeableConcept
    if med_code is not None:
        for med_code_coding in med_code.coding or []:
            med_code_coding_display = med_code_coding.display
            if med_code_coding_display is not None:
                data.name = med_code_coding_display.value
    med_ref = med.medicationReference
    if med_ref is not None:
        med_ref_display = med_ref.display
        if med_ref_display is not None:
            data.name = med_ref_display.value
    for med_dose in med.dosage or []:
        med_dose_text = med_dose.text
        if med_dose_text is not None:
            data.dosis = med_dose_text.value

def i_medication_data(med, data):
    medication_data(med, data)
    med_effper = med.effectivePeriod
    if med_effper is not None:
        med_effper_start = med_effper.start
        if med_effper_start is not None:
            data.beginn = fhirpath.single(fhirpath_utils.toString([dateutil.parse(str(med_effper_start.value))]))
    med_status = med.status
    if med_status is not None:
        data.status = med_status.value
    med_code = med.medicationCodeableConcept
    if med_code is not None:
        for med_code_coding in med_code.coding or []:
            med_code_coding_code = med_code_coding.code
            if med_code_coding_code is not None:
                data.code = med_code_coding_code.value
            med_code_coding_system = med_code_coding.system
            if med_code_coding_system is not None:
                data.codesystem = med_code_coding_system.value

def problems_data(condi, data):
    condi_code = condi.code
    if condi_code is not None:
        for condi_code_coding in condi_code.coding or []:
            condi_code_coding_display = condi_code_coding.display
            if condi_code_coding_display is not None:
                data.diagnose = condi_code_coding_display.value
                data.allergies = condi_code_coding_display

def i_problems_data(condi, data):
    problems_data(condi, data)
    condi_code = condi.code
    if condi_code is not None:
        for condi_code_coding in condi_code.coding or []:
            condi_code_coding_code = condi_code_coding.code
            if condi_code_coding_code is not None:
                data.code = condi_code_coding_code.value
            condi_code_coding_cs = condi_code_coding.system
            if condi_code_coding_cs is not None:
                data.codesystem = condi_code_coding_cs.value
    condi_clinstat = condi.clinicalStatus
    if condi_clinstat is not None:
        for condi_clinstat_codi in condi_clinstat.coding or []:
            condi_clinstat_codi_disp = condi_clinstat_codi.display
            if condi_clinstat_codi_disp is not None:
                data.status = condi_clinstat_codi_disp.value
    condi_veristat = condi.verificationStatus
    if condi_veristat is not None:
        for condi_veristat_codi in condi_veristat.coding or []:
            condi_veristat_codi_disp = condi_veristat_codi.display
            if condi_veristat_codi_disp is not None:
                data.status = condi_veristat_codi_disp.value

def procedures_data(proc, data):
    problems_data(proc, data)
    proc_performedDateTime = proc.performedDateTime
    if proc_performedDateTime is not None:
        data.zeitpunkt = fhirpath.single([v2 for v1 in fhirpath_utils.toString([dateutil.parse(str(proc_performedDateTime.value))]) for v2 in fhirpath_utils.substring(v1,[0],[4])])

def i_procedures_data(proc, data):
    procedures_data(proc, data)
    proc_code = proc.code
    if proc_code is not None:
        for proc_code_coding in proc_code.coding or []:
            proc_code_coding_code = proc_code_coding.code
            if proc_code_coding_code is not None:
                data.code = proc_code_coding_code.value
            proc_code_coding_cs = proc_code_coding.system
            if proc_code_coding_cs is not None:
                data.codesystem = proc_code_coding_cs.value
            proc_code_coding_display = proc_code_coding.display
            if proc_code_coding_display is not None:
                data.operation = proc_code_coding_display.value
    proc_status = proc.status
    if proc_status is not None:
        data.status = proc_status.value

def i_immunizations_data(immunization, data):
    immunization_occurrenceDateTime = immunization.occurrenceDateTime
    if immunization_occurrenceDateTime is not None:
        data.zeitpunkt = fhirpath.single([v2 for v1 in fhirpath_utils.toString([dateutil.parse(str(immunization_occurrenceDateTime.value))]) for v2 in fhirpath_utils.substring(v1,[0],[4])])
    immunization_code = immunization.vaccineCode
    if immunization_code is not None:
        for immunization_code_coding in immunization_code.coding or []:
            immunization_code_coding_display = immunization_code_coding.display
            if immunization_code_coding_display is not None:
                data.name = immunization_code_coding_display.value
    for immunization_protocolApplied in immunization.protocolApplied or []:
        for immunization_protocolApplied_targetDisease in immunization_protocolApplied.targetDisease or []:
            for immunization_protocolApplied_targetDisease_coding in immunization_protocolApplied_targetDisease.coding or []:
                immunization_protocolApplied_targetDisease_coding_display = immunization_protocolApplied_targetDisease_coding.display
                if immunization_protocolApplied_targetDisease_coding_display is not None:
                    data_immunizationtarget = malac_vidi.immunizationtargetType()
                    data.immunizationtarget.append(data_immunizationtarget)
                    data_immunizationtarget.immunizationtarget = immunization_protocolApplied_targetDisease_coding_display.value

def i_careplan_data(careplan, data):
    cp_status = careplan.status
    if cp_status is not None:
        data.status = cp_status.value
    cp_intent = careplan.intent
    if cp_intent is not None:
        data.zweck = cp_intent.value
    for cp_cat in careplan.category or []:
        cp_cat_text = cp_cat.text
        if cp_cat_text is not None:
            data.kategorie = cp_cat_text.value
    cp_title = careplan.title
    if cp_title is not None:
        data.titel = cp_title.value
    cp_desc = careplan.description
    if cp_desc is not None:
        data.beschreibung = cp_desc.value
    cp_created = careplan.created
    if cp_created is not None:
        data.erstellt_am = fhirpath.single([v2 for v1 in fhirpath_utils.toString([dateutil.parse(str(cp_created.value))]) for v2 in fhirpath_utils.substring(v1,[0],[23])])
    cp_author = careplan.author
    if cp_author is not None:
        cp_author_disp = cp_author.display
        if cp_author_disp is not None:
            data.verantwortlich = cp_author_disp.value
    for cp_addr in careplan.addresses or []:
        cp_addr_disp = cp_addr.display
        if cp_addr_disp is not None:
            data.abklaerung = cp_addr_disp.value
    for cp_goal in careplan.goal or []:
        cp_goal_disp = cp_goal.display
        if cp_goal_disp is not None:
            data_ziel = malac_vidi.zielType()
            data.ziel.append(data_ziel)
            data_ziel.ziel = cp_goal_disp.value
    for cp_act in careplan.activity or []:
        for cp_act_outref in cp_act.outcomeReference or []:
            cp_act_outref_disp = cp_act_outref.display
            if cp_act_outref_disp is not None:
                data_task_aktivitaet = malac_vidi.task_aktivitaetType()
                data.task_aktivitaet.append(data_task_aktivitaet)
                data_task_aktivitaet.task_aktivitaet = cp_act_outref_disp.value

def i_tasks_data(task, data):
    task_id = task.id
    if task_id is not None:
        data.id = task_id.value
    task_status = task.status
    if task_status is not None:
        data.status = task_status.value
    task_intent = task.intent
    if task_intent is not None:
        data.intent = task_intent.value
    task_priority = task.priority
    if task_priority is not None:
        data.priority = task_priority.value
    task_desc = task.description
    if task_desc is not None:
        data.beschreibung = task_desc.value
    task_code = task.code
    if task_code is not None:
        for task_coding in task_code.coding or []:
            task_code_disp = task_coding.display
            if task_code_disp is not None:
                data.code = task_code_disp.value
    task_focus = task.focus
    if task_focus is not None:
        task_focus_disp = task_focus.display
        if task_focus_disp is not None:
            data.focus = task_focus_disp.value
    task_authored = task.authoredOn
    if task_authored is not None:
        data.authoredOn = fhirpath.single([v2 for v1 in fhirpath_utils.toString([dateutil.parse(str(task_authored.value))]) for v2 in fhirpath_utils.substring(v1,[0],[23])])
    task_modified = task.lastModified
    if task_modified is not None:
        data.lastModified = fhirpath.single([v2 for v1 in fhirpath_utils.toString([dateutil.parse(str(task_modified.value))]) for v2 in fhirpath_utils.substring(v1,[0],[23])])
    task_requester = task.requester
    if task_requester is not None:
        task_req_disp = task_requester.display
        if task_req_disp is not None:
            data.requester = task_req_disp.value
    for task_perfType in task.performerType or []:
        for task_perf_coding in task_perfType.coding or []:
            task_perf_disp = task_perf_coding.display
            if task_perf_disp is not None:
                data.performerType = task_perf_disp.value
    task_owner = task.owner
    if task_owner is not None:
        task_owner_disp = task_owner.display
        if task_owner_disp is not None:
            data.owner = task_owner_disp.value

def i_goals_data(goal, data):
    goal_id = goal.id
    if goal_id is not None:
        data.id = goal_id.value
    goal_status = goal.lifecycleStatus
    if goal_status is not None:
        data.lifecycleStatus = goal_status.value
    for goal_cat in goal.category or []:
        for cat_coding in goal_cat.coding or []:
            cat_disp = cat_coding.display
            if cat_disp is not None:
                data.category.append(cat_disp.value)
    goal_priority = goal.priority
    if goal_priority is not None:
        for prio_coding in goal_priority.coding or []:
            prio_disp = prio_coding.display
            if prio_disp is not None:
                data.priority = prio_disp.value
    goal_desc = goal.description
    if goal_desc is not None:
        goal_desc_txt = goal_desc.text
        if goal_desc_txt is not None:
            data.description = goal_desc_txt.value
    goal_subject = goal.subject
    if goal_subject is not None:
        subj_disp = goal_subject.display
        if subj_disp is not None:
            data.subject = subj_disp.value
    goal_start = goal.startDate
    if goal_start is not None:
        data.startDate = fhirpath.single(fhirpath_utils.toString([goal_start]))
    for goal_target in goal.target or []:
        target_measure = goal_target.measure
        if target_measure is not None:
            for tm_coding in target_measure.coding or []:
                tm_disp = tm_coding.display
                if tm_disp is not None:
                    data_target = malac_vidi.targetType()
                    data.target.append(data_target)
                    data_target.measure = tm_disp.value
    dq = goal_target.detailQuantity
    if dq is not None:
        dq_value = dq.value
        if dq_value is not None:
            data_target.detail_value = fhirpath.single(fhirpath_utils.toString([dq_value]))
        dq_comp = dq.comparator
        if dq_comp is not None:
            data_target.detail_comparator = dq_comp.value
        dq_unit = dq.unit
        if dq_unit is not None:
            data_target.detail_unit = dq_unit.value
        dq_system = dq.system
        if dq_system is not None:
            data_target.detail_system = dq_system.value
        dq_code = dq.code
        if dq_code is not None:
            data_target.detail_code = dq_code.value
    expr_by = goal.expressedBy
    if expr_by is not None:
        expr_disp = expr_by.display
        if expr_disp is not None:
            data.expressedBy = expr_disp.value
    for addr in goal.addresses or []:
        addr_disp = addr.display
        if addr_disp is not None:
            data.addresses.append(addr_disp.value)
    for note in goal.note or []:
        note_text = note.text
        if note_text is not None:
            data.note.append(note_text.value)

# output
# 1..1 result (boolean)
# 0..1 message with error details for human (string)
# 0..* match with (list)
#   0..1 equivalence/relationship
#   0..1 concept
#       0..1 system
#       0..1 version
#       0..1 code
#       0..1 display 
#       0..1 userSelected will always be false, because this is a translation
#   0..1 source (conceptMap url)
# TODO implement reverse
def translate(url=None, conceptMapVersion=None, code=None, system=None, version=None, source=None, coding=None, codeableConcept=None, target=None, targetsystem=None, reverse=None, silent=False)              -> dict [bool, str, list[dict[str, dict[str, str, str, str, bool], str]]]:
    start = sys_time.time()
    
    # start validation and recall of translate in simple from
    if codeableConcept:
        if isinstance(codeableConcept, str): 
            codeableConcept = r4.parseString(codeableConcept, silent)
        elif isinstance(codeableConcept, r4.CodeableConcept):
            pass
        else:
            raise BaseException("The codeableConcept parameter has to be a string or a CodeableConcept Object (called method as library)!")
        # the first fit will be returned, else the last unfitted value will be returned
        # TODO check translate params
        for one_coding in codeableConcept.get_coding():
            if (ret := translate(url=url, source=source, coding=one_coding, 
                                 target=target, targetsystem=targetsystem, 
                                 reverse=reverse, silent=True))['result']:
                return ret
        else: return ret
    elif coding:
        if isinstance(coding, str): 
            coding = r4.parseString(coding, silent)
        elif isinstance(coding, r4.Coding):
            pass
        else:
            raise BaseException("The coding parameter has to be a string or a Coding Object (called method as library)!")
        # TODO check translate params
        return translate(url=url,  source=source, code=coding.code.value, system=(coding.system.value if coding.system else None), 
                         target=target, targetsystem=targetsystem, 
                         reverse=reverse, silent=True)
    elif code:
        if not isinstance(code,str): 
            raise BaseException("The code parameter has to be a string!")
    elif target:
        if not isinstance(code,str): 
            raise BaseException("The target parameter has to be a string!")
    elif targetsystem:
        if not isinstance(code,str): 
            raise BaseException("The targetsystem parameter has to be a string!")
    else:
        raise BaseException("At least codeableConcept, coding, code, target or targetSystem has to be given!")
    # end validation and recall of translate in simplier from

    # look for any information from the one ore more generated conceptMaps into conceptMap_as_7dimension_dict
    match = []
    unmapped = []
    if url and url not in conceptMap_as_7dimension_dict.keys():
        print('   #ERROR# ConceptMap with URL "'+ url +'" is not loaded to this compiled conceptMap #ERROR#')
    else:
        for url_lvl in conceptMap_as_7dimension_dict:
            if url_lvl == "%" or not url or url_lvl == str(url or ""):#+str(("/?version=" and conceptMapVersion) or ""):
                for source_lvl in conceptMap_as_7dimension_dict[url_lvl]:
                    if source_lvl == "%" or not source or source_lvl == source:
                        for target_lvl in conceptMap_as_7dimension_dict[url_lvl][source_lvl]:
                            if target_lvl == "%" or not target or target_lvl == target:
                                for system_lvl in conceptMap_as_7dimension_dict[url_lvl][source_lvl][target_lvl]:
                                    if system_lvl == "%" or not system or system_lvl == system:#+str(("/?version=" and version) or ""):
                                        for targetsystem_lvl in conceptMap_as_7dimension_dict[url_lvl][source_lvl][target_lvl][system_lvl]:
                                            if targetsystem_lvl == "%" or not targetsystem or targetsystem_lvl == targetsystem:
                                                for code_lvl in conceptMap_as_7dimension_dict[url_lvl][source_lvl][target_lvl][system_lvl][targetsystem_lvl]:
                                                    if code_lvl == "|" or code_lvl == "~" or code_lvl == "#":
                                                        unmapped += conceptMap_as_7dimension_dict[url_lvl][source_lvl][target_lvl][system_lvl][targetsystem_lvl][code_lvl]
                                                    if code_lvl == "%" or not code or code_lvl == code:
                                                        match += conceptMap_as_7dimension_dict[url_lvl][source_lvl][target_lvl][system_lvl][targetsystem_lvl][code_lvl]                
                                                    
    if not match:
        for one_unmapped in unmapped:
            tmp_system = ""
            tmp_version = ""
            tmp_code = ""
            tmp_display = ""
            # replace all "|" values with to translated code (provided from https://hl7.org/fhir/R4B/conceptmap-definitions.html#ConceptMap.group.unmapped.mode)
            if one_unmapped["concept"]["code"].startswith("|"):
                tmp_system = system
                tmp_version = version
                tmp_code = one_unmapped["concept"]["code"][1:] + code
            # replace all "~" values with fixed code (provided from https://hl7.org/fhir/R4B/conceptmap-definitions.html#ConceptMap.group.unmapped.mode)
            elif one_unmapped["concept"]["code"].startswith("~"):
                if tmp := one_unmapped["concept"]["system"]: tmp_system = tmp 
                tmp_code = one_unmapped["concept"]["code"][1:]
                tmp_display = one_unmapped["concept"]["display"]
            elif one_unmapped["concept"]["code"].startswith("#"):
                # TODO detect recursion like conceptMapA -> conceptMapB -> ConceptMapA -> ...
                return translate(one_unmapped["concept"]["code"][1:], None, code, system, version, source, 
                                 coding, codeableConcept, target, targetsystem, reverse, silent)
            # prepare the match.concept results
            concept = {}
            if tmp_system: concept["system"] = tmp_system
            if tmp_version: concept["version"] = tmp_version
            if tmp_code: concept["code"] = tmp_code
            if tmp_display: concept["display"] = tmp_display

            # if the concept dict is empty, than skip this broken value and give a warning, that there is a empty group
            if concept == {}:
                # TODO do a warning, that it seems like the conceptmap is broken, because there is a empty group
                continue
            
            match.append({"relationship": one_unmapped["relationship"], 
                          "concept": concept,
                          "source": one_unmapped["source"]})

    # see if any match is not in R4 "unmatched" or "disjoint" and in R5 "not-related-to"
    result = False
    message = ""
    for one_match in match:
        if one_match["relationship"] not in ['not-related-to']:
            result = True 
            # for printing only, if no url was initially given use the conceptmap
            if not url:
                url = one_match["source"]

    if not silent:
        print('Translation in '+str(round(sys_time.time()-start,3))+' seconds for code "'+(code or "NONE")+'" with ConceptMap "'+url+'"')
    return {"result": result, "message": message, "match": match}

conceptMap_as_7dimension_dict = {}

def unpack_container(resource_container):
    if resource_container is None:
        return None
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

def translate_unmapped(url, code):
    if url == 'http://hl7.org/fhir/ConceptMap/special-oid2uri': return [{'uri': 'urn:oid:%s' % code}]
    if url == 'OIDtoURI': return [{'code': 'urn:oid:%s' % code}]
    if url == 'StructureMapGroupTypeMode': return [{'code': 'none'}]
    if url == 'AllergyCategoryMap': return [{'code': None}]
    raise BaseException('Code %s could not be mapped to any code in concept map %s and no exception defined' % (code, url))

def translate_single(url, code=None, coding=None, codeableConcept=None, out_type='code'):
    trans_out = translate(url=url, code=code, coding=coding, codeableConcept=codeableConcept, silent=True)
    matches = [match['concept'] for match in trans_out['match'] if match['relationship']=='equivalent' or match['relationship']=='equal']
    # if there are mutliple 'equivalent' or 'equal' matches and CodeableConcept is not the output param, than throw an error
    if len(matches) > 1:
        raise BaseException("There are multiple 'equivalent' or 'equal' matches in the results of the translate and output type is not CodeableConcept!")
    elif len(matches) == 0:
        matches = translate_unmapped(url=url, code=code)
    if out_type == "Coding":
        return malac_vidi.Coding(system=(malac_vidi.uri(value=matches[0]['system']) if "system" in matches[0] else None), 
                              version=(malac_vidi.string(value=matches[0]['version']) if "version" in matches[0] else None), 
                              code=(malac_vidi.string(value=matches[0]['code']) if "code" in matches[0] else None), 
                              display=(malac_vidi.string(value=matches[0]['display']) if "display" in  matches[0] else None), 
                              userSelected=(malac_vidi.string(value=matches[0]['userSelected']) if "userSelected" in matches[0] else None))
    else:
        return matches[0][out_type]

def translate_multi(url, code=None, coding=None, codeableConcept=None):
    trans_out = translate(url=url, code=code, coding=coding, codeableConcept=codeableConcept, silent=True)
    matches = [match['concept'] for match in trans_out['match'] if match['relationship']=='equivalent' or match['relationship']=='equal']
    return malac_vidi.CodeableConcept(coding=[malac_vidi.Coding(system=(malac_vidi.uri(value=matches[0]['system']) if "system" in matches[0] else None), 
                                                          version=(malac_vidi.string(value=matches[0]['version']) if "version" in matches[0] else None), 
                                                          code=(malac_vidi.string(value=matches[0]['code']) if "code" in matches[0] else None), 
                                                          display=(malac_vidi.string(value=matches[0]['display']) if "display" in  matches[0] else None), 
                                                          userSelected=(malac_vidi.string(value=matches[0]['userSelected']) if "userSelected" in matches[0] else None)
                                                          ) for match in matches])


if __name__ == "__main__":
    parser = init_argparse()
    args = parser.parse_args()
    transform(args.source, args.target)
