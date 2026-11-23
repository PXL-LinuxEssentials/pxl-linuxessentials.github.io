#!/usr/bin/env python3
"""Genereert de figuren (SVG) van de cursus: boomdiagrammen, schema's en grapjes.
Gebruik: python bouw/figuren.py   (schrijft naar cursus/<hoofdstuk>/assets/)"""
import os, html
HERE = os.path.dirname(os.path.abspath(__file__))
COURSE = os.path.join(HERE, '..', 'cursus')
esc = html.escape
FONT = "system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif"
MONO = "ui-monospace,'Cascadia Code',Consolas,'DejaVu Sans Mono',monospace"
def tw(s, fs): return len(s) * fs * 0.58

# ------------------------------------------------------------------ bomen
STY = {  # fill, stroke, text
 'root': ('#334155', '#334155', '#ffffff'),
 'd': ('#e7eef8', '#a9bddb', '#1f3a5f'),
 'u1': ('#dff1ed', '#98cfc6', '#17504a'),
 'u2': ('#ece8f7', '#bdb2e0', '#43366f'),
 'f': ('#ffffff', '#cbd5e1', '#475569'),
 'hot': ('#fdf0d3', '#e0a53a', '#6b4a06'),
 'del': ('#fbe4e1', '#e19a92', '#8a2d22'),
}
class N:
    def __init__(s, spec, kids):
        s.hot = spec.startswith('*'); s.dele = spec.startswith('~')
        spec = spec.lstrip('*~')
        s.isdir = spec.endswith('/') or bool(kids)
        s.label = spec.rstrip('/') if spec != '/' else '/'
        s.kids = kids; s.x = s.y = s.w = s.sw = 0
        s.kind = 'root' if spec == '/' else 'f'
        if s.isdir and spec != '/': s.kind = 'd'
        if s.label == 'student': s.kind = 'u1'
        if s.label == 'teacher': s.kind = 'u2'
        if s.hot: s.kind = 'hot'
        if s.dele: s.kind = 'del'
def T(spec, *kids): return N(spec, [k for k in kids])
FS = 14; NH = 32; GAP = 14; ROW = 62
def lay(n, d=0):
    n.w = tw(n.label, FS) + 24 + (0 if n.kind != 'f' else 0)
    n.d = d
    for k in n.kids: lay(k, d + 1)
    if not n.kids: n.sw = n.w
    else:
        n.sw = max(n.w, sum(k.sw for k in n.kids) + GAP * (len(n.kids) - 1))
def place(n, x0):
    if not n.kids: n.x = x0 + n.sw / 2
    else:
        cx = x0 + (n.sw - (sum(k.sw for k in n.kids) + GAP * (len(n.kids) - 1))) / 2
        for k in n.kids: place(k, cx); cx += k.sw + GAP
        n.x = (n.kids[0].x + n.kids[-1].x) / 2
    n.y = n.d * ROW
def draw(n, out, oy):
    for k in n.kids:
        ym = n.y + oy + NH + (ROW - NH) / 2
        out.append('<path d="M%.1f %.1f V%.1f H%.1f V%.1f" fill="none" stroke="#c3cedc" stroke-width="2" stroke-linejoin="round"/>' % (n.x, n.y + oy + NH, ym, k.x, k.y + oy))
        draw(k, out, oy)
    f, s, t = STY[n.kind]
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="9" fill="%s" stroke="%s" stroke-width="1.6"/>' % (n.x - n.w / 2, n.y + oy, n.w, NH, f, s))
    w = 700 if n.kind in ('d', 'u1', 'u2', 'root', 'hot') and n.isdir else 500
    out.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-family="%s" font-size="%d" font-weight="%d" fill="%s"%s>%s</text>' % (n.x, n.y + oy + NH / 2 + 5, FONT if n.kind != 'f' else MONO, FS if n.kind != 'f' else 13, w, t, ' text-decoration="line-through"' if n.dele else '', esc(n.label)))
def depth(n): return 1 + max([depth(k) for k in n.kids] or [0])
def tree_panel(root, title=None, cmd=None):
    lay(root); place(root, 0)
    w = root.sw; h = depth(root) * ROW - (ROW - NH)
    return root, w, h
def panels_svg(panels, bridge=None):
    """panels: lijst (titel, cmd, root). bridge: tekst tussen twee panelen."""
    PAD = 22; HEAD = 34
    built = [(t, c, ) + tree_panel(r) for t, c, r in panels]
    W = max(b[3] for b in built) + 2 * PAD
    out = []; y = 0
    for i, (t, c, root, w, h) in enumerate(built):
        ph = HEAD + h + PAD + 6
        out.append('<rect x="0.8" y="%d" width="%d" height="%d" rx="16" fill="#ffffff" stroke="#dbe3ee" stroke-width="1.6"/>' % (y + 1, W - 1.6, ph))
        if t: out.append('<text x="%d" y="%d" font-family="%s" font-size="12.5" font-weight="800" letter-spacing="1.4" fill="#94a3b8">%s</text>' % (PAD, y + 24, FONT, esc(t.upper())))
        if c:
            cw = tw(c, 13) + 20
            out.append('<rect x="%d" y="%d" width="%.1f" height="24" rx="7" fill="#1e293b"/><text x="%.1f" y="%d" font-family="%s" font-size="13" fill="#e2e8f0">%s</text>' % (PAD + tw(t, 12.5) + 28, y + 8, cw, PAD + tw(t, 12.5) + 38, y + 25, MONO, esc(c)))
        sub = []; off = (W - w) / 2 - root.sw / 2 + root.sw / 2 - (root.x - root.sw / 2) - root.sw / 2 + (w / 2)
        draw_shift = (W - root.sw) / 2
        g = []; draw(root, g, y + HEAD)
        out.append('<g transform="translate(%.1f,0)">%s</g>' % (draw_shift, ''.join(g)))
        y += ph
        if i < len(built) - 1:
            bh = 46
            out.append('<path d="M%.1f %d V%d" stroke="#e0a53a" stroke-width="3" fill="none"/><path d="M%.1f %d l-7 -9 h14z" fill="#e0a53a"/>' % (W / 2, y + 4, y + bh - 10, W / 2, y + bh - 2))
            if bridge:
                out.append('<text x="%.1f" y="%d" font-family="%s" font-size="12.5" fill="#94a3b8">%s</text>' % (W / 2 + 14, y + 29, FONT, esc(bridge)))
            y += bh
    return svg(W, y + 2, ''.join(out))
