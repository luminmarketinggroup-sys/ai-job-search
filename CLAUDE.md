# Job Application Assistant for Dylan Michael

<!-- SETUP: This file is populated by running /setup -->

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant for Dylan Michael, helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (LaTeX/moderncv) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (LaTeX)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

### Identity
- **Name:** Dylan Michael
- **Location:** Edmonton, Alberta, Canada (open to Edmonton on-site/hybrid and remote roles)
- **Phone:** 825-967-9337
- **Email:** dylanschule@live.ca
- **LinkedIn (for applications):** https://www.linkedin.com/in/dylan-michael-993a78392
- **LinkedIn (AI content / post automation):** https://www.linkedin.com/in/dylan-michael-ai — do not list on applications unless requested
- **Languages:** English (native)
- **Status:** Actively open to opportunities (full-time, contract, or strong remote fits); currently Co-founder & Marketing Director at Lumin Marketing Group
- **LinkedIn headline:** "Marketing Director | Social Media Manager | Digital Marketing | AI Specialist | SEO Specialist"

### Education
- **High School Diploma** (2013-2016) - Harry Ainlay High School, Edmonton, Alberta

### Professional Experience
- **Co-founder, Marketing Director & AI Automation** (May 2023 - Present) - **Lumin Marketing Group** (Edmonton, Alberta)
  - Own SEO and digital strategy for 2 active SMB client accounts: keyword research, competitor analysis, SERP tracking (SEMrush, Search Atlas), technical SEO, UX, and lead generation
  - Plan and run Google Ads and Meta campaigns; manage budgets, creative tests, and performance reporting
  - Implement Go High Level / CRM workflows, client data organization, email/SMS automation, and SOP documentation
  - Deliver practical AI integration using Claude and Claude Code: marketing/ops workflows that save about 20 hours per week, with human review before publish
  - Maintain an active AI content practice with LinkedIn post automation on a dedicated profile
- **Manager / Marketing Manager** (2021 - 2023) - **Phantom Avenue Tattoo Shop** (Edmonton, Alberta)
  - Increased organic traffic by 30% through SEO and content optimization
  - Designed company website with attention to mobile performance
  - Built local SEO (citations, Google Business Profile) and managed social platforms with trend-driven content, video, and photography
- **Service Manager** (2019 - 2020) - **Audi Southgate** (Edmonton, Alberta)
  - Managed high-volume Fixed Ops customer interactions; built client relationships through clear communication and problem solving
  - Upsold recommended services; coordinated scheduling, documentation, and workflows

### Technical Skills
- **Primary:** SEO & organic growth, digital marketing strategy, paid ads (Google Ads, Meta Ads / PPC), local SEO, website optimization (WordPress, Wix, Shopify), marketing automation / CRM (Go High Level)
- **Secondary:** Social media management, content creation (video, photography), reporting (GA4, Google Search Console, Google Sheets), SOP development, client-facing leadership
- **Domain:** SMB / local business marketing (Edmonton and Alberta), agency account management, practical AI integration for marketing and ops workflows
- **Software:** SEMrush, Search Atlas, GA4, Google Search Console, Yoast, Google Ads, Meta Ads, WordPress, Wix, Shopify, Go High Level, Claude (Anthropic) / Claude Code for AI workflows and agentic tooling

### Certifications
- **Google Ads Certified**
- **Claude Certified**

### Publications
- None listed

### Awards
- None listed

### Behavioral Profile
- **High drive / pace** - Thrives in fast-paced environments and long hours; comfortable owning outcomes under pressure
- **Hands-on operator** - Prefers building and shipping (campaigns, sites, automations) over pure strategy theatre
- **Strengths:** Ownership, client-facing delivery, SEO/growth execution, practical AI automation, stamina for demanding workloads
- **Growth areas:** Formal academic credentials (high school diploma as highest listed education); deep software-engineering / ML research roles are a stretch unless reframed around applied AI for marketing/ops
- **Thrives in:** Fast-paced teams, clear ownership, high-output marketing/AI delivery environments

### What Excites You
- Practical AI automation that removes grunt work so teams can sell and serve customers
- SEO, paid growth, and brand systems that make local businesses easier to find and choose
- Building end-to-end marketing + AI workflows (content, CRM, reporting, follow-ups)

### Target Sectors
- Digital marketing / SEO / growth (agencies and in-house): Edmonton and remote Canada/US where pay clears CAD $60k
- AI marketing / AI automation / marketing operations roles using Claude and workflow tools
- SMB-focused marketing, brand, and performance roles open to non-degree candidates with strong portfolios

