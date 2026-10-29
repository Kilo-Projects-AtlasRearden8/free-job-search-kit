"""Verification script for the Free Job-Search Kit.

Checks:
- LICENSE contains the exact copyright line
- README credits Asdale Dynamics, LLC
- Every HTML file is well-formed (html.parser)
- Every HTML references the shared stylesheet
- Print media query present in CSS
- Required sections present in each Markdown file
- No .github/workflows directory
- No obvious secret patterns in any file
"""
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
failures = []


def fail(msg):
    failures.append(msg)
    print(f"FAIL: {msg}")


def ok(msg):
    print(f"ok: {msg}")


# 1. LICENSE exact copyright line
license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
EXACT = "Copyright (c) 2026 Asdale Dynamics, LLC"
if EXACT not in license_text:
    fail(f"LICENSE missing exact line: {EXACT!r}")
else:
    ok("LICENSE contains exact copyright line")

# 2. README credits
readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
if "Asdale Dynamics, LLC" not in readme_text:
    fail("README does not credit Asdale Dynamics, LLC")
else:
    ok("README credits Asdale Dynamics, LLC")

# 3-6. HTML files
html_files = sorted((ROOT / "printable").glob("*.html"))
if not html_files:
    fail("No HTML files found in printable/")
for path in html_files:
    text = path.read_text(encoding="utf-8")

    # well-formed HTML
    class CheckParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.errors = []

        def error(self, message):
            self.errors.append(message)

    parser = CheckParser()
    parser.feed(text)
    if parser.errors:
        fail(f"{path.name}: HTML parse errors: {parser.errors[:3]}")
    else:
        ok(f"{path.name}: well-formed HTML")

    # references styles.css
    if "styles.css" not in text:
        fail(f"{path.name}: does not reference styles.css")
    else:
        ok(f"{path.name}: references styles.css")

# print media query in CSS
css_text = (ROOT / "printable/styles.css").read_text(encoding="utf-8")
if "@media print" not in css_text:
    fail("CSS missing @media print")
else:
    ok("CSS has @media print")

# 7. Required sections in Markdown files
md_requirements = {
    "kit/resume-template.md": ["Template", "Example", "Quick checklist"],
    "kit/cover-letter-template.md": ["Template", "Example", "Quick checklist"],
    "kit/interview-prep.md": ["STAR", "Questions to ask them"],
    "kit/application-tracker.md": ["Tracker table", "Status ideas"],
    "kit/networking-emails.md": ["Reaching out", "referral", "Thank-you"],
}
for md_file, required in md_requirements.items():
    text = (ROOT / md_file).read_text(encoding="utf-8")
    for req in required:
        if req not in text:
            fail(f"{md_file}: missing required section {req!r}")
        else:
            ok(f"{md_file}: contains {req!r}")

# 8. No .github/workflows
if (ROOT / ".github" / "workflows").exists():
    fail(".github/workflows exists (must not)")
else:
    ok("No .github/workflows directory")

# 9. No obvious secret patterns anywhere
import re
secret_patterns = [r"sk-[A-Za-z0-9]{20,}", r"AKIA[0-9A-Z]{16}", r"[0-9]{3}-[0-9]{2}-[0-9]{4}"]
for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".md", ".html", ".css", ".py", ".txt", ".json"}:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pat in secret_patterns:
            if re.search(pat, text):
                fail(f"{path.relative_to(ROOT)}: possible secret pattern {pat!r}")
if not any("possible secret pattern" in f for f in failures):
    ok("No obvious secret patterns in text files")

print()
if failures:
    print(f"VERIFICATION FAILED: {len(failures)} issue(s)")
    raise SystemExit(1)
print(f"VERIFICATION PASSED: {len(html_files)} HTML files, {len(md_requirements)} Markdown files checked")