def svg(w, h, body, bg=None):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img">%s%s</svg>' %
            (w, h, w, h, '<rect width="100%%" height="100%%" fill="%s"/>' % bg if bg else '', body))
def write(ch, name, content):
    p = os.path.join(COURSE, ch, 'assets', name)
    open(p, 'w', encoding='utf-8').write(content); print('  ', ch.split('-')[0], name)

# ------------------------------------------------------------------ data
def dots(): return ['.bash_history', '.bashrc']
def student(extra_before=(), mid=(), extra_after=(), full=True):
    ks = list(extra_before) + [T('.bash_history'), T('.bashrc')] + list(mid) + list(extra_after) + [T('.ssh/')]
    return T('student', *ks)
def teacher(): return T('teacher', T('.bash_history'), T('.bashrc'), T('.ssh/'))
def fullroot(stu, extra_root=True, var=False):
    ks = [T('home', stu, teacher())]
    if extra_root: ks += [T('root', T('.bash_history'), T('.bashrc')), T('tmp/')]
    if var: ks += [T('var', T('www/'))]
    return T('/', *ks)
def dl(): return T('Downloads', T('Steam', T('games/')))
def backups(): return T('backups', T('Steam', T('games', T('PayDay2/'))))
def base(*extra, hot=()):  # student-boom met standaardmappen
    return [backups(), T('.bash_history'), T('.bashrc'), dl(), T('emptyfile')] + list(extra)

