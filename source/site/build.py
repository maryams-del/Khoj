import os, re, json, shutil
SRC = '/home/claude/khoj-gulab/project'; OUT = '/home/claude/khoj-site'
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
STATE = "<script>var S={};function R(){document.querySelectorAll('[data-if]').forEach(function(e){var k=e.getAttribute('data-if'),n=k.charAt(0)=='!';if(n)k=k.slice(1);e.style.display=(!!S[k]!=n)?'contents':'none'});document.body.style.setProperty('--boxbg',S.agreed?'#9C4560':'#FFFFFF')}var K={t:function(k){S[k]=!S[k];R()}};R()</script>"
# text the owner edited by hand on the canvas (opening scenes)
EDIT = {
 'WhatIs2': 'It shows as lasting patterns of <span style="color: rgb(156, 69, 96)">inattention</span>, <span style="color: rgb(156, 69, 96)">hyperactivity</span> and/or <span style="color: rgb(156, 69, 96)">impulsivity</span> that interfere with daily life.<br><br>It affects <span style="color: rgb(156, 69, 96)">brain development</span>, and executive functions like <span style="color: rgb(156, 69, 96)">planning</span> and <span style="color: rgb(156, 69, 96)">focus</span>.',
 'WhatIs4': 'It is chronic, but <span style="color: rgb(156, 69, 96)">manageable</span> through <span style="color: rgb(156, 69, 96)">therapy</span> and <span style="color: rgb(156, 69, 96)">medication</span>.',
}
names = []; PAGES = {}; CSS = []
for f in json.load(open(SRC + '/canvas.json'))['order']:
    if f.startswith('Laptop') or f == 'WhatIs3.dc.html': continue
    n = f[:-8]; t = open(f'{SRC}/{f}', encoding='utf-8').read()
    title = re.search(r'<title>(.*?)</title>', t).group(1)
    lang = re.search(r'<html([^>]*)>', t).group(1)
    helmet = re.search(r'<helmet>(.*?)</helmet>', t, re.S).group(1)
    body = t[t.index('</helmet>') + 9:t.index('</x-dc>')]
    if n in EDIT:
        if n == 'WhatIs2': body, k = re.subn(r'<p style="margin: 0; font-family: Fraunces[^>]*>.*?</p>', lambda m: open('/home/claude/site-build/scene2.html').read(), body, count=1, flags=re.S)
        else: body, k = re.subn(r'(<p style="margin: 0; font-family: Fraunces[^>]*>).*?(</p>)', lambda m: m.group(1) + EDIT[n] + m.group(2), body, count=1, flags=re.S)
        assert k == 1, n
    body = body.replace('WhatIs3.dc.html', 'WhatIs4.dc.html')
    if n.startswith('WhatIs') or n == 'HowWorks':   # four opening scenes now, not five
        body = body.replace('<span style="width: 8px; height: 8px; border-radius: 4px; background: rgba(156,69,96,0.3)"></span>', '', 1)
    body = re.sub(r'<sc-if value="\{\{ (\w+) \}\}"[^>]*>', lambda m: '<div data-if="%s" style="display: none">' % {'notAgreed': '!agreed'}.get(m.group(1), m.group(1)), body).replace('</sc-if>', '</div>')
    body = re.sub(r'onClick="\{\{ (\w+) \}\}"', lambda m: 'onclick="K.t(\'%s\')"' % {'toggle': 'agreed' if n == 'HowWorks' else 'open', 'togglePdf': 'pdf'}[m.group(1)], body)
    body = body.replace(' aria-pressed="{{ agreed }}"', '')
    body = body.replace('background: {{ boxBg }}', 'background: var(--boxbg, #FFFFFF)')
    assert '{{' not in body, (n, body[body.index('{{') - 80:body.index('{{') + 40])
    css = '\n'.join(l for l in re.search(r'<style>(.*?)</style>', helmet, re.S).group(1).split('\n') if l and not l.startswith('body{') and not l.startswith('a{color'))
    if css and css not in CSS: CSS.append(css)
    PAGES[n] = dict(t=title, b=body.replace('.dc.html', '.html'))
