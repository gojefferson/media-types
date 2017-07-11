import json
import xml.etree.ElementTree as ET

from extensions import EXTENSIONS
from names import FileName

READABLE_MAPPINGS = {

    # Word formats
    'application/msword': FileName.MS_WORD,
    'application/vnd.ms-word.template.macroEnabled.12': FileName.MS_WORD,
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': FileName.MS_WORD,
    'application/msword2': FileName.MS_WORD,
    'application/vnd.ms-word.document.macroenabled.12': FileName.MS_WORD,
    'application/vnd.ms-word.template.macroenabled.12': FileName.MS_WORD,

    # Email containers
    'application/vnd.ms-outlook-pst': FileName.EMAIL_CONTAINER,
    'application/mbox': FileName.EMAIL_CONTAINER,

    # Emails
    'message/x-emlx': FileName.EMAIL,
    'application/vnd.ms-outlook': FileName.EMAIL,

    # Archives
    'application/gzip': FileName.ZIPFILE,

    # CSV
    'text/csv': FileName.CSV,

    # PowerPoint
    'application/vnd.ms-powerpoint': FileName.POWERPOINT,
    'application/vnd.ms-powerpoint.presentation.macroenabled.12': FileName.POWERPOINT,

    # Excel
    'application/vnd.ms-excel': FileName.SPREADSHEET,

}

if __name__ == '__main__':
    types = {
        'mime-types': {},
        'extensions': {}
    }

    tree = ET.parse('tika/tika-types.xml')
    root = tree.getroot()

    for node in root.getchildren():
        globs = [g.get('pattern') for g in node.getchildren() if g.tag == 'glob']
        mime_type = node.get('type').lower()
        group = mime_type.split('/')[0].capitalize()
        types['mime-types'][mime_type] = {
            'Extensions': globs,
            'Tika': True,
            'Human Readable Name': READABLE_MAPPINGS.get(mime_type, group),
            'Group': group
        }

    for k, v in EXTENSIONS.items():
        for glob_pattern in v:
            types['extensions'][glob_pattern] = k

    with open('types.json', 'wt') as write_file:
        write_file.write(json.dumps(types, sort_keys=True, indent=4))