def ch4():
    c = '04-bestanden_en_mappen'
    # volledige boom
    full = T('/',
        T('dev', T('null'), T('tty1')),
        T('etc', T('apt/'), T('passwd')),
        T('home', T('student', T('.bash_history'), T('.bashrc'), T('.ssh/')), T('teacher', T('.bash_history'), T('.bashrc'), T('.ssh/'))),
        T('root', T('.bash_history'), T('.bashrc')), T('tmp/'),
        T('var', T('log', T('syslog')), T('www/')),
        T('usr', T('bin', T('ls')), T('sbin', T('reboot')),
          T('share', T('man', T('man1/'), T('man5/'), T('man8/')))))
    write(c, 'Ch4_CleanInstall.svg', panels_svg([('', '', full)]))
    write(c, 'Ch4_Emptyfile.svg', panels_svg([('', '', T('/', T('home', T('student', T('.bash_history'), T('.bashrc'), T('emptyfile'), T('.ssh/')), teacher()), T('root', T('.bash_history'), T('.bashrc')), T('tmp/'), T('var', T('www/'))))]))
    st0 = T('student', T('.bash_history'), T('.bashrc'), dl(), T('emptyfile'), T('.ssh/'))
    write(c, 'Ch4_Downloads_Steam_games_teacher.svg', panels_svg([('', '', fullroot(st0))]))
    write(c, 'Ch4_Downloads_Steam_games_teacher_backups.svg', panels_svg([('', '', fullroot(T('student', *base(T('.ssh/')))))]))
    write(c, 'Ch4_fileOne_fileTwo.svg', panels_svg([('', '', fullroot(T('student', *base(T('fileOne'), T('fileTwo'), T('.ssh/')))))]))
    write(c, 'Ch4_filenameWithSpaces.svg', panels_svg([('', '', fullroot(T('student', *base(T('File'), T('File Two'), T('fileOne'), T('fileTwo'), T('One'), T('.ssh/')))))]))
    # voor/na-figuren: alleen de inhoud van student
    def S(*ks): return T('student', *ks)
    B = lambda: [backups(), T('.bash_history'), T('.bashrc'), dl(), T('emptyfile'), T('File'), T('File Two'), T('fileOne'), T('fileTwo')]
    def sv(before, after, cmd):
        return panels_svg([('Voor', '', before), ('Na', cmd, after)])
    write(c, 'Ch4_MoveAFile.svg', sv(S(T('*aFile'), T('aFolder/'), *B(), T('One'), T('.ssh/')), S(T('aFolder', T('*aFile')), *B(), T('One'), T('.ssh/')), 'mv aFile aFolder/'))
    write(c, 'Ch4_MoveAndRenameFile.svg', sv(S(T('aFolder', T('*aFile')), *B(), T('One'), T('.ssh/')), S(T('aFolder/'), *B(), T('*newFileName'), T('One'), T('.ssh/')), 'mv aFolder/aFile newFileName'))
    write(c, 'Ch4_RenameFileWithMV.svg', sv(S(T('*aFolder/'), *B(), T('*newFileName'), T('One'), T('.ssh/')), S(*B(), T('*myFile'), T('*myFolder/'), T('One'), T('.ssh/')), 'mv aFolder myFolder  &&  mv newFileName myFile'))
    B2 = lambda: [backups(), T('.bash_history'), T('.bashrc'), dl()]
    write(c, 'Ch4_copy_emptyfile_emptyfilebackup.svg', sv(S(*B2(), T('*emptyfile'), T('File'), T('File Two'), T('fileOne'), T('fileTwo'), T('myFile'), T('myFolder/'), T('One'), T('.ssh/')), S(*B2(), T('emptyfile'), T('*emptyfile.backup'), T('File'), T('File Two'), T('fileOne'), T('fileTwo'), T('myFile'), T('myFolder/'), T('One'), T('.ssh/')), 'cp emptyfile emptyfile.backup'))
    R = lambda *k: S(*B2(), T('emptyfile'), T('File'), T('File Two'), T('fileOne'), T('fileTwo'), T('myFile'), *k, T('One'), T('.ssh/'))
    write(c, 'Ch4_copy_myfile_emptyfilebkp.svg', sv(R(T('myFolder/')), R(T('myFolder', T('*emptyfile.bkp'), T('*myFile'))), 'cp emptyfile myFolder/emptyfile.bkp  &&  cp myFile myFolder/'))
    write(c, 'Ch4_copy_recursive_myfolderbackup.svg', sv(R(T('*myFolder', T('emptyfile.bkp'), T('myFile'))), R(T('myFolder', T('emptyfile.bkp'), T('myFile')), T('*myFolder.backup', T('emptyfile.bkp'), T('myFile'))), 'cp -r myFolder myFolder.backup'))
    # renamedir-reeks
    def RD(files, hot=()):
        ks = []
        for f in files:
            ks.append(T(('*' if f in hot else '') + f))
        return S(T('myFolder.backup', T('emptyfile.bkp'), T('myfile')), T('One'), T('renamedir', *ks), T('.ssh/'))
    txt = ['aFile', 'aFile.backup', 'aFile.txt', 'anotherfile.txt', 'backup.txt', 'profiles.backup', 'profiles.txt', 'profiles2.odt', 'yaay.txt']
    nw = ['adocument.txt', 'aFile', 'aFile.backup', 'anotherdocument.txt', 'backup.txt', 'prodocuments.txt', 'profiles.backup', 'profiles2.odt', 'yaay.txt']
    write(c, 'Ch4_Rename.svg', sv(RD(txt, ('aFile.txt', 'anotherfile.txt', 'profiles.txt')), RD(nw, ('adocument.txt', 'anotherdocument.txt', 'prodocuments.txt')), 'rename  s/file/document/  *'))
    odt = ['adocument.odt', 'aFile', 'aFile.backup', 'anotherdocument.odt', 'backup.odt', 'prodocuments.odt', 'profiles.backup', 'profiles2.odt', 'yaay.odt']
    write(c, 'Ch4_Rename_Extentions.svg', sv(RD(nw), RD(odt, [f for f in odt if f.endswith('.odt')]), "rename 's/\\.txt$/.odt/' *.txt"))
    doc = ['adocument.doc', 'aFile', 'aFile.doc', 'anotherdocument.doc', 'backup.doc', 'prodocuments.doc', 'profiles.doc', 'profiles2.doc', 'yaay.doc']
    write(c, 'Ch4_Rename_Extentions_Case_Insensitive.svg', sv(RD(odt), RD(doc, [f for f in doc if f.endswith('.doc')]), "rename -i 's/\\.odt$/.doc/' *"))
    write(c, 'Ch4_rm_file.svg', sv(RD([('~' + f if f == 'profiles2.doc' else f) for f in doc]) if False else S(T('myFolder.backup', T('emptyfile.bkp'), T('myfile')), T('One'), T('renamedir', *[T(('~' if f == 'profiles2.doc' else '') + f) for f in doc]), T('.ssh/')),
        RD([f for f in doc if f != 'profiles2.doc']), 'rm renamedir/profiles2.doc'))
    fin = S(backups(), T('.bash_history'), T('.bashrc'), dl(), T('emptyfile'), T('File'), T('File Two'), T('fileOne'), T('fileTwo'), T('logo.png'), T('myFile'), T('myFolder', T('emptyfile.bkp'), T('myfile')), T('myFolder.backup', T('emptyfile.bkp'), T('myfile')), T('One'), T('.ssh/'))
    write(c, 'Ch4_rm_rf.svg', sv(S(T('myFolder.backup', T('emptyfile.bkp'), T('myfile')), T('One'), T('~renamedir', *[T(f) for f in doc if f != 'profiles2.doc']), T('.ssh/')), fin, 'rm -rf renamedir'))
    # oefeningen-figuren
    def PX(courses, soft=None):
        ks = [T('PXL', courses)] if not soft else [T('PXL', courses, soft)]
        return T('/', T('home', S(T('.ssh/'), T('.bash_history'), T('.bashrc'), *ks), teacher()), T('root', T('.bash_history'), T('.bashrc')))
    S1 = lambda *k: T('S1', *k)
    write(c, 'Ch4_Task2.svg', panels_svg([('', '', PX(T('Courses', S1(T('LinuxEss/')))))]))
    write(c, 'Ch4_Task3.svg', panels_svg([('', '', PX(T('Courses', S1(T('LinuxEss/')), T('S2', T('NetworksEss/')))))]))
    write(c, 'Ch4_Task4.svg', panels_svg([('', '', PX(T('Courses', S1(T('LinuxEss/'), T('WindowsEss/')), T('S2', T('NetworksEss/')))))]))
    write(c, 'Ch4_Task5.svg', panels_svg([('', '', PX(T('Courses', S1(T('LinuxEss/'), T('WindowsEss/')), T('S2', T('NetworksEss/'))), T('Software', T('Virtualization', T('VMware Workstation/')))))]))
    # directory-structuur
    items = [('/bin', 'Programma\'s (binaries)'), ('/boot', 'Bestanden om op te starten'), ('/dev', 'Apparaten als bestanden'), ('/etc', 'Configuratiebestanden'),
             ('/home', 'Persoonlijke map van gebruikers'), ('/lib', 'Gedeelde bibliotheken'), ('/media', 'Verwisselbare media (usb, dvd)'), ('/mnt', 'Tijdelijk gekoppelde schijven'),
             ('/opt', 'Optionele software'), ('/proc', 'Informatie over processen en kernel'), ('/root', 'Homefolder van de root-gebruiker'), ('/sbin', 'Systeemprogramma\'s voor beheer'),
             ('/srv', 'Gegevens van diensten (web, ftp)'), ('/tmp', 'Tijdelijke bestanden'), ('/usr', 'Programma\'s en data: bin, lib, share'), ('/var', 'Veranderlijke data: log, lock, tmp')]
    cols = 2; cw = 400; chh = 54; gap = 14; PAD = 22; W = cols * cw + (cols - 1) * gap + 2 * PAD
    rows = (len(items) + cols - 1) // cols; H = 74 + rows * (chh + gap) + PAD - gap
    o = ['<rect x="1" y="1" width="%d" height="%d" rx="16" fill="#fff" stroke="#dbe3ee" stroke-width="1.6"/>' % (W - 2, H - 2),
         '<rect x="%d" y="22" width="52" height="32" rx="9" fill="#334155"/><text x="%d" y="44" text-anchor="middle" font-family="%s" font-size="16" font-weight="700" fill="#fff">/</text>' % (PAD, PAD + 26, MONO),
         '<text x="%d" y="44" font-family="%s" font-size="17" font-weight="700" fill="#1e293b">De mappen onder de root-directory</text>' % (PAD + 66, FONT)]
    for i, (d, t) in enumerate(items):
        x = PAD + (i % cols) * (cw + gap); y = 74 + (i // cols) * (chh + gap)
        o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="11" fill="#f4f7fb" stroke="#dbe3ee" stroke-width="1.4"/><rect x="%d" y="%d" width="84" height="30" rx="8" fill="#e7eef8" stroke="#a9bddb" stroke-width="1.4"/><text x="%d" y="%d" text-anchor="middle" font-family="%s" font-size="15" font-weight="700" fill="#1f3a5f">%s</text><text x="%d" y="%d" font-family="%s" font-size="14.5" fill="#334155">%s</text>' % (x, y, cw, chh, x + 12, y + 12, x + 54, y + 32, MONO, d, x + 108, y + 32, FONT, esc(t)))
    write(c, 'Linux_Filesystem.svg', svg(W, H, ''.join(o)))

def ch2():
    c = '02-installatie'
    def box(x, y, w, h, t, fill, stroke, col='#1e293b', fs=14, bold=True):
        return '<rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="%s" stroke="%s" stroke-width="1.6"/><text x="%.1f" y="%.1f" text-anchor="middle" font-family="%s" font-size="%d" font-weight="%d" fill="%s">%s</text>' % (x, y, w, h, fill, stroke, x + w / 2, y + h / 2 + fs * 0.35, FONT, fs, 700 if bold else 500, col, esc(t))
    o = ['<rect x="1" y="1" width="858" height="318" rx="16" fill="#fff" stroke="#dbe3ee" stroke-width="1.6"/>']
    o.append('<text x="30" y="84" font-family="%s" font-size="14" fill="#64748b">Eén besturingssysteem op de hardware,</text><text x="30" y="104" font-family="%s" font-size="14" fill="#64748b">alle applicaties delen dat systeem.</text>' % (FONT, FONT))
    o.append('<text x="450" y="38" font-family="%s" font-size="1" fill="none">.</text>' % FONT)
    # links: zonder virtualisatie
    o.append('<text x="40" y="38" font-family="%s" font-size="13" font-weight="800" letter-spacing="1.3" fill="#94a3b8">ZONDER VIRTUALISATIE</text>' % FONT)
    for i in range(3): o.append(box(30 + i * 122, 150, 112, 44, 'Applicatie', '#e7eef8', '#a9bddb', '#1f3a5f'))
    o.append(box(30, 202, 356, 44, 'Host-besturingssysteem', '#fbeccd', '#e0b45a', '#6b4a06'))
    o.append(box(30, 254, 356, 44, 'Hardware', '#e5e9f0', '#b6c0cf', '#475569'))
    # rechts
    o.append('<text x="470" y="38" font-family="%s" font-size="13" font-weight="800" letter-spacing="1.3" fill="#94a3b8">TYPE 2-VIRTUALISATIE</text>' % FONT)
    cols = [('#e7eef8', '#a9bddb', '#1f3a5f'), ('#fbe4e1', '#e19a92', '#8a2d22'), ('#dff1ed', '#98cfc6', '#17504a')]
    for i, (f, s, t) in enumerate(cols):
        x = 450 + i * 132
        o.append('<rect x="%d" y="52" width="122" height="104" rx="10" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="5 4"/><text x="%d" y="70" text-anchor="middle" font-family="%s" font-size="12" font-weight="700" fill="%s">VM %d</text>' % (x, s, x + 61, FONT, t, i + 1))
        o.append(box(x + 8, 78, 106, 34, 'Applicatie', f, s, t, 13))
        o.append(box(x + 8, 116, 106, 34, 'Gast-OS', '#fbeccd', '#e0b45a', '#6b4a06', 13))
    o.append(box(450, 164, 386, 40, 'Hypervisor (bv. VMware Workstation)', '#f3dccf', '#d9a98d', '#7a3f1d'))
    o.append(box(450, 210, 386, 40, 'Host-besturingssysteem', '#fbeccd', '#e0b45a', '#6b4a06'))
    o.append(box(450, 256, 386, 40, 'Hardware', '#e5e9f0', '#b6c0cf', '#475569'))
    o.append('<path d="M429 40 V300" stroke="#e2e8f0" stroke-width="2" stroke-dasharray="4 5"/>')
    write(c, 'Virtualization.svg', svg(860, 320, ''.join(o)))

def term(lines, w=860, fs=14.5, title='student@ubserv', extra=''):
    lh = fs * 1.42; h = 46 + len(lines) * lh + 22
    o = ['<rect x="1" y="1" width="%d" height="%d" rx="14" fill="#0f172a" stroke="#1e293b" stroke-width="1.6"/><path d="M1 40 H%d" stroke="#1e293b"/>' % (w - 2, h - 2, w - 1),
         '<circle cx="24" cy="21" r="6" fill="#e5877e"/><circle cx="44" cy="21" r="6" fill="#e6c36f"/><circle cx="64" cy="21" r="6" fill="#7fc98f"/>',
         '<text x="%d" y="26" text-anchor="middle" font-family="%s" font-size="13" fill="#64748b">%s</text>' % (w / 2, MONO, esc(title))]
    for i, (t, col) in enumerate(lines):
        y = 46 + (i + 1) * lh - 4
        o.append('<text x="22" y="%.1f" xml:space="preserve" font-family="%s" font-size="%s" fill="%s">%s</text>' % (y, MONO, fs, col, t))
    return h, ''.join(o) + extra
def ch3():
    c = '03-command_line_interface_(CLI)'
    G = '#cbd5e1'; D = '#64748b'; Gr = '#86d6a0'; B = '#7dd3fc'
    L = [('Ubuntu 24.04 LTS ubserv tty1', G), ('', G), ("Try contacting this VM's SSH server via 'ssh vsock%172684340' from host.", D), ('', G),
         ('ubserv login: <tspan fill="#fde68a" font-weight="700">student</tspan>', G), ('Password:', G), ('Welcome to Ubuntu 24.04 LTS (GNU/Linux x86_64)', G), ('', G),
         (' * Documentation:  https://docs.ubuntu.com', D), (' * Management:     https://landscape.canonical.com', D), (' * Support:        https://ubuntu.com/pro', D), ('', G),
         (' System load:  0.0            Processes:     223', G), (' Usage of /:   31.1% of 9.75GB  Users logged in: 0', G), (' Memory usage: 2%              IPv4 address for ens33: 192.168.112.136', G), ('', G),
         ('14 updates can be applied immediately.', G), ('', G),
         ('<tspan fill="%s" font-weight="700">student@ubserv</tspan>:<tspan fill="%s" font-weight="700">~</tspan>$ <tspan fill="#fde68a">▌</tspan>' % (Gr, B), G)]
    def tag(n, t, y):
        w = tw(t, 13) * 1.12 + 52; x = 836 - w
        return '<g><rect x="%.1f" y="%d" width="%.1f" height="26" rx="13" fill="#efe0b4"/><text x="%.1f" y="%d" font-family="%s" font-size="13" font-weight="800" fill="#3b2a05">%s  %s</text></g>' % (x, y, w, x + 14, y + 18, FONT, n, esc(t))
    h, body = term(L)
    lh = 14.5 * 1.42
    ex = tag('1', 'gebruikersnaam', int(46 + 5 * lh - 30)) + tag('2', 'wachtwoord (je ziet niets verschijnen)', int(46 + 5 * lh - 1)) + tag('3', 'de prompt: je bent ingelogd', int(46 + 19 * lh - 22))
    write(c, 'CLI_Login_And_Welcome.svg', svg(860, int(h), body + ex))


def prompt_fig():
    fs = 24; cw = fs * 0.6; x0 = 28; y0 = 52
    parts = [('student', '#86d6a0', 'gebruikersnaam', '#3f8a5c', 'username'), ('@', '#94a3b8', None, None, None), ('linux-ess', '#86d6a0', 'computernaam', '#3f8a86', 'hostname'),
             (':', '#94a3b8', None, None, None), ('~', '#7dd3fc', 'map', '#3b82a8', 'path'), ('$', '#94a3b8', None, None, None), (' ', '#fff', 'je commando', '#b8693f', 'command')]
    W = 540; H = 134; o = ['<rect x="1" y="1" width="%d" height="%d" rx="16" fill="#0f172a" stroke="#1e293b" stroke-width="1.6"/>' % (W - 2, H - 2)]
    x = x0; cur = x0
    for t, col, lab, lc, _ in parts:
        w = len(t) * cw
        if _ == 'command': cur = x + cw * 0.3
        if t.strip():
            o.append('<text x="%.1f" y="%d" xml:space="preserve" font-family="%s" font-size="%d" font-weight="700" fill="%s">%s</text>' % (x, y0, MONO, fs, col, esc(t)))
        if lab:
            if t == ' ': w = 11 * cw; bx0 = x; bx1 = x + w
            else: bx0 = x; bx1 = x + w
            o.append('<path d="M%.1f 70 v8 H%.1f v-8" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>' % (bx0 + 2, bx1 - 2, lc))
            cx = (bx0 + bx1) / 2
            o.append('<text x="%.1f" y="%d" text-anchor="middle" font-family="%s" font-size="12.5" font-weight="700" fill="%s">%s</text>' % (cx, 100, FONT, lc if False else '#e2e8f0', esc(lab)))
            o.append('<text x="%.1f" y="%d" text-anchor="middle" font-family="%s" font-size="10.5" fill="%s">%s</text>' % (cx, 117, MONO, '#64748b', esc(_)))
        x += w
    # cursor
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#fde68a" opacity=".9"/>' % (cur, y0 - 20, cw * 0.7, 25))
    # let op: placeholder-commando ls na de cursor wordt niet getoond
    write('03-command_line_interface_(CLI)', 'prompt.svg', svg(W, H, ''.join(o)))


def tar_fig():
    W = 760; PAD = 24
    rows = [('UITPAKKEN', 'tar -xzvf archief.tar.gz', [('x', 'Xtra'), ('z', 'Zakken'), ('v', 'Vol'), ('f', 'Fruit')], 'e<b>x</b>tract = uitpakken', '#dff1ed', '#98cfc6', '#17504a'),
            ('INPAKKEN', 'tar -czvf archief.tar.gz map/', [('c', 'Cadeautjes'), ('z', 'Zijn'), ('v', 'Voor'), ('f', 'Feestjes')], '<b>c</b>reate = aanmaken', '#fbeccd', '#e0b45a', '#6b4a06')]
    o = ['<rect x="1" y="1" width="%d" height="284" rx="16" fill="#fff" stroke="#dbe3ee" stroke-width="1.6"/>' % (W - 2)]
    y = 24
    for title, cmd, words, note, fill, stroke, col in rows:
        o.append('<text x="%d" y="%d" font-family="%s" font-size="12.5" font-weight="800" letter-spacing="1.4" fill="#94a3b8">%s</text>' % (PAD, y + 12, FONT, title))
        cw = tw(cmd, 14) + 22
        o.append('<rect x="%d" y="%d" width="%.1f" height="26" rx="8" fill="#1e293b"/><text x="%d" y="%d" font-family="%s" font-size="14" fill="#e2e8f0">%s</text>' % (PAD + 100, y - 2, cw, PAD + 111, y + 16, MONO, esc(cmd)))
        x = PAD
        for l, w in words:
            bw = tw(w, 17) + 58
            o.append('<rect x="%.1f" y="%d" width="%.1f" height="44" rx="12" fill="%s" stroke="%s" stroke-width="1.6"/><text x="%.1f" y="%d" font-family="%s" font-size="20" font-weight="800" fill="%s">%s</text><text x="%.1f" y="%d" font-family="%s" font-size="17" font-weight="600" fill="%s">%s</text>' % (x, y + 40, bw, fill, stroke, x + 14, y + 69, MONO, col, l, x + 38, y + 68, FONT, col, w[1:] if False else w))
            x += bw + 10
        o.append('<text x="%.1f" y="%d" font-family="%s" font-size="13.5" fill="#64748b">%s</text>' % (x + 6, y + 68, FONT, note.replace('<b>', '').replace('</b>', '')))
        y += 104
    o.append('<text x="%d" y="%d" font-family="%s" font-size="14" font-style="italic" fill="#64748b">De f (file) staat altijd als laatste: daarna volgt de bestandsnaam.</text><text x="%d" y="%d" font-family="%s" font-size="14" font-style="italic" fill="#64748b">Met -t (toon) zie je wat erin zit, zonder uit te pakken.</text>' % (PAD, 240, FONT, PAD, 262, FONT))
    write('05-software_en_paketten', 'tar-commando.svg', svg(W, 286, ''.join(o)))

# ------------------------------------------------------------------ rechten
ON = ('#dff1ed', '#98cfc6', '#17504a')     # bit staat aan
OFF = ('#ffffff', '#d5dde8', '#94a3b8')    # bit staat uit
SPEC = ('#fdf0d3', '#e0a53a', '#6b4a06')   # speciale bit
def cell(x, y, w, h, txt, sty, fs=22, mono=True, bold=800):
    f, st, c = sty
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="10" fill="%s" stroke="%s" stroke-width="1.6"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="%s" font-size="%d" font-weight="%d" fill="%s">%s</text>'
            % (x, y, w, h, f, st, x + w / 2, y + h / 2 + fs * 0.35, MONO if mono else FONT, fs, bold, c, esc(txt)))
