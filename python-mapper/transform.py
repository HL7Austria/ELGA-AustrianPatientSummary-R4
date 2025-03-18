import IpsToVidi_new
import os

directory = os.path.dirname(os.path.abspath(__file__))
print(os.path.join(directory, '..', 'fsh-generated', 'resources', 'Bundle-APS-1-no-problems-medication-allergies.json'))

source = os.path.join(directory, '..', 'fsh-generated', 'resources', 'Bundle-APS-2-preventive-medical-checkup.json')
target = os.path.join(directory, '..', 'fsh-generated', 'resources', 'Bundle-APS-1-no-problems-medication-allergies_vidi.json')


IpsToVidi_new.transform(source, target)