# Search Queries for Job Scraper

## Search Sites

Primary (Canada / Edmonton market):
- **linkedin.com/jobs** - primary board for Edmonton + remote Canada
- **indeed.com** / **ca.indeed.com** - volume listings
- **glassdoor.ca** - company + salary signal
- **wowjobs.ca** / **jobbank.gc.ca** - Canadian aggregators
- Company career pages via Google `site:` filters

Note: Built-in Danish portal CLIs (Jobindex, Jobbank.dk, Jobdanmark, Jobnet) are out of scope for this candidate. Prefer LinkedIn + Indeed + WebSearch. The `linkedin-search` Bun CLI may be used with `-l "Edmonton, Alberta, Canada"` or `-l "Remote"`.

## Query Categories

### Priority 1: Digital Marketing / SEO / Growth (strongest fit)

```
site:linkedin.com/jobs "SEO" OR "Digital Marketing" Edmonton Alberta
site:linkedin.com/jobs "Marketing Manager" Edmonton Alberta
site:linkedin.com/jobs "SEO Specialist" OR "SEO Manager" Canada remote
site:ca.indeed.com "SEO" OR "Digital Marketing Specialist" Edmonton
"Google Ads" OR "PPC" "Marketing" Edmonton OR "remote Canada"
```

### Priority 2: AI Marketing / AI Automation / Marketing Ops

```
site:linkedin.com/jobs "AI Marketing" OR "AI Automation" Edmonton OR Canada
site:linkedin.com/jobs "Marketing Operations" OR "Marketing Automation" Canada remote
site:linkedin.com/jobs "Claude" OR "AI Specialist" Marketing Canada
"AI automation" marketing OR CRM OR "Go High Level" remote Canada
"practical AI" OR "AI integration" marketing Edmonton
```

### Priority 3: Adjacent marketing leadership & content

```
site:linkedin.com/jobs "Social Media Manager" Edmonton Alberta
site:linkedin.com/jobs "Growth Marketing" OR "Performance Marketing" Canada remote
site:linkedin.com/jobs "Content Strategist" OR "Brand Manager" Edmonton
"Marketing Director" OR "Marketing Lead" Edmonton SMB OR agency
```

### Priority 4: Broader opportunistic fits (still marketing/AI-adjacent)

```
site:linkedin.com/jobs "CRM" OR "RevOps" OR HubSpot OR "marketing automation" Canada remote
site:linkedin.com/jobs "Fractional Marketing" OR "Marketing Consultant" Alberta
site:linkedin.com/jobs "Customer Success" marketing automation Canada
"WordPress" OR Shopify "digital marketing" Edmonton OR remote
```

## Location Filter

When evaluating results, verify the job location matches:
- **Ideal:** Edmonton, AB (on-site or hybrid); fully remote Canada
- **Acceptable:** St. Albert, Sherwood Park, Leduc, Spruce Grove, Greater Edmonton; remote US/Canada with CAD-equivalent pay ≥ $60k
- **Borderline:** Calgary hybrid with partial remote (discuss)
- **Too far:** Mandatory relocation outside Edmonton region without remote option

## Compensation Filter

- **Career track:** Skip roles with stated base pay under CAD $60,000; if unknown, include and flag
- **Survival / local basic track:** Do NOT skip for pay under $60k. Prioritize proximity to 11110 68 Ave NW (Southgate, 68 Ave, Calgary Trail)

## Priority 0: Local survival jobs (near 11110 68 Ave NW)

Run these every scrape while dual-track is active:

```
warehouse OR barista OR cafe OR cashier OR retail "Southgate" Edmonton
"68 Avenue" OR "68 Ave" Edmonton warehouse OR labour OR unloader
Starbucks OR Nespresso OR Chipotle OR "sales associate" Southgate Edmonton
"Calgary Trail" barista OR retail OR warehouse Edmonton
```

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- "/scrape AI" -> Priority 2 + custom AI automation queries
- "/scrape SEO" -> Priority 1 SEO-focused queries
- "/scrape remote" -> add Remote filter across Priority 1-3
