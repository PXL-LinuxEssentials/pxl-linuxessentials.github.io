#!/usr/bin/env python3
"""Bouwt de volledige offline Linux-cursus (alle hoofdstukken) tot één HTML-bestand."""
import art, re, html, base64, sys, os, unicodedata, json, glob, hashlib, subprocess, io
import markdown
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
COURSE = os.environ.get('COURSE', os.path.join(HERE, '..', 'cursus'))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'dist', 'index.html')
CACHE = os.path.join(HERE, '..', '.cache')
os.makedirs(CACHE, exist_ok=True)
esc = html.escape

# ---------------------------------------------------------------- configuratie
CHAPTERS = [
    dict(num='01', dir='01-introductie', title='Introductie', blurb='Wat is Linux, waar komt het vandaan en waarom gebruiken we het?'),
    dict(num='02', dir='02-installatie', title='Installatie', blurb='Je eigen Ubuntu-omgeving opzetten: een desktop-VM en een server in de cloud.'),
    dict(num='03', dir='03-command_line_interface_(CLI)', title='Command Line Interface', blurb='De prompt, commando\'s, opties en hulp zoeken met man en tldr.'),
    dict(num='04', dir='04-bestanden_en_mappen', title='Bestanden en mappen', blurb='Navigeren, aanmaken, kopiëren, verplaatsen en verwijderen.'),
    dict(num='05', dir='05-software_en_paketten', title='Software en pakketten', blurb='Software beheren met apt, snap en dpkg; archieven met tar en zip.'),
    dict(num='06', dir='06-bestandsinhoud', title='Bestandsinhoud', blurb='Bestanden lezen, doorzoeken en bewerken met cat, less, tail en nano.'),
    dict(num='07', dir='07-geavanceerde_commandostructuren', title='Geavanceerde commandostructuren', blurb='Globbing, aliassen, redirection en control operators.'),
    dict(num='08', dir='08-filters', title='Filters', blurb='Tekst filteren en bewerken met grep, sed, sort, cut en reguliere expressies.'),
    dict(num='09', dir='09-gebruikers_en_groepen', title='Gebruikers en groepen', blurb='Gebruikers en groepen aanmaken, wijzigen en beheren.'),
    dict(num='10', dir='10-rechten', title='Rechten', blurb='Eigenaars, groepen en permissies: chmod, chown, umask en ACL\'s.'),
    dict(num='11', dir='11-automatisatie', title='Automatisatie', blurb='Bash-scripts, de PATH-variabele, at en cron.'),
    dict(num='12', dir='12-extras', title='Extra\'s', blurb='Aanvullende onderwerpen, zoals Ubuntu Pro.'),
]
SET_TITLES = {
    ('02-installatie', 'oefeningen-installatie_ubuntu_desktop_in_vmware_workstation.md'): 'Ubuntu Desktop in VMware Workstation',
    ('02-installatie', 'oefeningen-installatie_ubuntu_server_in_azure_cloud.md'): 'Ubuntu Server in Azure Cloud',
}
PDF_TITLES = {
    '01-Introductie-Spiekbrief.pdf': 'Introductie',
    '02-Installatie-Spiekbrief.pdf': 'Installatie',
    '03-Command-Line-Interface-Spiekbrief.pdf': 'Command Line Interface',
    'Linux-Snelle-hulp-tldr-Spiekbrief.pdf': 'Snelle hulp met tldr',
    '04-Bestanden-en-mappen-Spiekbrief.pdf': 'Bestanden en mappen',
    '05-Software-en-pakketten-Spiekbrief.pdf': 'Software en pakketten',
    '06-Bestandsinhoud-Spiekbrief.pdf': 'Bestandsinhoud',
    '07-Geavanceerde-commandostructuren-Spiekbrief.pdf': 'Geavanceerde commandostructuren',
    '08-Filters-Spiekbrief.pdf': 'Filters',
    '09-Gebruikers-en-groepen-Spiekbrief.pdf': 'Gebruikers en groepen',
}
ICO = {'start': '🏁', 'theorie': '📘', 'oefeningen': '🛠', 'kennistoets': '🧠', 'overzicht': '📄', 'extra': '➕'}
NAMES = {'start': 'Start', 'theorie': 'Theorie', 'oefeningen': 'Oefeningen', 'kennistoets': 'Kennistoets', 'overzicht': 'Overzicht'}

PDF_DATA = {}   # bestandsnaam -> dict(b64, pages, text, thumb)
WARN = []

# ---------------------------------------------------------------- inline helpers
def kbd_html(spec):
    parts = [p.strip() for p in re.split(r'\+', spec) if p.strip() != '']
    if spec.endswith('+'): parts.append('+')
    def k(p):
        return '<kbd>' + ''.join('&#%d;' % ord(c) if c in '\\_*<>&`' else c for c in p) + '</kbd>'
    return '<span class="keys">' + '<i>+</i>'.join(k(p) for p in parts) + '</span>'

def kbds(s): return re.sub(r'\{\{(.+?)\}\}', lambda m: kbd_html(m.group(1)), s)