def label(x, y, txt, fs=13, col='#64748b', anchor='middle', bold=600, mono=False, ital=False):
    return ('<text x="%.1f" y="%.1f" text-anchor="%s" font-family="%s" font-size="%s" font-weight="%d" fill="%s"%s>%s</text>'
            % (x, y, anchor, MONO if mono else FONT, fs, bold, col, ' font-style="italic"' if ital else '', esc(txt)))
def head(x, y, txt):
    return '<text x="%d" y="%d" font-family="%s" font-size="12.5" font-weight="800" letter-spacing="1.4" fill="#94a3b8">%s</text>' % (x, y, FONT, esc(txt))
def chip(x, y, txt, fs=14):
    w = tw(txt, fs) + 22
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="26" rx="8" fill="#1e293b"/><text x="%.1f" y="%.1f" font-family="%s" font-size="%d" fill="#e2e8f0">%s</text>'
            % (x, y, w, x + 11, y + 18, MONO, fs, esc(txt))), w
def card(w, h): return '<rect x="1" y="1" width="%d" height="%d" rx="16" fill="#fff" stroke="#dbe3ee" stroke-width="1.6"/>' % (w - 2, h - 2)

def rechten_lezen():
    W, H = 760, 300; o = [card(W, H), head(24, 30, 'RECHTEN LEZEN')]
    c, cw = chip(160, 14, '-rwxrw-r--'); o.append(c)
    # type
    o.append(label(24 + 36, 76, 'type', 13)); o.append(cell(24, 90, 72, 56, '-', OFF, 26)); o.append(label(24 + 36, 166, 'bestand', 12.5)); o.append(label(24 + 36, 183, '(d = map)', 12, '#94a3b8'))
    groups = [('EIGENAAR', 'user · 1e naam', 'rwx'), ('GROEP', 'group · 2e naam', 'rw-'), ('ANDEREN', 'others · de rest', 'r--')]
    x0 = 130; gw = 200; vals = [4, 2, 1]
    for gi, (t, sub, bits) in enumerate(groups):
        gx = x0 + gi * (gw + 10)
        o.append(label(gx + 85, 62, t, 13, '#475569', bold=800)); o.append(label(gx + 85, 79, sub, 12, '#94a3b8'))
        tot = 0
        for i, b in enumerate(bits):
            on = b != '-'; tot += vals[i] if on else 0
            o.append(cell(gx + i * 58, 90, 52, 56, b if on else '–', ON if on else OFF, 24))
            o.append(label(gx + i * 58 + 26, 166, str(vals[i]), 13, '#94a3b8', mono=True))
        parts = [str(vals[i]) if bits[i] != '-' else '0' for i in range(3)]
        o.append(label(gx + 85, 196, ' + '.join(parts) + ' = ', 14, '#64748b', mono=True, anchor='end')); o.append(label(gx + 93, 197, str(tot), 22, '#17504a', anchor='start', mono=True, bold=800))
    o.append('<path d="M24 222 H736" stroke="#e5ebf3" stroke-width="1.6"/>')
    o.append(label(24, 256, 'Octaal:', 14, '#64748b', anchor='start', bold=700)); o.append(label(100, 258, '7 6 4', 26, '#17504a', anchor='start', mono=True, bold=800))
    c, cw = chip(250, 238, 'chmod 764 bestand'); o.append(c)
    o.append(label(250 + cw + 14, 256, 'r = 4 · w = 2 · x = 1: tel op wat aan staat', 13.5, '#64748b', anchor='start'))
    write('10-rechten', 'rechten-lezen.svg', svg(W, H, ''.join(o)))

