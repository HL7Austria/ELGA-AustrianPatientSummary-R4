import IpsToVidi
import os
import glob
import shutil

# directory of this script: ./python-mapper/
directory = os.path.dirname(os.path.abspath(__file__))
# directory of sushi-generated resources: ./../fsh-generated/resources/
bundle_dir = os.path.join(directory, '..', 'fsh-generated', 'resources')
# directory of IG publisher output: ./../output/
output_dir = os.path.join(directory, '..', 'output')
# directory of VIDi files: ./../vidi/
vidi_dir = os.path.join(directory, '..', 'vidi')
# directory containing the transformed json (FHIR Bundle -> VIDi tables)
transformed_dir = os.path.join(vidi_dir, 'scripts', 'tables')

# source = os.path.join(directory, '..', 'fsh-generated', 'resources', 'Bundle-APS-2-preventive-medical-checkup.json')
# target = os.path.join(directory, '..', 'fsh-generated', 'resources', 'Bundle-APS-1-no-problems-medication-allergies_vidi.json')

# for each Bundle resource
for fhir_bundle_with_path in list(glob.glob(bundle_dir + os.sep + 'Bundle-*.json')):
    # strip the whole path and retain filename only, e.g. Bundle-aps-1.json
    fhir_bundle_basename = os.path.basename(fhir_bundle_with_path)
    # HTML file which has been created by IG publisher, e.g. Bundle-aps-1.html
    ig_bundle_basename = fhir_bundle_basename.replace('.json', '.html')
    ig_bundle_with_path = os.path.join(output_dir, ig_bundle_basename)

    # HTML file displaying VIDi content
    vidi_html_basename = fhir_bundle_basename.replace('.json', '.vidi.html')
    vidi_html_with_path = os.path.join(vidi_dir, vidi_html_basename)
    # file containing the info transformed for VIDi
    vidi_tables_basename = fhir_bundle_basename.replace('.json', '_vidi.json')
    vidi_tables_with_path = os.path.join(transformed_dir, vidi_tables_basename)

    target = fhir_bundle_with_path.replace(bundle_dir, transformed_dir).replace('.json', '_vidi.json')
    # transform FHIR bundle to VIDi tables
    IpsToVidi.transform(fhir_bundle_with_path, vidi_tables_with_path)

    # copy VIDi template HTML file and rename it accordingly
    shutil.copyfile(os.path.join(vidi_dir, 'index.html'), vidi_html_with_path)

    # within corresponding VIDi HTML file set link to corresponding VIDi tables file
    with open(vidi_html_with_path,'r',encoding='utf-8') as file:
        filecontent = file.read()

    filecontent = filecontent.replace('_ips_as_vidi_example.json', vidi_tables_basename)

    with open(vidi_html_with_path, 'w', encoding='utf-8') as file:
        file.write(filecontent)

    # activate tab-link in corresponding HTML-output file
    with open(ig_bundle_with_path,'r',encoding='utf-8') as file:
        filecontent = file.read()

    filecontent = filecontent.replace('<!-- <a href="' + vidi_html_basename + '">VIDi</a> -->', '<a href="' + vidi_html_basename + '">VIDi</a>')

    with open(ig_bundle_with_path, 'w', encoding='utf-8') as file:
        file.write(filecontent)

