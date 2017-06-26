import csv
import json
import os
import xml.etree.ElementTree as ET

files = [
    'application.csv',
    'audio.csv',
    'font.csv',
    'image.csv',
    'message.csv',
    'model.csv',
    'multipart.csv',
    'text.csv',
    'video.csv'
]


mappings = {
    'application/msword': 'Word',
    'application/vnd.ms-word.template.macroEnabled.12': 'Word',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'Word',
}


if __name__ == '__main__':
    types = {}
    for file in files:
        fpath = os.path.join(os.getcwd(), 'iana', file)
        with open(fpath) as _file:
            reader = csv.DictReader(_file)
            mime_types = [r for r in reader]
            group = file.split('.')[0].capitalize()
            for type_obj in mime_types:
                type_obj['group'] = group
                del type_obj['Name']
                del type_obj['Reference']
                key = type_obj['Template'].lower()
                del type_obj['Template']
                type_obj['IANA'] = True
                types[key] = type_obj

    tree = ET.parse('tika/tika-types.xml')
    root = tree.getroot()

    for node in root.getchildren():
        print(f'type: {node.get("type")}')
        print(f'in types?: {node.get("type") in types.keys()}')
        globs = [g.get('pattern') for g in node.getchildren() if g.tag == 'glob']
        mime_type = node.get('type').lower()
        if mime_type in types.keys():
            types['extensions'] = globs
            types['Tika'] = True
        else:
            types[mime_type] = {
                'extensions': globs,
                'Tika': True,
                'group': mime_type.split('/')[0].capitalize()
            }

    with open('types.json', 'wt') as write_file:
        write_file.write(json.dumps(types, sort_keys=True, indent=4))