def pdf_card(name, text, compact=True):
    info = PDF_DATA.get(name)
    if not info:
        WARN.append('PDF ontbreekt: ' + name); return ''
    thumb = '<img class="pthumb" alt="" src="%s">' % info['thumb']
    return ('<div class="pdfcard%s" data-pdf="%s">%s<div class="pbody"><b>%s</b><small class="fn">%s</small><small>%d pagina\'s · PDF</small>'
            '<div class="pact"><button class="btn pdf-open" type="button">Openen</button><button class="btn ghost pdf-dl" type="button">Downloaden</button></div></div></div>'
            ) % (' compact' if compact else '', esc(name, quote=True), thumb, esc(text), esc(name), info['pages'])

def md(text):
    text = kbds(text)
    h = markdown.markdown(text, extensions=['tables', 'sane_lists'])
    h = re.sub(r'<table>(.*?)</table>', r'<div class="tablewrap"><table>\1</table></div>', h, flags=re.S)
    h = re.sub(r'<p><a href="\./spiekbrief/([^"]+\.pdf)">(.*?)</a></p>', lambda m: pdf_card(m.group(1), m.group(2)), h)
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a target="_blank" rel="noopener" href="\1"', h)
    return h

# ---------------------------------------------------------------- code blokken
PROMPT = re.compile(r'^(\w[\w.-]*)@([\w.-]+):(\S*?)\$\s?(.*)$')

def hl_cmd(cmd):
    out = []; expect = True; marker_next = False
    for tok in re.findall(r'"[^"]*"|\'[^\']*\'|>>|>|<<|\||\S+|\s+', cmd):
        e = esc(tok)
        if tok.isspace(): out.append(e); continue
        if marker_next: out.append('<span class="mk">%s</span>' % e); marker_next = False; continue
        if tok[0] in '"\'': out.append('<span class="str">%s</span>' % e); expect = False; continue
        if tok in ('>', '>>', '<<', '|'):
            out.append('<span class="op">%s</span>' % e)
            if tok == '<<': marker_next = True
            if tok == '|': expect = True
            continue
        if expect:
            if tok == 'sudo': out.append('<span class="sudo">sudo</span>'); continue
            out.append('<span class="cmd">%s</span>' % e); expect = False; continue
        if tok.startswith('-') and len(tok) > 1: out.append('<span class="fl">%s</span>' % e); continue
        out.append('<span class="arg">%s</span>' % e)
    return ''.join(out)

def annot_split(line):
    if '⟵' in line:
        a, b = line.split('⟵', 1)
        return a.rstrip(), b.strip()
    return line, None

def copy_btn(txt):
    return '<button class="copy" type="button" data-copy="%s">Kopieer</button>' % esc(txt, quote=True)

def annotation(a):
    return '<span class="annot">%s</span>' % kbds(esc(a)).replace('&amp;#', '&#') if a else ''

CMDS = set('''ls cd cp mv rm rmdir mkdir touch cat less more head tail grep egrep fgrep sed awk sort cut wc tr uniq echo printf man whatis whereis which type find locate nano vim vi chmod chown chgrp umask sudo su apt apt-get apt-cache snap dpkg tar zip unzip gzip gunzip bzip2 useradd usermod userdel adduser deluser groupadd groupmod groupdel gpasswd passwd chage id who whoami w last date cal alias unalias history tee diff cmp file stat ln pwd clear exit reboot shutdown poweroff ssh scp wget curl ping ip hostname hostnamectl timedatectl crontab at atq atrm source export env set unset read tree df du free top htop ps kill uname lsblk mount umount getent getfacl setfacl dpkg-reconfigure systemctl service journalctl bash sh time sleep yes true false seq xargs column paste join comm tac rev nl od xxd strings basename dirname realpath readlink tldr tealdeer select-editor update-locale locale locale-gen sync fg bg jobs nohup watch'''.split())

def looks_cmd(lines):
    ls = [l for l in lines if l.strip() and not l.strip().startswith('#')]
    if not ls: return False
    ok = 0
    for l in ls:
        t = l.strip().split()
        if t and t[0] == 'sudo' and len(t) > 1: t = t[1:]
        if t and (t[0] in CMDS or re.match(r'^(\./|~/|/)\S+$', t[0]) or re.match(r'^\w+=', t[0])): ok += 1
    return ok / len(ls) >= 0.7

