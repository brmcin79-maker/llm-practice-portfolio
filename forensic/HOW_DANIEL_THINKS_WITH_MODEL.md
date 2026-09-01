# How Daniel thinks when a model is involved

> **Public copy.** Adapted from the private Planning `FORENSIC/` maps so readers
> without that repository can still see how the machine is described. **Not law.**
> Chunk ids such as N-03 or C-04 name files in the private `governance/` tree.
> Product paths name files in the private product repository. Hold / drift / fail
> means: the running program matches the lock, only partly lives it, or contradicts it.

---

**Status:** Forensic map. **Not law.** Chunks under `governance/` win if this file and a chunk disagree.  
**Date:** 2026-08-31  
**Snapshot:** Product `79eeb97` (CF-096 Complete).  
**Scope:** Hybrid on, or quiet help on. A live model path is connected. Local still runs the sitting. The model is pattern-sense on facts local already placed.  
**Companion:** Talk families live in [`HOW_DANIEL_RESPONDS.md`](HOW_DANIEL_RESPONDS.md). Local-only intellect (help off) lives in [`HOW_DANIEL_THINKS_LOCAL.md`](HOW_DANIEL_THINKS_LOCAL.md). This paper is the **gate + sandwich + three surfaces** half.  
**Not this file:** A coding paper. An NLG mouth. Reopening **N-03**. Growing sandwich regex as sitting law. G-WEB. A watcher LLM.


**How to read the compare:** **Holds** = product matches the lock. **Drifts** = lock is live but only partly lived. **Fails** = product contradicts a lock.

---

## 0. Law register

This map is Hybrid engagement plus stay-talk paint plus quiet help, **with local still deciding the beat**. Open north-star, communication (who speaks), organism (consent), AI organ, and substrate DET default.

| Chunk | Job for this map |
|-------|------------------|
| **N-03** | Local decides the beat and speaks. Quiet help fills one handle for the rung local already chose. Paint restates. AI off still moves |
| **N-01** | Honesty/testability, not the model as product |
| **C-03** | Numbered menus never the model. Free chat is the one default AI body when connected. HELP Explain more is labeled rewrite of locked facts |
| **C-08** | Banner honesty: if it says AI on, chat works. Banner also shows quiet help |
| **C-09** | Every live model call emits a hold the boundary can see |
| **O-07** | Quiet help is nested consent, off by default. FLOW cannot turn it on. No live path → it does not run |
| **A-01** | How to open Hybrid law. People never hear gateway / sandwich / pack |
| **A-02** | The model is pattern-sense, not a second Daniel, not the sitting |
| **A-03** | Dual register: local names and speaks stay-talk; quiet help before; paint after; skip paint on a complete question |
| **A-04** | Local fetches and places. No model tool belt |
| **A-05** | Sandwich: pack → candidate → local wins. Cheap DET pulse-watch. Not a second LLM as hall monitor |
| **A-06** | Unique recall injects silently. Ambiguous: local asks until they agree |
| **A-07** | Pathing never live web. Local fetches. Unlabeled web is stripped |
| **A-09** | Place / sandwich / people Want tables |
| **A-11** | One engagement path. Reuse `work_partner_brief`. Model never authors numbered lists |
| **S-03** | DET default. The model is optional color, not the floor |

**Skipped:** C-07 Atlas packs; C-10/C-11 leftover-hunt script (use when cutting a paper); G-WEB / G-CALC (deferred); A-08 shipped-vs-lock catalog (cite when checking whether to build); A-10 plains; reaching 3E scorer.

---

## 1. What model intellect is

**Law:** **A-02** · **N-03** · **A-04**

The model does not run a sitting. It does not browse the ledger, the catalog, the dossier, or the web. It does not pick a method rung. It does not write a row. It does not classify `okay` vs leftover vs stuck vs empty as product law — **local owns those families** (**A-03**).

What it does: pattern-sense over **granted** strips plus trained world-knowledge. Wider language for brainstorm, story-map, voice, and a restatement of a take local already named.