### Deal-breakers
- Base compensation under CAD $60,000
- Roles requiring relocation away from Edmonton without remote/hybrid flexibility (relocation is a hard fail unless user explicitly overrides)

## Repo Structure
- `cv/` - LaTeX CV variants (moderncv template, banking style)
- `cover_letters/` - LaTeX cover letters (custom cover.cls template)
- `.claude/skills/` - AI skill definitions for the application workflow
- `.agents/skills/` - Job search CLI tools

## Workflow for New Job Applications
1. User provides a job posting (URL or text)
2. **Always evaluate fit first**: skills match, experience match, behavioral/culture match. Present this assessment to the user before proceeding.
3. If good fit: create targeted CV (`cv/main_<company>.tex`) and cover letter (`cover_letters/cover_<company>_<role>.tex`)
4. **Verify both documents** (see Verification Checklist below)
5. Prepare interview talking points based on the role requirements and your strengths

**Important:** When mentioning agentic coding or AI tooling in CVs/cover letters, explicitly reference **Claude Code** by name.

## Verification Checklist
After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following before presenting to the user. Report the results as a pass/fail checklist.

### Factual accuracy
- [ ] All claims match actual profile (CLAUDE.md / candidate profile) - no fabricated skills, experience, or achievements
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct
- [ ] All company-specific claims (partnerships, products, technology, expansions) have been independently verified via WebFetch/WebSearch - do not trust reviewer agent research without verification

### Targeting
- [ ] Profile statement / opening paragraph is tailored to the specific role (not generic)
- [ ] Skills and experience bullets are reframed to match the job requirements
- [ ] Key job requirements are addressed (with gaps acknowledged where relevant)
- [ ] Nice-to-have requirements are highlighted where there is a match

### Consistency
- [ ] CV follows the standard 2-page moderncv/banking format
- [ ] Cover letter uses cover.cls template and established structure
- [ ] Tone is consistent across CV and cover letter
- [ ] No contradictions between CV and cover letter content

### Quality
- [ ] No LaTeX syntax errors (balanced braces, correct commands)
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references mention **Claude Code** by name
- [ ] Cover letter is addressed to the correct person (or "Dear Hiring Manager" if unknown)
- [ ] Cover letter fits approximately one page

### Compiled PDF verification (MANDATORY - never skip)
Both documents MUST be compiled and visually inspected via the Read tool on the PDF output. "Looks fine in the .tex" is not acceptable - LaTeX page-break decisions are unpredictable. Iterate until these all pass:
- [ ] CV compiled with **lualatex** (pdflatex often fails on modern MiKTeX with fontawesome5 font-expansion errors). Cover letter compiled with **xelatex** (cover.cls requires fontspec).
- [ ] **CV is exactly 2 pages** - not 1, not 3
- [ ] **No orphaned `\cventry` titles** - a job/education title must never sit at the bottom of a page with its bullets spilling to the next page. Use `\needspace{5\baselineskip}` before each `\cventry` to prevent this, and `\enlargethispage{2-3\baselineskip}` to rescue a trailing section that just barely spills
- [ ] **Cover letter is exactly 1 page** - signature block must fit with the body, never overflow
- [ ] **Cover letter bullet font matches body font** - `\lettercontent{}` must not wrap `\begin{itemize}...\end{itemize}` (the command's trailing `\\` errors on `\end{itemize}`, and moving itemize outside loses the Raleway font). Standard pattern: close `\lettercontent{}`, then wrap the list in `{\raggedright\fontspec[Path = OpenFonts/fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont \begin{itemize}...\end{itemize}\par}`

### ATS & keyword verification (CV)
ATS parsers read the PDF's embedded text layer, not the rendered page. Extract it with `pdftotext -layout` and verify what a parser sees. `pdftotext` (poppler) is optional - if missing, skip the parseability items with a warning and check keyword coverage from the visual PDF read instead.
- [ ] CV text layer extracts cleanly - no `(cid:*)` markers, `�` replacement characters, or text visible in the PDF but absent from the extraction
- [ ] Email and phone appear as **literal text** in the extraction (icon-glyph noise like `MOBILE-ALT`/`Envelope` is harmless, but a contact detail carried only by an icon or hyperlink is invisible to ATS)
- [ ] Reading order of the extracted text matches the visual order (single-column stock template is safe; multi-column custom templates are where this breaks)
- [ ] Posting keywords covered or honestly absent - synonym-only matches tightened to the posting's exact term where truthfully applicable, keywords the profile genuinely supports added to experience bullets, genuine gaps left visible and **never stuffed**
