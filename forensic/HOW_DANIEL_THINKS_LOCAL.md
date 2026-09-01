# How Daniel thinks locally

> **Public copy.** Adapted from the private Planning `FORENSIC/` maps so readers
> without that repository can still see how the machine is described. **Not law.**
> Chunk ids such as N-03 or C-04 name files in the private `governance/` tree.
> Product paths name files in the private product repository. Hold / drift / fail
> means: the running program matches the lock, only partly lives it, or contradicts it.

---

**Status:** Forensic map. **Not law.** Chunks under `governance/` win if this file and a chunk disagree.  
**Date:** 2026-08-31  
**Snapshot:** Product `79eeb97` (CF-096 Complete).  
**Scope:** **Quiet help off. Local only.** No model classifies the line. No quiet-help advise. No Hybrid paint. Banner would read `DET:ON AI:OFF` (or paint skipped because no live path). This is the AI-off floor `N-03` requires.  
**Companion:** Talk families, leftover, and Hybrid color live in [`HOW_DANIEL_RESPONDS.md`](HOW_DANIEL_RESPONDS.md). Gates and DET harness when a model is involved live in [`HOW_DANIEL_THINKS_WITH_MODEL.md`](HOW_DANIEL_THINKS_WITH_MODEL.md). This paper is the **menu pick** and **spine / cognizance** half.  
**Not this file:** A coding paper. A house model. A second mind. Reopening Track S. Changing gather-prefer.


**How to read the compare:** **Holds** = product matches the lock. **Drifts** = lock is live but only partly lived. **Fails** = product contradicts a lock.

---

## 0. Law register

This map is stay-with plus menus plus nervous system, **with the model gated out**. Open communication, organism, substrate, and **N-03**. Skip Hybrid engagement chunks except where they lock the floor (AI off still moves; no silent model on a numbered pick).

| Chunk | Job for this map |
|-------|------------------|
| **N-03** | Local decides the beat and speaks. AI off still moves |
| **N-01** | Industry-grade is honesty/testability, not the model as product |
| **C-02** | Continuity with consent + pathing when blocked |
| **C-03** | Numbered menus are local templates. Never the model. Local logic first |
| **C-04** | Lists are for a yes. Find-block. Collaborative ball. Internals off people screens |
| **C-05** | Show the list, then accept the digit. HELP anytime. SHOW MENU reprints |
| **C-06** | Talk shelves chrome; digits stale until SHOW MENU |
| **C-08** | Banner honesty; after a pick, where am I and what can I type |
| **C-09** | Every turn that matters emits a hold the boundary can see |
| **C-12** | System speech in helpers; numbered_picks; find-block starts talk-through |
| **O-01** | What he is; intelligence named; model does not run the sitting |
| **O-02** | Cognizance from **local facts**; gather-prefer; he carries the next move |
| **O-03** | Digit is consent; he keeps bouncing unless they stop |
| **O-04** | Sense → Ground → next beat; silent prepare; consume-ask after find-block |
| **O-06** | Two surveys: catalog tools + outstanding ledger work. Hot slice only |
| **O-07** | Quiet help off until nested consent; FLOW cannot turn it on |
| **O-08** | DET surveys; model does not invent tools or fire commands |
| **O-09** | Sitting facts on the active boundary |
| **S-01** | Substrate is awareness bus, not a second mind, not all of Daniel |
| **S-02** | Atomic outbox; mediator; reaching is silent hot-boundary prepare |
| **S-03** | DET default |
| **S-05** | End-to-end protocol: write + event → fanout → DET assess → speak. AI never required |

**Skipped:** C-07 Atlas packs; C-10/C-11 leftover-hunt script (use when cutting a paper); A-03–A-05 paint/quiet-help (gated **off** here); A-02/A-04 still true as “model does not browse,” but this floor does not call the model; G-WEB; reaching 3E scorer (off by default).

---

## 1. What local intellect is

**Law:** **O-01** · **O-02** · **N-03** · **C-02**