Daniel is **one companion**. Local never leaves. All deterministic code is local Daniel. Some of it is the **environment** (menus, ledger, dossiers). Some is the **harness** (brief, inject, N11, post-check, quiet-help gate) that exists to engage, constrain, and verify the model.

**Compare:** Holds as design. When Designer hears a kit lecture or a misspoke-about-the-kit line, that is the model filling a gap local did not grant. The sandwich is supposed to catch it. It is not a second mind that “understood the bathroom.”

---

## 2. Three surfaces (not three Daniels)

**Law:** **C-03** · **A-03** · **A-11**

Every live model call walks one engagement path (`domains/ai/engage.py`). People hear one voice. The three surfaces differ in **when** the model is called and **what it is allowed to return**.

| Surface | When | What the model may return | Who speaks to people |
|---------|------|---------------------------|----------------------|
| **Quiet help (before)** | Stay-talk, switch on, live path, smell passed | Closed JSON slots: meaning, talk-shape, optional object, optional thought | **Local.** Slots feed `_apply_quiet_slots`. Fail → floor families. People never hear the JSON |
| **Stay-talk paint (after)** | Local already named a take; Hybrid connected; take is not a complete question; quiet help did not advise this pulse | One restatement of that take | Local card prints first. Paint is an extra beat under it, or dropped |
| **Free chat** | No command; chrome shelved or never printed; Hybrid connected | Ordinary talk over the pack | The model body, after DET gateway and after-candidate. Local still owns writes |

A fourth labeled door exists and is not stay-talk: **HELP Explain more / `AI HELP`** — optional rewrite of locked local facts only (**C-03**). Not mapped beat-by-beat here.

Quiet help and paint **never run on the same pulse**. If quiet help advised, `maybe_paint_stay_take` pops the paint hold and returns the DET card unchanged.

---

## 3. Gate ladder (every live call)

**Law:** **O-07** · **A-04** · **A-05** · **C-08** · **A-07**

Gates are **deterministic**. The model does not choose whether to retrieve, whether this pulse is a menu, or whether quiet help is on.

```text
typed line
    → DET classifies the surface (command / live digit / stay-talk / free chat)
    → consent gates (quiet-help switch, Hybrid connected, domain_ai, global allow_ai)
    → shape gates (smell_stay_talk / numbered chrome / complete-question skip)
    → local-first gateway (pulse-watch, recall-until-agree, grant strips)   [free chat]
    → spend gates (secrets mask, N11 longtext, N11 context, RPD, preflight)
    → DET pack (boundary + granted strips + brief / quiet-help JSON instruction)
    → route_chat (sticky failover; model has no tools)
    → DET after (gate_slots or after_candidate + paint beat)
    → local speaks or local card + optional paint beat
```

People never hear the words gateway, sandwich, pack, pulse-watch, or receipt (**A-01**).

---

## 4. Consent gates (before any adapter)

**Law:** **O-07** · **C-08** · **C-05**

These are sitting flags and security. Not model judgment.

| Gate | DET function / hold | Pass means | Fail means |
|------|---------------------|------------|------------|
| Quiet-help **switch** | `quiet_help.setting_on` — `session["quiet_help"]` | They turned it on at SETUP AI path 5 (On/Off card). FLOW cannot set this | Advise returns `None`. Floor families run |
| Live **chat path** | `quiet_help.chat_path_ready` → `ai_connected` and `ai_route` not offline/none; may `refresh_connected_flag` | A provider is actually connected | Switch on with no path: quiet help does not run (**O-07**) |
| Quiet help **enabled** | `quiet_help.enabled` = switch **and** path | `advise_before` may continue | Same as floor |
| Hybrid / paint **want_live** | `ai_connected` and route not offline (paint and free chat) | Paint or adapter may call `route_chat` | DET card / offline chat reply. AI off still moves |
| Global **allow_ai** | `packages/security/policy.py` `allow_ai` | Domain may use live model | `refuse_live_reason` fires; no live call |
| **domain_ai** hub | `get_domain_mode` / `resolve_domain_ai` / `refuse_live_reason` (`packages/security/domain_ai.py`) | `auto`: live. `ask`: needs `_hub_ai_confirmed` or quiet help skips. `off`: refuse | Quiet help: `None`. Paint: DET card. Free chat: warm offline reply, or a CONFIRM card if ask-pending |
| Banner | `kernel/banner.py` | `DET / AI / NET / quiet help` must match what actually runs | If banner says AI on, chat must work (**C-08**) |