def umask_fig():
    W = 760; o = []
    cols = ['EIGENAAR', 'GROEP', 'ANDEREN']; cx = [210, 330, 450]; cwid = 100
    def block(y, title, mx, um, res, rwx, octal, note):
        out = [head(24, y + 4, title)]
        for i, c in enumerate(cols): out.append(label(cx[i] + cwid / 2, y + 28, c, 12, '#94a3b8', bold=800))
        rows = [('maximum', mx, OFF, '#475569'), ('umask: weghalen', um, SPEC, '#6b4a06'), ('resultaat', res, ON, '#17504a')]
        for r, (name, vals, sty, col) in enumerate(rows):
            yy = y + 40 + r * 46
            out.append(label(24, yy + 28, name, 14, col, anchor='start', bold=700))
            for i in range(3): out.append(cell(cx[i], yy, cwid, 38, vals[i], sty, 20))
        out.append(label(590, y + 40 + 2 * 46 + 26, rwx, 20, '#17504a', anchor='start', mono=True, bold=800))
        out.append(label(590, y + 40 + 2 * 46 + 46, octal, 12.5, '#94a3b8', anchor='start'))
        out.append(label(590, y + 40 + 46 + 26, note, 12.5, '#94a3b8', anchor='start', ital=True))
        return ''.join(out)
    H = 540
    o.append(card(W, H)); o.append(head(24, 30, 'UMASK: WAT KRIJG JE NIET?'))
    c, cw = chip(250, 14, 'umask 027'); o.append(c)
    o.append(label(24, 54, 'De umask bepaalt welke rechten je bij nieuwe bestanden en mappen niet krijgt.', 13.5, '#64748b', anchor='start'))
    o.append(block(84, 'NIEUWE MAP', ['7', '7', '7'], ['0', '2', '7'], ['7', '5', '0'], 'rwxr-x---', '750', 'w (2) en alles (7) weg'))
    o.append(block(288, 'NIEUW BESTAND', ['6', '6', '6'], ['0', '2', '7'], ['6', '4', '0'], 'rw-r-----', '640', 'een bestand krijgt nooit x'))
    o.append('<path d="M24 478 H736" stroke="#e5ebf3" stroke-width="1.6"/>')
    o.append(label(24, 506, 'Standaard voor student: umask 002 (bestand 664, map 775). Voor root: umask 022 (bestand 644, map 755).', 13.5, '#64748b', anchor='start'))
    write('10-rechten', 'umask.svg', svg(W, H, ''.join(o)))