He does not “reason” the way a model does. There is no inner monologue, no chain-of-thought, no world simulation. **Cognizance** is knowing, from **local facts**:

1. What is in **focus**.
2. What is **outstanding** on this ledger (rows already written — not a kit he imagined).
3. What **tools match** this sitting (catalog organs, not HELP as a quiz).
4. Which **beat** we are on (look-at, stay offer, sit-through, talk-through).
5. That **he carries the next move** unless they pause, CANCEL, LEAVE THIS, EXIT, or take the ball.
6. Which child is **in-hand** (named, else gather/supplies/tools title, else first open).

That is the whole intellect. Pathing when blocked is: Ground, then **one method** that still is this task. Continuity is: the ledger and spine remember.

**Compare:** Holds as design. The rigidity Designer feels on find-block is this intellect doing its job: match a title, pick gather-prefer, speak a template. It is not a failure to “think about the bathroom.” There is no bathroom organ.

---

## 2. One pulse — local only, help off

**Law:** **C-05** · **C-08** · **C-03** · **S-05** · **N-03**

```text
they type
    → pulse_count += 1
    → set_turn_meta (pulse, session, ledger)   so every spine event shares this turn
    → if a numbered list is live and they typed a digit in range
         → do not call quiet help (even if it were on)
         → do not call Hybrid
         → map digit → option index (1-based people, 0-based code)
         → run that door’s local handler
         → handler may read ledger, set hold, append_event, save session
         → print the next local card
    → wrap_response: banner + body + one-line footer
```

Quiet help’s own smell (`quiet_help.smell_stay_talk`) **returns false** on a live digit. `C-03`: no silent model calls for sticky/spendy options. A menu pick is a **yes**, not a sentence to interpret.

If Hybrid were on and the next card were stay-talk *without* numbered picks, paint could still run. **This paper assumes it does not** (AI off, or skip-paint). Try 720–733 had Hybrid on with help off; that paint leak is the companion paper, not this floor.

**Compare:** Holds. AI off still moves. Menus never AI-authored.

---

## 3. Spine and awareness on every pulse

**Law:** **C-09** · **S-01** · **S-02** · **S-05** · **O-02** · **O-06** · **O-09**

Three layers. They are not a second Daniel.

### 3.1 Session hold (working memory)

The stay lives in `state.session`: `pending_stay_with`, `pending_sit_through`, `pending_work_block`, `picks_live`, `working_on`, `last_take`, `last_take_kind`, `eval_stall`, `pathing_rung`, smaller titles copied onto the hold.

**This is what the next pulse actually reads.** Stay-talk does not query the graph to decide the sentence. It reads the hold + ledger rows.

### 3.2 Spine events (outbox)

`append_event(category, kind, payload)` writes one JSON line (`data/spine/events.jsonl`), stamps this pulse from `set_turn_meta`, then sync-fanout (index, graph projection, reaching).

Command dispatch always emits `command / DISPATCH` via the mediator (`S-02` 2A), even if the handler forgets. Stay-with also emits kinds such as `STAY_WITH_OFFER`, `TALK_THROUGH`, `TALK_EVAL_KEEP`.

The bus is **coverage**: later SHOW BOUNDARY / snapshot / (if Hybrid were on) the brief can see the turn. It is not a reasoner.

### 3.3 Active boundary (hot slice)

`active_boundary()` in `spine/graph_ledger.py` **projects** session + recent events into one dict: focus, ledger, open pendings, `working_on`, `last_take`, stall, quiet help on/off, smaller_open, etc.

Local stay-talk **writes** those fields onto the hold so the boundary can see them (`C-09`). Local stay-talk does **not** call `active_boundary()` to choose gather-prefer. Gather-prefer reads `_smaller_titles` from the ledger file.

People inspect with **SHOW BOUNDARY**. They never hear field names (`C-04` internals).

### 3.4 Reaching (silent prepare)

**Law:** **O-04** silent prepare · **O-06** · **S-02** 3A+3B+3D · **O-08**

