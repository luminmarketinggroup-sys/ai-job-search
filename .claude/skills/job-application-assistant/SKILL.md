---
name: job-application-assistant
description: >
  Assists with job applications for Dylan Michael or Lillian Schule Zech: evaluating job postings,
  tailoring CVs, writing cover letters, and preparing for interviews. Triggers on keywords like:
  job posting, job application, CV, cover letter, resume, interview prep, job fit, career,
  application, apply, ansøgning, stilling, Lillian, Dylan, insurance claims
allowed-tools: Read, Glob, Grep, WebFetch, WebSearch, Edit, Write, AskUserQuestion
---

# Job Application Assistant (Dual Candidate)

This repo serves **two candidates**. See [`candidates/README.md`](../../../candidates/README.md) and root [`CLAUDE.md`](../../../CLAUDE.md).

| ID | Name | Output root |
|----|------|-------------|
| `dylan` | Dylan Michael | `candidates/dylan/` |
| `lillian` | Lillian Schule Zech | `candidates/lillian/` |

---

## Step 0: Select Candidate (mandatory)

1. Infer `dylan` or `lillian` from the user message (name, role type, or explicit tag).
2. If unclear, ask once: "Is this application for Dylan or Lillian?"
3. Load:
   - `candidates/<id>/PROFILE.md`
   - `candidates/<id>/profile/01-candidate-profile.md`
   - `candidates/<id>/profile/02-behavioral-profile.md`
   - `candidates/<id>/profile/03-writing-style.md` (plus shared `03-writing-style.md` in this folder for global rules)
   - `candidates/<id>/profile/07-interview-prep.md` when doing interview prep
4. Apply deal-breakers immediately:
   - **Lillian:** skip sales and kitchen/food-service roles
   - **Dylan:** skip Southgate Centre public-facing retail/food roles

---

## Workflow

When the user provides a job posting (URL or text), follow this workflow:

### Step 1: Research & Evaluate Fit
- Fetch the job posting content (use WebFetch for URLs)
- Analyze required competencies, keywords, and priorities
- Research the company (website, LinkedIn, mission, recent news)
- Score against the **selected candidate** using `04-job-evaluation.md` + their PROFILE
- Present the evaluation table and verdict
- Suggest whether to call the employer before applying (see `04-job-evaluation.md`)
- Ask whether to proceed (unless that candidate’s PROFILE grants auto-draft autonomy for this fit level)

### Step 2: Tailor CV
- Start from `candidates/<id>/cv/main_example.tex` (or the closest tailored variant)
- Follow `05-cv-templates.md`
- Create `candidates/<id>/cv/main_<company>.tex`
- Adjust profile statement, skills emphasis, experience bullets, section order

### Step 3: Write Cover Letter
- Follow candidate `03-writing-style.md` + shared `03-writing-style.md` (no em-dashes, no cliches)
- Follow `06-cover-letter-templates.md`
- Create `candidates/<id>/cover_letters/cover_<company>_<role>.tex` (uses symlinked `cover.cls`)
- Connect specific experience to role requirements

### Step 4: Interview Preparation
- Use `candidates/<id>/profile/07-interview-prep.md` plus shared tough-question framework in this folder’s `07-interview-prep.md` if needed
- Prepare STAR answers, talking points, and questions for the interviewer

### Step 5: Tracker
- Append/update `candidates/<id>/job_search_tracker.csv` only

---

## Reference Files

| File | Purpose |
|------|---------|
| `candidates/<id>/PROFILE.md` | Full candidate brief + deal-breakers (source of truth) |
| `candidates/<id>/profile/01-candidate-profile.md` | Structured education, experience, skills |
| `candidates/<id>/profile/02-behavioral-profile.md` | Behavioral traits, ideal environments |
| `candidates/<id>/profile/03-writing-style.md` | Candidate-specific tone notes |
| `03-writing-style.md` (this folder) | Global writing rules |
| `04-job-evaluation.md` | Scoring framework |
| `05-cv-templates.md` | LaTeX CV structure and tailoring rules |
| `06-cover-letter-templates.md` | Cover letter structure |
| `candidates/<id>/profile/07-interview-prep.md` | Candidate STAR stubs / talking points |

---

## Quick Commands

- "Evaluate this job posting for Lillian/Dylan" - Step 1 only
- "Write a CV for [company] for Lillian/Dylan" - Step 2 only
- "Write a cover letter for [role] at [company]" - Step 3 (confirm candidate)
- "Help me prepare for an interview at [company]" - Step 4
- "What jobs should Lillian/Dylan look for?" - Career strategy using that PROFILE