def speciale_bits_fig():
    W, H = 760, 330; o = [card(W, H), head(24, 30, 'SPECIALE BITS IN DE OCTALE MODUS')]
    c, cw = chip(350, 14, 'chmod 3770 map'); o.append(c)
    # vier cijfers
    o.append(label(24, 88, 'Vier cijfers:', 14, '#64748b', anchor='start', bold=700))
    o.append(label(150 + 91, 76, 'speciaal', 12, '#94a3b8', bold=800)); 
    # speciaal-blok met drie bits
    sp = [('4', 'setuid', False), ('2', 'setgid', True), ('1', 'sticky', True)]
    for i, (v, nm, on) in enumerate(sp):
        o.append(cell(150 + i * 64 - 2, 94, 58, 50, v, SPEC if on else OFF, 22)); o.append(label(150 + i * 64 + 27, 162, nm, 12.5, '#6b4a06' if on else '#94a3b8', bold=700))
    o.append(label(150 + 3 * 64 + 6, 126, '=', 22, '#94a3b8', anchor='start', mono=True)); o.append(cell(150 + 3 * 64 + 30, 94, 58, 50, '3', SPEC, 26))
    for i, (dgt, nm) in enumerate([('7', 'eigenaar'), ('7', 'groep'), ('0', 'anderen')]):
        xx = 150 + 3 * 64 + 120 + i * 70
        o.append(cell(xx, 94, 58, 50, dgt, ON if dgt != '0' else OFF, 26)); o.append(label(xx + 29, 162, nm, 12.5, '#475569', bold=700))
    o.append(label(150 + 3 * 64 + 61, 76, 'som', 12, '#94a3b8', bold=800))
    o.append('<path d="M24 190 H736" stroke="#e5ebf3" stroke-width="1.6"/>')
    # ls-uitvoer
    o.append(label(24, 228, 'ls -ld toont:', 14, '#64748b', anchor='start', bold=700))
    ls = 'drwxrws--T'
    o.append('<rect x="150" y="206" width="190" height="34" rx="9" fill="#0f172a"/>')
    o.append('<text x="164" y="229" xml:space="preserve" font-family="%s" font-size="19" font-weight="700" fill="#e2e8f0">drwx<tspan fill="#fde68a">r</tspan><tspan fill="#fde68a">w</tspan><tspan fill="#fdba74">s</tspan>--<tspan fill="#fdba74">T</tspan></text>' % MONO)
    o.append(label(360, 222, 's bij de groep: setgid staat aan, de x eronder ook', 13.5, '#6b4a06', anchor='start'))
    o.append(label(360, 242, 'T bij anderen: sticky staat aan, maar de x eronder staat uit', 13.5, '#6b4a06', anchor='start'))
    o.append('<path d="M24 262 H736" stroke="#e5ebf3" stroke-width="1.6"/>')
    o.append(label(24, 292, 'Kleine letter (s, t): x staat ook aan.  Hoofdletter (S, T): x staat uit.', 13.5, '#64748b', anchor='start'))
    o.append(label(24, 314, 'Alle speciale bits wissen: zet een extra nul voor de modus (chmod 00770).', 13.5, '#64748b', anchor='start'))
    write('10-rechten', 'speciale-bits.svg', svg(W, H, ''.join(o)))

