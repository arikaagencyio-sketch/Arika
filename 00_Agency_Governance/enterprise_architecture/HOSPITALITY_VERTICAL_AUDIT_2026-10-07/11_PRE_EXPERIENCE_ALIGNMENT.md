# 11 — Pre-Experience Alignment and the Corporate-Tennis Prototype

**Protocol §8:** *Pre-Experience Marketing — communication that allows a prospective customer to imagine, emotionally understand and anticipate a hospitality experience before physically experiencing it.* Where does it belong? *"Do not force it into a single category if the architecture shows that it operates across layers."*
**Protocol §18:** can the OS support a master prototype — a fictional representative property — and where exactly should it live? First concept: **corporate tennis** — faceless, cinematic; movement, sound, environment, food, music, competition, social interaction, anticipation.

---

## 1. Presence in the repository

**Absent (`CONFIRMED`).** "pre-experience", "pre experience", "preexperience", "tennis" and "faceless" (in this sense) return no matches. There is no definition, owner, procedure, gate or asset. Everything below is therefore an **alignment analysis**: which existing capabilities the methodology would be assembled from, what collides with it, and what must be decided first.

## 2. What Pre-Experience is, in this OS's own terms

Tested against the protocol's eight candidate categories:

| Candidate | Fits? | Evidence of the fit |
|---|---|---|
| Marketing strategy | ◐ — it is a *demand* strategy for Plane B, not a channel plan | Marketing owns campaign strategy and demand generation (`MARKETING_OS.md` §3) |
| **Creative methodology** | ✅ — the core of it: a repeatable way of turning a place and an occasion into anticipatory, sensory, faceless imagery and motion | Design Production Engine; EE scene/storyboard disciplines |
| Content format | ◐ — it produces formats (cinematic short, itinerary visualisation, seasonal preview) but is not one | Content DB 6 `Format` |
| **Campaign architecture** | ✅ — previews must be timed to need-dates and booking windows | Content DB 4 Campaign + plugin P7 activation offsets |
| Experience design | ◐ — it *depicts* an experience; it does not design the guest's real experience | EE designs *digital* experiences only |
| Demand generation | ✅ (outcome) — anticipation is the demand mechanism | — |
| **Sales enablement** | ✅ — for the agency (a prototype that demonstrates capability) and for a client (a preview a sales team can send a corporate buyer) | Claims policy §3 permits *"real, non-client proof"* |
| Brand storytelling | ◐ — it carries the client's brand, but its unit is an occasion, not the brand | Branding narrative stack |

**Classification:** a **cross-layer creative methodology**, expressed as a **campaign pattern**, produced by the **existing production chain**, used for **demand generation** (client) and **sales enablement** (agency and client). It is **not** a department, **not** an agent, **not** a store, and **not by itself an offer** (whether it is sold — as a deliverable inside the Hospitality offer, as its own offer, or only as an agency demonstration — is decision `HD-10`).

## 3. The layers it would run across — what each already supplies

| Layer | Supplies to Pre-Experience | Existing artefact | State |
|---|---|---|---|
| **Sector (01)** | *Where and when*: DB 16 `Visual Language`, `Content Angles`, `Booking / Decision Triggers`, `Travel / Purchase Motivations`; P5 themes; DB 7 seasons and events; P7 timing; DB 15 origin markets | `SECTOR_NOTION_SCHEMA.md` DB 16; plugin P5/P7 | `LIVE` for 3 destinations |
| **Offer (02)** | *Whether it is sold and to whom* | Draft 41 D3–D5 are the nearest deliverables | `DESIGNED`; no Pre-Experience deliverable |
| **Content (04)** | *The story*: narrative pattern, campaign phase, brief | Story Architecture; DB 4 Campaign; DB 7 Brief (with the `Visual Direction` and `Canva Instructions` hand-off fields) | `BUILT` — but **every arc is problem-led** (below) |
| **Design (19)** | *The making*: Story → Image → Video → Voice → Animation → Music → Enhancement/Upscale → Assembly; 7-field storyboard; asset library with a reuse gate before credit spend; brand/environment checker with an AI-artifact gate | `DESIGN_OS.md` §3, §10; 6 agents; `design-plugin/` KIE client | Engine `DESIGNED`/partly `BUILT`; one real generation run; credit-constrained |
| **Experience Engineering (20)** | *The immersive surface*: scroll-driven, motion-native microsite or presentation; 9-field scene storyboard; motion and camera language; QA/performance gate | `EXPERIENCE_SPEC_SYSTEM.md`; 11 agents; 4 skills | `BUILT` (spec system); website the only real build |
| **Presence (21) / Marketing (03)** | *Getting it seen* | Presence registry; Marketing §10 | `DESIGNED`; nothing published |
| **Legal (10)** | *Whether it may be shown* | Claims policy; AI tooling terms; IP terms §4 | Drafts, **unreviewed**; **no depiction rule** |
| **Measurement** | *Whether it worked* | — | **absent** (`HV-18`) |

