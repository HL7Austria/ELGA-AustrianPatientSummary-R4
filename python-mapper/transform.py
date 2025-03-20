import IpsToVidi_new
import os
import glob
import shutil

directory = os.path.dirname(os.path.abspath(__file__))
vidi_dir = os.path.join(directory, '..', 'vidi')
bundle_dir = os.path.join(directory, '..', 'fsh-generated', 'resources')
transformed_dir = os.path.join(directory, '..', 'vidi', 'scripts', 'tables')

# source = os.path.join(directory, '..', 'fsh-generated', 'resources', 'Bundle-APS-2-preventive-medical-checkup.json')
# target = os.path.join(directory, '..', 'fsh-generated', 'resources', 'Bundle-APS-1-no-problems-medication-allergies_vidi.json')

for source in list(glob.glob(bundle_dir + os.sep + 'Bundle-*.json')):
    target = source.replace(bundle_dir, transformed_dir).replace('.json', '_vidi.json')
    IpsToVidi_new.transform(source, target)

    html_filename = os.path.basename(source).replace('.json', '.html')
    vidi_filename = os.path.basename(target)

    shutil.copyfile(os.path.join(vidi_dir, 'index.html'), os.path.join(vidi_dir, html_filename))

    with open(os.path.join(vidi_dir, html_filename),'r',encoding='utf-8') as file:
        filecontent = file.read()

    filecontent = filecontent.replace('_ips_as_vidi_example.json', vidi_filename)

    with open(os.path.join(vidi_dir, html_filename), 'w', encoding='utf-8') as file:
        file.write(filecontent)

