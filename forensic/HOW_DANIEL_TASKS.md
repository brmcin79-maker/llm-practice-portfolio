# How Daniel tasks

> **Public copy.** Adapted from the private Planning `FORENSIC/` maps so readers
> without that repository can still see how the machine is described. **Not law.**
> Chunk ids such as N-03 or C-04 name files in the private `governance/` tree.
> Product paths name files in the private product repository. Hold / drift / fail
> means: the running program matches the lock, only partly lives it, or contradicts it.

---

**Status:** Forensic map. **Not law.** Chunks under `governance/` win if this file and a chunk disagree.  
**Date:** 2026-08-31  
**Snapshot:** Product `79eeb97` (CF-096 Complete).  
**Scope:** Listing and tasking: what a **task** is, how a line becomes one, smaller tasks, **focus**, **complete** / **drop** / **LIST ARCHIVE**, **project** as a ledger heading, **stay one task**, fork, related-task collision, logs and snapshots. Two **roadmap** meanings. Garden three-paths (`TASKING_EVOLUTION.md`) is discuss only — not this map’s law.  
**Companion:** Speech: [`HOW_DANIEL_TALKS.md`](HOW_DANIEL_TALKS.md). How a line is classified: [`HOW_DANIEL_RESPONDS.md`](HOW_DANIEL_RESPONDS.md). Local intellect: [`HOW_DANIEL_THINKS_LOCAL.md`](HOW_DANIEL_THINKS_LOCAL.md).  
**Not this file:** A coding paper. Shipping locked / gated / open as people words. Parent/child as a new organ. Item notes (CF-097 gated). `has_supplies`. A second quick-list product.


**How to read the compare:** **Holds** = product matches the lock. **Drifts** = lock is live but only partly lived. **Fails** = product contradicts a lock.

---

## 0. Law register

This map is **organism** (what is outstanding, writes wait, JUMP) plus **communication** (people words, lists as consent, chat color is not a task). Local owns writes (**N-03**). Garden brainstorm is not a chunk.

| Chunk | Job for this map |
|-------|------------------|
| **C-02** | Continuity with consent. Chat color is not already a task |
| **C-04** | People words: ledger, focus, task, complete, drop. Items on a task are not tasks until a yes |
| **C-05** | Look-at stay-with doors. Close-out YES. LIST ARCHIVE. Keep this as one task |
| **C-06** | Likes never write. Help-me is not a project heading. Collision. Stay one. Leftover is not a title |
| **C-09** | Holds on the boundary: smaller_open, stay_one, working_on, named_set |
| **C-12** | `add_task` is the writer. Eval/stuck/empty never mint a row |
| **N-03** | Local owns writes and `working_on` |
| **O-02** | Outstanding children are ledger facts. Gather-prefer. Leftover does not mint |
| **O-03** | COMPLETE / DROP TASK / LIST TASKS / LIST ARCHIVE / FOCUS as verbs |
| **O-04** | Lists for consent. Silent write is forbidden. Cue packs wait for Name smaller tasks |
| **O-05** | Thin speech never a title. Outstanding smaller tasks are facts. Stay one until they ask to grow |
| **O-06** | Outstanding-work survey: ledger, focus, smaller jobs, project title, saved chat roadmap idea |
| **O-07** | Writes still wait. Add-all only from numbered door or write-verb yes. Auto-group is an offer |

**Skipped:** C-07 Atlas packs (cite when cutting HELP copy); C-11 leftover script; F-01–F-05 (no new organ this turn); P-01–P-03 (Complete of a CF paper ≠ complete of a task); garden F4 three paths — `TASKING_EVOLUTION.md` (private Planning file) discuss only.

---

## 1. The objects (people vs disk)

**Law:** **C-04** · **C-12** · **O-03**

One companion. **One live list** per active ledger. Not a second notebook product.

