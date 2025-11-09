# websec-toolkit

A compact collection of small web-security and analysis tools — bundled into a single repository.

> **Legal & Ethical Notice:** These tools are intended for **authorized security testing only** (assets you own or have explicit permission to test). Do not use them against systems or services without clear authorization. The repository owner is not responsible for misuse.

---

## Tools (actual filenames)

Repository `Tools/` directory contains the following files and structure you provided:

```
Tools/
├─ combine_two_files_remove_dublicates.py
├─ common_path.py
├─ domains.txt
├─ extract_email_using_regix.py
├─ extract_secret_from_html.py
├─ extract_url_from_webpages.py
├─ file.html
├─ file.js
├─ file_one.txt
├─ file_two.txt
├─ hosts_live_domains.py
├─ output_file.txt
├─ secrets.js
└─ bruteforce/
   ├─ bruteforce_on_login_page.py
   ├─ index.php
   ├─ welcome.php
   └─ wordlist.txt
```

> Note: Filenames kept as provided (typos preserved — e.g., `dublicates`, `regix`) so they match your local files exactly. If you want me to normalize names (e.g., `duplicates`, `regex`) tell me and I will rename consistently.

---

## What each file/tool does

* `hosts_live_domains.py` — Check reachability for domains listed in `domains.txt` and write statuses to `output_file.txt`.
* `common_path.py` — Test common paths (e.g., `/admin`, `/backup`) against domains in `domains.txt` or a single URL.
* `combine_two_files_remove_dublicates.py` — Merge `file_one.txt` and `file_two.txt` into a single deduplicated file (output filename configurable).
* `extract_secret_from_html.py` — Scan `file.html`, `file.js`, or `secrets.js` to find strings that look like secrets (API keys, tokens). Review results manually.
* `extract_url_from_webpages.py` — Fetch a web page and extract all `<a href>` links; can accept local `file.html` as input.
* `extract_email_using_regix.py` — Read a file and print/extract email addresses using a regex.
* `bruteforce/bruteforce_on_login_page.py` — Educational brute-force script that tries credentials from `bruteforce/wordlist.txt` against `bruteforce/index.php` (use locally and only for testing).

---

## Quick run examples (using your filenames)

* Check live hosts (writes to `output_file.txt`):

```bash
python Tools/hosts_live_domains.py --input Tools/domains.txt --output Tools/output_file.txt
```

* Test common paths for a single domain from `domains.txt` or URL:

```bash
python Tools/common_path.py --domains Tools/domains.txt --paths common_paths.txt

# or for one URL
python Tools/common_path.py --url https://example.com --paths common_paths.txt
```

* Merge two files and remove duplicates:

```bash
python Tools/combine_two_files_remove_dublicates.py Tools/file_one.txt Tools/file_two.txt -o Tools/merged.txt
```

* Extract emails from a file:

```bash
python Tools/extract_email_using_regix.py Tools/file.html --output Tools/emails.txt
```

* Extract links from a webpage or local HTML file:

```bash
python Tools/extract_url_from_webpages.py https://example.com --output Tools/links.txt
# or
python Tools/extract_url_from_webpages.py Tools/file.html --local
```

* Extract potential secrets:

```bash
python Tools/extract_secret_from_html.py Tools/file.js --report Tools/secrets_report.txt
```

* Run the local brute-force test (educational only):

```bash
# WARNING: only run locally against the included PHP test files
python Tools/bruteforce/bruteforce_on_login_page.py --url http://localhost/bruteforce/index.php --users users.txt --passlist Tools/bruteforce/wordlist.txt
```

---

## Recommendations & housekeeping

1. **Rename typos (optional):** Consider renaming `dublicates` -> `duplicates` and `regix` -> `regex` for clarity. I kept original names by request.
2. **requirements.txt:** Add a `requirements.txt` listing required Python libraries (e.g., `requests`, `beautifulsoup4`, `aiohttp`). I can create it for you.
3. **.gitignore:** Add a `.gitignore` to exclude `.pyc`, `__pycache__/`, virtualenvs, and sensitive files.
4. **LICENSE:** Add an `LICENSE` (MIT recommended) and an `AUTHORIZATION.md` that makes the legal usage explicit.
5. **Docs & examples:** Consider adding short example inputs (`domains.txt`, `file_one.txt`) and expected outputs to help users run tools quickly.

---

## Next steps — what I can do for you now

* Create `requirements.txt`, `.gitignore`, and an MIT `LICENSE` file.
* Generate skeleton/CLI templates for each Python script (so you have runnable placeholders).
* Normalize filenames (rename typos) and update README accordingly.

Tell me which of the above you want me to create, and I will add them into the repo (I can generate the files and provide their contents here).