**domain_ai ask** is a people confirm, not a model confirm. Free chat queues `pending_hub_ai`; CONFIRM calls `_chat_via_adapter` with `_hub_ai_confirmed`. Quiet help and paint **do not** queue that card: if hub is `ask` and unconfirmed, they simply skip the model (`advise_before` / `maybe_paint_stay_take` return floor).

---

## 5. Shape gates (is this pulse allowed to call a model)

**Law:** **C-03** · **A-03** · **C-05**

### 5a. Quiet help — `smell_stay_talk`

Product: `domains/ai/quiet_help.py` `smell_stay_talk`.

Returns **false** (no advise) when any of:

- empty line
- `pending_flow` is set (a numbered hub/menu is live)
- no `pending_work_block`, or stay is not `awaiting_talk`
- stay has `picks_live` **and** they typed a digit
- line is `help`, `show menu`, `show boundary`, `status`, `status ai`, `ai status`
- line starts with `where are we`
- line starts with `help` / `status` / `setup ai` / `how we work` / `research advise`

A live numbered pick never spends quiet help. That is the C-03 / A-03 smell lock.

### 5b. Stay-talk paint — `maybe_paint_stay_take`

Product: `domains/ai/engage.py` `maybe_paint_stay_take`.

Skip (return the DET card unchanged) when any of:

- `quiet_help.advised_this_pulse` (pops `_quiet_help_advised`; also pops `pending_stay_take_paint`)
- no `pending_stay_take_paint` dict, or empty `take`
- `_take_is_complete_question`: the take contains `?` (first-item ask and the answer-to-ask bridge are already complete questions — **A-03** / **A-05**)
- the DET card still has numbered chrome (`^ {2}1 {2}` or `\n  1  `)
- not `want_live`
- domain_ai hub is `ask` without confirm, or `refuse_live_reason` is set

Local **always** named the take first. Paint is color, not the mouth.

### 5c. Free chat — never if local already held the pulse

Product: `surface/handlers.py` `_chat_via_adapter` only after command-check, pending confirms, and stay consume declined. Numbered doors never reach it. `engage.try_local_first` can still **steal the pulse back** before the adapter (recall ask-until-agree).

---

## 6. Quiet help — DET before, model slots, DET after

**Law:** **N-03** · **A-03** · **O-07**

Call site: `stay_with.py` `_consume_talk_through` — word-help first, then `qh.advise_before`, then `_apply_quiet_slots`. If slots route, that **is** the take. If not, floor families continue (stuck before empty before item-answer — see the respond map).

### 6a. Before — local already chose the rung

`advise_before`:

1. Pop `_quiet_help_advised`.
2. `enabled` (switch + path).
3. `smell_stay_talk`.
4. domain_ai hub ask without `_hub_ai_confirmed` → `None`.
5. `refuse_live_reason(state, "hub")` → `None`.
6. DET `_pack(state, text)` — **not** free-chat wrap. JSON instruction plus:
   - `format_boundary_for_prompt(active_boundary)`
   - `this_line`, `working_on`, `smaller_open`, `last_take`, `last_take_kind`
   - **`chosen_rung`** from `_chosen_rung_label` (DET, from last-take kind + nod/empty regex)
   - closed **MEANINGS** and **SHAPES** lists
   - a forbidden-phrase list in the prompt (harness, not people speech)
7. `route_chat(state, pack)` — one silent spend. Exception → `None` (floor).
8. `gate_slots` on the raw reply.

`_chosen_rung_label` is **local intellect**, same grain as the help-off paper: last-take kind plus a tiny DET nod/empty test. Quiet help may fill **one handle for that rung only**. It must not choose JUMP, LENS, or the rung (**A-03**).

