"""Builds the static pages from one shared header/footer. Run: python3 build.py  (no dependencies, no trackers)."""

from pathlib import Path

EMAIL = "ainews402@gmail.com"
UPDATED = "October 8, 2026"
ROOT = Path(__file__).parent

PROFILES = [
    ("YouTube @dataonthemap", "https://www.youtube.com/@dataonthemap"),
    ("TikTok @thedataonthemap", "https://www.tiktok.com/@thedataonthemap"),
    ("Instagram @dataonthemap", "https://www.instagram.com/dataonthemap/"),
    ("Facebook", "https://www.facebook.com/dataonthemap"),
]


def page(path: str, title: str, description: str, body: str, robots: str = "") -> None:
    up = "../" if path else ""                         # one level deep; relative links work under /dataonthemap-site/
    mail = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{description}">{robots}
<link rel="icon" href="{up}favicon.png"><link rel="stylesheet" href="{up}style.css"></head><body><div class="wrap">
<header><a class="brand" href="{up or './'}"><img src="{up}assets/logo-120.png" alt="Data on the Map logo" width="40" height="40">Data on the Map</a>
<nav><a href="{up or './'}">Home</a><a href="{up}privacy/">Privacy</a><a href="{up}terms/">Terms</a></nav></header>
{body.replace("{MAIL}", mail).replace("{UPDATED}", UPDATED).replace("{UP}", up)}
<footer><a href="{up or './'}">Home</a><a href="{up}privacy/">Privacy Policy</a><a href="{up}terms/">Terms of Service</a><br>
&copy; 2026 Data on the Map &middot; Contact: {mail}</footer></div></body></html>
"""
    out = ROOT / path / "index.html" if path else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


follow = " &middot; ".join(f'<a href="{u}">{n}</a>' for n, u in PROFILES)

page("", "Data on the Map - the world explained with data",
     "Short videos that explain the world with data on a 3D globe, every claim with its source.", f"""