def render_code(lang, body, in_details):
    lines = body.split('\n')
    has_prompt = any(PROMPT.match(l) for l in lines)
    if lang == 'output':
        rows = ''.join('<span class="l out">%s</span>' % esc(l) for l in lines)
        return '<div class="term"><div class="bar"><i></i><i></i><i></i><span>Uitvoer</span>%s</div><pre>%s</pre></div>' % (copy_btn(body), rows)
    is_file = (not has_prompt) and any(l.startswith('#!') for l in lines)
    if is_file:
        return '<div class="filebox script"><div class="bar"><span>📜 Script</span>%s</div><pre>%s</pre></div>' % (copy_btn(body), esc(body))
    if has_prompt or lang in ('bash', 'sh', 'shell') or (lang == '' and (in_details or looks_cmd(lines))):
        script = not has_prompt
        rows = []; copy = []; title = 'Terminal'
        mode_input = False; marker = None
        for l in lines:
            raw, an = annot_split(l)
            m = PROMPT.match(raw)
            if m:
                user, host, path, cmd = m.groups(); title = '%s@%s' % (user, host)
                mode_input = False; marker = None
                pr = '<span class="pu">%s@%s</span><span class="pd">:</span><span class="pp">%s</span><span class="pd">$</span> ' % (esc(user), esc(host), esc(path))
                rows.append('<span class="l">%s%s%s</span>' % (pr, hl_cmd(cmd), annotation(an)))
                copy.append(cmd)
                hm = re.search(r'<<\s*(\S+)', cmd)
                if hm: marker = hm.group(1); mode_input = True
                elif re.match(r'^cat\s*>\s*\S+\s*$', cmd): mode_input = True; marker = None
                continue
            if mode_input:
                if marker and raw.strip() == marker:
                    rows.append('<span class="l"><span class="mk">%s</span>%s</span>' % (esc(raw), annotation(an))); copy.append(raw); mode_input = False; marker = None
                else:
                    rows.append('<span class="l inp">%s%s</span>' % (esc(raw), annotation(an))); copy.append(raw)
                continue
            if script:
                if raw.strip() == '': rows.append('<span class="l"></span>'); copy.append(''); continue
                hm = re.search(r'<<\s*(\S+)', raw)
                rows.append('<span class="l cmdline">%s%s</span>' % (hl_cmd(raw), annotation(an))); copy.append(raw)
                if hm: marker = hm.group(1); mode_input = True
                elif re.match(r'^cat\s*>\s*\S+\s*$', raw): mode_input = True
                continue
            rows.append('<span class="l out">%s%s</span>' % (esc(raw), annotation(an)))
        cp = '\n'.join(copy).strip('\n')
        cls = 'term script' if script else 'term'
        if script: title = 'Commando'
        return '<div class="%s"><div class="bar"><i></i><i></i><i></i><span>%s</span>%s</div><pre>%s</pre></div>' % (cls, esc(title), copy_btn(cp), ''.join(rows))
    return '<div class="filebox"><div class="bar"><span>📄 Tekst / bestandsinhoud</span>%s</div><pre>%s</pre></div>' % (copy_btn(body), esc(body))

# ---------------------------------------------------------------- componenten
def attrs(tag):
    return {m.group(1).lstrip(':'): m.group(2) for m in re.finditer(r'(:?\w+)="(.*?)"', tag, re.S)}

def render_component(kind, tag, body):
    a = attrs(tag)
    if kind == 'Quiz':
        opts = a['opties'].split('|'); c = int(a['correct'])
        items = ''.join('<button class="opt" type="button">%s</button>' % esc(o) for o in opts)
        return ('<div class="q" data-type="quiz" data-correct="%d"><div class="qt"><span class="n"></span>%s</div><div class="opts">%s</div>'
                '<div class="explain" hidden>%s<p><a href="javascript:void(0)" class="retry">↺ Opnieuw proberen</a></p></div></div>') % (c, esc(a['vraag']), items, md(body.strip()))
    if kind == 'Match':
        prompts = a['prompts'].split('|'); ans = a['antwoorden'].split('|'); dis = [x for x in a.get('afleidingen', '').split('|') if x]
        rows = ''.join('<div class="matchrow"><div class="term-chip">%s</div><select aria-label="Antwoord voor %s"><option value="">Kies het juiste antwoord…</option></select><div class="mark"></div></div>' % (esc(p), esc(p)) for p in prompts)
        return ('<div class="q" data-type="match" data-answers=\'%s\' data-all=\'%s\'><div class="qt"><span class="n"></span>%s</div>%s'
                '<div class="actions"><button class="btn check" type="button">Controleer</button><button class="btn ghost show" type="button">Toon oplossing</button><span class="fb"></span></div></div>') % (
            esc(json.dumps(ans, ensure_ascii=False), quote=True).replace("'", '&#39;'), esc(json.dumps(ans + dis, ensure_ascii=False), quote=True).replace("'", '&#39;'), esc(a['vraag']), rows)
    if kind == 'FillIn':
        v = esc(a['vraag']).replace('___', '<span class="answer">&nbsp;&nbsp;&nbsp;&nbsp;</span>')
        pat = a.get('patroon')
        if not pat: pat = '^' + re.escape(a['antwoord'].strip()) + '$'; flags = 'i'
        else: flags = ''
        return ('<div class="q" data-type="fill" data-pattern="%s" data-flags="%s" data-answer="%s"><div class="qt"><span class="n"></span>%s</div><div class="fill"><div class="row"><input type="text" autocomplete="off" spellcheck="false" placeholder="Typ je antwoord…" aria-label="Antwoord"></div></div>'
                '<div class="actions"><button class="btn check" type="button">Controleer</button><button class="btn ghost show" type="button">Toon antwoord</button><span class="fb"></span></div></div>') % (esc(pat, quote=True), flags, esc(a['antwoord'], quote=True), v)

ICONS = {'info': 'ℹ️', 'tip': '💡', 'warning': '⚠️', 'danger': '⛔'}
DEFTITLE = {'info': 'Info', 'tip': 'Tip', 'warning': 'Let op', 'danger': 'Gevaar'}

