"""Render assets/top-langs.svg from the bytes of code per language.

Sums GitHub's per-repository language breakdown across every non-fork repo
the user owns, so C++ inside a repo whose primary language is C still counts.
Uses STATS_TOKEN (a personal token) when set to include the user's private
repos, otherwise GITHUB_TOKEN and public repos only. Collaborator and
organisation repos are left out because their totals include other people's code.
"""
import json
import os
import urllib.request

USER = os.environ["USERNAME"]
TOKEN = os.environ.get("STATS_TOKEN") or os.environ["GITHUB_TOKEN"]
PRIVATE = bool(os.environ.get("STATS_TOKEN"))
EXCLUDE = {"HTML", "CSS", "Jupyter Notebook", "Makefile", "CMake", "Shell",
           "Batchfile", "PowerShell", "Dockerfile", "Linker Script", "Assembly",
           # Companion-app and web code; the card shows firmware languages.
           "Dart", "TypeScript", "JavaScript", "Swift", "Kotlin", "Objective-C", "Procfile"}
TOP = 8
COLORS = {"C": "#555555", "C++": "#f34b7d", "Python": "#3572A5", "Java": "#b07219",
          "GDScript": "#355570", "VHDL": "#adb2cb", "Dart": "#00B4AB",
          "JavaScript": "#f1e05a", "TypeScript": "#3178c6", "MATLAB": "#e16737",
          "BitBake": "#00bce4", "Kotlin": "#A97BFF", "Go": "#00ADD8", "Rust": "#dea584"}


def get(url):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def repos():
    base = ("https://api.github.com/user/repos?affiliation=owner&visibility=all"
            if PRIVATE else f"https://api.github.com/users/{USER}/repos?type=owner")
    page = 1
    while True:
        batch = get(f"{base}&per_page=100&page={page}")
        if not batch:
            return
        yield from batch
        page += 1


totals = {}
for repo in repos():
    if repo["fork"] or repo["archived"]:
        continue
    for lang, size in get(repo["languages_url"]).items():
        if lang not in EXCLUDE:
            totals[lang] = totals.get(lang, 0) + size

ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:TOP]
total = sum(size for _, size in ranked) or 1

W, ROW = 340, 30
H = 60 + ROW * len(ranked) + 10
rows = []
for i, (lang, size) in enumerate(ranked):
    pct = 100 * size / total
    y = 58 + i * ROW
    color = COLORS.get(lang, "#8b949e")
    bar = max(2, 190 * pct / 100)
    rows.append(
        f'<text x="25" y="{y}" class="lang">{lang}</text>'
        f'<rect x="25" y="{y + 7}" width="190" height="8" rx="4" fill="#21262d"/>'
        f'<rect x="25" y="{y + 7}" width="{bar:.1f}" height="8" rx="4" fill="{color}"/>'
        f'<text x="228" y="{y + 15}" class="pct">{pct:.1f}%</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .title {{ font: 600 18px 'Segoe UI', Ubuntu, sans-serif; fill: #58a6ff; }}
  .lang {{ font: 400 13px 'Segoe UI', Ubuntu, sans-serif; fill: #c9d1d9; }}
  .pct {{ font: 400 12px 'Segoe UI', Ubuntu, sans-serif; fill: #8b949e; }}
</style>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="6" fill="#0d1117" stroke="#2e343b"/>
<text x="25" y="34" class="title">Most Used Languages</text>
{"".join(rows)}
</svg>
'''
os.makedirs("assets", exist_ok=True)
with open("assets/top-langs.svg", "w") as f:
    f.write(svg)
print("\n".join(f"{lang}: {size}" for lang, size in ranked))
