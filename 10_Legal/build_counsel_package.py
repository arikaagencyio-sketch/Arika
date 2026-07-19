"""Convert the counsel package from Markdown to styled HTML, ready for Word.

Everything runs locally. Tables and headings survive the trip, which is the whole
point -- the contract drafts are mostly tables and clause hierarchies.
"""
import pathlib
import markdown

REPO = pathlib.Path(r"C:\Users\USER\OneDrive\Documents\The Agency Drafts\10_Legal")
OUT = REPO / "_counsel_package"
OUT.mkdir(exist_ok=True)

CSS = """
body { font-family: Calibri, Arial, sans-serif; font-size: 11pt; line-height: 1.45;
       max-width: 7in; color: #000; }
h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 6px; }
h2 { font-size: 15pt; margin-top: 22px; border-bottom: 1px solid #bbb; padding-bottom: 3px; }
h3 { font-size: 12.5pt; margin-top: 16px; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; }
th, td { border: 1px solid #888; padding: 6px 8px; text-align: left; vertical-align: top;
         font-size: 10.5pt; }
th { background: #e8e8e8; font-weight: bold; }
code { font-family: Consolas, monospace; font-size: 10pt; background: #f2f2f2; padding: 1px 3px; }
blockquote { border-left: 3px solid #999; margin-left: 0; padding-left: 12px; color: #333; }
hr { border: none; border-top: 1px solid #ccc; margin: 20px 0; }
"""

FILES = [
    ("COUNSEL_ENGAGEMENT_BRIEF.md", "00 - Instruction Brief - Arika Agency"),
    ("LEGAL_RESEARCH.md",           "01 - Research Note (AI desk research - verify)"),
    ("templates/MSA.md",            "02 - DRAFT - Master Services Agreement"),
    ("templates/SOW_TEMPLATE.md",   "03 - DRAFT - Statement of Work"),
    ("templates/DPA.md",            "04 - DRAFT - Data Processing Agreement"),
    ("templates/NDA.md",            "05 - DRAFT - NDA"),
    ("templates/IP_COPYRIGHT_TRADEMARK_TERMS.md", "06 - DRAFT - IP, Copyright, Trademark"),
    ("templates/API_AND_AI_TOOLING_TERMS.md",     "07 - DRAFT - API and AI Tooling Terms"),
    ("templates/CLAIMS_SUBSTANTIATION_POLICY.md", "08 - DRAFT - Claims Substantiation Policy"),
]

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])

for src, title in FILES:
    path = REPO / src
    if not path.exists():
        print(f"  MISSING {src}")
        continue
    body = md.reset().convert(path.read_text(encoding="utf-8"))
    html = (
        f'<!DOCTYPE html>\n<html><head><meta charset="utf-8">'
        f"<title>{title}</title><style>{CSS}</style></head><body>\n{body}\n</body></html>"
    )
    dest = OUT / f"{title}.html"
    dest.write_text(html, encoding="utf-8")
    print(f"  {dest.name}")

print(f"\nHTML written to: {OUT}")