## 4. What collides with it — five structural conflicts

1. **The word "Experience" is taken.** `AEIT_06` defines `Experience` as an EE interactive build (*spec_id, scenes, tech_stack*). A hospitality "experience" (the corporate tennis day itself) entered under the same name would fork the canonical model. → `HV-39`. *Use "guest experience" or "offering" for the product; keep `Experience` for EE builds.*
2. **Every narrative arc in the OS is problem-led and B2B.** Content's Story Architecture: *Problem → Insight → Demonstration → Framework → Proof → Action*. EE's arc: *Attention → Problem → Transformation → Proof → Offer*. Content DB 4 campaign phases: *Problem · Insight · Reframe · Education · Proof · Solution · Commercial Relevance · Action*. Pre-Experience is **desire- and anticipation-led** — it has no problem beat. → `HV-14`.
3. **The publishing gate would reject it.** `content-publishing-gate` requires *"Does it solve an executive problem?"*, *"Would a decision maker find this useful?"* and enforces *"Never publish: Offer Before Problem"* as a hard stop (`.claude/agents/content-publishing-gate.md` Gates 1–3). A cinematic tennis preview for a hotel's corporate guests fails all three by design — the gate is built for the agency's own B2B content. → `HV-14`.
4. **Design's AI standard points the wrong way for a real property.** The only AI-specific quality bar is *"No visible AI artifacts — human-realistic production"* (`DESIGN_OS.md:123`), enforced as a gate. For a **real** property, photoreal AI imagery of facilities, food or scenes that do not exist exactly as shown is a representation risk; nothing requires a depiction to be *true to the property* or *labelled as a visualisation*. → `HV-13`.
5. **The claims policy has no visual class.** Classes A–D govern statements (`CLAIMS_SUBSTANTIATION_POLICY.md` §2). An image of an experience is an implied Class A/B claim (*"this exists, this is what you will get"*) with no rule. → `HV-13`.

## 5. Where it should live (recommendation for decision — not applied)

| Element | Owner | Form | Why there |
|---|---|---|---|
| The methodology (definition, when to use, narrative pattern, campaign template) | **Content (04)** | A ratified **Plane B narrative variant** beside Story Architecture, plus a campaign-phase option set for anticipation-led campaigns | Content owns narrative sequencing and the `Campaign` entity (ratified 2026-08-16) |
| The production recipe | **Design (19)** | A documented route through the existing Production Engine with the faceless/environmental constraints | Design owns asset production |
| The immersive surface (optional) | **Experience Engineering (20)** | A spec through the six-station Spec System | EE owns interactive builds |
| Whether and how it is sold | **Offer (02)** | Decision `HD-10`; if sold, an OEOS deliverable | Offer owns packaging |
| Depiction, disclosure and likeness rules | **Legal (10)** with Design's checker enforcing | An extension of the claims policy (a visual/depictive class) + a check in the brand/environment checker and the publishing gate | Legal owns claims; Design and Content own the gates |
| Timing | **Sector (01)** plugin P7 | Existing activation offsets | Already built |

**Nothing new is created except one methodology document, one narrative variant and one policy extension.** Everything else is an existing owner doing its existing job.

## 6. The corporate-tennis prototype (protocol §18)

### 6.1 Can the OS support it today?

| The prototype must demonstrate | Available? | Where |
|---|---|---|
| Property | ◐ — no fictional demonstration property exists; the namespace for one does (`SIM-*`, `CRM_SCHEMA.md` pilot activation rule) | — |
| Revenue centres | ❌ | `HV-12` |
| Experience menu | ❌ | no offering object |
| Audience | ◐ | P5 themes; Plane B segments absent |
| Occasion | ◐ | `Sports`, `Sales/MICE` signal types; `Corporate Retreat` theme |
| Season | ✅ | DB 7, P7, P13 |
| Pre-experience | ❌ | this file |
| Content | ◐ | Content stores (no client/demo dimension) |
| Distribution | ◐ | Presence (nothing live) |
| Sales | ◐ | Sales enablement agent; no deck |
| Revenue | ❌ | no measure beyond rooms |
| Retention | ❌ | — |