def render_blocks(text, in_details=False):
    lines = text.split('\n'); i = 0; out = []; buf = []
    def flush():
        if buf and ''.join(buf).strip(): out.append(md('\n'.join(buf)))
        buf.clear()
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            flush(); lang = l[3:].strip(); i += 1; body = []
            while i < len(lines) and not lines[i].startswith('```'): body.append(lines[i]); i += 1
            i += 1; out.append(render_code(lang, '\n'.join(body), in_details)); continue
        m = re.match(r'^:::\s*(\w+)\s*(.*)$', l)
        if m:
            flush(); kind, title = m.group(1), m.group(2).strip(); i += 1; inner = []; fence = False; depth = 0
            while i < len(lines):
                if lines[i].startswith('```'): fence = not fence
                if not fence:
                    if re.match(r'^:::\s*\w+', lines[i]): depth += 1
                    elif lines[i].strip() == ':::':
                        if depth == 0: break
                        depth -= 1
                inner.append(lines[i]); i += 1
            i += 1; itext = '\n'.join(inner)
            if kind == 'details':
                out.append('<details class="solution"><summary><span class="stt">%s</span><span class="hint">klik om te openen</span></summary><div class="dbody">%s</div></details>' % (esc(title or 'Oplossing tonen'), render_blocks(itext, True)))
            else:
                out.append('<div class="callout %s"><div class="ct"><span class="ic">%s</span>%s</div>%s</div>' % (kind, ICONS.get(kind, 'ℹ️'), esc(title or DEFTITLE.get(kind, 'Info')), render_blocks(itext, in_details)))
            continue
        m = re.match(r'^<(Match|FillIn|Quiz)\b', l)
        if m:
            flush(); kind = m.group(1); tag = [l]
            if kind == 'Quiz':
                while not tag[-1].rstrip().endswith('>'): i += 1; tag.append(lines[i])
                i += 1; body = []
                while i < len(lines) and not lines[i].startswith('</Quiz>'): body.append(lines[i]); i += 1
                i += 1; out.append(render_component(kind, '\n'.join(tag), '\n'.join(body)))
            else:
                while not tag[-1].rstrip().endswith('/>'): i += 1; tag.append(lines[i])
                i += 1; out.append(render_component(kind, '\n'.join(tag), ''))
            continue
        buf.append(l); i += 1
    flush()
    return '\n'.join(out)

# ---------------------------------------------------------------- hulpfuncties
def slug(s):
    s = html.unescape(re.sub(r'<[^>]+>', '', s)); s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-') or 'x'

def read(path):
    t = open(path, encoding='utf8').read().replace('\r\n', '\n')
    t = re.sub(r'\A---\n.*?\n---\n', '', t, flags=re.S)
    return t

IMG_CACHE = {}
def image_uri(chapdir, fn):
    path = os.path.join(COURSE, chapdir, 'assets', fn)
    if not os.path.exists(path):
        WARN.append('Afbeelding ontbreekt: %s/%s' % (chapdir, fn)); return ''
    key = hashlib.md5(open(path, 'rb').read()).hexdigest()
    if key in IMG_CACHE: return IMG_CACHE[key]
    cp = os.path.join(CACHE, key + '.webp')
    if not os.path.exists(cp):
        im = Image.open(path)
        if im.mode in ('P', 'LA'): im = im.convert('RGBA')
        elif im.mode not in ('RGB', 'RGBA'): im = im.convert('RGB')
        if im.width > 1500:
            im = im.resize((1500, round(im.height * 1500 / im.width)), Image.LANCZOS)
        im.save(cp, 'WEBP', quality=82, method=6)
    uri = 'data:image/webp;base64,' + base64.b64encode(open(cp, 'rb').read()).decode()
    IMG_CACHE[key] = uri
    return uri

def inline_images(h, chapdir):
    h = re.sub(r'src="\./assets/([^"]+)"', lambda m: 'src="%s"' % image_uri(chapdir, m.group(1)), h)
    h = re.sub(r'<img ', '<img decoding="async" ', h)
    def fig(m):
        alt = m.group(2)
        cap = '<figcaption>%s</figcaption>' % alt if (' ' in alt.strip()) else ''
        return '<figure>%s%s</figure>' % (m.group(1), cap)
    return re.sub(r'<p>(<img [^>]*alt="([^"]*)"[^>]*>)</p>', fig, h)

def split_md(text):
    """Splitst markdown in [(niveau, titel, [regels])] buiten codeblokken. Eerste item = (0,'',intro)."""
    out = [[0, '', []]]; inf = False
    for l in text.split('\n'):
        if l.startswith('```'): inf = not inf
        m = None if inf else re.match(r'^(#{1,3}) (.+?)\s*$', l)
        if m: out.append([len(m.group(1)), m.group(2), []])
        else: out[-1][2].append(l)
    return out

def plain(s): return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

def strip_num(t): return re.sub(r'^\s*\d+\.\s*', '', t)

# ---------------------------------------------------------------- pagina's
def page_shell(pid, title_html, lead, body, toc, pager_html, extra_cls=''):
    toc = []
    grid = 'page-grid'
    toc_h = ''
    if toc:
        toc_h = '<aside class="toc"><b>Op deze pagina</b>' + ''.join('<a href="#%s"%s>%s</a>' % (i, ' class="sub"' if sub else '', esc(t)) for i, t, sub in toc) + '</aside>'
    return ('<main class="page %s" id="p-%s" data-pid="%s"><div class="wrap"><div class="%s"><div class="content">%s<div class="lead">%s</div>%s%s</div>%s</div></div></main>'
            % (extra_cls, pid, pid, grid, title_html, lead, ''.join(body), pager_html, toc_h))

def title_block(h1, sub):
    return '<h1 class="pagetitle">%s<small>%s</small></h1>' % (esc(h1), esc(sub)) if h1 else ''

