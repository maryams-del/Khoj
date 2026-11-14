# Khoj

Khoj is a parent-education app about ADHD for families and teachers in Pakistan. It explains how ADHD is diagnosed, shows the DSM-5 criteria in plain words, and is the companion to **Dus Pattay**, a 20-minute screening game for children aged 8 to 12.

This repository holds the clickable prototype of Khoj.

**Live site:** https://khoj-for-dus-pattay.vercel.app

The site deploys automatically on Vercel whenever `main` changes.

## What is here

| Path | What it is |
| --- | --- |
| `index.html` | The whole prototype as one self-contained page. This is the file deployed to Vercel. |
| `source/screens/` | Python scripts that generate every phone screen (`gen.py`, with shared pieces in `lib.py`). |
| `source/site/` | The script that turns the screens into `index.html` (`build.py`), the page shell (`shell.html`), and the Urdu text (`ur.py`, keyed to `strings.json`). |
| `source/icon/` | The Khoj icon: a serif K with a leaf beside it. |

## How the prototype behaves

- **Phone:** runs the full phone flow, starting from the welcome screen.
- **Laptop:** opens with a welcome card (log in, sign up, or continue as a guest). After that, Home stays on the left and whatever is opened appears on the right.
- **Urdu:** the Urdu button switches every screen.
- **Nothing is saved.** There is no backend; accounts, children and reports are sample data.

## Status and known gaps

- This is a prototype, not the released app. Listen, Ask Khoj (voice), uploads and sharing show a "Feature in progress" message.
- The Urdu text is a first draft and needs review by a native speaker, especially the clinical terms.
- On a laptop, only the diagnostic path has a layout designed for a wide screen. Other pages are the phone layout stretched wider.
- The home-screen icon is embedded in the page and has not been tested on a real phone.

## Rebuilding

The scripts were written to run in one fixed workspace, so the folder paths at the top of `gen.py`, `lib.py` and `build.py` need changing to match your machine before they will run. After that:

```
python3 source/screens/gen.py   # writes one file per screen
python3 source/site/build.py    # combines them into index.html
```

Khoj does not diagnose. Only a clinician can diagnose ADHD.
