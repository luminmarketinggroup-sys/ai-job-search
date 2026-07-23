# AGENTS.md

This is an AI job-search framework (a Claude Code toolkit). The primary authoring
rules, candidate-profile format, and the CV/cover-letter verification checklist live
in `CLAUDE.md` — read it first for any application/CV/cover-letter work. `README.md`
and `SETUP.md` document the end-user workflow and standard commands.

## Components

- Job-search CLIs — `.agents/skills/{jobbank,jobdanmark,jobindex,jobnet,linkedin}-search/cli`
  (TypeScript, run with Bun). `linkedin-search` is country-agnostic and has zero runtime deps.
- Salary tool — `salary_lookup.py` + `tools/convert_salary_excel.py` (Python 3, stdlib only;
  `convert_salary_excel.py` needs `openpyxl` only if you convert from Excel).
- Documents — `cv/main_example.tex` (moderncv, compile with `lualatex`) and
  `cover_letters/cover.cls` + `OpenFonts/` (compile with `xelatex`).

## Cursor Cloud specific instructions

Environment (TeX Live, Bun, and a CTAN copy of `moderncv` in `~/texmf`) is provisioned in
the VM snapshot. The startup update script only re-runs `bun install` in each CLI. Per-CLI
`node_modules`, compiled PDFs, and `salary_data.json` are gitignored and never committed.

- Bun: installed at `~/.bun/bin` (on `PATH` via `~/.bashrc`). A fresh non-login shell may not
  have it on `PATH`; use `~/.bun/bin/bun` or `export PATH="$HOME/.bun/bin:$PATH"` first.
- Run a CLI: `bun run .agents/skills/linkedin-search/cli/src/cli.ts search -l "Copenhagen, Denmark" -q "data scientist" --limit 3`
  (LinkedIn needs network; the four Danish portals also hit live sites). Per-CLI scripts:
  `bun test`, `bun run typecheck`, `bun start`. Only `linkedin-search` and `jobindex-search`
  ship tests; the other three have none (`bun test` reports 0 tests, which is expected).
- LaTeX gotcha (non-obvious): the CV template uses `\firstnamestyle`/`\lastnamestyle`, which
  only exist in `moderncv` >= 2.4. TeX Live 2024 ships 2.3.1 (too old) and the latest 2.6.x
  pulls in `fontawesome6` (not in TeX Live, which only has `fontawesome5`). The snapshot pins
  `moderncv` **2.5.1** in `~/texmf/tex/latex/moderncv` — the sweet spot that has the name-style
  commands and still uses `fontawesome5`. If the CV fails with `\firstnamestyle undefined` or
  `fontawesome6.sty not found`, that pinned copy is missing; reinstall moderncv 2.5.1 into
  `~/texmf` (do NOT edit the template).
- Compile from inside the document's directory (font/import paths are relative):
  `cd cv && lualatex -interaction=nonstopmode main_example.tex` (expect 2 pages);
  `cd cover_letters && xelatex -interaction=nonstopmode <file>.tex` (expect 1 page). There is
  no committed example cover letter — cover letters are generated per application by `/apply`.
- ATS check uses `pdftotext` (poppler), which is installed.