def build_generic(pid, chapdir, md_text, cls_alt=False):
    parts = split_md(md_text)
    intro = '\n'.join(parts[0][2]); h1 = None
    secs = []
    rest = parts[1:]
    if rest and rest[0][0] == 1:
        h1 = strip_num(rest[0][1]); intro += '\n' + '\n'.join(rest[0][2]); rest = rest[1:]
    # groepeer: h2 = sectie; h3 binnen sectie blijft '###'
    cur = None; sections = []
    for lvl, title, body in rest:
        if lvl <= 2:
            cur = [title, []]; sections.append(cur)
            if lvl == 1: pass
        else:
            if cur is None: cur = ['', []]; sections.append(cur)
            cur[1].append('#' * lvl + ' ' + title)
        cur[1].extend(body)
    lead = inline_images(render_blocks(intro.strip()), chapdir)
    body = []; toc = []
    for n, (title, lines) in enumerate(sections, 1):
        inner = inline_images(render_blocks('\n'.join(lines)), chapdir)
        sid = '%s-%s' % (pid, slug(title))
        subs = []
        def h3(x):
            hid = '%s-%s' % (pid, slug(x.group(1)))
            subs.append((hid, plain(x.group(1)), True)); return '<h3 id="%s">%s</h3>' % (hid, x.group(1))
        inner = re.sub(r'<h3>(.*?)</h3>', h3, inner)
        toc.append((sid, plain(title), False)); toc.extend(subs)
        body.append('<section class="sec c%d" id="%s"><h2><span class="num">%d</span>%s</h2>%s</section>' % ((n - 1) % 6, sid, n, esc(title), inner))
    return h1, lead, body, toc

def exercise_units(parts):
    """parts uit split_md van één bestand -> lijst sets [(titel, intro_md, [units])]; unit=(num,label,tag,cls,body_md)."""
    sets = []; cur = None; last_h2_ex = True
    def newset(t):
        nonlocal cur
        cur = dict(title=t, intro=[], units=[]); sets.append(cur)
    newset('')
    first_h1 = True; cur_unit = None
    isex = lambda t: re.match(r'^(Oefening\s+\d+|Optionele oefening)', t, re.I)
    # intro vóór eerste kop
    cur['intro'].extend(parts[0][2])
    for lvl, title, body in parts[1:]:
        if lvl == 1:
            if first_h1: first_h1 = False; cur['h1'] = title
            else: newset(re.sub(r'^Oefeningen op\s+', '', title)); cur_unit = None
            cur['intro'].extend(body); cur_unit = None; continue
        if lvl == 2:
            if isex(title): last_h2_ex = True; cur_unit = [title, body[:]]; cur['units'].append(cur_unit)
            else:
                last_h2_ex = False
                if cur['units']: newset(title)
                else: cur['title'] = title
                cur['intro'].extend(body); cur_unit = None
            continue
        if lvl == 3:
            if isex(title) and not last_h2_ex: cur_unit = [title, body[:]]; cur['units'].append(cur_unit)
            elif cur_unit is not None: cur_unit[1].append('### ' + title); cur_unit[1].extend(body)
            else: cur['intro'].append('### ' + title); cur['intro'].extend(body)
    sets = [x for x in sets if x['units']]
    if len(sets) > 1 and not sets[0]['title'] and sets[0].get('h1'):
        sets[0]['title'] = re.sub(r'^Oefeningen op\s+', '', sets[0]['h1'])
    return sets

def build_exercises(pid, chapdir, files):
    all_sets = []; h1 = None
    for fname in files:
        parts = split_md(read(os.path.join(COURSE, chapdir, fname)))
        sets = exercise_units(parts)
        for s in sets:
            if not h1 and s.get('h1'): h1 = s['h1']
        st = SET_TITLES.get((chapdir, fname))
        if st:
            sets[0]['title'] = st
        all_sets.extend(sets)
    out = []; total = 0
    for si, s in enumerate(all_sets):
        intro = inline_images(render_blocks('\n'.join(s['intro']).strip()), chapdir)
        units = []; has_sol = False
        for ui, (title, lines) in enumerate(s['units']):
            mm = re.match(r'Oefening\s+(\d+)\s*(.*)$', title)
            cls = 'ex'; tag = ''
            if mm:
                num = mm.group(1); rest_t = mm.group(2)
                tm = re.search(r'\((.*?)\)\s*$', title)
                label = re.sub(r'\s*\(.*?\)\s*$', '', title).strip()
                if tm: cls += ' extra'; tag = '<span class="tag">%s</span>' % esc(tm.group(1))
            else:
                num = '★'; label = title; cls += ' optional'; tag = '<span class="tag">optioneel</span>'
            body_h = inline_images(render_blocks('\n'.join(lines)), chapdir)
            if 'class="solution"' in body_h: has_sol = True
            eid = '%s-s%d-e%d' % (pid, si, ui)
            units.append('<section class="%s" id="%s" data-ex="%s"><header><span class="badge">%s</span><h2>%s%s</h2>'
                         '<div class="exctl"><button class="st st-done" type="button" data-act="done">✔ Klaar</button><button class="st st-skip" type="button" data-act="skip">⏭ Overslaan</button></div></header>%s</section>'
                         % (cls, eid, eid, num, esc(label), tag, body_h))
            total += 1
        stitle = s['title'] or ('Oefeningen' if len(all_sets) == 1 else 'Set %d' % (si + 1))
        bar = ('<div class="setbar"><div class="stitle">%s</div><b class="cnt">0 / %d afgewerkt</b><div class="meter"><i></i></div>'
               '<span class="lockmsg"></span><button class="btn showall" type="button" hidden>Alle oplossingen tonen</button>'
               '<button class="btn ghost reset" type="button">Wis voortgang</button></div>') % (esc(stitle), len(units))
        if len(all_sets) == 1 and not s['title']:
            bar = bar.replace('<div class="stitle">Oefeningen</div>', '<div class="stitle">Voortgang</div>')
        out.append('<div class="exset" data-set="%s-s%d" data-hassol="%d" data-n="%d">%s%s%s</div>' % (pid, si, 1 if has_sol else 0, len(units), bar, ('<div class="setintro">%s</div>' % intro) if intro.strip() else '', ''.join(units)))
    return h1, ''.join(out), total, len(all_sets)