| People word | What it is | What it is not |
|-------------|------------|----------------|
| **Ledger** | The task list they stay with. File `data/ledgers/daniel_ledger_{id}.md`. Registry holds title, project heading, linked ids, stay-one ids | Workbook. “Live list” as a second name. A jot-pad notebook |
| **Ledger title** | Name of this ledger (`TITLE LEDGER`). Default UNTITLED | The project heading |
| **Task** | One **active** ledger row, written by `add_task` | Chat color. A like. I don't know. An item they named while staying. A suggestion set until a write-yes |
| **Smaller tasks** | Other active rows that already belong to this parent (project links + usual-kit titles already written) | A blank tree he invented. Cue-pack titles that were never yes’d |
| **Focus** | The command and the people word for the ledger **task** we stay with (`active_focus_task_id`) | “In front” as a second product. “Later notes attach” as the people definition |
| **Complete** | After a yes: this task is done; it **leaves this ledger** (status COMPLETED; row retained). LIST ARCHIVE can put it back | Checking an item off a need-list. Drop. Auto-close of children |
| **Drop** | After a yes: I am not going to do this task (status DROPPED). History keeps it | CANCEL (leaves a menu). Complete |
| **LIST ARCHIVE** | Live numbered menu of completed, dropped, and forked jobs. Pick one to put completed/dropped **back**. Forked are named, not reopened from here | A dump you cannot pick. A delete |
| **Project name** | A **short heading on this ledger** (`project_title` in the registry). Optional `project_task_ids` link rows under it | A new app. A second list. Minted from “help me mop” |
| **Stay one task** | A leaf mark: this row will not grow smaller tasks, a project, or a roadmap until they transfer. Numbered yes: **Keep this as one task.** After: **This is one task.** | A people name (“simple task”). Locked/gated/open |
| **Item** | A supply/referent named while staying with a task | A ledger task until a yes. CF-097 durable check-off is **gated** until the phrase is locked |

Disk row fields (people never hear the headers as speech): `TASK_ID`, `ORIGIN_PULSE`, `DS_DATE`, `DESCRIPTION`, `STATUS`, `DUE_DATE`, `LINEAGE`. Ids look like `TL1-…`. Statuses: ACTIVE, COMPLETED, DROPPED (legacy CANCELLED still reads as dropped), FORKED.

**Compare:** Holds one-list, one-writer. Parent/child is **inferred** from links + title match, not a first-class organ (garden F1 still discuss).

---

## 2. How something becomes a task

**Law:** **C-12** · **O-07** · **C-02** · **N-03**

**`ledger.add_task` is the only writer.** Accidental SET KEY / SETUP AI / ingest pastes are never tasks. Secret-shaped text on an explicit TASK walk **warns**; only a masked reminder or a short label may be written.

Consent bar: a numbered pick, **Add all of these**, or a yes that names writing (put / add / take / save / write). Liking the set, including “I like all of those,” is not consent (**O-07**).

### 2a. Doors that write

| Door | Mechanic | After the write |
|------|----------|-----------------|
| Typed **TASK** + remainder, or bare TASK then the next line | `start_task_describe` → `add_task` | Optional finish card, then stay-with / look-at unless `finish_card=False` |
| Chat overlay **YES** on a *new* named idea | `add_task(..., finish_card=False)` then short stay-with | Does **not** steal FOCUS from a parent already in stay (**C-05**) |
| Stay-with **Add all of these** / write-verb yes on offered examples | Loop `add_task` on shaped titles | Collision check first (CF-079) |
| Type your own while naming is open | Same writer after shape + collision | Named child already on this parent still matches |
| **Add anyway** on a collision card | `force` write | Second row with same wording, same parent — they meant it |

Before a **new** row from chat: conservative match against active titles (`related.find_related_active`). If related: numbered **look at the one they already have** vs **add a new row anyway** vs keep talking (**C-04**). Same parent + **exact** wording: `duplicate.sibling_by_wording` — look-at vs add-anyway vs **Don't add**. Two different parents may share a wording. No silent unique-title skip of the whole ledger.

### 2b. What never becomes a task

**Law:** **C-06** · **O-05** · **C-12**

- Evaluation: okay, yeah, fine, I like these, I like all of those, I said okay
- Stuck/blank: whole-line I don't know / idk / I dunno
- Empty-possession: I don't have any of those / I don't have anything
- Leftover English while stay is pinned (does not retitle `working_on`, does not start new intake)
- A question about the last beat
- Work-shaped **help me mop** (help with the doing, not a project name and not a heading)
- Greeting `hi`
- Chat bullets / model outline headings until they asked to write them (`cue_jobs.jobs_from_last_outline` only after a write-ask)
- Cue-pack “usual jobs” spoken as examples — **not silent rows** when children already exist (**O-02**, CF-076)
- Items named on a consume-ask until a yes (**C-04**)
- Pulse-0 “tracked as a task” only when the last typed line matches a written row

