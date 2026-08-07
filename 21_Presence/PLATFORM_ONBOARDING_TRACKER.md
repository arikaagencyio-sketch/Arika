# Platform Onboarding & Account-Health Tracker (Presence 21)

**Version:** v0.1.0
**Last updated:** 2026-08-07
**Owner:** Mary Thuo (Agency Governance, 00) · coordinated by Presence (21)
**Purpose:** Track each of the confirmed platform accounts from *creation → warmed-up → connected → verified* **without getting flagged, monitored, or suspended.** One platform per working session; advance its stage; commit. This is the operational companion to `CONTENT_DISTRIBUTION_ENGINE.md` (the engine) and enforces its **account warm-up rule** (Phase 0). Also a **reusable client-onboarding SOP.**

> Read `CONTENT_DISTRIBUTION_ENGINE.md` first. Platform behavioral profiles live in `04_Content/PLATFORM_INTELLIGENCE_REGISTRY.md` (PIL). This file tracks *account health & onboarding state*, not platform strategy.

---

## 1. How to use this (session discipline)

- **One social media per session.** Open it, do the next safe stage, update its row + section here, commit. Never batch-rush multiple new accounts into automation on the same day — that pattern is what platforms flag.
- **Never skip a stage.** Especially never jump an account straight to S4/S5 (API/automation) — S2 + S3 (humanize + warm up) are the flag-protection.
- **When in doubt, wait.** A suspended account costs weeks; a slow one costs nothing.

---

## 2. Onboarding stage model (every account moves through these)

| Stage | Meaning | Flag-safety role |
|---|---|---|
| **S0** | Not started | — |
| **S1** | Account/handle created | — |
| **S2** | Humanized & verified — real photo, bio, details; phone/email verified | Makes the account read as a real person/brand |
| **S3** | Warming up — posting **manually**, engaging normally, building history (days–weeks) | **The core anti-flag buffer** |
| **S4** | Developer app / API access created (where the platform needs one) | — |
| **S5** | Connected to Postiz (OAuth done, channel added) | Only after S2+S3 |
| **S6** | Verified live — a real post published *through the engine* | `verified_at` set |

**Golden rule:** an account may not enter **S4/S5** until it has genuinely cleared **S2 and S3.** Automation before warm-up = the flag.

---

## 3. Anti-flag health doctrine (all platforms)

1. **No API automation on an account younger than its warm-up window** (see per-platform below). This is non-negotiable.
2. **Complete + verify the profile** (photo, bio, phone/email) before anything else.
3. **Warm up with genuine, native manual content** — not identical cross-posts. Each platform gets platform-native content (per PIL).
4. **Ramp gradually** — a warmed account still shouldn't jump from 0 to 10 posts/day on day one of automation. Step it up.
5. **Consistent, clean login location** — don't log in rapidly from many IPs/countries/VPNs; that trips security holds.
6. **One new asset at a time** — creating a personal account + Page + Business + dev app + auto-poster all in one day is the classic ban pattern.
7. **Respect rate limits** — the engine's rate governor (L5) enforces per-platform ceilings once connected.
8. **Every claim substantiable** (Legal Class C) — content-level, but it also keeps accounts out of policy trouble.

---

## 4. Master status (as of 2026-08-07)

| # | Platform | Stage | Flag-risk | Current note |
|---|---|---|---|---|
| — | **Engine / Executor (Postiz)** | ✅ **LIVE** | — | Hostinger KVM 2 + Coolify; Postiz+PG+Redis healthy. App verified; 0 channels connected. |
| 1 | **LinkedIn** | **S1** | Medium–High | Personal profile created ("Arika"). **Company Page BLOCKED** — new account lacks the connections LinkedIn requires. Page is required before the dev app. → warm up profile + add connections. |
| 2 | **Facebook** | **S1–S2** | **High (90-day bans)** | Personal account + **Page already exist** (pre-existing). Verify personal acct; warm up Page. |
| 3 | **Instagram** | **S1** | **High** | Account exists, **not yet linked** — needs Professional→**Business** + link to the FB Page. |
| 4 | **Threads** | **S0** | High | Comes via Meta; start only after IG is established. |
| 5 | **TikTok** | **S0** | High | Content Posting API needs app review; defer until warmed. |
| 6 | **Pinterest** | **S0** | Low–Med | Business account + API; relatively tolerant. Good *early* API candidate. |
| 7 | **Website (owned hub)** | n/a | — | **Not a Postiz social channel** — EE-built hub on `arikaagency.com`. Tracked separately. |
| 8 | **X (Twitter)** | **S0** | High | ⚠️ API posting now needs a **paid** X API tier; flag-happy on automation. Decision needed before effort. |
| 9 | **Newsletter (owned)** | n/a | — | **Not a Postiz social channel** — an email tool (TBD). Tracked separately. |
| 10 | **YouTube** | **S0** | Low–Med | Google project + channel + OAuth; tolerant for your own channel. |
| — | **Meta Business Suite** | partial | — | Set up but with "fragments" to finish (IG link, Page/Business tidy-up). |