def build_quiz(pid, chapdir, text):
    h1, lead, body, toc = build_generic(pid, chapdir, text)
    n = len(re.findall(r'class="q"', ''.join(body) + lead))
    score = ('<div class="scorecard"><b class="sc-label">0 / 0</b><div class="meter"><i class="sc-meter"></i></div>'
             '<button class="btn ghost quizreset" type="button">Opnieuw beginnen</button></div>')
    return h1, lead + score, body, toc, n

def build_pdfs(chapdir):
    out = []
    for p in sorted(glob.glob(os.path.join(COURSE, chapdir, 'overzicht', '*.pdf'))):
        out.append(os.path.basename(p))
    return out

def load_pdf(name, path):
    raw = open(path, 'rb').read()
    pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', path], capture_output=True, text=True).stdout).group(1))
    txt = subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True).stdout
    tp = os.path.join(CACHE, 'thumb-' + hashlib.md5(raw).hexdigest())
    if not os.path.exists(tp + '.webp'):
        subprocess.run(['pdftoppm', '-f', '1', '-l', '1', '-r', '70', '-png', path, tp], check=True)
        pngs = glob.glob(tp + '-*.png')
        Image.open(pngs[0]).convert('RGB').save(tp + '.webp', 'WEBP', quality=80)
        for x in pngs: os.remove(x)
    thumb = 'data:image/webp;base64,' + base64.b64encode(open(tp + '.webp', 'rb').read()).decode()
    PDF_DATA[name] = dict(b64=base64.b64encode(raw).decode(), pages=pages, text=re.sub(r'\s+', ' ', txt).strip(), thumb=thumb)

def pager_html(prev, nxt):
    p = '<div class="pager">'
    if prev: p += '<a href="#%s" class="prev"><small>← Vorige</small><b>%s</b></a>' % prev
    if nxt: p += '<a href="#%s" class="next"><small>Volgende →</small><b>%s</b></a>' % nxt
    return p + '</div>'