When named work is pinned, reaching may **warm** the hot boundary and memory. People do not see a menu of warms. Unasked RESOURCE ALIGNMENT is parked as a first stuck. Reaching mode can be off. The 3E AI scorer is off by default.

After a **command** dispatch, `maybe_after_dispatch` may evaluate rules (throttled). A stay-with **digit** that never goes through `mediate_dispatch` may not hit that hook; the hold still saved, and `append_event` still fanouts.

**Compare:**

- **Holds:** Event + hold + boundary exist. DET default. No second mind. Hot slice, not a dump of every row.
- **Drifts:** O-04 “silent prepare warms outstanding smaller tasks… first thin pulse delivers that piece” — the **delivery** is gather-prefer + consume-ask, not reaching naming a tool. Reaching is mostly prefetch/status, not the people next method.
- **Does not:** Spine does not infer why they picked 2. Graph edges are a projection of events already emitted.

---

## 4. When a menu option is selected

**Law:** **C-04** · **C-05** · **C-12** · **O-03** · **C-03**

Numbered lists are **necessary for consent** (write a row, spend, pick a hub step, pick find-block). They are not everyday support (`O-04` body). A sitting that is only `1 / 2 / 3` feels finite even when the picks are correct. That Want is live.

### 4.1 What the digit is

`_pick_index`: if the line is all digits and `1 ≤ n ≤ len(options)` and `picks_live`, the index is `n - 1`. No synonym. No “they meant the second idea.” Wrong number or stale digit: not that door (`C-05` / `C-06`).

There is **no analysis of motive**. He does not ask why they picked find-block. The pick **is** the yes.

### 4.2 What does not run

| Gated off on a live digit | Law |
|---------------------------|-----|
| Quiet help advise | C-03 no silent model on spendy options; `smell_stay_talk` false |
| Hybrid paint of the pick itself | Menus never AI-authored |
| Line-family classifier (stuck / empty / leftover) | Digit is not English leftover |
| Gather-prefer | Not yet — that runs **after** find-block, when composing the next card |

### 4.3 What does run (index switch)

Stay offer (`_consume_stay_pick`) — pulse 724 class:

| Digit | Door | Local effect |
|-------|------|----------------|
| Name smaller tasks | Elicit | Consent to write children |
| Daniel continues with ideas | His ball | He speaks a next thought (`O-03`) |
| I'll take the next line | Their ball | They have the next line |
| Let's complete this task | Stay yes | Pin FOCUS; sit-through list (`C-04`) |
| Pause | Pause fork | Row stays on the ledger |
| Task actions | Nested list | Complete / drop / due / … |

Sit-through (`_consume_sit_pick`) — pulse 725 class:

| Digit | Door | Local effect |
|-------|------|----------------|
| 1 Mark complete | Write | `complete_task`; hold cleared |
| 2 Find what is in the way | Start the find | `_open_talk_through` (`C-04`, `C-12`) |
| 3 Split | Split offer | Smaller-task consent |
| 4 Pause | Pause | Row stays |

Look-at / where-are-we digits focus a **row already on the ledger**. That is matching, not inventing (`C-09` local logic first).

**Compare:** Holds as consent machine. **Drifts** vs collaborative Want: the find-block pick does not open a conversation about the block; it **executes** start-the-find. That is the lock (`C-04` after they pick it, start the find).

---

## 5. After the pick — where DET “logic” lives

The intellect that feels like thinking happens **composing the next card**, still with no model.

### 5.1 Find-block → talk-through (the usual Try)

**Law:** **O-02** · **O-04** · **C-04** · **C-12**

`_open_talk_through`:

1. `ledger.focus_task` on the parent (already focused).
2. `_smaller_titles` — open children **already written** on this parent.
3. **Gather-prefer:** first title containing `gather` / `supplies` / `tools`; else first open; else the parent. String match. Not “cleaning needs supplies.”
4. Write `pending_work_block`: `working_on` = that title, `examples` = the child list, `ledger_facts` = true if children exist, `eval_stall` = 0, chrome **stale** (`awaiting_talk`).
5. `append_event("command", "TALK_THROUGH", …)`.
6. Speak template: `{in-hand} is the next move. What supplies do you already have for {parent}?` (`voice.in_hand_take`). Kind `in_hand`. No lens. No JUMP.

If this parent had **no** smaller tasks, he would not invent Gather supplies as a silent write (`O-02`, CF-076). Cue packs (`cue_jobs_for`) match bathroom/garden/app **wording** only when offering examples to **write**, after they asked to name or split — not as fake ledger rows on find-block when children already exist.

### 5.2 Sense → Ground → next beat (O-04), on a digit

On a **digit**, Sense is “they yes’d this door.” Ground on the next card is often the FOCUS pin + naming the in-hand title, not “I heard you said 2.” Intuit is which template matches that door. The next sentence is the consume-ask.

That is weaker Ground than talk (`C-04` Ground this line names what they said). A digit is not a sentence. The lock still wants the next screen to answer **where am I** and **what can I type now** (`C-08`). FOCUS pin + consume-ask + talk footer does that.

### 5.3 What he does not do after the pick

- Does not survey the house (`A-04` even if Hybrid were on: model never accesses the house; local has no house store).
- Does not rank siblings by chemistry or “smallest first” unless they pick that **other** sit door (`Start with the smallest open task` is a different index).
- Does not call live web for pathing (`A-07`; this floor does not call web anyway).
- Does not invent bleach / under the sink (`O-04` local help-off).

**Compare:** Gather-prefer **holds** as law and as code. Collaborative discover-the-block **drifts** (Want in `C-04` / `O-04` vs silent first child). Cue-pack matching bathroom titles **holds** only as suggestion source, not as find-block in-hand when ledger children exist.

---

## 6. Worked example — digits only (help off, local floor)

Same bathroom sitting as Try 720–733, **stopping where talk begins**. If AI were off, pulses 723–726 would look like this with no second paint paragraph.

| Pulse | They typed | What local read | What local did | Spine / hold | Law |
|-------|------------|-----------------|----------------|--------------|-----|
| 723 | `where are we` | Command/talk organ, not a digit | Print ledger recap; `picks_live` on those rows | Recap hold; last_take uncleared (`C-09`) | C-04 where-are-we |
| 724 | `2` | Live digit; option 2 = focused parent | Look-at; stay offer; digits live on **new** list | `STAY_WITH_OFFER`; `pending_stay_with` | C-05 show list then digit |
| 725 | `4` | Live digit; Let's complete this task | Pin FOCUS; sit-through list; start-the-find is pick 2 | `pending_sit_through`; FOCUS | C-04 stay door |
| 726 | `2` | Live digit; Find what is in the way | **No** family match. `_open_talk_through`. Ledger children → gather-prefer → consume-ask. Chrome **shelved** | `TALK_THROUGH`; `working_on` = Gather supplies; `last_take` = consume-ask; `last_take_kind` = `in_hand` | O-02, O-04, C-12 |

From pulse 727, they type English (`i don't know`). That is **not** a menu pick. Classifier + method ladder = companion paper. Local-only, that ladder still runs (`_eval_keep_ball`); only paint and quiet help stay off.

**Compare:** Digit path **holds**. The jump from “find the block” to “Gather supplies is the next move” is gather-prefer, not spine inference.

---

## 7. Two surveys — toolkit vs outstanding

**Law:** **O-06** · **O-08**

| Survey | Truth | Used on a find-block digit? |
|--------|-------|------------------------------|
| **Toolkit** | Command catalog | No. He does not offer RESOURCE ALIGNMENT or LIST TASKS as the find. Unasked alignment is parked |
| **Outstanding work** | Ledger + focus + smaller jobs already written | **Yes.** `_smaller_titles` is this survey. Hot slice only |

Matching the whole bench (calendar, marks, GENERATE) is **not** what find-block does. Cognizance on this pulse is outstanding children + in-hand title.

