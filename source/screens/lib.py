import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'project')
P = {
 'steps': '<path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"></path>',
 'child': '<circle cx="12" cy="8" r="4"></circle><path d="M4 20c1.5-4 5-5 8-5s6.5 1 8 5"></path>',
 'eye': '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"></path><circle cx="12" cy="12" r="3"></circle>',
 'leaf': '<path d="M5 19c0-8 5-14 14-14 0 9-6 14-14 14zM5 19l7-7"></path>',
 'right': '<path d="M9 6l6 6-6 6"></path>',
 'left': '<path d="M15 6l-6 6 6 6"></path>',
 'down': '<path d="M6 9l6 6 6-6"></path>',
 'up': '<path d="M6 15l6-6 6 6"></path>',
 'home': '<path d="M4 11l8-7 8 7v9h-5v-6H9v6H4z"></path>',
 'game': '<rect x="3" y="7" width="18" height="10" rx="3"></rect><path d="M8 10v4M6 12h4M16 12h.01"></path>',
 'report': '<path d="M7 3h7l4 4v14H7zM10 12h5M10 16h5"></path>',
 'sound': '<path d="M4 10v4h4l5 4V6L8 10zM17 9a4 4 0 0 1 0 6"></path>',
 'check': '<path d="M5 12l5 5 9-10"></path>',
 'globe': '<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"></path>',
}
def svg(name, size=24, sw=2):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (size, size, sw, P[name]))

def page(fname, title, fonts, link, hover, body, h=917, lang='en', rtl=False, css='', logic=None):
    html = ('<!doctype html>\n<html lang="%s"%s>\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?%s&amp;display=swap">\n<style>\nbody{margin:0}\na{color:%s}a:hover{color:%s}\n%s</style>\n</helmet>\n%s\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":412,"height":%d}}\'>\nclass Component extends DCLogic {\nrenderVals() {\nreturn {};\n}\n}\n</script>\n</body>\n</html>\n'
            ) % (lang, ' dir="rtl"' if rtl else '', title, fonts.replace('&', '&amp;'), link, hover, css, body, h)
    if logic: html = html.replace('class Component extends DCLogic {\nrenderVals() {\nreturn {};\n}\n}', logic)
    assert '&amp;amp;' not in html
    with open(os.path.join(ROOT, fname), 'w', encoding='utf-8') as f:
        f.write(html)
    print(fname, len(html))

# Shared, research-based copy (tightened, same meaning)
AREAS = [
 ('Pregnancy and birth history', ['Any complications during pregnancy?', "Mother's mental and physical health during pregnancy", 'Any complications during birth?', 'Premature birth or low birth weight']),
 ('Developmental history', []), ('Family history', []), ('Academic history', []), ('Social and home behaviour', []), ('Presenting complaints', []),
]
STEPS = ['Consultation', 'History-taking with parents', 'Clinical and behavioural interview', 'Baseline assessment', 'Formal ADHD assessment', 'Comparing with DSM-5 criteria', 'Outcome and next steps']
SIGNS = [
 ('Careless mistakes', 'Misses details in schoolwork or other tasks.'),
 ('Trouble staying focused', 'Loses focus in lessons, conversations or long reading. Gets distracted mid-task.'),
 ('Seems not to listen', 'Mind seems elsewhere, even when spoken to directly and with no obvious distraction.'),
 ('Easily distracted', 'Sounds, sights or thoughts pull attention away.'),
 ("Doesn't follow through", 'Starts homework or chores but leaves them unfinished.'),
 ('Struggles to organise', 'Finds order, tidiness, deadlines and time hard to manage.'),
 ('Avoids mental effort', 'Avoids tasks that need long thinking, like schoolwork or forms.'),
 ('Loses things', 'Often misplaces pencils, books, glasses or keys.'),
 ('Forgetful', 'Often forgets chores, errands or appointments.'),
]
EN = dict(lang='en', rtl=False, brand='Khoj', other='اردو', hello='Assalam-o-alaikum, Esha', ask='What would you like to understand today?',
  t1='How diagnosis works', d1='The steps clinicians follow in Pakistan.',
  t2='My children and reports', d2='Add a child and view their report.',
  t3='Signs to look for', d3='The DSM-5 criteria for ADHD, in plain words.',
  game='Dus Pattay', gsub='The game', gdesc='A 20-minute tablet game for children aged 8 to 12. It observes attention while your child plays.',
  connect='Connect', about='About the game', note='Khoj explains and guides. Only a clinician can diagnose.',
  home='Home', gnav='Game', rep='Reports', listen='Listen')
UR = dict(lang='ur', rtl=True, brand='کھوج', other='English', hello='السلام علیکم، ایشا', ask='آج آپ کیا جاننا چاہتے ہیں؟',
  t1='تشخیص کیسے ہوتی ہے', d1='پاکستان میں ماہرین کون سے مراحل اپناتے ہیں۔',
  t2='میرے بچے اور رپورٹس', d2='بچے کا پروفائل بنائیں اور رپورٹ دیکھیں۔',
  t3='کن علامات پر غور کریں', d3='ADHD کے DSM-5 معیار، آسان الفاظ میں۔',
  game='دس پتے', gsub='کھیل', gdesc='8 سے 12 سال کے بچوں کے لیے 20 منٹ کا ٹیبلٹ گیم۔ کھیل کے دوران بچے کی توجہ کا مشاہدہ کیا جاتا ہے۔',
  connect='جوڑیں', about='کھیل کے بارے میں', note='کھوج رہنمائی کرتا ہے۔ تشخیص صرف ماہر معالج کر سکتا ہے۔',
  home='ہوم', gnav='کھیل', rep='رپورٹس', listen='سنیں')