**Verdict:** the production *machinery* exists (Design + EE + Content); the *subject* (a property with revenue centres and offerings) and the *governance* (depiction rules) do not.

### 6.2 Where it should live — options

The repository already holds **two** simulated hospitality fixtures. Neither may become a public prototype under the decisions that created them.

| Option | Verdict | Reason |
|---|---|---|
| **A1 — Reuse A001** (the fictional 9-unit group) | ❌ **Reject** | Ratified as an internal simulation sandbox only (D17); its output may justify *mechanisms*, never *"any claim about real hotels"* (D20); its simulation package was *"modelled on"* a real brand whose facts are held only in a key file (A001 §4), and the owner has since said that brand is the intended real pilot (`GLOBAL_OS.md` header, 2026-10-02). A public "fictional" prototype derived from it could resemble a real company — the intended client. → `HV-28` |
| **A2 — Reuse SYNCO-01 / its property `SYNCO-01-P01`** | ❌ **Reject as-is** · ✅ **reuse its field shape** | Adopted 2026-09-29 as a synthetic company fixture **for normalisation only**, with the D20 boundary extended to it; reference-aligned to an unnamed real brand; *"every synthetic person, contact, guest, employee, booking, stay and review"* excluded permanently; *"no external write of any kind"* authorised (`SECTOR_OS.md` §8, 2026-09-29 entries). **But** its approved P01 property schema — unit categories, venue count and capacities, wellness, a club window, an open F&B outlet count — is the nearest thing in the estate to a property-with-revenue-centres shape. It lives only in the private sandbox; this audit did not read it |
| **B — A fresh simulated demonstration property, `SIM-H-001`** | ✅ **Recommend** | Uses the existing `SIM-*` namespace; may reuse SYNCO-01-P01's **field shape, never its values**, following that fixture's own rule that values are *"invented for this fixture, designed against the shape of the fields rather than derived from any real property"*; owned by **Offer (02)** as the Hospitality offer's demonstration specimen; organised in **Content DB 4** as an agency campaign with Objective = `Sales Enablement`; produced by Design; optionally assembled by EE. **Needs its own owner decision**, because a *public* demonstration is an external use that neither D20 nor the SYNCO-01 decision permits |
| **C — A new "prototype" folder or department** | ❌ Reject | Structure ahead of content — the owner's standing preference (`right-sized-architecture-preference`) and `REGISTRY_TAXONOMY_REFERENCE.md` both forbid it |

### 6.3 Preconditions before any frame is generated

1. **`HD-10`** decided — is Pre-Experience sold, demonstrated, or both?
2. **A depiction policy** (`HV-13`) — at minimum: label every preview *"visualisation — fictional demonstration property"*; no synthetic identifiable faces (the protocol's *faceless* constraint already reduces likeness risk and should be kept as a rule, not a style); no depiction of a real brand, venue or property; music and sound licensing recorded per asset.
3. **A Plane B narrative variant** ratified (`HV-14`) so the content gate does not reject the work, and a publishing-gate path for client/demonstration content.
4. **A budget check** — at the last recorded balance (2026-07-07, past the 30-day decay in `AEIT_11` R3) KIE.ai held 62 credits at 18 credits per Nano Banana Pro image, and OpenArt's free pool was exhausted (`DESIGN_OS.md:79`). A cinematic video concept cannot be produced on that runway. `UNKNOWN` today — `IR-M3`.
5. **Claims class** — the prototype is a **Class B capability demonstration** (*"we can make this"*), never a Class C result. It must not be presented as a client, a case study or a typical outcome.

### 6.4 The concept's elements, mapped to existing capability

| Element | Existing capability | Gap |
|---|---|---|
| Movement | EE motion director; Design motion primitives (`DESIGN_LANGUAGE_SYSTEM.md` §2 — *"none… have defined timing curves"*) | Motion surface undefined |
| Sound / music | Production Engine *Music* stage | Tool and licensing undecided |
| Environment | Design's Creative Digital Twin environment doctrine + brand/environment checker | Doctrine is the **agency's** environment, not a property's |
| Food | — | F&B as a revenue centre absent (`HV-12`) |
| Competition | `Sports` signal type; tournament as an occasion | Occasion vocabulary (P3) |
| Social interaction | Faceless constraint | Needs to be a written rule |
| Anticipation | — | The methodology itself |
