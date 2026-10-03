# Prospecting Cycle

**Owner:** Sales (05), Mary Thuo
**Activated:** 2026-10-03 for public-company research and preparation of a manual first outreach batch, following the owner's request to execute prospecting today.
**Current run:** `PROSPECT-H-20261003-01` - four real companies researched, 23 organization levels mapped, three first-touch emails and one company-switchboard script prepared. **Zero verified CRM rows, zero emails sent, zero calls made.**

**Owner release decision:** keep the three messages as drafts for edits. Zoho restored an authenticated support mailbox; the three drafts were saved from the available Mary alias and read back in its Drafts list. Provider references and screenshot evidence remain outside Git. This is verified draft preparation, not send authorization or DKIM/reply verification.

## Run Today

1. Verify official company pages and record the observation, URL, observation date and review date. Separate published facts, inferred buyer roles, hypotheses and unknowns.
2. Reserve `ORG-*` identities outside Git and map group, property, outlet and shared-service levels. Check CRM for existing records before claiming registration there. A published brand portfolio does not establish legal subsidiary ownership.
3. Qualify the exact buyer level. Groups with sourced child levels route to group discovery; central booking or brand teams change the route. A property with a direct booking path routes to property discovery. H1/H2 size governs single-property MVP delivery. Need, authority, budget and delivery scope remain unconfirmed until discovery.
4. Sector supplies the evidence and angle; Sales owns the message. Use one coordinated public company routing channel per account. No guessed address, named-person enrichment, pricing, fabricated audit finding or performance promise. A public inbox is neither buyer authority nor consent to a marketing sequence.
5. Review the exact message and sender, authenticate the mailbox, verify sender/reply operation and actual DKIM configuration. Release one manual first touch. The current batch remains unreleased pending these checks and human message review.
6. Verify the Sent view and write/read back the Lead and actual touch in ClickUp. Until then, record `crm_delivery: not_verified` and `sent: 0`; never promote a prepared queue to `contacted`.
7. On a positive reply, confirm who decides, the commercial priority and permission to continue. Arrange discovery from the owner's actual availability. A stop request suppresses the account immediately. Day 0/2/5/9/14/21/30 starts at the actual first send and follows the response/permission state.
8. A paid audit, quote, contract, private-data collection or invoice uses the existing Offer, Legal and Finance gates. This run has no commercial commitment.

## Artifacts

Identity root: `C:\Users\USER\.codex\visualizations\2026\10\02\01a0fddc-38d0-7323-a942-cf2f131a343f\public-prospecting\2026-10-03\identities`

Work root: `C:\Users\USER\.codex\visualizations\2026\10\02\01a0fddc-38d0-7323-a942-cf2f131a343f\public-prospecting\2026-10-03\work`

Both roots are outside Git and OneDrive and contain public company data only. Their use for this owner-requested public research run is not approval to store private client data. The human-readable exact-message review file is `FIRST_TOUCH_REVIEW.md` beside them. Existing Drive records have not been accessed or updated.

```powershell
python 05_Sales/prospecting/prospecting_cycle.py --batch <outside-git>/batch.json --out <outside-git>/cycle --date 2026-10-03
```

This executed step validates evidence freshness, identity hierarchy, contact provenance and duplicate routes, then generates an ID-labelled queue. Re-running the same batch preserves it. A changed batch requires a new cycle folder. It makes no API/model call, sends nothing and activates no follow-ups. Eight focused tests exercise the tree, evidence, destination and history rules.

## Release Work

| Work | Actual state | Exit evidence |
|---|---|---|
| Mailbox | Authenticated Zoho support mailbox; Mary/growth aliases observed; three Mary drafts saved/read back | Sender/reply operation verified before any future release |
| Mail authentication | Zoho MX verified through Cloudflare; SPF and monitoring DMARC verified through Google. Google MX response disagreed. DKIM selector unknown | Actual selector verified in Zoho Admin or an authenticated message header |
| CRM | ClickUp sign-in screen; historic provisioning evidence present | Real Company/Lead records written and read back; deduplication performed |
| Messages | Three saved Zoho drafts; owner requested drafts for edits, not sends | Edited exact messages reviewed and explicitly released by owner |
| Company phone | Completed switchboard script | Owner call and actual result logged |
| Website | No apex A/AAAA/www address in public DNS; HTTPS failed resolution | Correct deployed-project domain records and successful HTTPS load |
| Named-person marketing / private exports | Existing counsel, transfer, retention and storage review open | Relevant reviewed posture and permissions; a published contact alone is insufficient |
| Paid delivery | Hospitality pricing/scope, reviewed contract and invoicing gates open | Offer/Legal/Finance evidence for the specific engagement |

The website link is omitted from this batch. A LinkedIn Company Page, scraper, paid contact database, scheduler or automated sequence is not a dependency for a manual public-company routing inquiry. Their implementation decisions remain separate.

## Repository Reconciliation

This workspace started at `acbbd9f`, while the Claude checkout at `C:\Users\USER\OneDrive\Documents\The Agency Drafts` and live GitHub were at `79d1071`. The 136 current commits were fast-forwarded here, and pending edits reconciled with newer CRM, intake, delivery and runtime evidence. The preservation stash remains available. This corrects the earlier assumption that both paths were the same working copy.

The earlier Offer readiness packet's preparation-only restrictions describe its historic OEOS rehearsal. This owner-requested Sales cycle adds real public-company research and first-touch preparation. It spends no synthetic fixture authorization and claims no S10 delivery, complete intake ratification, priced offer or active engagement.

## Decision Log

- 2026-10-03: Acted on the owner's request for real prospecting today. Created the public evidence and actual message batch, executed preparation on it, extended the two Sector advisory agents and Sales qualification for Hospitality decision levels, and corrected the runtime so human-gated automatic invocation is refused and review-required results advertise no downstream events. After Zoho session restoration, saved and read back all three drafts. Owner chose drafts for edits; no sends/follow-ups. CRM registration still awaits account access/deduplication.