| last_take_kind / test | chosen_rung sent to the model |
|-----------------------|-------------------------------|
| `need_list` + nod | `need_list_get` |
| `need_list` else | `need_list` |
| line matches empty-possession regex | `need_list` |
| `listed_lens` + nod | `accepted_lens` |
| `listed_lens` else | `list_door` |
| `list_door` + nod | `list_beat` |
| `list_door` else | `their_line` |
| `in_hand` + `enactment_failed` | `need_list` |
| empty / `in_hand` / `reach_handle` / `existence` | `listed_lens` |
| `their_line` + nod | `work-talk` |
| else | `work-talk` |

Nod test (`_line_is_nod`): whole-line `ok` / `okay` / `yeah` / `yep` / `yup` / `sure` / `fine` / `yes` / `that works` / `sounds good`. Empty test (`_line_is_empty`): regex `don't have any/anything/none | have none | have nothing`. These are **prompt labels for the model**, not the product family classifier. Product stuck vs empty is still `stay_with._looks_like_stuck` / `_looks_like_empty` on the floor if the gate drops.

### 6b. Closed vocab (what the model is allowed to mean)

**MEANINGS:** `nod` · `empty` · `stuck` · `ask-last` · `leftover-not-a-title` · `named-possession` · `defer-look` · `list-offer-accept`

**SHAPES:** `ground-stay` · `empty sit-with` · `deepen ground` · `start-list-beat` · `sibling` · `reprint last take` · `work-talk` · `listed-lens` · `list-door` · `their-line` · `default-offer` · `need-list`

Reply must parse as JSON (or key:value lines) via `_parse_slots`. Open prose is dropped.

### 6c. After — `gate_slots` (local wins)

Product: `quiet_help.gate_slots`. Fail → `advise_did_not_land` on the stay hold; SHOW BOUNDARY may say the advise did not land; idle people screens do not (**A-03**).

Drop the whole payload (`None`) when any of:

- parse failed
- meaning not in MEANINGS
- shape not in SHAPES
- they nodded **and** meaning is `ask-last` or shape is `reprint last take` (must not relabel okay)
- meaning `nod` **and** shape `sibling` (no sibling census on a nod)
- `_FORBIDDEN_MARK` or `_LEDGER_SPEAK_MARK` or `_SLOT_NAME_MARK` hits the blob or thought (kit, “the next line”, rooms, vector, row/child, live web, therapy, …)
- `object` longer than 40 characters
- shape `sibling` but `last_take_kind` is not `sibling_offer`

Identity veto: `thought_clones_last_take` — if the thought reprints `last_take` (or a sentence of it), thought is **cleared**, not the whole payload. Local still Grounds.

On pass: set `_quiet_help_advised`, optional 80-char crumb on the hold (`quiet_help_crumb` — local hold, not the model window — **A-02**), spine `QUIET_HELP_ADVISE`.

### 6d. Local still Grounds — `_apply_quiet_slots`

Product: `stay_with.py` `_apply_quiet_slots`. Second veto layer. Returns `None` to fall through to floor families.

DET still steals the pulse when local already knows the family:

- named possession / `_looks_like_named_possession` → `_named_possession_keep_ball` (quiet help must not steal this)
- open item-ask + `_looks_like_item_answer` → `_answer_to_ask_keep_ball` (quiet help must not steal a bare noun that fills the ask — **A-03**)
- eval/stuck + ask-last / reprint → `None` (floor eval/stuck)
- nod + sibling → `None`

Otherwise meaning/shape maps onto **existing** local handlers (`_amend_keep_ball`, `_eval_keep_ball`, `_quiet_thought_keep_ball`, `_ask_last_keep_ball`, `_defer_look_keep_ball`). `_quiet_thought_keep_ball` speaks a local template (`quiet_thought_take`) using the gated thought. **No JUMP.** Working_on stays the in-hand child.

**Compare:** Holds the architecture. Quiet help does **not** make `I don't know` mean empty. O-05 whole-line stuck still fires on the floor if slots miss or if meaning is stuck. Turning help on is not a synonym engine. Try 727 (help off) is the floor; help on would still not reclassify that line unless slots returned `empty` **and** `gate_slots` plus `_apply_quiet_slots` accepted it — and `_line_is_empty` does not match `I don't know`.