**Compare:** Holds the writer and the never-mint families. Cue packs still **suggest** bathroom/garden/app wording for Name smaller tasks; they must not appear as if they were already on the ledger when they are not.

---

## 3. Relationships (parent, smaller, in-hand)

**Law:** **O-02** · **C-05** · **C-09**

There is **no shipped parent/child organ**. “Smaller tasks on this parent” is a **local survey**:

`ledger.smaller_open_for(parent_id, parent_desc)`:

1. If the parent id is in this ledger’s `project_task_ids`, every other linked id that is still ACTIVE counts.
2. Else/also: active rows whose **title** matches a usual-kit string from `cue_jobs_for(parent_desc)` (Gather supplies, Clean the sink, …) — only if those rows were **already written**.

Unrelated rows on the same ledger stay out.

**In-hand** (`working_on`): they named it; else a gather/supplies/tools title already on this parent; else the first open. Thin speech and talk-through work **with** that row. JUMP changes `working_on` only after an accepted lean. First talk-through: no lens (gather-prefer) (**O-04**).

Look-at a task: quiet Looking-at line, then if smaller tasks exist **name them as facts**; if none, offer that this can stay one task or they can name smaller ones. Numbered stay-with: name smaller tasks, Keep this as one task (leaf only), Daniel continues with ideas, I'll take the next line, pause, task actions, Let's complete this task. Nested lists do not re-offer the stay door.

Name smaller tasks is **not a blank tree** when children already exist — Tasks so far lists them.

**Stay one:** `mark_stay_one` refuses if smaller_open_for is non-empty. Transfer (lifts the mark): Name smaller tasks, split-ask, or **PROJECT TITLE** (`clear_stay_one`). While the mark is on: do not invent a kit or offer a project (**C-06**).

**Compare:** Holds ledger-truth awareness (CF-076). Full parent/child as an organ is parked (garden F1 / sitting deferred). Cue-title match can **drift** if a usual-kit string exists as a row that is not really this parent’s child (same wording, different parent is allowed by CF-079 — `smaller_open_for` usual-kit path does not require a project link).

---

## 4. How something becomes a project

**Law:** **O-07** · **C-06** · **C-04**

A project is **not** a new list. It is a **heading on this ledger**.

| Step | Mechanic |
|------|----------|
| Bare **PROJECT TITLE** | Asks: “What project name should this ledger have?” |
| After smaller jobs land and they keep talking | `maybe_offer_group`: those jobs can sit under one project name — type a short name, **or keep talking**. Not required |
| They type a short heading | `set_project_title` stores `project_title`. Ledger title is unchanged. Stay-one on the focused row lifts (`STAY_ONE_TRANSFER`) |
| Optional link | `project_task_ids` / `PROJECT TASKS` / `add_project_task` |
| **PROJECT SHOW** | Speaks the heading and linked job titles |
| **PROJECT CLEAR** | Clears heading **and** linked ids. Ledger title stays |
| Talk that rejects an existing heading | Walk **Change the project name** vs **Clear the project name** (CF-086). Not a new task |

Help-me / okay / leftover is **keep talking**, not a name. Chat does not mint a project. Silent merge is Do not (**O-07**).

Garden **project suggest as a structural organ** (F2/F9) is not shipped. Today’s offer is the heading ask after related jobs exist — not an ontology of life-tasks.

**Compare:** Holds heading vs ledger title. Auto-group is offer-only. Designer garden “he may suggest; they determine path” stays discuss.

---

## 5. Listing (what they see)

**Law:** **C-05** · **O-06** · **C-08**

| Surface | What it lists | Live? |
|---------|---------------|-------|
| **LIST TASKS** | Active rows on this ledger (ids + titles). Optional archived views exist in code; people close-out uses LIST ARCHIVE | Numbered when opened as a menu |
| **Where are we?** | Same inventory as a **live menu**: look at, close out, or keep talking. Highlights focus. Does not stack last free chat or stay-with endings on that pulse | Yes |
| **What is in focus?** | Skips the full ledger; goes to that task’s stay-with | Stay-with doors |
| **LIST ARCHIVE** | Completed / dropped / forked. Pick completed or dropped to reopen | Yes |
| **LIST LEDGERS** | Ledgers with active mark and project heading | Glance |
| Stay-with offered examples | Suggestion set — titles on that pulse if he names the set (CF-077) | Yes **while chrome is printed**; talk shelves digits |
| RESOURCE ALIGNMENT | Matching **commands**, not extra tasks | Numbered organ offer |