tpl = open('/home/claude/site-build/index.html', encoding='utf-8').read()
assert tpl.count('/*PAGES*/{}') == 1 and tpl.count('/*PAGECSS*/') == 1
import importlib.util
sp = importlib.util.spec_from_file_location('ur', '/home/claude/site-build/ur.py'); um = importlib.util.module_from_spec(sp); sp.loader.exec_module(um)
strs = json.load(open('/home/claude/site-build/strings.json'))
URD = {strs[i]: u for i, u in um.UR.items() if strs[i] != u}
URD.update(um.EXTRA)
URD.update({'Hyperactivity': 'حد سے زیادہ سرگرمی', 'Impulsivity': 'جلد بازی', 'Inattention': 'عدم توجہی', 'One or more of these, interfering with daily life.': 'ان میں سے ایک یا زیادہ، جو روزمرہ زندگی میں رکاوٹ بنتی ہیں۔', 'It also affects brain development, and executive functions like planning and focus.': 'یہ دماغ کی نشوونما اور انتظامی صلاحیتوں، جیسے منصوبہ بندی اور توجہ، پر بھی اثر انداز ہوتا ہے۔', 'Start: Consultation': 'شروع کریں: مشاورت', 'Listen is still in progress.': 'سننے کی سہولت پر ابھی کام جاری ہے۔'})
URD.update({'Sign up': 'سائن اپ', 'Continue as a guest ›': 'مہمان کے طور پر جاری رکھیں ›', 'Continue as a guest': 'مہمان کے طور پر جاری رکھیں', 'Just looking? Explore Khoj with sample children.': 'صرف دیکھنا چاہتے ہیں؟ نمونے کے بچوں کے ساتھ کھوج دیکھیں۔', 'Welcome back': 'خوش آمدید', 'Back': 'واپس', 'You’re a guest. The children and reports here are sample data.': 'آپ مہمان ہیں۔ یہاں کے بچے اور رپورٹس صرف نمونہ ہیں۔', 'Click, and Khoj will guide you by voice': 'کلک کریں، کھوج آواز سے رہنمائی کرے گا', 'Khoj hasn’t launched yet': 'کھوج ابھی باضابطہ شروع نہیں ہوا', 'This is a preview, so accounts and details aren’t saved. You can skip signing in.': 'یہ صرف ایک جھلک ہے، اس لیے اکاؤنٹ اور تفصیلات محفوظ نہیں ہوتیں۔ آپ سائن اِن چھوڑ سکتے ہیں۔', 'Skip signing in': 'سائن اِن چھوڑیں', 'Sign up anyway': 'پھر بھی سائن اپ کریں', '·': '·'})
missing = [s for i, s in enumerate(strs) if i not in um.UR]
print('untranslated:', missing)
tpl = tpl.replace("/*WIDEPATH*/''", json.dumps(open('/home/claude/site-build/widepath.html', encoding='utf-8').read(), ensure_ascii=False).replace('</', '<\\/'))
import base64, urllib.parse
ICD = '/home/claude/site-build/icon/'
b64 = lambda f: base64.b64encode(open(ICD + f, 'rb').read()).decode()
svgu = 'data:image/svg+xml,' + urllib.parse.quote(open(ICD + 'icon.svg').read())
man = {'name': 'Khoj', 'short_name': 'Khoj', 'description': 'Understanding ADHD, made easy', 'start_url': '.', 'display': 'standalone', 'background_color': '#FBF5F5', 'theme_color': '#9C4560',
       'icons': [{'src': 'data:image/png;base64,' + b64('icon-192.png'), 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any maskable'}, {'src': 'data:image/png;base64,' + b64('icon-512.png'), 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any maskable'}]}
icons = ('<link rel="icon" type="image/svg+xml" href="' + svgu + '">\n<link rel="icon" type="image/png" sizes="192x192" href="data:image/png;base64,' + b64('icon-192.png') + '">\n'
  '<link rel="apple-touch-icon" sizes="180x180" href="data:image/png;base64,' + b64('apple-180.png') + '">\n'
  '<link rel="manifest" href="data:application/manifest+json,' + urllib.parse.quote(json.dumps(man)) + '">\n'
  '<meta name="theme-color" content="#9C4560">\n<meta name="apple-mobile-web-app-title" content="Khoj">\n<meta name="application-name" content="Khoj">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-capable" content="yes">')
assert tpl.count('<!--ICONS-->') == 1
tpl = tpl.replace('<!--ICONS-->', icons)
assert tpl.count('/*UR*/{}') == 1
tpl = tpl.replace('/*UR*/{}', json.dumps(URD, ensure_ascii=False).replace('</', '<\\/'))
out = tpl.replace('/*PAGECSS*/', '\n'.join(CSS)).replace('/*PAGES*/{}', json.dumps(PAGES, ensure_ascii=False).replace('</', '<\\/'))
open(OUT + '/index.html', 'w', encoding='utf-8').write(out)
names = list(PAGES)
tot = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(OUT) for f in fs)
print(len(names), 'pages', tot // 1024, 'KB')