<h1>The world explained with data.</h1>
<p class="lead">Data on the Map makes short videos that explain what is happening in the world (markets, natural events,
country comparisons and popular questions) with data on a 3D globe. Every number on screen comes with its source.</p>
<div class="card"><h2>What the Data on the Map app does</h2>
<p>The Data on the Map Publisher app is an internal publishing tool used only by the Data on the Map team. It lets us:</p>
<ul><li>upload our own finished videos, with their titles and descriptions, to our own YouTube channel, TikTok account,
Instagram account and Facebook Page;</li>
<li>read our own accounts' basic information and the statistics of our own videos, to check that uploads worked and to
learn which videos people find useful.</li></ul>
<p>The app does not offer accounts to the public and does not access anyone else's data.</p></div>
<div class="card"><h2>Follow Data on the Map</h2><p>{follow}</p></div>
<p>Read our <a href="privacy/">Privacy Policy</a> and <a href="terms/">Terms of Service</a>. Questions: {{MAIL}}.</p>
""")

page("privacy", "Privacy Policy - Data on the Map", "How the Data on the Map app handles data.", """
<h1>Privacy Policy</h1><p class="lead">Effective date: {UPDATED}</p>
<p>This policy explains how Data on the Map ("we", "us") handles information when the Data on the Map Publisher app
accesses YouTube, TikTok, Instagram and Facebook on our behalf. Data on the Map is operated from Spain.
Contact: {MAIL}.</p>
<h2>Who uses the app</h2><p>The app is an internal tool. It is used only by the Data on the Map team to publish our own
videos to our own accounts. It is not offered to the public, and it has no third-party users.</p>
<h2>Data we access</h2><p>When a team member signs in and grants permission, the app may access, for our own accounts only:</p>
<ul><li><strong>YouTube</strong> (scopes <code>youtube.upload</code> and <code>youtube</code>): permission to upload videos
to our own channel and to read our own channel's information and video statistics.</li>
<li><strong>TikTok</strong> (scopes <code>user.info.basic</code> and <code>video.upload</code>): permission to read our own
account's basic profile and to send videos we made to our own TikTok inbox as drafts. We review and publish every draft
ourselves in the TikTok app.</li>
<li><strong>Instagram and Facebook</strong> (permissions <code>instagram_basic</code>, <code>instagram_content_publish</code>,
<code>pages_show_list</code>, <code>pages_read_engagement</code>, <code>pages_manage_posts</code>): permission to publish
our own videos to our own Instagram account and Facebook Page and to read their basic information and engagement.</li></ul>
<h2>How we use it</h2><p>We use this access only to publish Data on the Map videos on our own accounts and to measure how
our own videos perform. We do not use it for advertising, we do not sell it, and we do not share it with third parties
except as needed to deliver it to the platforms themselves.</p>
<h2>Google API Services User Data Policy</h2><p>Data on the Map's use and transfer of information received from Google
APIs adheres to the <a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services User
Data Policy</a>, including the Limited Use requirements. The app uses the
<a href="https://developers.google.com/youtube/terms/api-services-terms-of-service">YouTube API Services</a>; by using the
app you also agree to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a> and the
<a href="https://policies.google.com/privacy">Google Privacy Policy</a>.</p>
<h2>TikTok</h2><p>Our use of TikTok follows the
<a href="https://www.tiktok.com/legal/page/global/tik-tok-developer-terms-of-service/en">TikTok Developer Terms of
Service</a>. We do not collect data about other TikTok users. Access can be revoked in the TikTok app under Settings and
privacy &rarr; Security &rarr; Apps and services.</p>
<h2>Meta (Instagram and Facebook)</h2><p>Our use of Instagram and Facebook follows the
<a href="https://developers.facebook.com/terms/">Meta Platform Terms</a>. Access can be removed in Facebook under Settings
&rarr; Business integrations.</p>
<h2>Storage and security</h2><p>Access tokens are stored privately on infrastructure controlled by Data on the Map, are
never shared or sold, and are used only for the actions described above. The app does not collect personal data about
viewers or other users. This website uses no cookies, no analytics and no trackers.</p>
<h2>Retention and deletion</h2><p>We keep tokens only while the app is in use. Google access can be revoked at any time at
<a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a>. To ask us to delete any stored
data, email {MAIL}; we will do so within 30 days.</p>
<h2>Your rights</h2><p>Under the GDPR you may request access to, correction of or deletion of your personal data, and you
may complain to the Spanish Data Protection Agency (AEPD).</p>
<h2>Changes</h2><p>If this policy changes, we will update this page and the date above.</p>
""")

page("terms", "Terms of Service - Data on the Map", "Terms for the Data on the Map app and website.", """
<h1>Terms of Service</h1><p class="lead">Effective date: {UPDATED}</p>
<p>These terms apply to the Data on the Map website and the Data on the Map Publisher app. By using them you agree to
these terms.</p>
<h2>The service</h2><p>The Data on the Map Publisher app is an internal tool used by the Data on the Map team to publish
our own videos to our own YouTube channel, TikTok account, Instagram account and Facebook Page. It has no third-party
users; access is limited to authorized team members.</p>
<h2>Third-party services</h2><p>The app uses YouTube API Services, TikTok's Content Posting API and Meta's Graph API. Its
use is also subject to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a>, the
<a href="https://policies.google.com/privacy">Google Privacy Policy</a>, the
<a href="https://www.tiktok.com/legal/page/global/terms-of-service/en">TikTok Terms of Service</a> and the
<a href="https://developers.facebook.com/terms/">Meta Platform Terms</a>.</p>
<h2>Acceptable use</h2><p>You may not use the app to upload content you do not have the rights to, to violate any
platform's policies, or to access accounts or data that are not yours.</p>
<h2>Content</h2><p>Data on the Map videos, texts and artwork are ours unless stated otherwise. The data we show belongs to
the sources we cite on screen. Our videos are informative; they are not financial, legal or investment advice.</p>
<h2>No warranty</h2><p>The website and app are provided "as is", without warranties of any kind. To the extent permitted by
law, Data on the Map is not liable for indirect or consequential damages arising from their use.</p>
<h2>Changes and termination</h2><p>We may change these terms or discontinue the app at any time. Changes will be posted on
this page.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of Spain.</p>
<h2>Contact</h2><p>{MAIL}</p>
""")

page("tiktok-callback", "Authorization - Data on the Map", "Data on the Map app authorization callback.", """
<h1>Authorization</h1>
<p id="msg" class="lead">Reading the authorization response&hellip;</p>
<p><textarea id="code" readonly rows="3" hidden></textarea></p>
<p><button id="copy" hidden>Copy code</button></p>
<p>This page only shows the one-time code that TikTok returns after you authorize the Data on the Map app. It sends
nothing anywhere. Copy the code into the setup step within a few minutes; it expires and works only once.</p>
<script>
const q = new URLSearchParams(location.search), msg = document.getElementById('msg'), box = document.getElementById('code'), btn = document.getElementById('copy');
if (q.get('error')) { msg.textContent = 'TikTok returned an error: ' + q.get('error') + ' ' + (q.get('error_description') || ''); }
else if (q.get('code')) { msg.textContent = 'Authorized. State: ' + (q.get('state') || '(none)') + '. Code:'; box.value = q.get('code'); box.hidden = btn.hidden = false;
  btn.onclick = () => { box.select(); navigator.clipboard ? navigator.clipboard.writeText(box.value) : document.execCommand('copy'); btn.textContent = 'Copied'; }; }
else { msg.textContent = 'No authorization code in this address.'; }
</script>
""", robots='<meta name="robots" content="noindex">')
print("built: index.html, privacy/, terms/, tiktok-callback/")