# ---------------------------------------------------------------- bouwen
def main():
    # 1) PDF's laden

    chapters_out = []   # (html pages, tabs, meta)
    all_pages = []      # per hoofdstuk lijst (page_key, label)
    meta = []
    for ch in CHAPTERS:
        d = ch['dir']; num = ch['num']; base = os.path.join(COURSE, d)
        files = {os.path.basename(f) for f in glob.glob(os.path.join(base, '*.md'))}
        pages = []   # (key, label)
        if 'wat-zal-je-leren.md' in files: pages.append('start')
        if 'theorie.md' in files: pages.append('theorie')
        oef = sorted(f for f in files if f.startswith('oefeningen'))
        if oef: pages.append('oefeningen')
        if 'kennistoets.md' in files: pages.append('kennistoets')
        if 'overzicht.md' in files: pages.append('overzicht')
        extras = []
        if d == '01-introductie' and 'ms-visual-studio-pro.md' in files: extras.append(('extra-vs', 'ms-visual-studio-pro.md', 'Visual Studio Pro'))
        if d == '12-extras':
            extras.append(('extra', 'ubuntu_pro.md', 'Ubuntu Pro'))
        for k, f, l in extras: pages.append(k)
        meta.append(dict(num=num, title=ch['title'], blurb=ch['blurb'], pages=pages, extras={k: l for k, f, l in extras}))

    # navigatievolgorde
    flat = []
    labels = {}
    for m in meta:
        for k in m['pages']:
            lab = NAMES.get(k) or m['extras'].get(k)
            labels[(m['num'], k)] = (ICO.get(k, ICO['extra']) + ' ' + lab)
            flat.append((m['num'], k))
    def nb(m, k):
        i = flat.index((m, k))
        prev = ('%s/%s' % flat[i - 1], '%s · %s' % (CHAPTERS[int(flat[i - 1][0]) - 1]['title'], labels[flat[i - 1]])) if i > 0 else None
        nxt = ('%s/%s' % flat[i + 1], '%s · %s' % (CHAPTERS[int(flat[i + 1][0]) - 1]['title'], labels[flat[i + 1]])) if i + 1 < len(flat) else None
        return prev, nxt
    def pgr(m, k):
        p, n = nb(m, k)
        if p and p[0].split('/')[0] == m: p = (p[0], labels[(m, p[0].split('/')[1])])
        if n and n[0].split('/')[0] == m: n = (n[0], labels[(m, n[0].split('/')[1])])
        return pager_html(p, n)

    pages_html = []; tabs_html = []; side_html = []; cards = []; ex_total_all = 0
    for ch, mt in zip(CHAPTERS, meta):
        d = ch['dir']; num = ch['num']; base = os.path.join(COURSE, d)
        tabs = []
        info = dict(week=None, uur=None, nex=0, nq=0, nsets=0)
        for k in mt['pages']:
            pid = '%s-%s' % (num, k)
            lab = labels[(num, k)]
            tabs.append('<a href="#%s/%s" data-page="%s">%s</a>' % (num, k, k, lab))
            subtitle = ch['title']
            if k == 'start':
                txt = read(os.path.join(base, 'wat-zal-je-leren.md'))
                wk = re.search(r'week\s+(\d+)', txt); uu = re.search(r'±\s*(\d+)\s*uur', txt)
                info['week'] = wk.group(1) if wk else None; info['uur'] = uu.group(1) if uu else None
                h1, lead, body, toc = build_generic(pid, d, txt)
                body = [b.replace('<ol>', '<ol class="questions">', 1) if 'kernvragen' in b[:120] else b for b in body]
                # tegels
                tiles = ''
                tl = [('theorie', '📘', 'Theorie', 'Leer de commando\'s en concepten', 't1'), ('oefeningen', '🛠', 'Oefeningen', 'Oefen in je Ubuntu-VM', 't2'), ('kennistoets', '🧠', 'Kennistoets', 'Test wat je kent', 't3'), ('overzicht', '📄', 'Overzicht', 'Het hoofdstuk op één pagina', 't4')]
                tiles = '<div class="tiles">' + ''.join('<a class="tile %s" href="#%s/%s"><span>%s</span><b>%s</b><small>%s</small></a>' % (c, num, kk, ic, t, s) for kk, ic, t, s, c in tl if kk in mt['pages']) + '</div>'
                chips = ''
                if info['week']: chips += '<span class="chip">📅 Week %s</span>' % info['week']
                if info['uur']: chips += '<span class="chip">⏱ ± %s uur</span>' % info['uur']
                hero = ('<section class="hero">'+art.hero_art(num)+'<div class="kicker">Linux · Hoofdstuk %s</div><h1>%s</h1><p>%s</p><div class="chips">%s<span class="chip" id="chips-%s"></span></div></section>'
                        % (num, esc(ch['title']), esc(ch['blurb']), chips, num))
                pages_html.append(page_shell(pid, '', hero + lead, body + [tiles], [], pgr(num, k), 'p-start'))
            elif k == 'theorie':
                h1, lead, body, toc = build_generic(pid, d, read(os.path.join(base, 'theorie.md')))
                pages_html.append(page_shell(pid, title_block(h1 or ch['title'], 'Theorie'), lead, body, toc, pgr(num, k)))
            elif k == 'oefeningen':
                oef = sorted(f for f in os.listdir(base) if f.startswith('oefeningen') and f.endswith('.md'))
                h1, content, total, nsets = build_exercises(pid, d, oef)
                info['nex'] = total; info['nsets'] = nsets
                sub = 'Probeer eerst zelf. De oplossingen openen zodra je alle oefeningen van een set hebt afgewerkt (een oefening overslaan mag).'
                nohint = all('data-hassol="0"' in x for x in re.findall(r'<div class="exset"[^>]*>', content))
                if nohint: sub = 'Volg de stappen en vink af wat je gedaan hebt.'
                pages_html.append(page_shell(pid, title_block(h1 or 'Oefeningen', sub), '', [content], [], pgr(num, k)))
            elif k == 'kennistoets':
                h1, lead, body, toc, nq = build_quiz(pid, d, read(os.path.join(base, 'kennistoets.md')))
                info['nq'] = nq
                pages_html.append(page_shell(pid, title_block(h1 or 'Kennistoets', 'Antwoord, controleer en leer uit je fouten'), lead, body, [], pgr(num, k)))
            elif k == 'overzicht':
                h1, lead, body, toc = build_generic(pid, d, read(os.path.join(base, 'overzicht.md')))
                lead = '<p><button class="btn printbtn" type="button">🖨 Afdrukken</button></p>' + lead
                pages_html.append(page_shell(pid, title_block('Overzicht hoofdstuk', ch['title']), lead, body, toc, pgr(num, k)))
            else:  # extra pagina's
                f = [e for e in extras_for(num) if e[0] == k][0]
                h1, lead, body, toc = build_generic(pid, d, read(os.path.join(base, f[1])))
                pages_html.append(page_shell(pid, title_block(h1 or f[2], 'Extra'), lead, body, toc, pgr(num, k)))
        tabs_html.append('<nav class="tabs" data-chap="%s">%s</nav>' % (num, ''.join(tabs)))
        side_html.append('<details class="sch" data-chap="%s"><summary><span class="n">%s</span><b>%s</b></summary>%s</details>' % (num, num, esc(ch['title']), ''.join(tabs)))
        cards.append((ch, mt, info))

    # home
    chap_cards = ''
    for ch, mt, info in cards:
        pills = ''
        if info['week']: pills += '<span class="pill">Week %s</span>' % info['week']
        if info['uur']: pills += '<span class="pill">± %s u</span>' % info['uur']
        if info['nex']: pills += '<span class="pill">%d oef.</span>' % info['nex']
        if 'overzicht' in mt['pages']: pills += '<span class="pill pk">📄 overzicht</span>'
        first = mt['pages'][0]
        chap_cards += ('<a class="chcard c%d" href="#%s/%s" data-chap="%s"><span class="cn">%s</span>%s<div class="cb"><b>%s</b><small>%s</small><div class="pills">%s</div>'
                       '<div class="cprog" hidden><div class="meter"><i></i></div><span></span></div></div></a>') % ((int(ch['num']) - 1) % 6, ch['num'], first, ch['num'], ch['num'], art.card_art(ch['num']), esc(ch['title']), esc(ch['blurb']), pills)
    pdf_rows = ''.join('<a class="pdfrow" href="#%s/overzicht"><span class="pn">%s</span><span>%s</span><span class="go">Openen →</span></a>' % (ch['num'], ch['num'], esc(ch['title'])) for ch, mt, info in cards if 'overzicht' in mt['pages'])
    home = ('<main class="page" id="p-home" data-pid="home"><div class="wrap"><section class="hero big"><div class="kicker">PXL · Toegepaste Informatica</div><h1>Linux Essentials</h1>'
            '<p>De volledige cursus in één bestand: theorie, oefeningen, kennistoetsen en overzichten. Alles werkt offline.</p>'
            '<div class="chips"><span class="chip">12 hoofdstukken</span><span class="chip">🛠 oefeningen met oplossingen achteraf</span><span class="chip">📄 overzichtjes</span><span class="chip">🔍 zoeken</span></div>'
            '<div class="herocta"><a class="btn big" id="resume" href="#01/start" hidden>Verder waar je gebleven was →</a><a class="btn big ghostw" href="#01/start">Begin bij hoofdstuk 1</a></div></section>'
            '<div class="overall"><b id="overall-label">Voortgang</b><div class="meter"><i id="overall-meter"></i></div><button class="btn ghost" id="resetall" type="button">Alles wissen</button></div>'
            '<h2 class="hh">Hoofdstukken</h2><div class="chgrid">%s</div>'
            '<h2 class="hh">Overzichten per hoofdstuk</h2><div class="pdflist">%s</div>'
            '<div class="callout tip"><div class="ct"><span class="ic">💡</span>Zo werken de oefeningen</div><p>Bij elke oefening kies je <b>Klaar</b> of <b>Overslaan</b>. Zodra je alle oefeningen van een set hebt afgewerkt, openen de oplossingen. Een oefening overslaan mag: zo kan je niet blijven hangen. Je voortgang wordt in je browser bewaard.</p></div>'
            '</div></main>') % (chap_cards, pdf_rows)

    css = open(os.path.join(HERE, 'style_all.css'), encoding='utf8').read()
    js = open(os.path.join(HERE, 'app_all.js'), encoding='utf8').read()
    chap_options = ''.join('<a href="#%s/%s"><span>%s</span>%s</a>' % (m['num'], m['pages'][0], m['num'], esc(m['title'])) for m in meta)
    doc = f"""<!DOCTYPE html>
<html lang="nl" data-theme="light">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<meta name="googlebot" content="noindex, nofollow">
<title>Linux Essentials · cursus</title>
<style>{css}</style></head>
<body>
<header class="topbar"><div class="in">
<a class="brand" href="#home"><span class="logo">&gt;_</span><div>Linux Essentials<small>Cursusmateriaal</small></div></a>
<button class="btn chbtn" id="chbtn" type="button" aria-controls="side" aria-expanded="true">☰ Menu</button>
<div class="tabswrap">{''.join(tabs_html)}</div>
<button class="iconbtn" id="searchbtn" type="button" title="Zoeken (Ctrl+K of /)">🔍</button>
<button class="iconbtn" id="theme" type="button" title="Donker / licht thema">🌙</button></div>
<div class="progressbar"><i></i></div>
<div class="chpanel" id="chpanel" hidden style="display:none"><div class="in">{chap_options}</div></div></header>
<aside class="side" id="side" aria-label="Hoofdstukken"><div class="sidehead"><a class="sh" href="#home">🏠 Overzicht cursus</a><div class="sidetools"><button type="button" id="sideopen">Alles open</button><button type="button" id="sideclose">Alles dicht</button></div></div>{''.join(side_html)}</aside><div class="sideback" id="sideback"></div>
<div class="searchov" id="searchov" hidden><div class="box"><input id="searchin" type="search" placeholder="Zoek in theorie, oefeningen, kennistoetsen en overzichten…" autocomplete="off"><div id="searchres"></div><small>Esc om te sluiten</small></div></div>
<div class="docentbar" id="docentbar" hidden>Docentenmodus: alle oplossingen zijn ontgrendeld.</div>
<div class="toast" id="toast" hidden></div>
<div class="lightbox" id="lightbox" hidden><img alt=""></div>
{home}{''.join(pages_html)}
<footer>Dit bestand werkt volledig offline: open het in je browser. Je voortgang wordt lokaal in je browser bewaard.</footer>
<script>{js}</script>
</body></html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf8').write(doc)
    print('geschreven', OUT, round(len(doc) / 1024 / 1024, 2), 'MB')
    for w in sorted(set(WARN)): print('WAARSCHUWING', w)

def extras_for(num):
    if num == '01': return [('extra-vs', 'ms-visual-studio-pro.md', 'Visual Studio Pro')]
    if num == '12': return [('extra', 'ubuntu_pro.md', 'Ubuntu Pro')]
    return []

if __name__ == '__main__':
    main()