Pulse-0 / CONTINUE / STATUS name the **last named ledger row** (ledger fallback when session text is interview prose) — not the model’s last paragraph.

---

## 6. Close-out: complete, drop, archive, reopen, fork

**Law:** **C-05** · **O-03**

**No silent close.** Talk (“close out the dentist”) asks complete vs drop, then **YES**. Numbered ledger rows and `complete 2` / `drop 2` are aliases for the same confirm. After YES: optional short note (SKIP continues) — a prompt, not a numbered list. That note is `lineage` `close_note=…`, not a reopen.

| Verb | Status | Snapshot sidecar | People |
|------|--------|------------------|--------|
| **COMPLETE** / archive_task | COMPLETED | Yes — append row to `daniel_archive_L{n}.md` | Leaves this ledger; LIST ARCHIVE can put it back |
| **DROP TASK** | DROPPED | No | Not going to do it; still in history |
| Old **CANCEL TASK** | Same as drop | No | People screens do not offer it |
| **LIST ARCHIVE** pick | ACTIVE again (`reopen_task`) | — | Opened again: {title} |
| **FORK** | Sources FORKED with lineage; copies ACTIVE on a new or named ledger | — | Copy+renumber. Forked rows are **not** reopened from LIST ARCHIVE |
| **FORK** of project links | All `project_task_ids` | — | New ledger |

Complete of the **parent** does not auto-complete children (**O-02** Do not). Garden F16 (ask before parent closes when all children complete) is **not built**.

Focus clears when that row leaves ACTIVE.

**Compare:** Holds yes-before-write. Complete and drop are different statuses. “Archive” in people speech is LIST ARCHIVE (the menu) **and** a silent sidecar file on complete — people do not need to know the sidecar. Calling ARCHIVE as a people command beside COMPLETE would mint a second dialect (**C-04** reuse).

---

## 7. Logged (spine, files, notes)

**Law:** **C-09**

| Log | Where | What |
|-----|-------|------|
| Spine | `data/spine/events.jsonl` | TASK add, FOCUS, PROJECT_TITLE, SET_STATUS, CLOSE_NOTE, FORK, STAY_ONE_TRANSFER, TASK_EDIT_LOG, … |
| Task edit trail | `outputs/task_edit_log.jsonl` | Status and description edits (pulse, ids, before/after) |
| Ledger file | `data/ledgers/daniel_ledger_*.md` | Live table; completed/dropped **rows retained** with new status |
| Complete sidecar | `data/ledgers/daniel_archive_L*.md` | Snapshot copy of the completed row |
| Session | `active_focus_task_id`, `last_roadmap_idea`, stay holds | Hot slice; SHOW BOUNDARY must see smaller_open, stay_one, working_on |
| Optional close note | Row `LINEAGE` | After YES; does not reopen |

The model does not invent ids or write rows. Chat brief may see related existing task and `smaller_open` so it does not invent a second bathroom row.

Chronicles / `data/archives/chronicles` are **chat sitting** archives, not LIST ARCHIVE. Do not conflate.

---

## 8. Roadmap (three different things)

**Law:** **O-06** · **C-05**

| Thing | People | Durable? |
|-------|--------|----------|
| **Saved chat roadmap idea** | Overlay they confirmed; session `last_roadmap_idea`. Boundary and pulse-0 may name it. **Not a task.** Not the ROADMAP command | Session / boundary until they write a row |
| **ROADMAP** command | Package-aware **Daniel product** map (`maintenance/roadmap.py`) — what is shipped in this app, Path A | Catalog / manifests. Not their bathroom plan |
| **Developer ledger ROADMAP** | DL1 notes (`APPEND DL1`) | A different ledger for builders |

A meaning-ask “what is roadmap?” may show **two** meanings if they just saved an idea (**C-05**). Bare `roadmap` just-checks the package command.

Stay-one forbids offering a roadmap until they transfer. Chat must not treat a painted outline as already on the ledger.

---

## 9. Cue packs, split, and items

**Law:** **O-04** · **C-04**

`cue_jobs_for(title)` is DET wording for **suggestion to write** (bathroom / garden / app packs). Silent prepare may warm those titles. People see them when they pick Name smaller tasks / split — not as fake outstanding children.

