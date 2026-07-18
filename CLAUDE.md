# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this site is

A Jekyll site (Korean language) that records the history of Korean teams at math olympiads — IMO, RMM, CGMO, APMO, FKMO, KMO, KMO junior division (중등부), plus winter/summer schools, people (인물), and schools (학교). Deployed via GitHub Pages as `imo-korea.github.io` (uses the `github-pages` gem, `jekyll-theme-cayman` theme).

## Commands

```sh
bundle install                 # install dependencies
bundle exec jekyll serve       # build and serve locally at http://localhost:4000
bundle exec jekyll build       # build only (output to _site/)
./linkcheck                    # run linkchecker against the live people page (requires `linkchecker`)
```

There are no tests or linters. Deployment happens automatically when pushed to GitHub (GitHub Pages builds the site).

## Architecture: data-driven pages

Almost all content lives in CSV files under `_data/`; the HTML is generated from them by Liquid templates. To update content (e.g., add a new year's results), edit the CSVs — not the HTML.

**Three-layer structure:**

1. **Page files** (`index.html`, `apmo.html`, `kmo.html`, …) are 3–5 line stubs: front matter with `layout: home`, an `<h1>` with an anchor id, and one `{% include %}`.
2. **`_layouts/home.html`** wraps every page with `head.html` (Bootstrap 4 CDN + inline CSS), a fixed-bottom navbar linking all pages, and `foot.html`.
3. **`_includes/*list.html`** templates iterate over the `_data` CSVs and render the year-by-year records.

**Data conventions in `_data/`:**

- Per-contest event metadata: `imo.csv`, `apmo.csv`, `rmm.csv`, `cgmo.csv` (year, host country/city, Korea's ranking, website, `story` column holds `|`-separated links to 후기 write-ups).
- Per-contest Korean participants: `*-korea.csv` (e.g., `imo-korea.csv` has year, name, korname, school, per-problem scores, rank, award, and the imo-official.org participant `id`).
- Leaders/observers: `teacher.csv` (IMO), `rmmteacher.csv`, `cgmoteacher.csv`, `schoolteacher.csv` — keyed by year and role (단장, 부단장, 참관인; role `후보` is skipped in listings).
- `people.csv`: person → affiliation, website, Math Genealogy id. `school.csv`: winter/summer school sessions.

**Cross-linking conventions (important when touching templates or data):**

- People are linked by exact Korean name string: `linkpeople.html` generates `/people.html#{{name}}` anchors, so a person's `name` in `people.csv` must match `korname`/`name` values in every other CSV exactly.
- Schools link to `/school.html#{{aff with spaces removed}}`.
- `history.html` builds a person's full cross-contest participation history by looking up their name across all `*-korea.csv` and `*teacher.csv` files.
- IMO entries link to imo-official.org using `year` and the participant `id` column.

**Helper scripts** (`_data/apmo.py`, `_data/fkmo.py`): interactive one-off Python scripts that parse pasted award-announcement text into CSV rows. They contain Python 2 remnants (`print` statements, `raw_input`) despite the python3 shebang — treat them as scratch tools, not maintained code.

`link.html` and `linkcheck` at the repo root are link-checker output/script, not site pages.