---

## 5. Per-platform detail (update these as you advance)

### 1. LinkedIn — S1 (gated)
- **Account:** personal profile created. **Company Page blocked** (needs connections + profile maturity).
- **Warm-up (S2→S3):** complete profile (photo, headline "Founder, Arika Agency", 1 experience, About); add real connections; verify email+phone; post a couple of manual updates. ~1–2 weeks.
- **Then:** create Page → create developer app (must attach to the Page) → products (Sign In w/ OpenID Connect + Share on LinkedIn; Advertising API for token refresh) → redirect `https://<postiz-domain>/integrations/social/linkedin` → creds into Coolify → connect.
- **Flag notes:** new-account Page gate; known Postiz OAuth "Not enough scopes" bug.

### 2. Facebook — S1–S2
- **Account:** personal FB + Arika Page already exist.
- **Warm-up:** verify personal account (phone); complete the Page (logo, About, `arikaagency.com`); post manually ~2–4 weeks; light genuine engagement.
- **Then (Phase 3):** Meta Developer App (Facebook Login + Graph API), permissions (pages_manage_posts, pages_read_engagement…), redirect to Postiz, creds→Coolify, connect.
- **Flag notes:** **highest ban-risk.** Never wire the dev app + auto-poster to a fresh/unverified account.

### 3. Instagram — S1 (link pending)
- **Account:** exists; **not linked.** Next safe step: switch to **Professional → Business**, then **link to the Arika FB Page** (via IG settings or Meta Business Suite). This is normal account setup — **safe to do now** (not automation).
- **Warm-up:** post manually alongside FB for 2–4 weeks.
- **Then:** same Meta app as Facebook (instagram_basic, instagram_content_publish); connect via Postiz.

### 4. Threads — S0 · 5. TikTok — S0 · 6. Pinterest — S0 · 8. X — S0 · 10. YouTube — S0
- Not started. Begin each in its own session, S1→S2→S3, before any API. **X needs a paid-tier decision first.** Pinterest/YouTube are the gentlest API connections to attempt earliest.

### Owned surfaces (not via Postiz)
- **7. Website** — EE-built hub; **9. Newsletter** — email tool (unchosen). Handled outside the social-posting engine.

---

## 6. Recommended safe sequence

1. **Warm up in parallel, manually** (no API): Facebook Page + Instagram (link IG now), and LinkedIn (build the profile/connections). 2–4 weeks of genuine activity.
2. **Prove the engine now on a throwaway** (Bluesky/Mastodon — no dev app, no ban risk) so the infrastructure is validated while real accounts age.
3. **First real API connections** once warmed: start with the **gentlest** (Pinterest, YouTube), then Meta (FB/IG/Threads) once well-established, then LinkedIn (once its Page exists), then X/TikTok (paid/approval permitting).
4. Advance one platform per session; set `verified_at` only at **S6**.

---

## 7. Session log

| Date | Platform | Stage moved | What was done |
|---|---|---|---|
| 2026-08-07 | Engine | → LIVE | Postiz deployed on Hostinger+Coolify, admin login confirmed |
| 2026-08-07 | LinkedIn | → S1 | Personal profile created; Page blocked (connections) |
| 2026-08-07 | Facebook | → S1–S2 | Personal + Page confirmed pre-existing |
| 2026-08-07 | Instagram | → S1 | Account exists; link-to-Page pending |

---

## 8. Decision Log
- **2026-08-07 — Tracker created.** Per-platform onboarding/health tracking established, enforcing the engine's account warm-up rule; one-platform-per-session discipline adopted to avoid platform flags/suspensions (owner priority: not being flagged/suspended). Reusable as a client-onboarding SOP. — Claude Code (Opus 4.8)
