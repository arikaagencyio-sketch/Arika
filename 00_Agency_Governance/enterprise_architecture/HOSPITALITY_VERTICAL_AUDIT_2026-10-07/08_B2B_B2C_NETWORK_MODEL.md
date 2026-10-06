# 08 — B2B / B2C / B2B2C / B2C2B / B2C2C Network Model

**Protocol §10:** does the system understand *relationship pathways* rather than merely audiences? **§13:** does it distinguish *audience vs buyer vs decision maker vs influencer vs user vs booker vs intermediary* — "mandatory for B2B/B2C hybrid hospitality"?

**Search result first (`CONFIRMED`):** `B2B2C`, `B2C2B` and `B2C2C` return **zero** matches anywhere in the repository; `wedding planner` and `event planner` return zero; `travel agent` and `tour operator` appear once each (intake question H-B05).

---

## 1. Whose pathways? Both planes have them

| | Plane A — Arika ⇄ hospitality businesses | Plane B — a hospitality business ⇄ its market |
|---|---|---|
| The protocol's examples | — | All five (guest, company, travel trade, employee→HR, guest→peer) |
| Modelled in the repo | **Yes** — direct, partner, referral, event, inreach (CRM `Lead.source`; Partner object; Presence's four directions) | **Barely** — market-level themes and route audiences; no pathway, role or intermediary model |

**The protocol's pathways are Plane B.** They describe how the *client* earns revenue, which the agency must understand to deliver the Hospitality offer, but which the agency does not itself transact.

## 2. Plane B pathways — what exists, what is missing

| Pathway | Hospitality meaning | What the OS represents today | Gap | Class |
|---|---|---|---|---|
| **B2C** — property → individual | Leisure guest books a stay, a spa day, a dinner | DB 16 demand themes; DB 15 route audiences (free text: *leisure · corporate · group · VFR · MICE · safari · beach*); intake H-C01 guest mix (aggregate); direct-booking content (Draft 41 D3–D6) | No guest-segment vocabulary; DB 16 audiences relate to Plane A rows (`HV-17`) | **EXTEND** (P3) |
| **B2B** — property → company | Conferences, retreats, team building, tournaments, meetings | `Sales/MICE` signal type and P7 offsets (T-365 strategic); P5 `Conferences/MICE`, `Corporate Retreat`; CRM outlet `MICE / Conference Unit`; intake H-C05 | No corporate-buyer model on the client side (who in a company books what); MICE revenue unmeasured | **EXTEND** |
| **B2B2C** — property → intermediary → consumer | Travel agents, tour operators, DMCs, wedding/event planners, corporate travel managers | P6 `Travel-Trade` signal type (dominant); P8 trade-show sources; intake H-B05 *"tour operators, DMCs, travel agents, wholesalers, GDS, corporate or MICE contracts"* (one S2 question); P2 Travel-Trade cells (`owner_reasoning`) | **No intermediary entity or relationship**; the CRM `Partner` object is **Arika's** partners, not the client's trade partners; contracting/allocation cycles unmodelled | **NEW** (vocabulary) + **EXTEND** |
| **B2C2B** — individual → internal advocate → decision maker → organisation | *Employee discovers a corporate tennis experience → sends to HR → HR requests a proposal → company books* | **Nothing** | Needs: an occasion (team building), a segment (corporate), decision roles (employee = user/influencer; HR = decision maker/booker), an offering, and a conversion asset (proposal request) | **NEW** |
| **B2C2C** — customer → peer network → new customer | Guest experience → social sharing → friend books | Presence/PIL engagement doctrine (agency-side only); review platforms on the PIL **watchlist (not built)** | No guest-referral, UGC or review model on the client side | **NEW** (P2) |

## 3. Plane A pathways — the agency's own (for completeness)

| Pathway | Where | State |
|---|---|---|
| Direct outbound / inbound | `Lead.source` (`inbound`, `outbound`); Presence directions | Live field; **live `Source` options omit `inreach`** (`CRM_SCHEMA.md` live check 2026-09-22) |
| Partner-sourced (Arika's B2B2B) | CRM `Partner` + `sourced_opportunity_ids`; ClientPartner (06) | Live list; no partner exists |
| Referral / advocacy | `Lead.source = referral`; `client-success-advocacy` | Designed; nothing to capture (Class C banned) |
| Event | `Lead.source = event`; plugin P7 *"Travel-Trade (Arika's own attendance)"* offsets | Rules exist; no event plan (file 09 §4) |
| Internal advocate inside a hotel (Arika's own B2C2B) | Draft 41 §2.2: Revenue Manager as *operational user* who *"holds booking/channel data"*; GM/Owner as economic buyer | **Present in prose** — not as a decision-role record (`Person` is blueprint only) |

## 4. The seven roles (protocol §13)

| Role | Plane A representation | Plane B representation | Verdict |
|---|---|---|---|
| **Audience** | DB 9 role lenses (Operator · Buyer · Amplifier · Enabler); Content DB 6 `Audience Role` (**CEO · CMO · Sales Leader · COO · Investor · Founder** — SaaS-only, `HV-43`) | DB 15 text; DB 16 → DB 9 (mis-targeted); P5 themes | Three vocabularies, none for guests |
| **Buyer** | DB 9 `Buyer` lens; Draft 41 *economic buyer* (GM, Owner/MD) | — | Plane A only |
| **Decision maker** | DB 10 titles (GM · Owner/MD · Director of Revenue · DOSM); `AEIT_06` `Person.decision_authority` + `decision_scope` (group / property / outlet / shared service) — **blueprint** | — | Plane A designed, unbuilt |
| **Influencer** | DB 9 `Amplifier` lens | — (travel influencers, review sites, planners-as-recommenders: absent) | Plane A only |
| **User** | Draft 41 *operational user* (Revenue Manager) | the guest / attendee — absent | Plane A only |
| **Booker** | — | — (PA, travel manager, event planner booking on behalf of others) | **Absent on both planes** |
| **Intermediary** | CRM `Partner` (Arika's); plugin P1 business models *management-contract*, *franchise* | intake H-B05; P6 `Travel-Trade` | No entity on Plane B |

**DOSM's role** in the buying process is explicitly undefined in the offer (Draft 41 §9 #17).

**Verdict (`CONFIRMED`):** the OS distinguishes audience, buyer, decision maker, influencer and user **for its own sale** (by lens, title and prose), but has **no role model at all for the hotel's market**, and **"booker" appears on neither plane**. The distinction the protocol calls mandatory is half present.

## 5. Minimum sufficient design (proposal — not applied)

The repository already owns the right places; nothing below adds a store.

1. **One role vocabulary, used on both planes:** `buyer · decision_maker · influencer · user · booker · intermediary · advocate`. Plane A: a controlled value set for `AEIT_06` `Person.role` when `Person` is built. Plane B: an attribute on each P3 demand pattern. *(Tier 1 vocabulary — ratify once.)*
2. **One pathway vocabulary for Plane B demand patterns:** `B2C · B2B · B2B2C · B2C2B · B2C2C`, authored in plugin **P3** alongside guest segments and occasions. *(Tier 2 values.)*
3. **Intermediaries as client context, not as Arika partners:** captured per client through intake (expand H-B05 into rows for trade partner types, contract cycles and allocation timing); the CRM `Partner` object stays Arika's. *(Tier 3.)*
4. **Do not** build a second CRM, a B2B2C pipeline, an intermediary database or a "network graph" store. When the knowledge graph is built (`AEIT_10` Phase C), pathways become typed edges — not before.

### Worked example — the protocol's B2C2B case, expressed in the minimal model

| Element | Value | Lives in |
|---|---|---|
| Occasion | team building / corporate offsite | P3 `occasion` vocabulary |
| Segment | corporate (domestic) | P3 `guest_segment` vocabulary |
| Pathway | `B2C2B` | P3 `pathway` |
| Roles | employee = `user` + `advocate`; HR = `decision_maker` + `booker` | role vocabulary |
| Offering | corporate tennis day (client's product) | intake → client folder |
| Conversion asset | proposal-request path for HR | client deliverable (D5-type) |
| Timing | `Sales/MICE` offsets (T-365 → T-30) | plugin P7 |
| Proof | Arika's own outcome claims: Class C **banned** until measured (claims policy §3). Claims *inside a client deliverable*: governed by Draft 41 QG2/QG3. **Neither covers a visual depiction of the experience** (`HV-13`) | claims policy; Draft 41 §8 |