**Compare:** Holds for outstanding. Toolkit survey is mostly idle on this Try path (O-06 Want: person should not need HELP to discover tools — **drifts** here; he pathings on gather instead of naming a matching organ).

---

## 8. What local intellect is not

| Not present | Law that keeps it out |
|-------------|------------------------|
| Model planning the next beat | N-03, C-03 |
| Dialog-act / NLG / JSON mouth | N-03 Do not |
| Watcher LLM grading the pick | A-05 (companion); N-03 |
| `has_supplies` table | O-02 Do not |
| Four-layer scene / affordance graph | N-03, O-02 |
| Live web to decide the next move | A-07; O-04 Do not |
| Therapy / how do you feel | O-04 |
| Census of all children with no move | O-02 Do not |
| Silent JUMP because they picked find-block | O-02, O-04 |
| People-visible stall policy | O-03 Do not |

The AI-off floor can still feel like a finite state machine. That is honest. Law wanted mixed-initiative conversation **after** chrome is shelved (`C-04`, `O-04`). The digit itself is supposed to be rigid. The leftover hunt is the **talk** that follows, not the pick.

---

## 9. Law vs product — synthesis (local, help off, menus)

| Lock | Chunk | Local menu path |
|------|-------|-----------------|
| AI off still moves | N-03 | **Holds** |
| Menus local; no silent model on a digit | C-03 | **Holds** |
| Show list then digit; stale after welcome/talk | C-05, C-06 | **Holds** |
| After a pick: where am I, what can I type | C-08 | **Holds** (FOCUS + next list or consume-ask + talk footer) |
| Lists are for a yes; fabric is conversation | C-04 | **Holds** the yes; **drifts** the fabric until chrome is shelved |
| Find-block starts the find | C-04, C-12 | **Holds** |
| Gather-prefer first in-hand | O-02, O-04 | **Holds** |
| Cognizance = local facts, not invented kit | O-02 | **Holds** |
| Spine event + boundary hold | C-09, S-05 | **Holds** on stay/talk-through emits |
| Silent prepare ≠ people menu of warms | O-04, S-02 | **Holds**; reaching is not the next method |
| Quiet help off until nested consent | O-07, C-05 | **Holds** |
| Internals off people screens | C-04 | **Holds** |

---

## 10. Where to open next

| Question | Open |
|----------|------|
| Who runs the sitting / AI-off floor | **N-03** |
| Cognizance | **O-02** |
| Sense → Ground → beat; silent prepare | **O-04** |
| Two surveys | **O-06** |
| Digit / HELP / SHOW MENU | **C-05** |
| Lists as consent; find-block | **C-04** |
| Coverage / boundary | **C-09** |
| Outbox + reaching letters | **S-02** |
| DET-first protocol | **S-05** |
| Product: digit → door | `stay_with.py` `_pick_index`, `_consume_stay_pick`, `_consume_sit_pick`, `_open_talk_through` |
| Product: pulse + banner | `main.py` `handle_line`, `kernel/banner.py` `wrap_response` |
| Product: events + hot slice | `spine/events.py`, `spine/graph_ledger.py` `active_boundary` |
| Product: silent prepare | `packages/reaching/service.py` |
| Talk after chrome is shelved | [`HOW_DANIEL_RESPONDS.md`](HOW_DANIEL_RESPONDS.md) |
| Gates / sandwich / quiet help / paint when a model is on | [`HOW_DANIEL_THINKS_WITH_MODEL.md`](HOW_DANIEL_THINKS_WITH_MODEL.md) |
| Speech, people words, defined-word use | [`HOW_DANIEL_TALKS.md`](HOW_DANIEL_TALKS.md) |

This file is a map of **local-only intellect**. A menu pick is consent, not interpretation. Analysis is ledger facts plus a title scan plus a template. Spine records the turn; it does not think it. Changing gather-prefer or find-block into a collaborative interview is guide-update, not a silent edit here.
