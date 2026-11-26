<p align="center"><a href="#demo"><picture>
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner-light.png">
  <img alt="Data on the Map: the world explained with data, the channel's home and legal pages" src="docs/images/banner.png" width="100%">
</picture></a></p>

<p align="center"><b>The world explained with data. The public home and legal pages of the channel.</b><br>
<a href="#how-to-build">Install</a> · <a href="#demo">Demo</a> · <a href="#how-it-works">How it works</a> · <a href="build.py">Source</a></p>

<p align="center">
  <img alt="static HTML" src="https://img.shields.io/badge/site-static%20HTML-f16554?style=flat-square&labelColor=1a1a1a">
  <img alt="Python stdlib" src="https://img.shields.io/badge/build-python3%20stdlib-f16554?style=flat-square&labelColor=1a1a1a">
  <img alt="trackers: 0" src="https://img.shields.io/badge/trackers-0-f16554?style=flat-square&labelColor=1a1a1a">
  <img alt="hosting: GitHub Pages" src="https://img.shields.io/badge/hosting-GitHub%20Pages-f16554?style=flat-square&labelColor=1a1a1a">
</p>

# Data on the Map: website

Public home, Privacy Policy and Terms of Service for the Data on the Map channel and its internal publisher app.
TikTok, Meta and Google point their app listings at these pages. Plain HTML/CSS: no cookies, no analytics, no trackers,
no third-party requests.

- Edit `build.py` (shared header and footer, page text, contact email), then run `python3 build.py`.
- `assets/app-icon-1024.png` is the 1024x1024 app icon (TikTok). `favicon.png` and `assets/logo-120.png` are made from
  brand logo A (`lagowski/dataonthemap-studio` `brand/avatar_light_1080.png`).
- `tiktok-callback/` only displays the one-time code TikTok returns; it sends nothing anywhere.
- No secret ever goes in this repo.

## How to build

```bash
python3 build.py                  # writes index.html, privacy/, terms/, tiktok-callback/
python3 -m http.server 8000       # preview at http://localhost:8000
```

## Demo

<p align="center"><img alt="The Data on the Map home page and terms page" src="docs/images/demo.gif" width="900"></p>

<sub>Real pages, served locally from this repo: the home page and the terms page.</sub>

## How it works

<p align="center"><img alt="How the site is built and used" src="docs/images/how-it-works.png" width="100%"></p>

`build.py` writes the four pages with one shared header and footer. GitHub Pages serves them as plain files, and the
TikTok, Meta and Google app listings of the internal publisher app link to the privacy and terms pages. Nothing on the
pages calls a third party.
