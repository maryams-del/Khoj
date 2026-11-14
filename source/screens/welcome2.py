import json
from lib import *
BG, INK, MUT, PRI, TINT, SKY, LINE = '#FBF5F5', '#33202A', '#6A5560', '#9C4560', '#F6DFE5', '#DCEAF7', '#EBD6DC'
EN_F = "'Plus Jakarta Sans', system-ui, sans-serif"; UR_F = "'Noto Nastaliq Urdu', serif"
F = 'family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Noto+Nastaliq+Urdu:wght@400;700&family=Fraunces:opsz,wght@9..144,500'
TAG = f'<p style="margin: 0; font-size: 17px; line-height: 25px; text-align: center; color: {MUT}">Understanding ADHD, made easy</p>'
MARK = f'<h1 style="margin: 0; font-family: Fraunces, Georgia, serif; font-size: 68px; line-height: 72px; font-weight: 500; text-align: center; color: {PRI}">Khoj</h1>'
GLASS = 'background: rgba(255,255,255,0.55); -webkit-backdrop-filter: blur(18px); backdrop-filter: blur(18px); border: 1px solid rgba(255,255,255,0.9)'
def build(fname, title, decor, top):
    content = (f'<div style="position: relative; display: flex; flex-direction: column; gap: 14px; height: 100%">{top}'
      f'<div style="margin-top: auto; display: flex; flex-direction: column; gap: 10px"><span style="font-size: 13px; font-weight: 700; text-align: center">Choose your language</span>'
      f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px"><a href="#" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: {PRI}; color: #FFFFFF; text-decoration: none; font-size: 15px; font-weight: 700">English</a><a href="#" lang="ur" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: #FFFFFF; color: {INK}; text-decoration: none; font-family: {UR_F}; font-size: 18px">اردو</a></div>'
      f'<a href="Role.dc.html" style="display: flex; align-items: center; justify-content: center; height: 56px; margin-top: 8px; border-radius: 28px; border: 2px solid {PRI}; color: {PRI}; text-decoration: none; font-size: 15px; font-weight: 700">Begin exploring</a>'
      f'<p style="margin: 0; text-align: center; font-size: 14px; line-height: 44px">Already have an account? <a href="Login.dc.html" style="font-weight: 700">Log in</a></p></div></div>')
    body = f'<div style="position: relative; overflow: hidden; width: 412px; height: 917px; box-sizing: border-box; padding: 24px 20px 16px; background: {BG}; color: {INK}; font-family: {EN_F}"><div aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 412px; height: 917px">{decor}</div>{content}</div>'
    page(fname, title, F, PRI, INK, body)
def sh(st): return f'<span style="position: absolute; {st}"></span>'
# D: frosted glass panel over soft colour
dD = sh('left: -70px; top: 60px; width: 280px; height: 280px; border-radius: 50%; background: #EDB9C9; filter: blur(46px)') + sh('right: -70px; top: 250px; width: 260px; height: 260px; border-radius: 50%; background: #B3D0EE; filter: blur(46px)') + sh('left: 120px; top: 20px; width: 120px; height: 120px; border-radius: 50%; background: #F6DFE5; filter: blur(20px)')
tD = f'<div style="height: 150px"></div><div style="display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 36px 20px 30px; border-radius: 32px; {GLASS}; box-shadow: 0 20px 40px rgba(156,69,96,0.12)">{MARK}{TAG}</div>'
build('WelcomeD.dc.html', 'Welcome option D · Frosted glass', dD, tD)
# E: stacked panels with depth
tE = (f'<div style="height: 120px"></div><div style="position: relative; height: 300px">'
  f'<span aria-hidden="true" style="position: absolute; left: 30px; top: 26px; width: 312px; height: 240px; border-radius: 32px; background: {TINT}; transform: rotate(-8deg); box-shadow: 0 14px 24px rgba(51,32,42,0.08)"></span>'
  f'<span aria-hidden="true" style="position: absolute; left: 30px; top: 22px; width: 312px; height: 240px; border-radius: 32px; background: {SKY}; transform: rotate(5deg); box-shadow: 0 14px 24px rgba(51,32,42,0.08)"></span>'
  f'<div style="position: absolute; left: 30px; top: 24px; width: 312px; height: 240px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 32px; background: #FFFFFF; box-shadow: 0 26px 44px rgba(51,32,42,0.14)">{MARK}</div></div>{TAG}')
build('WelcomeE.dc.html', 'Welcome option E · Stacked panels', '', tE)
# F: soft 3D shapes behind a glass tile
def ball(x, y, s, a, b, c): return sh(f'left: {x}px; top: {y}px; width: {s}px; height: {s}px; border-radius: 50%; background: radial-gradient(circle at 32% 28%, #FFFFFF 0%, {a} 42%, {b} 100%); box-shadow: 0 {s // 6}px {s // 3}px {c}')
dF = (ball(50, 96, 160, '#F6DFE5', '#DDA3B6', 'rgba(156,69,96,0.22)') + ball(250, 70, 96, '#DCEAF7', '#9DBFE3', 'rgba(31,68,104,0.20)') + ball(292, 222, 50, '#F6DFE5', '#DDA3B6', 'rgba(156,69,96,0.20)')
  + sh('left: 96px; top: 262px; width: 128px; height: 46px; border-radius: 23px; background: linear-gradient(180deg, #EEF5FC 0%, #A9C7E6 100%); transform: rotate(-16deg); box-shadow: 0 12px 20px rgba(31,68,104,0.18)')
  + sh(f'left: 150px; top: 120px; width: 140px; height: 140px; border-radius: 30px; background: rgba(255,255,255,0.42); -webkit-backdrop-filter: blur(10px); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.95); transform: rotate(12deg); box-shadow: 0 16px 30px rgba(51,32,42,0.10)'))
tF = f'<div style="height: 330px"></div><div style="display: flex; flex-direction: column; align-items: center">{MARK}</div>{TAG}'
build('WelcomeF.dc.html', 'Welcome option F · Soft 3D shapes', dF, tF)
c = json.load(open('project/canvas.json'))
for i, (f, t) in enumerate([('WelcomeD.dc.html', 'Welcome option D · Frosted glass'), ('WelcomeE.dc.html', 'Welcome option E · Stacked panels'), ('WelcomeF.dc.html', 'Welcome option F · Soft 3D shapes')]):
    c['boards'][f] = dict(x=(i + 3) * 492, y=-1640, w=412, h=917, title=t, radius=28)
    if f not in c['order']: c['order'].append(f)
c['notes']['welcome'] = dict(x=0, y=-1920, text='Welcome screen · options to choose from', kind='title1', maxW=2860)
json.dump(c, open('project/canvas.json', 'w'), ensure_ascii=False, indent=1)