---

## 7. Stay-talk paint — DET after local named the take

**Law:** **A-03** · **A-05**

Call site: after stay consume returns a card, `engage.maybe_paint_stay_take(state, det_card, user_text=...)`.

If shape gates pass:

1. `grant_strip` kind `stay_take` — named take, in-hand, FOCUS, “paint this; do not invent a kit.” Empty sit-with adds extra: do not name other children; do not say the next step is to gather.
2. DET send text: restated instruction + the take + `format_boundary_for_prompt` + `wrap_send` (pack_block).
3. Spine `PAINT_STAY_TAKE`.
4. `route_chat`. Exception → DET card.
5. `after_candidate` (same sandwich as free chat).
6. `_one_paint_beat` — **DET length and kit gate on the painted sentence**:
   - drop if it contains quiz / house-versus-need / “is the next move” (unless that phrase is in the take) / “one short step” / start-there slogans / “doesn't need supplies”
   - drop if more than two sentences or more than 48 words
   - drop if `_KIT_EXTRA` token appears in paint and not in the take
   - drop if `_foreign_child_in_sentence` (sibling title not in the take)
   - drop if empty sit-with take and paint says gather-next
   - drop if it reprints their spoken leftover as “is the next move”
7. Drop if empty or `_is_unchanged_take_reprint`.
8. Else append the beat under the DET card: `{card}\n\n{beat}`.

The model is asked **not** to say “the line,” rooms, closets, “want a hand with,” “anything jump out.” That is prompt + `_one_paint_beat` + `_strip_invented_kit`, not a second grading model.

**Compare:** Skip-paint on `?` **holds** (CF-096 first-item ask stays a local question). Kit paint **fails** A-05 when `_KIT_EXTRA` / how-to marks miss a near-synonym (Try 727 “I misspoke… kit” with help off was Hybrid paint, not quiet help). A-05 Do not: do not grow sandwich regex as sitting law. Leftover kit lines are a new CF row, not a longer forbid list in this map.

---

## 8. Free chat — DET gateway then one adapter

**Law:** **A-04** · **A-05** · **A-06** · **A-11**

Product: `surface/handlers.py` `_chat_via_adapter`.

### 8a. Local-first — `try_local_first`

Product: `engage.try_local_first`. A people card means the model **does not run this pulse**.

1. `note_pulse_watch` → `watch.note_pulse` → cheap regex classify: `creation` | `environment` | `recall` | `write` (or mixed → recall wins). Stored as `last_pulse_watch`. Spine `PULSE_WATCH`. Silent on pure brainstorm. **Not a second model** (**A-05**).
2. `recall.try_consume` — they are answering a numbered stored-talk list.
3. Else `recall.try_before_chat` — ambiguous old-talk smell: local asks until they agree (**A-06**). Unique hit injects; they do not see “searching.”
4. `_maybe_grant_environment` — if they pointed at a dossier / last fetch, local places a strip. The model does not fetch.

`watch.classify` regexes (DET, not NLU):

- **recall:** that/the/our/last chat|talk|sitting; we talked/decided; remember when; what did we say; last time we; …
- **environment:** on the ledger/list; in focus; this/that task; the dossier; that file/essay; web search; you fetched
- **write:** add a task; mark complete; drop this task; write it down; put it on the ledger

### 8b. Spend and honesty gates (still DET)

Order in `_chat_via_adapter` after local-first:

| Step | DET | On fail |
|------|-----|---------|
| Secrets | `domains/ai/secrets.py` `contains_sensitive` → mask; people warning prefix | Masked text still may send |
| Refresh route | `refresh_connected_flag` if continuity is HYBRID/FREE_CLOUD/LOCAL and not connected | |
| domain_ai refuse | `refuse_live_reason` while `want_live` | Warm `offline_chat_reply` (no internal refuse dump). Spine `ADAPTER_BLOCKED` |
| domain_ai ask | queue `pending_hub_ai`; CONFIRM later | People CONFIRM/CANCEL card. No model yet |
| N11 longtext | `llm_longtext.verify` | Refuse message. No adapter |
| N11 context | `llm_context.pre_send_check` | Block message. Warn prefix may still attach on a later send |
| Persona / story | `persona_inject.prefix_for_chat`, `story_svc.prefix_for_chat` | Injected into send_text, not spoken as a second system |
| Boundary | `format_boundary_for_prompt(active_boundary)` when live | Hot slice every pulse. Window is not memory (**A-02**) |
| Suggestion tags | `build_chat_suggestion_instructions` | Protocol for tagged suggestions; local writes only after a meant yes |
| Pack | `engage.wrap_send` → `pack_block` | Granted strips + next-pulse mend |

`work_partner_brief` (`domains/ai/brief.py`) is the **adapter system line**, reused, not a second mouth (**A-11**). It is DET steer: stay with named work, do not invent ids, do not quiz supplies, do not treat I don't know as a title, paint `last_take` when present. Adapters attach it; people never see it as a screen.

### 8c. During — `route_chat`

Product: `domains/ai/router.py` `route_chat`.

DET sticky ladder. For each candidate provider:

1. Skip if `cap.rpd_exhausted` (local daily budget).
2. Skip if `llm_tight.preflight` mismatches (wrong model/key shape).
3. `ad.chat(text, state=state)` — **plain chat**. No tool belt (**A-04**). The model cannot `SEARCH CHAT`, `WEB SEARCH`, or walk the catalog.
4. On success: persist `last_provider_used`, optional failover awareness line, spine `ROUTE_CHAT`.
5. On failover-class error (401/402/403/429/5xx/529): mark failure, try next.
6. Hard non-failover: `wrap_hard_fail` coach, stop.
7. Exhausted: `recovery.note_route_exhausted`. Spine `ROUTE_CHAT_EXHAUSTED`.

The model never picks the next provider.

### 8d. After — candidate, then people body

1. `process_model_reply` — suggestion-tag harvest (local pending, not silent writes).
2. `after_candidate` — sandwich (section 9).
3. Warn prefixes (context / longtext warn) prepended.
4. Chat history append (user + model). Commands were excluded before this function.
5. Optional proactive nudge (DET suggest).
6. `still_here_line` if stay is pinned.

The model never authors a numbered list. If it tries, Dual register still forbids it as product chrome (**A-03** / **A-11**). Writes stay local: numbered yes, YES after explain, typed command that exists.

---

## 9. Sandwich DET (`pack_block` / `after_candidate`)

**Law:** **A-05** · **A-09**

Not a second grading LLM. Regex and string-in-strip checks. People never hear pack / sandwich.

### 9a. Pack this pulse — `pack_block`

Always DET. Placed after the usual boundary inject via `wrap_send`.

- Header: granted this pulse; trained knowledge free; do not invent stored talks, ledger ids, or a web lookup.
- **Next-pulse mend:** if `pending_ai_mend` is set, one honesty instruction (last speech claimed X; stored note is Y; in-character; do not say you are an AI that hallucinated), then clear the hold.
- `granted_coverage` if any.
- Up to four `granted_strips` (kind, coverage, body ≤ 1800). Empty → `(no extra strips this pulse)`.

Who places strips: local only (`recall.grant_strip`, paint’s stay_take grant, environment grant, unique recall inject). The model does not add a strip.

### 9b. After — `after_candidate`

| Check | DET | On hit |
|-------|-----|--------|
| Fake task ids | `_strip_fake_ids` — `TL\d+-\d{6}-\d+\.\d+` not on ledger and not in their line → replace with “a task on the ledger” | Sets mend |
| Unlabeled web | `_strip_unlabeled_web` — `https?://` not in this sitting’s fetched set | Strip / mend |
| Quotes not in strip | `_soften_fake_quotes` — quoted span ≥ 12 chars not in granted blob | Soften / mend |
| Invented kit | `_strip_invented_kit` — only if a stay take is on the hold. Sentence dropped if `_KIT_EXTRA` token not in take/grants/user text, or how-to / quiz / house-need marks, or empty-sit gather command | Mend |

