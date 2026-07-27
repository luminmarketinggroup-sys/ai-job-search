# Job Application Assistant — Dylan Michael & Lillian Schule Zech

This repository is a **dual-candidate** job application workspace.

| Candidate | ID | Focus |
|-----------|----|-------|
| **Dylan Michael** | `dylan` | Digital marketing, SEO, paid media, AI automation (Edmonton / remote) |
| **Lillian Schule Zech** | `lillian` | Entry-level insurance claims & insurance customer service (Edmonton / Alberta) |

## Always select a candidate first

Before evaluating a job, drafting a CV/cover letter, or updating a tracker:

1. Determine whether the work is for **Dylan** or **Lillian** (ask once if unclear).
2. Load `candidates/<id>/PROFILE.md` and `candidates/<id>/profile/*` as the source of truth.
3. Write all outputs under `candidates/<id>/` only.
4. Never mix contact details, experience, or tracker rows across candidates.

See [`candidates/README.md`](candidates/README.md) for the full layout and routing rules.

## Shared tooling (not candidate-specific)

- `.claude/skills/job-application-assistant/` — shared evaluation, CV/cover templates, workflow skill
- `.claude/skills/job-scraper/` — search orchestration (queries should be candidate-aware)
- `.agents/skills/` — job portal CLIs
- Root `cover_letters/cover.cls` + `OpenFonts/` — shared LaTeX cover-letter class (symlinked into each candidate)

Candidate-specific writing notes and interview prep live under each candidate’s `profile/` folder and override the empty placeholders in the shared skill files when present.

## Hard filters

### Dylan (`candidates/dylan/`)
- Career track: prefer CAD $60k+; Edmonton / remote
- Survival local warehouse track near 11110 68 Ave NW may be softer on pay (see his PROFILE)
- **Skip** Southgate Centre public-facing retail/food roles

### Lillian (`candidates/lillian/`)
- Target: Claims Assistant / Intake / Coordinator / Administrator, Insurance CSR, Junior Claims Adjuster Trainee (Alberta)
- **Skip sales roles** and **skip kitchen / food-service roles** — do not draft or prioritize
- CIPR \#770356; preparing for Alberta Adjuster Level 1 (entry-level / trainee OK)

## Workflow for New Job Applications

1. Identify candidate (`dylan` or `lillian`)
2. User provides a job posting (URL or text), or scraper finds one
3. **Evaluate fit** against that candidate’s PROFILE (skills, experience, culture, deal-breakers)
4. If good fit: create targeted CV `candidates/<id>/cv/main_<company>.tex` and cover letter `candidates/<id>/cover_letters/cover_<company>_<role>.tex`
5. **Verify** using the checklist below (compile + visual PDF inspect + ATS text extract)
6. Update `candidates/<id>/job_search_tracker.csv`
7. Prepare interview talking points when moving to interview stage

**Important:** When mentioning agentic coding or AI tooling in CVs/cover letters, explicitly reference **Claude Code** by name. (Primarily relevant for Dylan; do not invent AI tooling experience for Lillian.)

## Master resumes (general-use copies)

- Dylan: `candidates/dylan/cv/main_example.tex` → compile with `lualatex`
- Lillian: `candidates/lillian/cv/main_example.tex` → compile with `lualatex` (this is the copy she can use generally)

## Verification Checklist

After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following. Report pass/fail.

### Factual accuracy
- [ ] All claims match the **selected candidate’s** PROFILE / profile files — no fabricated skills, experience, or achievements
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct for that candidate only
- [ ] Company-specific claims verified via WebFetch/WebSearch

### Targeting
- [ ] Profile statement / opening paragraph tailored to the role
- [ ] Skills and experience bullets reframed to the job (without failing the interview backtrack test)
- [ ] Key requirements addressed; gaps acknowledged where relevant
- [ ] For Lillian: sales metrics and kitchen detail de-emphasized; CIPR called out when relevant

### Consistency
- [ ] CV follows 2-page moderncv/banking format
- [ ] Cover letter uses cover.cls and established structure
- [ ] Tone consistent across CV and cover letter
- [ ] No contradictions; no cross-candidate contamination

### Quality
- [ ] No LaTeX syntax errors
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references mention **Claude Code** by name (when applicable)
- [ ] Cover letter addressed correctly; fits approximately one page

### Compiled PDF verification (MANDATORY)
- [ ] CV compiled with **lualatex**; cover letter with **xelatex**
- [ ] **CV is exactly 2 pages**
- [ ] **No orphaned `\cventry` titles** — use `\needspace{5\baselineskip}` before each `\cventry`
- [ ] **Cover letter is exactly 1 page**
- [ ] Cover letter bullet font matches body font (itemize outside `\lettercontent{}` with Raleway wrapper)

### ATS & keyword verification (CV)
- [ ] `pdftotext -layout` extracts cleanly (or skip with warning if missing)
- [ ] Email and phone appear as literal text
- [ ] Reading order matches visual order
- [ ] Posting keywords covered honestly — never stuffed
