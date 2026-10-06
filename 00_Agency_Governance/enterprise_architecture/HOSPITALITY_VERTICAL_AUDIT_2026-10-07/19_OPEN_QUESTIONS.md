# 19 — Open Questions

Unknowns this audit could not resolve from the repository, and why. Each names **the test that would resolve it** (`AEIT_11` R1: a state is claimed only with its named test). Decisions are in file 18; owner-supplied facts are in file 17. This file is for things that are *true or false out in the world* and simply were not observable from here.

**Why so many live-state unknowns:** this audit made no connector call. The repository records even read-only CRM checks as owner-authorised events, and none was authorised for an audit. Every live state below is therefore quoted from its last recorded verification.

---

| ID | Question | Why it is unknown | How to resolve | Who |
|---|---|---|---|---|
| **HQ-01** | Do `Company` and `Pilot Engagement` lists exist in ClickUp now? | Last statement (2026-10-03): *"not yet confirmed live"*; no call made | Owner-authorised read-only list query, recorded like the 2026-09-22 live check | Governance (00) |
| **HQ-02** | Current live row counts and states of Sector DB 7, DB 16 and Content DB 4/5/7 | Last verified 2026-08-24 → 2026-10-02 | Authorised `COUNT(*)` queries (the method used for F19) | Sector (01), Content (04) |
| **HQ-03** | Are DB 16's `Primary/Secondary Audiences` relations populated, and with which DB 9 rows? | Schema confirmed (HV-17); population not read | Read the three DB 16 rows | Sector (01) |
| **HQ-04** | Is the Postiz executor still running, and is any channel connected? | Recorded `LIVE` 2026-08-07 with 0 channels — 60 days old, past the 30-day decay | `techstack-connection-verifier` free read-only check | Tech Stack (13) |
| **HQ-05** | **Does safari-circuit seasonality differ from the coast's**, such that a country-level "Kenya's peak is Dec–Jan" signal would misdate a lodge calendar? | This audit did not open DB 7 rows and makes no claim about Kenyan seasons (file 06 §4) | Verify against a T1 destination source; check at which `Level` each seasonality signal is tagged; run S09 for Maasai Mara and inspect inherited signals | Sector (01) |
| **HQ-06** | Which origin-side calendars are registered and `active` in DB 14 (German *Land* school holidays, UK and US holidays)? | Plugin P8 lists them as candidates; later changelogs say all T1 signals are backed; the specific origin rows were not enumerated in the files read | Query DB 14 `Signal Role = Origin-side` | Sector (01) |
| **HQ-07** | Does a `finos` Postgres database exist anywhere, or is the schema unused? | Schema and docker-compose exist; no evidence of a running instance | Check for a running container or a connection record | Finance (09) |
| **HQ-08** | Current KIE.ai and OpenArt credit balances | Last recorded 2026-07-07 (KIE 62; OpenArt 0) | `KieClient.getCredits()` (free, read-only) and OpenArt account read | Design (19) / Tech Stack (13) |
| **HQ-09** | Zoho Books plan state; business bank account | Trial expired at the 2026-07-15 check; bank account "on hold" (2026-10-06) | Owner; `list_organizations` read | Finance (09) / owner |
| **HQ-10** | Has counsel replied to the 2026-09-16 scope request? | The latest repository record says reply awaited | Owner's correspondence | Legal (10) / owner |
| **HQ-11** | What instruction authorised applying the group/outlet reconciliation on 2026-10-03? | Recorded as "owner direction" by the Codex session; the instruction itself is not quoted (HV-46) | Owner confirms; quote it in a decision entry | owner |
| **HQ-12** | Is the intended pilot group among the four companies researched on 2026-10-03? | Identities are correctly kept out of the repository | Owner, outside the repository | owner |
| **HQ-13** | Were A001's and SYNCO-01's reference brands the same company, and is either the intended pilot? | Reference facts live only in sandbox key files, never read in a session (D3) | Owner, outside the repository | owner |
| **HQ-14** | Is the Creative Pipeline cloud routine still alive? | Last verified 2026-07-15 (a forced run); the hourly cadence was *"not yet proven post-restoration"* | `automation-reliability-monitor` read of `enabled` / `last_fired_at` | Automation (16) |
| **HQ-15** | Is the readiness assessment's D4 (runtime approval bypass) formally closed by `7d341f5`? | Code and tests now refuse unattended gated dispatch (verified 2026-10-06); the assessment has not been re-measured | Re-run the assessment's D4 test and update §11 | Governance (00) |
| **HQ-16** | Is B2B SaaS still being actively pursued, or paused while Hospitality pilots? | Root documents say SaaS; activity says Hospitality; the profile says both | Owner (feeds HD-02) | owner |
| **HQ-17** | Which guest languages matter per origin market for client content (e.g. German, Italian)? | No localisation capability or research exists | Research task once a pilot property's origin mix is known (intake H-C02) | Sector (01) / Content (04) |
| **HQ-18** | Is the website currently reachable at a public URL, and which version is deployed? | Last recorded 2026-10-03: no apex DNS record; `.vercel.app` subdomain | `curl -I` the deployment and the apex domain | Experience Engineering (20) |
| **HQ-19** | Do Kenya's and the origin markets' advertising rules treat AI-generated depictions of a real hotel differently from photographs? | Legal question; Claude is not counsel | Counsel (file 12 §6) | Legal (10) |
| **HQ-20** | Will the intended group's central teams (reservations, revenue, marketing) be the buyer, or will each property buy separately? | Depends on the group's real structure and on discovery | Public evidence at S1; discovery at S2 | Sales (05) |