If any claimed: `pending_ai_mend` for **next** pack; spine `CANDIDATE_MEND`. This pulse’s people line is the cleaned candidate, not a confession.

`_KIT_EXTRA` (closed token list, not a second mind): bleach, vinegar, baking soda, toilet brush, grout brush, rubber gloves, shower curtain, plunger, ammonia, magic eraser, soap(s), spray(s), cloths, cleaner, sponge(s).

**Compare:** Architecture **holds**. Phrase coverage **drifts** — A-05 forbids growing this list as sitting law. Pathing leftover (kit lecture, “the line,” rooms) stays a CF cut, not a longer regex in this paper.

---

## 10. What the model never decides

**Law:** **N-03** · **A-03** · **A-04** · **O-02**

Even with Hybrid and quiet help on, these stay **local DET**:

| Fact / move | Who |
|-------------|-----|
| `working_on`, JUMP vs LENS, which listed title is in-hand | Local (`_keep_in_hand`, gather-prefer). Quiet help must not JUMP |
| Method **rung** | Local. Quiet help gets `chosen_rung` as an input |
| Family of the line (`okay`, leftover, stuck, empty, I-have, answer-to-ask) | Local consume table. Quiet help may **label** a meaning; `_apply_quiet_slots` can refuse and fall through |
| Numbered menu / digit | Local. Model never authors doors |
| Ledger write, FOCUS, complete | Local, after a meant yes |
| Retrieve (chat search, dossier, web) | Local. Model has no tools |
| Whether quiet help / Hybrid / web is on | Nested people consent. FLOW cannot turn quiet help or AI on |
| Gather-prefer after find-block | Local title scan. Unchanged by this map |

The help-off intellect paper still describes the floor. This paper adds color and one optional handle. It does not replace gather-prefer with a model interview.

---

## 11. One pulse — model involved (stay-talk)

```text
they type (chrome already shelved; awaiting_talk)
    → word-help DET (feature question → local card; no model)
    → quiet help enabled?
         no  → floor consume (stuck → empty → possession → item-ask → eval → leftover)
         yes → smell_stay_talk?
              no  → floor consume
              yes → domain_ai / path ok?
                   no  → floor consume
                   yes → DET _pack (boundary + chosen_rung + closed vocab)
                        → route_chat
                        → gate_slots
                             fail → advise_did_not_land; floor consume
                             pass → _apply_quiet_slots
                                  steal/refuse → floor family handler
                                  accept → local template from thought or family
    → local card always
    → maybe_paint_stay_take
         skipped if quiet help advised this pulse
         skipped if take contains ?
         skipped if numbered chrome or not want_live or domain refuse
         else grant stay_take strip → route_chat → after_candidate → _one_paint_beat
              fail → DET card only
              pass → DET card + one painted beat
```

Free chat skips stay consume, then `try_local_first` may still return a people card (recall list). Only then: spend gates → pack → route_chat → after_candidate.

---

## 12. Spine / cognizance when a model runs

**Law:** **C-09** · **A-02**

The model does not read the spine. Local injects the hot slice every pulse (`format_boundary_for_prompt`). Quiet-help crumbs live on the **local hold**, not in the model window.

Events this map cares about (names people never hear):

| Event | When |
|-------|------|
| `QUIET_HELP` | Switch on/off |
| `QUIET_HELP_ADVISE` | Slots passed the gate |
| `QUIET_HELP_OFFER` | On/Off card after SETUP |
| `PULSE_WATCH` | Free-chat classify |
| `ADAPTER_CHAT` / `AI_ENGAGED` | Free-chat send / live reply |
| `ADAPTER_BLOCKED` | domain_ai / longtext / context |
| `HUB_AI_PENDING` | domain_ai ask queued |
| `PAINT_STAY_TAKE` | Paint spend |
| `ROUTE_CHAT` / `ROUTE_CHAT_EXHAUSTED` | Router |
| `CANDIDATE_MEND` | Sandwich claimed a leak |

SHOW BOUNDARY can see granted strips, coverage, and (when the gate dropped) that advise did not land. Idle pulse-0 does not dump slot names.

---