Split-ask (`looks_like_split_request`) opens naming, not a silent tree.

Items on a need-list stay **notes on the stay**, not tasks, until a yes. **Complete** still closes the **task**. A later check-off phrase for an item is **CF-097**, gated until Designer locks the words. Do not ship that durable note yet.

---

## 10. Beat map (named work)

```text
discuss (free chat) — color is not a task
    → they name work in their own words
        → related already on ledger? look-at vs add-anyway vs keep talking
        → meant yes → add_task → stay-with
    → or they look at a row (LIST TASKS / where-are-we / FOCUS)
        → smaller_open facts or stay-one offer
        → doors: name smaller / keep as one / he continues / they take the ball /
                  pause / task actions / Let's complete this task
            → Name smaller: offered list; Add all or type own; collision card
            → after children exist: optional project-name heading (or keep talking)
            → Let's complete: stay until YES complete; then LIST ARCHIVE can restore
            → DROP TASK: YES; dropped, not completed
```

Autonomy **Keep us moving** may bring the next matching **organ**; it still must not invent rows they did not name (**O-07**).

---

## 11. Garden (not law)

`TASKING_EVOLUTION.md` (private Planning file) designs three **paths** (locked / gated / open), clone-with-keep, compost, growth dial. Sitting forbids minting locked / gated / open as people words **now**. Do not treat F-rows as chunks. This map describes **what ships**: one ledger, heading as project, stay-one mark, yes-gated writes.

---

## 12. Compare (Hold / Drift / Fail)

| Lock | Chunk | Verdict |
|------|-------|---------|
| add_task is the writer; likes never write | C-12, O-07 | **Holds** |
| Chat color is not a task | C-02, C-04 | **Holds** |
| Thin speech never a title | O-05, C-06 | **Holds** |
| Outstanding smaller tasks are facts; no invented kit | O-02, C-06 | **Holds** awareness. Cue packs **drift** if spoken as if written |
| Collision: look-at / add-anyway / Don't add | C-06 | **Holds** |
| Stay one until they ask to grow | C-05, C-06 | **Holds** |
| Project is a heading; help-me is not a name | O-07, C-06 | **Holds** |
| Complete vs drop; YES; LIST ARCHIVE reopen | C-05, O-03 | **Holds** |
| Items ≠ tasks until a yes | C-04 | **Holds**. Durable item notes **gated** (CF-097) |
| Silent write forbidden | C-04, O-04 | **Holds** as lock |
| Parent/child organ | Garden F1 | **Not shipped** — inferred survey only |
| All-children-complete asks before parent close | Garden F16 | **Not built** |

---

## 13. Product homes

| Job | Owner |
|-----|--------|
| Write / status / list / stay-one / smaller_open | `domains/tasks/ledger.py` |
| Stay-with, elicit, add-all | `domains/tasks/stay_with.py` |
| Where-are-we, look-at after FOCUS | `domains/tasks/open_work.py` |
| Task actions, close confirm, LIST ARCHIVE | `domains/tasks/task_actions.py` |
| Related before-add | `domains/tasks/related.py` |
| Same-parent wording collision | `domains/tasks/duplicate.py` |
| Cue packs / split smell | `domains/tasks/cue_jobs.py` |
| Project heading | `domains/projects/project.py` |
| Fork | `domains/projects/fork.py` |
| ROADMAP command | `maintenance/roadmap.py` |
| Chat overlay capture | `packages/support` suggest + `stay_with` |

---

## 14. Where to open next

| Question | Open |
|----------|------|
| People words complete / drop / focus | **C-04**, **C-05** |
| Never mint from a shrug | **C-06**, **O-05** |
| Outstanding / in-hand / gather-prefer | **O-02** |
| Writes wait; project offer | **O-07** |
| Who owns writes | **N-03** |
| Garden later | `TASKING_EVOLUTION.md` (private Planning file; not law) |
| Item notes | `CF097_TASK_ITEM_NOTES.md` (private milestone; gated) |
| How he talks | [`HOW_DANIEL_TALKS.md`](HOW_DANIEL_TALKS.md) |
| How a line is classified | [`HOW_DANIEL_RESPONDS.md`](HOW_DANIEL_RESPONDS.md) |

This file is a map of **listing and tasking as shipped**. Changing parent/child into an organ, minting path names, or shipping item check-off is guide-update plus a CF row, not a silent edit here.
