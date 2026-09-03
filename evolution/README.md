# How the LLM practice evolved

**Kind:** Self-directed education with language models — what they can do, what they cannot, and what had to become code. Not law.

This folder is the education. Daniel is the program that compiled it. The model was not dropped. What was learned was used to **gate** it, make sittings deterministic, and work with models in an IDE without letting chat become the authority.

The public landing has the 30-second map: [What I learned about LLMs — and how it was applied](../README.md#what-i-learned-about-llms--and-how-it-was-applied). This page is the evidence behind that table.

**Status:** work in progress. This page will grow as more private files are sorted.

**Sources (private):**

- Daniel V1 — local folder `task logger agent`. Frozen. Not in development.
- Pre-V1 LLM scripting — private archive [`04-Pre-IDE-LLM-Scripting`](https://github.com/brmcin79-maker/AI-LLM-Archive) (second file set). Stays private.
- Early experiments — [brmcin79-maker/AI-LLM-Archive](https://github.com/brmcin79-maker/AI-LLM-Archive) (first file set, folders `01`–`03`). Stays private.

Private sources stay private. This page is the methods.

**Contact:** [github.com/brmcin79-maker](https://github.com/brmcin79-maker) · brmcin79@gmail.com

Parent: [repository README](../README.md) · [planning map](../planning/README.md) · [product](../product/README.md) · [AI overview](../ai/README.md)

---

## What this practice learned

An LLM is a **pattern engine**. That is valuable. It is not a system of record, a consent gate, or a searchable archive.

| Pattern-sense is good at | It cannot be trusted to |
|--------------------------|-------------------------|
| Hearing a line, restating a named take, filling one handle | Remember the last sitting. The window is blank when it ends. |
| Drafting, naming, and versioning documents at speed (LLM scripting) | Enforce a constitution, a command table, or a yes |
| Color and paraphrase over facts you granted this beat | Browse the house, write the ledger, or run the sitting |
| Fast loops in ChatGPT, then Gemini, then an IDE | Be the product. Chat is not an application |

**For a business or a developer**, that split is the education. Use the pattern engine. Do not let it be the floor. Local code classifies the line, numbered consent writes state, the pulse is a searchable address for enhanced activity, and each model call gets only the pack this beat granted.

A stored Gem, Studio kit, or scripted constitution **simulates** memory. It still shares the same context window as the live thread. Advertised length (Gemini’s ~2M-token claim included) is not uniform recall. That finding is written for a hiring scan as [Context is not memory](../README.md#context-is-not-memory).

The rest of this page is how that was learned: stateless chat, written constitutions that could not lock, extensive LLM scripting, turns then pulses, then V1/V2 as deterministic programs with the model still in the loop — gated.

---

## Line of work

```text
OpenAI ChatGPT  →  Gemini (~April 2025)  →  local program (V1, then V2)

Early private archive (ChatGPT: custom GPTs, canvases, seed packets)
        →  Pre-V1 phase program (Gemini: LLM scripting, versioned Docs)
        →  Daniel V1  ("task logger agent")  — frozen
        →  Daniel V2  (clean-room rebuild)   — current, unfinished
```

V2 is **not** a file-port of V1. Outcomes that still matter were mapped, then rebuilt.

### Hosts

Daniel began as **OpenAI ChatGPT** work: custom GPTs, canvases, pasted system instructions, and the early upload-and-boot / seed-packet kit (the operator manual still says “open a new ChatGPT chat”).

Around **April 2025** the sitting **moved to Gemini**. That is the pre-V1 phase: versioned Google Docs, SAM, INITIATE, sender/receiver — LLM scripting against Gemini, not a ChatGPT custom GPT. The date is approximate (canvas and seed-packet files in the early archive are still dated that April and still name ChatGPT).

Changing hosts is why migration papers exist. A ChatGPT thread cannot be memory; neither can a Gemini thread. The constitution had to travel as files.

The product later **left both chat hosts**. V1 and V2 are local programs. Gemini can still be one optional model path. It is not the product, and Daniel is not a replacement for Gemini or ChatGPT.

---

## Stateless experimentation

A hosted chat is a **blank machine**. When the window ends or the token budget is spent, the model has no memory of the last sitting. Two threads on the same work will diverge. That was the first research problem — before an IDE product, and before Python was the runtime.

The experiments were ways to **carry state around the model**, not ways to make the model remember.

| Experiment | What they actually did | What it proved |
|------------|------------------------|----------------|
| **Re-instruct every thread** | Paste a personality file, system instructions, or a “current rules” canvas at the start of a new chat. | Continuity lives with the operator. The model starts empty every time. |
| **Live paper index** | A numbered canvas (later, folder) list of what is in force. Drift between chats and the list was a named failure mode. | “What is live” cannot be left in chat memory. |
| **Upload-and-boot** | A first-boot checklist: attach a kernel file and a state JSON to a new chat, instantiate, open a panel. | You can reconstruct a sitting *inside* a sandbox. You still lose it when the sandbox dies. |
| **Seed packets** | Small JSON (id, timestamp, payload, SHA-256). New chat uploads the latest packet; a loader checks the hash before rebuild. Capture / generate / merge when two branches diverged. | Checksums can protect a file. They cannot make a language model hold memory. |
| **Document migration** | Later sender / receiver / overlay papers: pack the sitting, open a new window (or a new host), unpack. Do not trust the transcript. | The window is a transport problem. Files are the memory. Changing ChatGPT → Gemini made that unavoidable. |
| **Numbered beats (turns, then pulses)** | Count each LLM sitting as a numbered beat, stamp date/time, write a searchable report — not a chat scroll. | You can say “pulse 312.” You cannot usefully search a typical model thread. |

None of this made the model stateful. It made the **files** stateful and the **operator** the courier. That is why V2 treats the chat strip as a one-pulse pack, not as the house.

---

## Constitutions and mandates

The other half of the same problem: if the model has no state, you try to **re-anchor** it every sitting with written law. They did not write one constitution. They wrote **many kinds**, each locking one constraint. When the model drifted, they versioned the paper instead of trusting the thread.

Early papers (private archive) were prompt-shaped: role mandates, personality / system-instruction files, a current-rules canvas, a master document list, output harnesses (“take notes” = exact wording, no paraphrase). Design mandates in the core doctrine were already non-negotiable in writing: do not wipe the field; do not silently overwrite; simplicity over feature creep; the PM role proposes and waits.

The pre-V1 phase then **compiled law as document families**. Counts below are versioned files in that tree (live heads plus Archives). Bodies are not copied here.

| Kind | Constraint it tried to lock | How far they took it |
|------|-----------------------------|----------------------|
| **Custom GPT / system-instruction files** | Who the model is this sitting; tone; what it may not do | ChatGPT-era personality files and a current-rules canvas; Gemini-era work re-anchored the same job in Docs and pasted protocols |
| **Project rules & structure** | Session rules; what is forbidden this phase | Numbered rule lists. Some sections were character-capped so they would still fit a prompt |
| **Lead PM + Scan / Train** | Propose, do not mutate. Wait for an explicit yes. Verify after a change. | Global protocols meant to work in every chat. Ancestor of numbered consent |
| **Canvas / document registry** | Which papers are live; sync across windows | Master list as the index. PM Scan’s job included catching desync |
| **Agent identity** | Who the agent is, separate from the last chat’s improvisation | **~60** identity papers (Phase 2–3), through `IDENTITY` v6 |
| **Definition lock** | Words do not drift in paraphrase | **~48** definition papers through the v5 line |
| **Terminology registry** | Same glossary every sitting | **~44** term papers, later a master term registry |
| **System Authority Matrix (SAM)** | Which paper wins. Who may authorize what. What a role may change. | **~100** SAM papers through **v10** |
| **System axioms** | Standing locks that survive a rewrite of other papers | Versioned axiom stack (through v3 in the core kit) |
| **Command structure / registry** | Only listed commands exist | **~80** command papers; later a master command registry |
| **Porosity + verification** | Where instruction leaks; what counts as a check | **~33** porosity / verification papers; later the audit suite |
| **Project rationale** | Why a rule exists — so the model does not invent a new why | Versioned rationale stack |
| **INITIATE (boot)** | Load order = which constitution is in force this sitting | **~38** boot papers: kernel, then orchestrator |
| **Output harnesses** | Exact line, no paraphrase, silent until released | Early “take notes” and similar command specs |

The volume is the demonstration. Identity alone ran through two dozen minor versions in one archive folder. SAM crossed a hundred files. That is not one prompt they liked. It is a long attempt to **compile constraints in documents** because the model would not hold them.

**Why written law still failed as a lock**

- A constitution in a Doc or a custom-GPT instruction is a **suggestion**. The model can paraphrase it, skip a gate, or load yesterday’s version.
- Two threads can each be “on” a different identity or SAM. There is no compiler to reject the stale one.
- Token limits mean you cannot paste the whole kit. INITIATE existed because they had to **choose a load order**.
- “Wait for approval” in Lead PM or SAM is an instruction. It is not a yes-gate.

What survived, as **jobs**:

| Then (paper) | Now |
|--------------|-----|
| Many constitutions, one job each | Planning `governance/` chunks + INDEX (open only what the question needs) |
| SAM — which paper wins | Walker roles; chunk wins over chat; no fourth constitution from memory |
| Lead PM / Scan — propose, wait, verify | Numbered consent; CF Return receipt |
| INITIATE load order | Planning `BOOT.md` as dispatcher |
| Definition / terminology / command registries | Defined words; catalog bound to the real command table |
| Porosity + verification | Forensic hold / drift / fail; MAINTENANCE |
| Seed packet / sender-receiver | Spine, snapshot, hot-slice pack — the window is not memory |
| No silent overwrite | Git; old chunks go to Planning `ARCHIVE/` |

V2 still has written law. The difference is **enforcement**: local classifies the line, the command table is code, and a model pulse gets only the strip this beat granted. The constitution is not re-pasted into a blank chat and hoped for.

---

## Pre-V1 phase program

The last work before Daniel lived in an IDE. Five numbered phases on Drive — this is the **Gemini** era (from around April 2025). The subject of that cycle stays in the private folder. This page is the **method**.

### LLM scripting — create, name, version; no compiler

This phase was **extensive LLM scripting**, not software development. There was no Python, no IDE, no repo. The model was the runtime.

A “script” was a named protocol in a Google Doc (or a canvas). The sitting used it to:

- **Create** a new document when a job needed its own paper (a new registry, a new audit module, a new sender)
- **Name** that paper with a stable family (`SAM`, `INITIATE`, `MIGRATION_SENDER`, `DEFINITION`, …)
- **Version** it (`_V3.2`, `_V10.0`) and leave the previous file in `Archives` instead of overwriting

The operator wrote and refined the script. The LLM executed it: draft the next artifact, apply the naming scheme, bump the version, run an audit overlay, emit a migration packet. Hundreds of dated copies in the tree are the residue of that loop — SAM through v10, INITIATE through two dozen boot revisions, work-task log into the v5 line, migration sender/receiver and overlays through v6.1, plus parallel stacks for terminology, definition, formula registry, command registry, SAP/MAR/FI audit modules.

That is the demonstration: a full system of authority, glossary, formulas, commands, boot, audit, thread-migration, and **numbered LLM-turn tracking** was grown **by scripting a language model**, before any of it was compiled.

Bodies of those Docs are not copied here. The map below is from the folder inventory, version stamps, and analysis titles. A curated copy now lives in the private archive as `04-Pre-IDE-LLM-Scripting`.

### Turns, then pulses — searchable LLM activity

A typical model chat is a scroll. It is weakly searchable. You cannot point a collaborator at “the model call on that date, that number.”

Before any IDE, they scripted a **numbered beat** so each sitting — especially each LLM / AI-enhanced turn — left a file you could find by **date, time, and number**.

The unit started as **turns**. It was renamed to **pulses** while the work was still LLM scripting (Gemini-era Docs), before V1 lived in an IDE. The surviving script family is a stack of historical reports ranged by pulse number (Phase 5: `SYSTEM_HISTORICAL_REPORT` covering **pulse 270 through 414**). That is not a chat export. It is a versioned paper that treats the model’s activity as an index.

What the pulse was for, then and now:

| Job | Then (script) | Now (local program) |
|-----|---------------|---------------------|
| Clock | Each LLM turn bumps a number the operator can cite | Each typed line is pulse N on the banner (AI off still counts) |
| Find it later | Date + time + pulse # in a report, not a scroll | `SEARCH PULSE`, `SEARCH CHAT`, date filters on the spine |
| Track AI spend | Which beats used the model vs local paper-work | Spine kinds such as `AI_ENGAGED`; optional model pack is *this* pulse only |
| Carry across hosts | Reports and logs travel as Docs when ChatGPT → Gemini | V1 pulse journals on disk; V2 `MIGRATE PULSE PACKS` into the spine |

The pulse is how **enhanced activity** is tracked without trusting the host’s chat history. Gemini and ChatGPT keep a thread. They do not give you a stable address. A pulse number does.

V1 compiled that instinct into pulse journals. V2 stamps every important turn on the spine so the same cite still works after the window is gone.

### Phase progression

| Phase | What the tree is doing |
|-------|-------------------------|
| **1** | Canvas as the index. Dual roles (analysis vs structure). PM Scan: diagnose, propose, wait for a yes, scan again. Dated logs and a written close-out. Still prompt-shaped. |
| **2** | System definition and verification split out as their own versioned papers. “Who is the agent” and “what counts as a check” stop living only in chat memory. |
| **3** | The kit becomes a **document family** with lettered/versioned files and a dedicated `Audit` folder. Live heads include **SAM** (System Authority Matrix) through **v10**, terminology, definition, command structure, and related keys. Archives keep long version runs (definition through the v4–v5 line; terminology through the v2 line; SAM through v9 before v10). |
| **4** | **Pillars, registries, audit suite, migration.** INITIATE (boot) is revised many times (v1.4 through v1.25 in archives). Courier guide in parallel. Command registry and **formula registry** appear. Audit becomes a suite: modular audit protocols (SAP modules 1–3), mathematical anchors (MAR), and an integrity/forensic schema (FI). Migration packets start. |
| **5** | **Core kit + dissection + transport.** Analysis reports sit beside live protocols. INITIATE moves from kernel to **orchestrator** (v2.x–v4.x). Command, term, formula, and rationale registries keep bumping. Work-task log runs into the v5 line. **Historical reports numbered by pulse** (270–414). Migration sender/receiver and overlays climb through **v6 / v6.1**. Audit overlay and SAP/MAR/FI get another version line. Studio migration roadmaps appear — the last step toward leaving the chat window. |

Then the first IDE product: Daniel V1 (`task logger agent`). V2 is a later clean-room rebuild.

### Scripting types that were in play

These were **LLM script families** — each one a repeatable prompt/protocol for making or revising a class of document — before those jobs became Python.

| Family | Job | How it shows up in the tree |
|--------|-----|------------------------------|
| **System Authority Matrix (SAM)** | Who may authorize what. Which paper wins. What a role is allowed to change. | Phase 3 live `SAM_V10.0`; archives from early ISP-matrix versions through `SAM_V9.0`. |
| **Terminology / definition** | A glossary and a definition lock, versioned separately so words do not drift in chat. | `TERMINOLOGY_*`, `DEFINITION_*` through multiple minor versions; later **master term registry**. |
| **Formula registry** | A database of named methods: same job → same named formula, not a new paragraph each time. | Phase 4 `FORMULA_REGISTRY_V1.0` → Phase 5 `MASTER_FORMULA_REGISTRY` into the v3 line. |
| **Command registry** | The list of real commands — ancestor of a catalog bound to code. | Phase 3 `COMMAND_*` → Phase 4/5 `COMMAND_REGISTRY` / `MASTER_COMMAND_REGISTRY` into the v4 line. |
| **INITIATE (boot)** | How a sitting starts: kernel, then orchestrator. Which files load, in what order. | Phase 4 INITIATE v1.x; Phase 5 `INITIATE_V2.1-KERNEL` then `INITIATE_V2.x–V3.x-ORCHESTRATOR` and v4.x. |
| **Audit scripts** | Integrity after a change: modular protocols, mathematical anchors, forensic schema, then an operational overlay. | Phase 3 `Audit\`; Phase 4 SAP / MAR / FI version stacks; Phase 5 `FORENSIC_AUDIT_PROTOCOL`, `AUDIT_OPERATIONAL_OVERLAY`, SAP/MAR/FI v2–v3.2. |
| **Migration scripts** | Move context from one thread (or tool) to another without trusting chat memory: **sender**, **receiver**, **overlay**. | Phase 5 `MIGRATION_SENDER` / `RECEIVER` v2.0 → v6.0/v6.1 plus overlays v1.0 → v6.1. Studio migration roadmaps in parallel. |
| **Work-task log** | Durable work list next to the registries. | `WORK_TASK_LOG` through the v5 line. |
| **Turn / pulse tracking** | Number each LLM sitting so enhanced activity is searchable by date, time, and beat — not by scrolling a host thread. Started as **turns**; renamed to **pulses** before the IDE. | Phase 5 `SYSTEM_HISTORICAL_REPORT` ranged by pulse (**270–414**). Ancestor of V1 pulse journals and V2 `SEARCH PULSE`. |
| **Axioms / rationale / courier** | Standing locks, why a rule exists, how a packet is carried. | `SYSTEM_AXIOMS`, `MASTER_PROJECT_RATIONALE`, `COURIER_GUIDE` — each with its own version stack. |
| **Logic / operational engines** | Named instruments beside the registries (not yet compiled Python). | `LOGIC_INSTRUMENT`, `OPERATIONAL_ENGINE`, plus a versioned timing/cycle engine in the core kit. |

Version numbers were the point of the scripting. A new SAM or sender did not silently overwrite the last one. Old files stayed in `Archives`. The same instinct later became git + living chunk ids. Here it was enforced only by the script and the operator.

### From LLM scripting to deterministic code

LLM scripting could create and version the constitution. It could not **enforce** it. A Google Doc or a chat thread cannot hold a checksum, a command table, or a yes-gate. “Wait for approval” in SAM is an instruction to a model. It is not a lock.

What survived the move, as **jobs**, not as those files:

| Document-script job | Later environment |
|---------------------|-------------------|
| SAM — who may change what | Walker roles; chunk locks; authority table (chunk wins over chat) |
| Terminology / definition registries | Defined words; catalog meanings; people words vs internals |
| Formula registry | Same job → same method; pathing rungs; parked calc/recipe idea |
| Command registry | Product command table; living catalog — Atlas / HELP / README AUTO are views of that table (`REFRESH DOCS`), not model-authored docs |
| INITIATE boot | Product boot + Planning `BOOT.md` as dispatcher |
| Audit suite | MAINTENANCE / architecture fitness; CF Return receipt; forensic hold/drift/fail |
| Migration sender / receiver | Seed packets in the early archive; later spine, snapshot, hot-slice pack (the window is not memory) |
| Work-task log | Ledger + tasks |
| Turn / pulse reports | Spine event per pulse; `SEARCH PULSE` / `SEARCH CHAT`; V1 journals via `MIGRATE PULSE PACKS` |
| Version + archive, no silent overwrite | Git history; old chunks go to Planning `ARCHIVE/` |

V1 compiled the *outcomes* into a local program (and grew large). V2 rebuilt the same jobs as deterministic Python plus small law chunks: local classifies the line, numbered consent writes the ledger, the model is optional.

**What carried (short)**

| Then | Now |
|------|-----|
| Numbered phases with a close-out | Continuous Fidelity / one paper at a time |
| Canvas list as the live index | `BOOT.md` + `governance/` INDEX files |
| SAM + split roles | Three walkers; chunk wins |
| Diagnose, propose, wait for yes | Numbered consent |
| Versioned registries | Command table + catalog |
| Sender / receiver / overlay | Spine, snapshot, strip for one pulse |
| Turns → pulses (scripted beat index) | Banner pulse #; spine; search by pulse / date / chat |

---

## Daniel V1 — Task Logger

The first full local product. The working folder kept the name **task logger agent**. That is Daniel V1. New feature work on it has stopped.

It was a local program for keeping work: ledgers and tasks, a pulse/session count, commands and hubs, Atlas / HELP / README, and an optional model path next to deterministic logic. It grew large. Catalog text and the real command table could drift (a “0 parser commands” failure V2 was designed not to repeat).

**What V2 kept as method, not as files**

| V1 | V2 |
|----|----|
| Local program first; model optional | AI-off floor; nested consent |
| Ledger, tasks, focus, archive (no silent true-delete) | Same outcomes on a thinner seam |
| Pulse journals (searchable beat log) | Spine + `SEARCH PULSE` / `SEARCH CHAT`; migrate V1 packs, do not delete sources |
| Living docs (Atlas, HELP, README) | One catalog bound to the real command table |
| DET vs AI routing | Local classifies and speaks; model is a gated layer |
| Behavior reference for forensic maps | Planning maps IS vs INTENT; then clean-room code |

V1 stays a **behavior reference** when a V2 paper needs “how did the old one do this.” It is not a second product track and not this public repo.

---

## Early archive — first file set

Early Daniel work happened in **ChatGPT** (canvases, custom GPTs), then in **Gemini** (around April 2025), then in small local Python tools, then in V1 and the current Planning + product pair.

This section keeps **methodologies that still correlate** with how Daniel is built now. It does not republish the archive.

If this file and a private Planning chunk disagree, the **chunk** wins.

---

## What the first set is

Three folders. Names below are the private archive names.

| Private folder | Epoch | Problem they were actually solving |
|----------------|-------|-------------------------------------|
| `01-Semantic-Logic-and-Prompts` | Prompt-as-architecture | Chat windows drift. Sessions die. The model paraphrases when you needed the exact line. Roles and consent had to be written as instructions before there was a program. |
| `02-Deterministic-Mapping-and-Rules` | Rules before code | Natural-language-only steering failed on multi-step work. They wrote If/Then gates, scan/train/lead roles, method ladders, and operator checklists. |
| `03-Functional-Scripting-and-Evolution` | Local packets | A ChatGPT thread cannot be memory. They built small JSON “spores,” a checksum on load, capture / generate / merge tools, and a local Python kernel so state could leave the chat. |

That third folder is the technical hinge: **continuity cannot live in the model window.**

---

## What carried (and where it lives now)

### Mycelium — many small nodes, not one dump

**Then:** Memory was modeled as a network of small packets (“spores”) instead of one growing transcript. Grow by adding a node. Do not bolt on a heavy static archive. Do not wipe state to start over. Simplicity over feature creep.

**Now:** The same job is the **spine** (one event per important turn), the **ledger**, and the **hot slice** packed for a model pulse — not the whole house. Planning still uses garden / mycelium language as *why* in a discuss-only paper. People using Daniel do not hear it. Burning the spine or ledger to start over is an explicit Out.

### Seeding — a portable, checkable packet

**Then:** A seed packet was a small JSON file (id, timestamp, payload, SHA-256 checksum). A new chat uploaded the latest packet and a loader verified the hash before reconstructing state. Capture wrote a snapshot. Merge joined two branch packets by union, then signed the result.

**Now:** The model still does not hold memory. Local writes the spine and the files. Each optional model pulse gets only the strip local built for that turn. Snapshot / ingest / SEARCH are the current doors. The archive’s “upload the kernel into ChatGPT” workflow is retired; the product is a local program.

### Agent roles — propose, do not mutate

**Then:** Lead PM / PM Scan / PM Train were named roles. The model was not allowed to assume an action. It surfaced a proposal. Sensitive commands needed explicit consent. One role oversaw integrity; another executed.

**Now:** That split is the **three walkers** (planner, coder, Studio). Studio brainstorms and never pushes. The planner writes the paper. The coder implements one paper. Numbered picks and YES still gate writes. Sitting policy cannot turn AI or live web on.

### Other direct correlations

| Archive move | Current environment |
|--------------|---------------------|
| Verbatim “take notes” — no paraphrase, exact wording | Ingest stores; people words; local does not silently rewrite their line into a new task |
| Method ladders — do not skip a validation step | Pathing: one next method on the named task when they stall |
| Operator manual + first-boot checklist | BOOT / walker roles / sitting script: which file to open, what this sitting is |
| Checksum before trust a packet | Local wins after a model reply (strip invented kit, fake ids, ungranted quotes) |
| Chat session as a dead end | AI-off floor; files and spine are memory; the window is not |

---

## Honest limits

- V1 is frozen. It is not a shipped consumer app and it is not this sitting’s product.
- The pre-V1 phase folder is not in the private archive yet. Scripting, constitution, and mandate detail on this page is from folder inventory, version stamps, and analysis titles — not a dump of the Google Docs. File counts (SAM ~100, identity ~60, command ~80, and the rest) are the evidence of how far written constraints were taken before code.
- The archive first set is only the files already sorted. More may be added later.
- Archive folder READMEs in the private repo can overclaim (“fully realized,” “autonomous”). This page does not repeat that.
- Mycelium / garden names are history and discuss-only. They are not a shipped organ.
- Quiet help and stay-talk are still being earned. A method that *carried* is not the same as a method that *finished*.