## 13. Compare (Hold / Drift / Fail)

| Lock | Chunk | Verdict |
|------|-------|---------|
| Local decides beat and speaks stay-talk | N-03, A-03 | **Holds** |
| Quiet help: one handle for chosen rung; fail → floor | N-03, A-03 | **Holds** |
| Quiet help off until nested consent; FLOW cannot turn it on; needs live path | O-07 | **Holds** |
| Live digit / menu never advises | C-03, A-03 | **Holds** (`smell_stay_talk`) |
| Local owns EVAL / STUCK / answer-to-ask; okay is not ask-last | A-03, C-06 | **Holds** in `gate_slots` + `_apply_quiet_slots`. Quiet help is **not** a synonym engine for `I don't know` vs empty |
| Skip paint on a complete question (`?`) | A-03, A-05 | **Holds** |
| Paint the named take only; no invented kit | A-03, A-05 | **Fails** when paint leaks kit/how-to that `_KIT_EXTRA` / `_one_paint_beat` missed (Try 727 Hybrid paint). **Do not** grow regex as this sitting’s law |
| Identity veto (thought ≠ last take) | A-05 | **Holds** (`thought_clones_last_take`) |
| Local gateway; no model tool belt | A-04, A-11 | **Holds** |
| Unique recall silent; ambiguous ask until agree | A-06 | **Holds** (`try_local_first`) |
| Pathing never live web; unlabeled URL stripped | A-07, A-05 | **Holds** the strip. G-WEB depth still deferred |
| Cheap pulse-watch; not a watcher LLM | A-05, A-09 | **Holds** |
| Banner: AI on ⇒ chat works; quiet help shown | C-08 | **Holds** as lock; honesty is a Try surface |
| Model never authors numbered lists | C-03, A-11 | **Holds** as product chrome |
| Next-pulse mend in character | A-05 | **Holds** (`pending_ai_mend` in `pack_block`) |
| People never hear sandwich names | A-01, A-09 | **Holds** |

---

## 14. Where to open next

| Question | Open |
|----------|------|
| Who runs the sitting | **N-03** |
| Who may speak on which surface | **C-03**, **A-03** |
| Pattern-sense vs second Daniel | **A-02** |
| Gateway; no tool belt | **A-04** |
| Sandwich / pulse-watch / mend | **A-05** |
| Recall until agree | **A-06** |
| No web pathing | **A-07** |
| Quiet help consent | **O-07** |
| Banner | **C-08** |
| One engagement path | **A-11** |
| Product: quiet help gates | `domains/ai/quiet_help.py` `enabled`, `smell_stay_talk`, `advise_before`, `_pack`, `gate_slots`, `_chosen_rung_label` |
| Product: apply slots | `domains/tasks/stay_with.py` `_apply_quiet_slots`, `_quiet_thought_keep_ball` |
| Product: paint | `domains/ai/engage.py` `maybe_paint_stay_take`, `_one_paint_beat` |
| Product: sandwich | `domains/ai/engage.py` `try_local_first`, `pack_block`, `after_candidate`, `wrap_send` |
| Product: pulse-watch | `domains/ai/watch.py` `classify`, `note_pulse` |
| Product: free chat | `surface/handlers.py` `_chat_via_adapter` |
| Product: router | `domains/ai/router.py` `route_chat` |
| Product: domain / global | `packages/security/domain_ai.py`, `packages/security/policy.py` `allow_ai` |
| Product: brief | `domains/ai/brief.py` `work_partner_brief` |
| Local-only floor (help off) | [`HOW_DANIEL_THINKS_LOCAL.md`](HOW_DANIEL_THINKS_LOCAL.md) |
| Talk families / leftover | [`HOW_DANIEL_RESPONDS.md`](HOW_DANIEL_RESPONDS.md) |
| Speech, people words, defined-word use | [`HOW_DANIEL_TALKS.md`](HOW_DANIEL_TALKS.md) |

This file is a map of **gates and DET harness**. The model is color on a floor that already thinks. Changing N-03 so the model classifies the line, or growing sandwich regex as law, is guide-update, not a silent edit here.
