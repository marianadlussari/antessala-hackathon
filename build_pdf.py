#!/usr/bin/env python3
"""Gera um PDF unico do kit de ICP do Antessala."""
import os, shutil, subprocess, sys, markdown

BASE = os.path.dirname(os.path.abspath(__file__))


def find_chrome():
    """Localiza um Chrome/Chromium headless em qualquer maquina."""
    env = os.environ.get("CHROME_PATH")
    if env and os.path.exists(env):
        return env
    for name in ("chromium", "chromium-browser", "google-chrome",
                 "google-chrome-stable", "chrome", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    for path in (
        "/opt/pw-browsers/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    ):
        if os.path.exists(path):
            return path
    sys.exit("Chrome/Chromium nao encontrado. Instale um ou defina CHROME_PATH=/caminho/do/chrome")
OUT = os.path.join(BASE, "Kit-ICP-Antessala.pdf")
TMP = os.path.join(BASE, "_tmp")
os.makedirs(TMP, exist_ok=True)

DOCS = [
    ("DOSSIE-HANDOFF.md", "Dossiê de handoff"),
    ("README.md", "Diagnóstico e prioridades"),
    ("prompt-versao-hackathon.md", "Prompt · versão hackathon"),
    ("achados-pesquisa-publica.md", "Achados da pesquisa pública"),
    ("achados-gatilhos-mercado.md", "Gatilhos observáveis e tamanho de mercado"),
    ("jornada-do-cliente.md", "Jornada do cliente · índice de decisões"),
    ("jornada-produto-pm.md", "Jornada · definição de produto"),
    ("jornada-superficie-ux.md", "Jornada · superfície do brief"),
    ("simulacoes-jornada.md", "Jornada · três simulações"),
    ("roteiro-entrevistas-primarias.md", "Roteiro de entrevistas"),
    ("contexto-antessala.md", "Contexto do Antessala"),
    ("prompt-deep-research-icp.md", "Prompt mestre"),
]

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif;
       font-size: 10.2pt; line-height: 1.55; color: #1c1c1e; margin: 0; }
h1 { font-size: 20pt; margin: 0 0 4pt; color: #0f172a; letter-spacing: -0.4pt;
     border-bottom: 2.5px solid #0f172a; padding-bottom: 6pt; }
h2 { font-size: 13.5pt; margin: 20pt 0 6pt; color: #0f172a; page-break-after: avoid;
     border-left: 3px solid #d97706; padding-left: 8pt; }
h3 { font-size: 11pt; margin: 14pt 0 4pt; color: #334155; page-break-after: avoid; }
p, li { orphans: 2; widows: 2; }
ul, ol { padding-left: 18pt; margin: 6pt 0; }
li { margin: 2.5pt 0; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 8.8pt;
        page-break-inside: avoid; }
th { background: #0f172a; color: #fff; text-align: left; padding: 5pt 7pt; font-weight: 600; }
td { border-bottom: 1px solid #e2e8f0; padding: 5pt 7pt; vertical-align: top; }
tr:nth-child(even) td { background: #f8fafc; }
code { font-family: 'SF Mono', Menlo, Consolas, monospace; font-size: 8.6pt;
       background: #f1f5f9; padding: 1pt 3pt; border-radius: 3px; color: #b45309; }
pre { background: #f8fafc; border: 1px solid #e2e8f0; border-left: 3px solid #64748b;
      padding: 8pt 10pt; border-radius: 4px; overflow: hidden;
      page-break-inside: avoid; font-size: 8.4pt; }
pre code { background: none; color: #334155; padding: 0; }
blockquote { border-left: 3px solid #d97706; background: #fffbeb; margin: 8pt 0;
             padding: 6pt 12pt; color: #78350f; page-break-inside: avoid; }
blockquote p { margin: 3pt 0; }
hr { border: none; border-top: 1px solid #e2e8f0; margin: 16pt 0; }
strong { color: #0f172a; }
.doc { page-break-before: always; }
.doc:first-child { page-break-before: avoid; }
.cover { page-break-after: always; text-align: left; padding-top: 55mm; }
.cover .kicker { font-size: 9pt; letter-spacing: 2.5pt; text-transform: uppercase;
                 color: #d97706; font-weight: 700; }
.cover h1 { font-size: 34pt; border: none; margin: 10pt 0 0; line-height: 1.1; }
.cover .sub { font-size: 12pt; color: #64748b; margin-top: 10pt; max-width: 120mm; }
.cover .rule { width: 60mm; height: 3px; background: #0f172a; margin: 22pt 0; }
.cover .meta { font-size: 9pt; color: #94a3b8; line-height: 1.9; }
"""

def render(md_text):
    return markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])

parts = ["""<div class="cover">
<div class="kicker">Pesquisa de ICP · B2B</div>
<h1>Kit de Deep Research<br>de ICP</h1>
<div class="sub">Como fechar as lacunas do V3 com evidência rastreável — priorizado pelo que realmente vale nota.</div>
<div class="rule"></div>
<div class="meta">Antessala · Sales Intelligence<br>Prioridades · Prompts · Roteiro de entrevistas</div>
</div>"""]

for fname, _label in DOCS:
    with open(os.path.join(BASE, fname), encoding="utf-8") as fh:
        parts.append('<div class="doc">' + render(fh.read()) + '</div>')

html = ("<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'>"
        f"<title>Kit de Deep Research de ICP</title><style>{CSS}</style></head>"
        f"<body>{''.join(parts)}</body></html>")

html_path = os.path.join(TMP, "icp.html")
with open(html_path, "w", encoding="utf-8") as fh:
    fh.write(html)

subprocess.run([
    find_chrome(), "--headless", "--no-sandbox",
    "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=4000",
    f"--print-to-pdf={OUT}", f"file://{html_path}",
], check=True, capture_output=True)
print("PDF gerado:", OUT, os.path.getsize(OUT), "bytes")
