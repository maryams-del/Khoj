import json, math
from lib import *
BG, INK, MUT, PRI, TINT, SKY, LINE = '#FBF5F5', '#33202A', '#6A5560', '#9C4560', '#F6DFE5', '#DCEAF7', '#EBD6DC'
EN_F = "'Plus Jakarta Sans', system-ui, sans-serif"; UR_F = "'Noto Nastaliq Urdu', serif"
def build(fname, title, fontq, decor, mark):
    F = 'family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Noto+Nastaliq+Urdu:wght@400;700&' + fontq
    content = (f'<div style="position: relative; display: flex; flex-direction: column; gap: 14px; height: 100%">'
      f'<div style="height: 330px"></div>{mark}'
      f'<p style="margin: 0; font-size: 17px; line-height: 25px; text-align: center; color: {MUT}">Understanding ADHD, made easy</p>'
      f'<div style="margin-top: auto; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 13px; font-weight: 700; text-align: center">Choose your language</span>'
      f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px"><a href="#" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: {PRI}; color: #FFFFFF; text-decoration: none; font-size: 15px; font-weight: 700">English</a><a href="#" lang="ur" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: #FFFFFF; color: {INK}; text-decoration: none; font-family: {UR_F}; font-size: 18px">اردو</a></div>'
      f'<a href="Role.dc.html" style="display: flex; align-items: center; justify-content: center; height: 56px; margin-top: 8px; border-radius: 28px; border: 2px solid {PRI}; color: {PRI}; text-decoration: none; font-size: 15px; font-weight: 700">Begin exploring</a>'
      f'<p style="margin: 0; text-align: center; font-size: 14px; line-height: 44px">Already have an account? <a href="Login.dc.html" style="font-weight: 700">Log in</a></p></div></div>')
    body = f'<div style="position: relative; overflow: hidden; width: 412px; height: 917px; box-sizing: border-box; padding: 24px 20px 16px; background: {BG}; color: {INK}; font-family: {EN_F}"><div aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 412px; height: 917px">{decor}</div>{content}</div>'
    page(fname, title, F, PRI, INK, body)
def sh(st): return f'<span style="position: absolute; {st}"></span>'
ur = lambda c: ''
# A: quiet rings
dA = sh(f'right: -150px; top: -150px; width: 400px; height: 400px; border-radius: 50%; border: 2px solid {TINT}') + sh(f'right: -90px; top: -90px; width: 280px; height: 280px; border-radius: 50%; border: 2px solid {TINT}') + sh(f'right: -40px; top: -40px; width: 180px; height: 180px; border-radius: 50%; background: {TINT}') + sh(f'left: -70px; top: 250px; width: 140px; height: 140px; border-radius: 50%; border: 2px solid {SKY}') + sh(f'left: 40px; top: 228px; width: 14px; height: 14px; border-radius: 50%; background: {SKY}')
mA = f'<div style="display: flex; flex-direction: column; align-items: center"><h1 style="margin: 0; font-family: Fraunces, Georgia, serif; font-size: 68px; line-height: 72px; font-weight: 500; color: {PRI}">Khoj</h1>{ur(MUT)}</div>'
build('WelcomeA.dc.html', 'Welcome option A · Rings', 'family=Fraunces:opsz,wght@9..144,500', dA, mA)
# B: ten leaves (Dus Pattay)
L = [(40, 70, 46, -30, TINT), (120, 40, 30, 20, SKY), (200, 90, 54, -50, TINT), (290, 50, 34, 35, LINE), (350, 120, 44, -15, SKY), (70, 170, 30, 60, SKY), (150, 200, 40, -70, LINE), (250, 190, 28, 10, TINT), (330, 230, 36, 50, TINT), (30, 270, 24, -40, LINE)]
dB = ''.join(sh(f'left: {x}px; top: {y}px; width: {s}px; height: {s}px; border-radius: 70% 0 70% 0; background: {c}; transform: rotate({r}deg)') for x, y, s, r, c in L)
mB = f'<h1 style="margin: 0; font-family: Outfit, sans-serif; font-size: 70px; line-height: 76px; font-weight: 300; letter-spacing: 0.06em; text-align: center; color: {INK}">khoj</h1>'
build('WelcomeB.dc.html', 'Welcome option B · Ten leaves', 'family=Outfit:wght@300', dB, mB)
# C: a dotted path (khoj means search)
dC = ''
for i in range(16):
    t = i / 15; x = 24 + t * 330; y = 250 - 150 * t - 46 * math.sin(t * math.pi * 2.2); s = 6 + round(t * 8)
    dC += sh(f'left: {x:.0f}px; top: {y:.0f}px; width: {s}px; height: {s}px; border-radius: 50%; background: {SKY if i % 3 == 1 else TINT if i < 12 else "#E3B9C6"}')
dC += sh(f'left: 352px; top: 58px; width: 34px; height: 34px; border-radius: 50%; background: {PRI}')
mC = f'<div style="display: flex; flex-direction: column; align-items: center"><h1 style="margin: 0; font-family: Marcellus, Georgia, serif; font-size: 64px; line-height: 70px; font-weight: 400; letter-spacing: 0.02em; color: {PRI}">Khoj</h1>{ur(MUT)}</div>'
build('WelcomeC.dc.html', 'Welcome option C · A path', 'family=Marcellus', dC, mC)
c = json.load(open('project/canvas.json'))
for i, (f, t) in enumerate([('WelcomeA.dc.html', 'Welcome option A · Rings'), ('WelcomeB.dc.html', 'Welcome option B · Ten leaves'), ('WelcomeC.dc.html', 'Welcome option C · A path')]):
    c['boards'][f] = dict(x=i * 492, y=-1640, w=412, h=917, title=t, radius=28)
    if f not in c['order']: c['order'].append(f)
c['notes']['welcome'] = dict(x=0, y=-1920, text='Welcome screen · three options to choose from', kind='title1', maxW=1400)
json.dump(c, open('project/canvas.json', 'w'), ensure_ascii=False, indent=1)
