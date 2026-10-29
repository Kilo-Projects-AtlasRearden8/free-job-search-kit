# STATUS

## What was built

A free, printable, no-account-needed job-search kit for Asdale Dynamics, LLC,
built entirely in the current folder (`/workspace/kilo-lab/free-job-search-kit`).
No remote repository was created and nothing was pushed or published.

### Contents

- `LICENSE` — MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — kit overview, credits Asdale Dynamics, LLC, how to use, license
- `kit/resume-template.md` — resume template, filled-out example, checklist
- `kit/cover-letter-template.md` — cover letter template, example, checklist
- `kit/interview-prep.md` — STAR method, common questions, questions to ask the interviewer
- `kit/application-tracker.md` — tracker table template, status ideas, tips
- `kit/networking-emails.md` — four email scripts (reaching out, referral, follow-up, thank-you) plus tips
- `printable/styles.css` — shared print styles with `@media print`, US Letter page size
- `printable/resume.html` — printable resume page
- `printable/cover-letter.html` — printable cover letter page
- `printable/interview-prep.html` — printable interview prep page
- `printable/application-tracker.html` — printable tracker page
- `printable/networking-emails.html` — printable email scripts page
- `printable/kit-all.html` — all-in-one printable page (every resource, one file)
- `printable/index.html` — kit landing page linking every resource
- `verify.py` — verification script

All examples use placeholders (e.g. `[Your Name]`, `[Company]`). No secrets, API
keys, or personal data are stored in any file. No `.github/workflows` files were
added. Nothing was pushed; no remote repository exists.

## How to run it

1. Open the folder: `cd /workspace/kilo-lab/free-job-search-kit`
2. Read the Markdown sources in `kit/` on any device, or
3. Open any file in `printable/` in a web browser and press `Ctrl+P` (or
   `Cmd+P`) to print. Each page is styled for clean printing with page breaks
   between sections. `printable/kit-all.html` prints the entire kit in one file.
4. Fill in the bracketed placeholders with your own details and save copies
   locally. Nothing is sent anywhere.

### Verification

Run `python3 verify.py` from the folder. It checks:

- LICENSE contains the exact copyright line
- README credits Asdale Dynamics, LLC
- All 7 HTML files are well-formed and reference `styles.css`
- CSS contains `@media print`
- Required sections present in all 5 Markdown files
- No `.github/workflows` directory
- No obvious secret patterns in text files

## Verification results

`python3 verify.py` passed: all checks ok. 7 HTML files and 5 Markdown files
verified. Commit `ccd74c2` on branch `master` contains the full kit.

## Known gaps

- No automated build step (the kit is static Markdown + HTML; nothing to compile)
- HTML files were hand-written rather than generated from Markdown, so Markdown
  and HTML sources should be kept in sync by hand when editing
- Browser print appearance depends on the browser/OS; tested via parser and
  `@media print` CSS, not via an actual printed page
- Tracker is a static table; no computed totals or reminders
