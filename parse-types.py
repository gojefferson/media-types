import json
import xml.etree.ElementTree as ET

MS_WORD = 'Word Document'
EMAIL = 'Email'
ZIPFILE = 'Archive'
CSV = 'CSV'
POWERPOINT = 'PowerPoint'
EMAIL_CONTAINER = 'Email Archive'
SPREADSHEET = 'Excel'

EXTENSIONS = {
    'No Mapping': [
        '*-gz', '*.123', '*.3dml', '*.3fr', '*.3g2', '*.3gp', '*.4th', '*.7z', '*.BAS', '*.Bas',
        '*.C', '*.CBL', '*.CLS', '*.COB', '*.CPP', '*.Cbl', '*.Cls', '*.Cob', '*.F', '*.FRM',
        '*.Frm', '*.H', '*.HPP', '*.MF', '*.MYD', '*.MYI', '*.PAS', '*.S', '*.a', '*.aab',
        '*.aam', '*.aart', '*.aas', '*.abw', '*.ac', '*.acc', '*.ace', '*.acfm', '*.acu',
        '*.acutc',
        '*.ad', '*.ad.txt', '*.ada', '*.adb', '*.adoc', '*.adoc.txt', '*.adp', '*.ads', '*.aep',
        '*.aet', '*.afm', '*.afp', '*.ai', '*.aif', '*.aifc', '*.air', '*.aj', '*.al', '*.am',
        '*.amfm', '*.ami', '*.amr', '*.anpa', '*.apk', '*.applescript', '*.application', '*.apr',
        '*.ar', '*.arj', '*.arw', '*.as', '*.asc', '*.asciidoc', '*.asf', '*.asice', '*.asics',
        '*.asm', '*.asnd', '*.aso', '*.asp', '*.aspx', '*.asx', '*.atc', '*.atom', '*.atomcat',
        '*.atomsvc', '*.atx', '*.au', '*.aw', '*.awk', '*.axx', '*.azf', '*.azs', '*.azw',
        '*.bas', '*.bash', '*.bat', '*.bay', '*.bcpio', '*.bdf', '*.bdm', '*.bh2', '*.bib',
        '*.bibtex', '*.bin', '*.bmi', '*.book', '*.box', '*.boz', '*.bpg', '*.bpk', '*.bpm',
        '*.btif', '*.bz', '*.bz2', '*.c', '*.c++', '*.c4d', '*.c4f', '*.c4g', '*.c4p', '*.c4u',
        '*.cab', '*.cap', '*.car', '*.cat', '*.cbl', '*.cbor', '*.cc', '*.cct', '*.ccxml',
        '*.cdbcmsg', '*.cdf', '*.cdkey', '*.fff', '*.fg5', '*.fgd', '*.fh', '*.fh10', '*.fh11',
        '*.fh12', '*.fh4', '*.fh40', '*.fh5', '*.fh50', '*.fh7', '*.fh8', '*.fh9', '*.fhc',
        '*.fig', '*.fit', '*.fits', '*.flc', '*.fli', '*.flo', '*.flv', '*.flw', '*.flx', '*.fly',
        '*.fm', '*.fn', '*.fnc', '*.fo', '*.for', '*.fp7', '*.fpx', '*.frame', '*.frm', '*.fsc',
        '*.fst', '*.ft', '*.ft10', '*.ft11', '*.ft12', '*.ft7', '*.ft8', '*.ft9', '*.ftc',
        '*.fti', '*.fts', '*.fv', '*.fvt', '*.fzs', '*.g', '*.g3', '*.gac', '*.gdl', '*.geo',
        '*.gex', '*.ggb', '*.ggt', '*.ghf', '*.gif', '*.gim', '*.gmx', '*.gnucash', '*.gnumeric',
        '*.go', '*.gph', '*.gqf', '*.gqs', '*.gram', '*.grb', '*.grb1', '*.grb2', '*.gre',
        '*.grm', '*.groovy', '*.grv', '*.grxml', '*.gsf', '*.gtar', '*.gtm', '*.gtw', '*.gv',
        '*.gz', '*.h', '*.h++', '*.h261', '*.h263', '*.h264', '*.h5', '*.haml', '*.hbci', '*.hdf',
        '*.he5', '*.hfa', '*.hh', '*.hlp', '*.hp', '*.hpgl', '*.hpid', '*.hpp', '*.hps', '*.hqx',
        '*.hs', '*.htke', '*.htm', '*.html', '*.hvd', '*.hvp', '*.hvs', '*.hx', '*.hxx', '*.i3',
        '*.ibooks', '*.icc', '*.ice', '*.icm', '*.icns', '*.ico', '*.ics', '*.idl', '*.ief',
        '*.ifb', '*.ifm', '*.ig', '*.iges', '*.igl', '*.igs', '*.igx', '*.ihtml', '*.iif',
        '*.iiq', '*.imp', '*.ims', '*.in', '*.indd', '*.ini', '*.inx', '*.ipa', '*.ipk', '*.irm',
        '*.irp', '*.iso', '*.iso19139', '*.itk', '*.itp', '*.ivp', '*.ivu', '*.j2c', '*.jad',
        '*.jam', '*.jar', '*.java', '*.jb2', '*.jbig2', '*.jfi', '*.jfif', '*.jif', '*.jisp',
        '*.jl', '*.jlt', '*.jmx', '*.jng', '*.jnilib', '*.jnlp', '*.joda', '*.jp2', '*.jpe',
        '*.jpf', '*.jpgm', '*.jpgv', '*.jpm', '*.js', '*.json', '*.jsp', '*.junit', '*.jx',
        '*.k25', '*.kar', '*.karbon', '*.kdc', '*.key', '*.kfo', '*.kia', '*.kil', '*.kml',
        '*.kmz', '*.kne', '*.knp', '*.kon', '*.kpr', '*.kpt', '*.ksp', '*.ktr', '*.ktz', '*.kwd',
        '*.kwt', '*.l', '*.latex', '*.lbd', '*.lbe', '*.les', '*.less', '*.lha', '*.lhs',
        '*.link66', '*.lisp', '*.list', '*.list3820', '*.listafp', '*.log', '*.lostxml',
        '*.lrf', '*.lrm', '*.lsp', '*.ltf', '*.lua', '*.lvp', '*.lwp', '*.lzh', '*.m', '*.m13',
        '*.m14', '*.m1v', '*.m2a', '*.m2v', '*.m3', '*.m3a', '*.m3u', '*.m4', '*.m4a', '*.m4b',
        '*.m4u', '*.m4v', '*.ma', '*.mag', '*.maker', '*.man', '*.manifest', '*.markdown',
        '*.mat', '*.mathml', '*.mb', '*.mbk', '*.mbox', '*.mc1', '*.mcd', '*.mcurl', '*.md',
        '*.mdi', '*.mdtext', '*.me', '*.mef', '*.mesh', '*.meta', '*.mf', '*.mfm', '*.mg',
        '*.mgz', '*.mht', '*.mhtml', '*.mid', '*.mif', '*.mime', '*.mj2', '*.mjp2', '*.mka',
        '*.mkd', '*.mkv', '*.ml', '*.mli', '*.mlp', '*.mmap', '*.mmas', '*.mmat', '*.mmd',
        '*.mmf', '*.mmmp', '*.mmp', '*.mmpt', '*.mmr', '*.mng', '*.mny', '*.mobi', '*.mod',
        '*.mos', '*.mpga', '*.mpkg', '*.mpm', '*.mpn', '*.mpp', '*.mpt', '*.mpx', '*.mpy',
        '*.mqy', '*.mrc', '*.mrw', '*.ms', '*.mscml', '*.mseed', '*.mseq', '*.msf', '*.msg',
        '*.msh', '*.msi', '*.msl', '*.msp', '*.mst', '*.msty', '*.mts', '*.mus', '*.musicxml',
        '*.mvb', '*.mwf', '*.mxf', '*.mxl', '*.mxml', '*.mxs', '*.mxu', '*.n-gage', '*.n3',
        '*.nb', '*.nc', '*.ncx', '*.nef', '*.ngdat', '*.nitf', '*.nlu', '*.nml', '*.nnd',
        '*.nns', '*.nnw', '*.npx', '*.nrw', '*.nsf', '*.ntf', '*.oa2', '*.oa3', '*.oas',
        '*.obd', '*.ocaml', '*.oda', '*.odb', '*.odc', '*.odf', '*.odft', '*.odg', '*.odi',
        '*.odp', '*.ods', '*.odt', '*.oga', '*.ogg', '*.ogm', '*.ogv', '*.ogx', '*.one',
        '*.onepkg', '*.onetmp', '*.onetoc', '*.onetoc2', '*.opf', '*.oprc', '*.opus', '*.orf',
        '*.org', '*.osf', '*.osfpvg', '*.ost', '*.otc', '*.otf', '*.otg', '*.oth', '*.oti',
        '*.otm', '*.otp', '*.ots', '*.ott', '*.owl', '*.oxps', '*.oxt', '*.p', '*.p10', '*.p12',
        '*.p7b', '*.p7c', '*.p7m', '*.p7r', '*.p7s', '*.pack', '*.pas', '*.patch', '*.pbd',
        '*.pbm', '*.pcap', '*.pcf', '*.pcl', '*.pclxl', '*.pct', '*.pcurl', '*.pcx', '*.pdb',
        '*.pef', '*.pen', '*.perl', '*.pfa', '*.pfb', '*.pfm', '*.pfr', '*.pfx',
        '*.pgm', '*.pgn', '*.pgp', '*.php', '*.php3', '*.php4', '*.pic', '*.pict', '*.pkg',
        '*.pki', '*.pkipath', '*.pl', '*.plb', '*.plc', '*.plf', '*.pls', '*.pm', '*.pml',
        '*.png', '*.pnm', '*.pod', '*.pom', '*.portpkg', '*.pot', '*.potm', '*.potx',
        '*.pp', '*.ppa', '*.ppam', '*.ppd', '*.ppj', '*.ppm', '*.pps', '*.ppsm', '*.ppsx',
        '*.ppz', '*.pqa', '*.prc', '*.pre', '*.prf', '*.pro', '*.project', '*.properties',
        '*.prt', '*.ps', '*.psb', '*.psd', '*.psf', '*.pst', '*.ptid', '*.pub', '*.pvb',
        '*.pwn', '*.pxn', '*.py', '*.pya', '*.pyv', '*.qam', '*.qbo', '*.qfx', '*.qps',
        '*.qpw', '*.qt', '*.qwd', '*.qwt', '*.qxb', '*.qxd', '*.qxl', '*.qxt', '*.r', '*.r3d',
        '*.ra', '*.raf', '*.ram', '*.rar', '*.ras', '*.raw', '*.rb', '*.rcprofile', '*.rdf',
        '*.rdz', '*.rep', '*.res', '*.rest', '*.restx', '*.rexx', '*.rgb', '*.rif', '*.rl',
        '*.rlc', '*.rld', '*.rm', '*.rmi', '*.rmp', '*.rms', '*.rnc', '*.rng', '*.rnx',
        '*.roff', '*.roles', '*.rpm', '*.rpss', '*.rpst', '*.rq', '*.rs', '*.rsd', '*.rss',
        '*.rst', '*.rtf', '*.rtx', '*.rw2', '*.rwz', '*.s', '*.s7m', '*.sa7', '*.saf', '*.sas',
        '*.sas7bacs', '*.sas7baud', '*.sas7bbak', '*.sas7bcat', '*.sas7bdat', '*.sas7bdmd',
        '*.sas7bfdb', '*.sas7bitm', '*.sas7bmdb', '*.sas7bndx', '*.sas7bpgm', '*.sas7bput',
        '*.sas7butl', '*.sas7bvew', '*.sbml', '*.sc', '*.sc7', '*.scala', '*.scd', '*.scm',
        '*.scq', '*.scs', '*.scurl', '*.sd2', '*.sd7', '*.sda', '*.sdc', '*.sdd', '*.sdkd',
        '*.sdkm', '*.sdp', '*.sdw', '*.sed', '*.see', '*.seed', '*.sema', '*.semd', '*.semf',
        '*.ser', '*.setpay', '*.setreg', '*.sf7', '*.sfd-hdstx', '*.sfdu', '*.sfs', '*.sgl',
        '*.sgm', '*.sgml', '*.sh', '*.shar', '*.shf', '*.shp', '*.shw', '*.si7', '*.sig',
        '*.silo', '*.sis', '*.sisx', '*.sit', '*.sitx', '*.skd', '*.skm', '*.skp', '*.skt',
        '*.sldasm', '*.slddrw', '*.sldm', '*.sldprt', '*.sldx', '*.slt', '*.sm7', '*.smf',
        '*.smi', '*.smil', '*.sml', '*.snd', '*.snf', '*.so', '*.sp7', '*.spc', '*.spf',
        '*.spl', '*.spot', '*.spp', '*.spq', '*.spx', '*.sql', '*.sr2', '*.sr7', '*.src',
        '*.srf', '*.srl', '*.srx', '*.ss7', '*.sse', '*.ssf', '*.ssml', '*.st', '*.st7',
        '*.stc', '*.std', '*.stf', '*.sti', '*.stk', '*.stl', '*.str', '*.stw', '*.stx',
        '*.su7', '*.sus', '*.susp', '*.sv4cpio', '*.sv4crc', '*.sv7', '*.svd', '*.svg',
        '*.svgz', '*.swa', '*.swf', '*.swi', '*.sxc', '*.sxd', '*.sxg', '*.sxi', '*.sxm',
        '*.sxw', '*.sz', '*.t', '*.tao', '*.tar', '*.tbz', '*.tbz2', '*.tcap', '*.tcl',
        '*.tcsh', '*.teacher', '*.tex', '*.texi', '*.texinfo', '*.text', '*.tfm', '*.tgz',
        '*.thmx', '*.tif', '*.tiff', '*.tk', '*.tld', '*.tmo', '*.toast', '*.torrent',
        '*.tpl', '*.tpt', '*.tr', '*.tra', '*.trm', '*.tsd', '*.tsv', '*.ttc', '*.ttf',
        '*.twd', '*.twds', '*.txd', '*.txf', '*.txt', '*.types', '*.u32', '*.uc2', '*.udeb',
        '*.ufd', '*.ufdl', '*.umj', '*.unityweb', '*.uoml', '*.uri', '*.uris', '*.urls',
        '*.ustar', '*.utz', '*.uu', '*.v', '*.vb', '*.vbs', '*.vcd', '*.vcf', '*.vcg',
        '*.vcs', '*.vcx', '*.vhd', '*.vhdl', '*.vis', '*.viv', '*.vm', '*.vmdk', '*.vor',
        '*.vox', '*.vrml', '*.vsd', '*.vsdm', '*.vsdx', '*.vsf', '*.vsl', '*.vss', '*.vssm',
        '*.vssx', '*.vst', '*.vstm', '*.vstx', '*.vsw', '*.vtt', '*.vtu', '*.vxml', '*.w3d',
        '*.w60', '*.wad', '*.war', '*.wav', '*.wax', '*.wb1', '*.wb2', '*.wb3', '*.wbmp',
        '*.wbs', '*.wbxml', '*.wcm', '*.wdb', '*.webarchive', '*.webm', '*.webp', '*.wks',
        '*.wm', '*.wma', '*.wmd', '*.wmf', '*.wml', '*.wmlc', '*.wmls', '*.wmlsc', '*.wmv',
        '*.wmx', '*.wmz', '*.wp', '*.wp5', '*.wp6', '*.wp61', '*.wpd', '*.wpl', '*.wps',
        '*.wpt', '*.wqd', '*.wri', '*.wrl', '*.wsdd', '*.wsdl', '*.wspolicy', '*.wtb',
        '*.wvx', '*.x32', '*.x3d', '*.x3f', '*.xap', '*.xar', '*.xargs', '*.xbap', '*.xbd',
        '*.xbm', '*.xcat', '*.xcf', '*.xconf', '*.xdm', '*.xdp', '*.xdw', '*.xegrm', '*.xenc',
        '*.xer', '*.xfdf', '*.xfdl', '*.xgrm', '*.xht', '*.xhtml', '*.xhvml', '*.xif', '*.xla',
        '*.xlam', '*.xlc', '*.xld', '*.xlex', '*.xll', '*.xlm', '*.xlog', '*.xlr', '*.xlt',
        '*.xltm', '*.xltx', '*.xlw', '*.xmap', '*.xmind', '*.xml', '*.xmp', '*.xo', '*.xop',
        '*.xpi', '*.xpm', '*.xport', '*.xpr', '*.xps', '*.xpt', '*.xpw', '*.xpx', '*.xq',
        '*.xquery', '*.xroles', '*.xsamples', '*.xsd', '*.xsl', '*.xslfo', '*.xslt', '*.xsm',
        '*.xsp', '*.xspf', '*.xul', '*.xvm', '*.xvml', '*.xwd', '*.xweb', '*.xwelcome', '*.xyz',
        '*.xz', '*.y', '*.yaml', '*.z', '*.zaz', '*.zip', '*.zir', '*.zirz', '*.zmm', '*.zoo',
        '.htaccess', 'INSTALL', 'KEYS', '^owl$', '^rdf$', 'a_*.txt', 'abs-linkmap',
        'abs-menulinks', 'i_*.txt', 's_*.txt', '*.cdx', '*.cdxml', '*.cdy', '*.cer', '*.cfc',
        '*.cfg', '*.cfm', '*.cfml', '*.cgi', '*.cgm', '*.chat', '*.chm', '*.chrt', '*.cif',
        '*.cii', '*.cil', '*.cl', '*.cla', '*.class', '*.classpath', '*.clj', '*.clkk',
        '*.clkp', '*.clkt', '*.clkw', '*.clkx', '*.clp', '*.cls', '*.cmc', '*.cmd', '*.cmdf',
        '*.cml', '*.cmp', '*.cmx', '*.cob', '*.cod', '*.coffee', '*.com', '*.conf', '*.config',
        '*.cpio', '*.cpp', '*.cpt', '*.cr2', '*.crd', '*.crl', '*.crt', '*.crw', '*.crx',
        '*.cs', '*.csh', '*.csml', '*.csp', '*.css', '*.cst', '*.csv', '*.cu', '*.curl',
        '*.cwiki', '*.cwk', '*.cww', '*.cxt', '*.cxx', '*.d', '*.daf', '*.data', '*.dataless',
        '*.davmount', '*.dbf', '*.dcl', '*.dcr', '*.dcs', '*.dcurl',
        '*.dd2', '*.ddd', '*.deb', '*.def', '*.deploy', '*.der', '*.dex', '*.dfac', '*.dib',
        '*.dif', '*.diff', '*.dir', '*.dis', '*.dist', '*.distz', '*.dita', '*.ditamap',
        '*.ditaval', '*.djv', '*.djvu', '*.dll', '*.dmg', '*.dmp', '*.dms', '*.dna', '*.dng',
        '*.do', '*.dp', '*.dpg', '*.dpr', '*.drc', '*.drf', '*.dsc', '*.dta', '*.dtb', '*.dtd',
        '*.dts', '*.dtshd', '*.dump', '*.dvi', '*.dwf', '*.dwfx', '*.dwg', '*.dxb', '*.dxf',
        '*.dxp', '*.dxr', '*.e', '*.ear', '*.ecelp4800', '*.ecelp7470', '*.ecelp9600', '*.ecma',
        '*.edm', '*.edx', '*.efif', '*.egrm', '*.ei6', '*.el', '*.elc', '*.emf', '*.emlx',
        '*.emma', '*.emz', '*.enr', '*.ent', '*.enw', '*.eol', '*.eot', '*.eps', '*.epsf',
        '*.epsi', '*.epub', '*.erf', '*.erl', '*.es3', '*.esf', '*.et3', '*.etx', '*.exp',
        '*.ext', '*.ez', '*.ez2', '*.ez3', '*.f', '*.f4v', '*.f77', '*.f90', '*.fb2', '*.fbs',
        '*.fdf', '*.fe_launch', '*.mpc',
    ],
    'Audio': [
        '*.aac',
        '*.aiff',
        '*.flac',
        '*.midi',
    ],
    'Executables': [
        '*.exe',
    ],
    EMAIL: [
        '*.eml',
    ],
    'Code': [
        'Makefile', 'README',
    ],
    CSV: [
        '*.csv',
    ],
    'PDF': [
        '*.pdf',
    ],
    'Video': [
        '*.avi', '*.mov', '*.movie', '*.mp2', '*.mp2a', '*.mp3', '*.mp4', '*.mp4a', '*.mp4s',
        '*.mp4v', '*.mpe', '*.mpeg', '*.mpg', '*.mpg4',
    ],
    'Image': [
        '*.bmp', '*.jpeg', '*.jpg', '*.ptx', '*.svg'
    ],
    MS_WORD: [
        '*.doc', '*.docm', '*.docx', '*.dot', '*.dotm', '*.dotx',
    ],
    'Document': [
        '*.pages',
    ],
    'Database': [
        '*.mdb', '*.sqlite', '*.db', '*.dbase', '*.dbase3',
    ],
    POWERPOINT: [
        '*.ppt', '*.pptm', '*.pptx',
    ],
    SPREADSHEET: [
        '*.numbers', '*.xls', '*.xlsb', '*.xlsm', '*.xlsx',
    ]
}

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
    'application/mbox': EMAIL_CONTAINER,

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
