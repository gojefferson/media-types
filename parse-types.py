import json
import xml.etree.ElementTree as ET

MS_WORD = 'Word Document'
EMAIL = 'Email'
ZIPFILE = 'Archive'
CSV = 'CSV'
POWERPOINT = 'PowerPoint'
EMAIL_CONTAINER = 'Email Archive'
SPREADSHEET = 'Excel'

READABLE_MAPPINGS = {

    # Word formats
    'application/msword': MS_WORD,
    'application/vnd.ms-word.template.macroEnabled.12': MS_WORD,
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': MS_WORD,
    'application/msword2': MS_WORD,
    'application/vnd.ms-word.document.macroenabled.12': MS_WORD,
    'application/vnd.ms-word.template.macroenabled.12': MS_WORD,

    # Email containers
    'application/vnd.ms-outlook-pst': EMAIL_CONTAINER,

    # Emails
    'message/x-emlx': EMAIL,
    'application/vnd.ms-outlook': EMAIL,

    # Archives
    'application/gzip': ZIPFILE,

    # CSV
    'text/csv': CSV,

    # PowerPoint
    'application/vnd.ms-powerpoint': POWERPOINT,
    'application/vnd.ms-powerpoint.presentation.macroenabled.12': POWERPOINT,

    # Excel
    'application/vnd.ms-excel': SPREADSHEET,

}

if __name__ == '__main__':
    types = {}

    tree = ET.parse('tika/tika-types.xml')
    root = tree.getroot()

    for node in root.getchildren():
        globs = [g.get('pattern') for g in node.getchildren() if g.tag == 'glob']
        mime_type = node.get('type').lower()
        group = mime_type.split('/')[0].capitalize()
        types[mime_type] = {
            'Extensions': globs,
            'Tika': True,
            'Human Readable Name': READABLE_MAPPINGS.get(mime_type, group),
            'Group': group
        }

    with open('types.json', 'wt') as write_file:
        write_file.write(json.dumps(types, sort_keys=True, indent=4))
