# Candidates

This repo supports **two job seekers** in parallel:

| ID | Name | Focus | Path |
|----|------|-------|------|
| `dylan` | Dylan Michael | Digital marketing, SEO, AI automation (Edmonton / remote) | [`candidates/dylan/`](dylan/) |
| `lillian` | Lillian Schule Zech | **Lane A priority:** CSR / member services / billing / contact centre / reception; claims secondary (Edmonton / Alberta) | [`candidates/lillian/`](lillian/) |

## How agents should load a candidate

1. Identify who the application is for (`dylan` or `lillian`) from the user message. If unclear, ask once.
2. Read that candidate’s profile as the source of truth:
   - `candidates/<id>/PROFILE.md`
   - `candidates/<id>/profile/01-candidate-profile.md`
   - `candidates/<id>/profile/02-behavioral-profile.md`
   - `candidates/<id>/profile/03-writing-style.md` (candidate-specific tone notes)
   - `candidates/<id>/profile/07-interview-prep.md`
3. Use shared framework files (evaluation, CV/cover templates, scraper tooling) under `.claude/skills/`.
4. Write outputs **only** under that candidate’s tree:
   - CVs: `candidates/<id>/cv/main_<company>.tex`
   - Cover letters: `candidates/<id>/cover_letters/cover_<company>_<role>.tex`
   - Tracker: `candidates/<id>/job_search_tracker.csv`
5. Never mix Dylan and Lillian contact details, experience, or trackers.

## Per-candidate layout

```
candidates/<id>/
  PROFILE.md                 # Full candidate brief + deal-breakers + autonomy
  profile/                   # Structured skill-profile files
  cv/                        # Master + tailored LaTeX CVs (+ compiled PDFs)
  cover_letters/             # Tailored letters (cover.cls + OpenFonts via symlink)
  documents/                 # Source materials (resume PDF, diplomas, etc.)
  job_search_tracker.csv     # Application tracker for this person only
```

## Hard filters (quick reference)

- **Dylan:** Skip Southgate Centre public-facing retail/food roles. Career track floor CAD $60k (survival local warehouse track is softer; see his PROFILE).
- **Lillian:** Skip **sales** and **kitchen / food-service** roles. **Prioritize Lane A** (CSR, member services, billing/account support, contact centre, reception). Claims/insurance service remains a secondary track.