# ------------------------------------------------------------------ grapjes
def joke(name, ch, title, lines, caption, w=760, fs=15):
    h, body = term(lines, w=w, fs=fs, title=title)
    cap = '<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-size="14" font-style="italic" fill="#64748b">%s</text>' % (w / 2, h + 26, FONT, esc(caption))
    write(ch, name, svg(w, int(h + 38), body + cap))
def jokes():
    G = '#cbd5e1'; D = '#64748b'; Gr = '#86d6a0'; B = '#7dd3fc'; Y = '#fde68a'; R = '#f2a1a1'
    P = lambda cmd: '<tspan fill="%s" font-weight="700">student@linux-ess</tspan>:<tspan fill="%s" font-weight="700">~</tspan>$ %s' % (Gr, B, cmd)
    joke('sudo-broodje.svg', '03-command_line_interface_(CLI)', 'student@linux-ess', [
        (P('maak een broodje'), G), ('Permission denied.', R), (P('sudo maak een broodje'), G), ('[sudo] password for student: ••••••••', D), ('Een broodje kaas-ham, onmiddellijk, chef! 🥪', Gr)],
        'Met sudo krijg je alles gedaan. Gebruik die macht met verstand.')
    joke('vim-afsluiten.svg', '06-bestandsinhoud', 'vim', [
        ('~', B), ('~', B), ('~                       Je opent Vim voor het eerst…', D), ('~', B), (':exit', Y), ('<tspan fill="%s">E492: Not an editor command: exit</tspan>' % R, G), (':quit', Y), ('<tspan fill="%s">E37: No write since last change (add ! to override)</tspan>' % R, G), (':wq', Y), ('<tspan fill="%s">"notities.txt" 3L, 41B written   — vrijheid.</tspan>' % Gr, G)],
        'Vim afsluiten: de eerste echte hindernis van elke Linux-student.')
    tar_fig()
    joke('chmod-777.svg', '10-rechten', 'student@linux-ess', [
        (P('./script.sh'), G), ('bash: ./script.sh: Permission denied', R), (P('chmod 777 script.sh'), G), (P('./script.sh'), G), ('<tspan fill="%s">Het werkt!</tspan>   (en nu mag iedereen alles)' % Gr, G)],
        '777 lost je probleem op en maakt er een veiligheidsprobleem bij. Gebruik de kleinste rechten die werken.')
    joke('distro-hoppen.svg', '01-introductie', 'student@linux-ess', [
        ('<tspan fill="%s">Maandag</tspan>    Ubuntu geïnstalleerd. Werkt prima.' % Y, G), ('<tspan fill="%s">Woensdag</tspan>  "Misschien toch eens Arch proberen?"' % Y, G), ('<tspan fill="%s">Vrijdag</tspan>    Terug naar Ubuntu. Wifi werkt weer.' % Y, G)],
        'Distro hoppen: leerzaam, tijdrovend en bijzonder verslavend.')

if __name__ == '__main__':
    ch2(); ch3(); prompt_fig(); ch4(); jokes(); rechten_lezen(); umask_fig(); speciale_bits_fig()
