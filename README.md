# LLM Practice Portfolio

What I learned about large language models, how I applied it in development, and the work that backs it. Chat is not the authority. The application repositories stay private.

Daniel V2 is a private local program used to apply that education. This repository is the methods and outcomes. The application and planning trees are not published here.

**Contact:** Brooke · [github.com/brmcin79-maker](https://github.com/brmcin79-maker) · brmcin79@gmail.com

**Snapshot:** 2026-09-01 · work in progress

**License:** [MIT](LICENSE)

---

## What this work demonstrates

| Skill | How it was earned |
|-------|-------------------|
| **LLM literacy** | Hosted chat (OpenAI ChatGPT, then Gemini from about April 2025), then IDE work. Extensive **LLM scripting** before any compiler: create, name, and version document families (authority matrices, boot protocols, migration packets, numbered-turn reports). |
| **What models are** | Pattern engines. Strong at draft, paraphrase, and a hinted classification. Blank when the window ends. They do not remember, enforce consent, or hold a command table. |
| **What must be code** | Consent gates, command tables, searchable activity logs, living docs bound to the real table, local classification of a typed line. |
| **How models are used in development** | Separate jobs so one model does not plan, implement, and grade the same change. Written constraints in small chunks. One scoped paper at a time. Brainstorm (AI Studio) is not the same job as implement (Cursor). Environments also include Visual Studio and VS Code with GitHub Copilot. |
| **How work is evaluated** | Hands-on review against written criteria. Gaps stay named. A slice is complete when tests and a receipt land — not when a model says it is done. |

The education path (hosts, constitutions, LLM scripting, turns → pulses, V1 → V2) is [evolution/](evolution/README.md). The table in the next section is the same story as **finding → design**.

---

## What I learned about LLMs — and how it was applied

An LLM is strong at **pattern-sense**. It is not a system of record, a consent gate, or a memory. That split is the education. Daniel V1 and V2 are where it was compiled — not as a product pitch, as the proof that the finding changed the design.

Evidence and file counts: [evolution/](evolution/README.md).

| Finding | How I learned it | What I built from it |
|---------|------------------|----------------------|
| **The window is blank when it ends.** Two threads on the same work diverge. | ChatGPT, then Gemini (~April 2025). Re-instruct every thread; seed packets with checksums; sender/receiver migration papers. None of that made the model remember. | Local files and a **spine** are memory. Each optional model pulse gets a **hot-slice pack** for that turn only — not the house. |
| **A constitution in a prompt is a suggestion.** The model can paraphrase it, skip a gate, or load yesterday’s version. | Pre-V1 **LLM scripting**: hundreds of versioned Docs — SAM (~100), identity (~60), command registry (~80), INITIATE boot, audit suites. No compiler to reject a stale paper. | Written law lives in a planning repo. **Enforcement is code**: command table, numbered consent, local line classification. Chat is not the lock. |
| **You can grow a whole system by scripting a model** — create, name, version — and still cannot enforce it. | Gemini-era document families (no Python yet). Version stamps instead of overwrite. | Living catalog: Atlas / HELP / README AUTO are views of the **real** command table (`REFRESH DOCS`). One scoped paper, tests, and a receipt — not “the model said it shipped.” |
| **A host thread is a scroll, not an address.** You cannot cite “the model call on that date, that number.” | Turns, then **pulses**, while still in Docs. Historical reports ranged **pulse 270–414**. | Each typed line is pulse N. Important turns write a spine event. `SEARCH PULSE` / `SEARCH CHAT`. V1 journals migrate in; sources stay. |
| **Propose, wait, verify — do not mutate.** | Lead PM / Scan / Train roles in chat. “Wait for a yes” was an instruction, not a gate. | **Three development jobs** (brainstorm ≠ plan ≠ implement). In the program: a digit, YES, or a real command writes; liking a suggestion does not. |
| **Catalog text can lie.** | V1 (Task Logger) could print living docs the parser did not have (“0 parser commands”). | V2 is a **clean-room rebuild** of the jobs that still mattered — not a file-port. One table, several views. |
| **A stored knowledge base is still tokens in the same window.** Scripts, Gems, and Studio files simulate memory; they do not give the model recall of every detail. | Gemini (~2M-token threads advertised) and Google AI Studio. Re-load constitutions to re-anchor. Upload ≠ a close read. | **Grant a named slice this pulse** (chunk / RAG instinct). Ingest stores locally. Longtext gates refuse a dump. Local review wins after the reply. See [Context is not memory](#context-is-not-memory). |
| **Pattern-sense is useful if it is gated.** | Hosted chat, then IDE work (Copilot, Cursor, AI Studio). Models were not abandoned. | Nested consent (connect path → quieter doors). Ingest **stores** without calling a model; talk later may **grant** a named slice. Local review wins after a reply. |

The same findings show up as **how I develop** (next section) and as **what the program enforces** ([Daniel V2](#daniel-v2-context)).

---

## Context is not memory

This is the LLM finding I want a hiring scan to see clearly. It is also why Daniel treats ingest, pulses, and the hot-slice pack as **code jobs**, not as a bigger prompt.

**What is true**

| Claim | Why it holds |
|-------|----------------|
| **Scripting can simulate memory.** | Re-instructing a thread, a Gemini **Gem**, or an AI Studio system instruction + files makes the sitting *look* continuous. The host is re-injecting text. The model is not holding a store. |
| **A live thread competes with that script.** | Attention is not uniform ([lost in the middle](https://arxiv.org/abs/2307.03172); [context rot](https://research.trychroma.com/context-rot)). Recent turns often outweigh a long constitution or an uploaded knowledge base. Instruction drift is normal as the window fills — even when the file is still “attached.” |
| **Advertised context ≠ usable recall.** | Gemini 1.5 Pro advertised up to **2 million tokens**. Needle-in-a-haystack tests can look strong while reasoning over the whole dump, or retrieving a buried constraint, degrades. The model will still speak as if it has the full kit. |
| **Upload is not a close read.** | Fitting a window is not reading. Files can be truncated, summarized, or attended only in part. Reloading a document re-anchors focus (it puts the lock back where attention is strong). It does not guarantee the next reply used every page. |
| **That is why RAG, chunking, and deterministic code.** | Retrieve and **grant the slice this turn**. Do not dump the house. The things that must not drift — consent, the command table, what was actually granted — belong in local code. RAG is still the model; local review still wins. |

**What I am not claiming**

- That a Gem or Studio “overrides” the model as a separate memory chip. Knowledge files and the chat share **one** context window. They compete.
- That hallucinations only start in long threads. They happen at any length. Long context makes **false recall** harder to notice.
- That RAG is a third kind of memory. It is controlled re-granting — the same instinct as a per-pulse pack.

**How this shows up in the work:** ingest stores without calling a model; talk may grant a named section with coverage honesty; N11 longtext warns or refuses a dump; the spine is searchable after the window dies. Detail: [evolution/](evolution/README.md) · [ai/](ai/README.md#ingest-and-dossiers) · [ingest on this page](#ingest-and-dossiers).

---

## How I collaborate with LLMs to develop

This practice does not depend on Daniel as a released application.

**Three jobs.** A model that brainstorms does not also write the code or choose the next slice.

| Job | Typical tool | Does | Does not |
|-----|--------------|------|----------|
| Brainstorm | Google AI Studio / Gemini | Explore options against a fixed brief | Change product code or become the spec |
| Plan | Cursor | Compare the running system to written constraints; write **one** implementation paper | Implement that paper |
| Implement | Cursor | Ship that paper, with tests and a receipt | Invent the next slice from chat memory |

**Tools.** Visual Studio and VS Code with GitHub Copilot; Cursor; Google AI Studio / Gemini. Copilot is everyday editor assistance. Cursor and Studio are the split-role loop on this practice (brainstorm ≠ implement).

**Written constraints, not prompt memory.** Law lives in a planning repository as short chunks. Product code lives in a second repository. Copies of constitutions are not vendored into the app — they drift. Session chat is not the source of truth.

**One paper at a time.** Each change is scoped, tested, and recorded. Open work stays visible. Detail of current research themes: [forensic/HOW_DANIEL_PULSES.md](forensic/HOW_DANIEL_PULSES.md).

**Nested gates when a model is in the loop.** Connecting a chat path is one consent. Quieter doors (assist before a local take, live web, paid models) are separate. Local code classifies the line. Each model call receives a small pack for that turn only. Local review wins after the reply. Detail: [ai/](ai/README.md).

**Searchable enhanced activity.** A typical host thread is a scroll. A **pulse** is an address (date, time, number). That began as scripted turn reports, then local journals, then a searchable event log. Model-enhanced turns can be found later.

Planning map: [planning/](planning/README.md).

---

## Daniel V2 (context)

A local-first terminal work companion: ledger, pulse log, stay-with talk, optional gated models. Intelligence means continuity with consent and a next method when work is blocked. Local code decides the beat and speaks it. The session still moves with AI off.

The program is in active development. The gaps below are the live research — named on purpose.

| Topic | Open |
|-------|------|
| What was coded: gates, catalog, living docs | [product/](product/README.md) |
| How a typed line is handled | Diagram below · [forensic/](forensic/README.md) |
| One gate in code | [highlights/](highlights/README.md) |

![How a typed line is handled](highlights/typed-line.svg)

Local code reads the line first. **Commands** and **digits** never call a model. **Talk** is a local take (stuck / empty / nod / leftover). Optional models sit behind nested doors: connect a path, then quiet help (one handle), then paint (restate a take already named). The pack is this pulse only. Local review wins. Important turns write a **spine** event — not every line.

```text
typed line → pulse N
   ├── COMMAND  → dispatch (model bypassed)
   ├── DIGIT    → numbered yes (model bypassed)
   └── TALK
         ├── local classifier → local take (AI off still moves)
         └── optional gated model (quiet help, paint, or free chat over a small pack)
   important turns write a spine event
```

### Ingest and dossiers

One concrete example of **gated pattern-sense**: bringing material in is **environment** (local files). Using it in chat is a separate **grant** on this pulse. The model is not engaged on the write.

| | **AI off** | **AI on** (chat connected) |
|---|------------|------------------------------|
| **Bring material in** | `INGEST TEXT`, `INGEST FILE`, `INGEST CLIPBOARD` → a numbered **dossier** on disk. Scenario Build and Atlas offer the same seam anytime. | Same path. Ingest never calls the model. |
| **Work the dossier** | `LIST DOSSIERS` · `OPEN DOSSIER` · `LOCK DOSSIER`. **STUDY** outline / quiz / critique runs locally (headings, key sentences — no model spend). Optional **OCR** → dossier when a local engine is installed. | When talk points at *the dossier* or *that file*, local places a **named slice** in this pulse’s pack (~1,600 chars) with coverage honesty (“opening slice only — do not claim you read the whole file”). The model does not browse the house. |
| **Long text** | A 10,000-word essay sits in the dossier whether or not a model is connected. Initial ingest may clip very long pastes; **LONGTEXT CHECK** sizes a file before any model sees it. | **N11 longtext gates** warn (~50k chars) or refuse (~200k) before an adapter runs. Section-by-section grant is local choreography — not one dump that simulates a close read. |
| **Safety** | API-key-shaped paste is blocked from dossier storage. Accidental ingest is never minted as a task. | Receipts (dossier slices, fetched pages) must be granted this pulse. Trained world-knowledge is free; pretending to have read what was not granted is not. |

Full feature map: [product/](product/README.md#document-ingest-and-dossiers). Consent and pack rules: [ai/](ai/README.md#ingest-and-dossiers).

---

## Open barriers

The deterministic floor is in place: local beat, consent, AI off still moves. What is still being earned is **how that floor behaves as a collaborator**. These are the same problems named in design sittings. They are not solved by handing the session to a model or by shipping a domain knowledgebase.

Full forensic compare: [How a pulse applies awareness](forensic/HOW_DANIEL_PULSES.md).

| Barrier | In place | Still open |
|---------|----------|------------|
| **Deterministic collaborative chat** | Stay on the named task; leftover English is not a silent write | Every answer should change the next sentence. Reprinting the same list, or climbing a step they already answered, is the hole |
| **Awareness through a blocked task** | Ledger and pulse log store what is in front; stuck / empty / nod are real doors; one method this pulse | Use that stored state to work *through* the block. The next card should apply what they just said — not ignore it or re-ask |
| **Intelligence: suggest and pivot** | Continuity with consent; one next method when blocked (local, not a bigger model) | Suggest a useful next move from facts already in front. Pivot when the current method is stuck — still this task, not a new job or a canned lecture |
| **House → this pulse** | Files and the spine remember more than this pulse speaks | Apply stored awareness in the spoken take without dumping the house |
| **Optional model assist** | Nested consent; local review after the reply | A handle that changes the take, or an honest miss — not a second mouth |

---

## Contents

| Folder | What it is |
|--------|------------|
| [evolution/](evolution/README.md) | Education behind the landing table: ChatGPT → Gemini; constitutions; LLM scripting; turns → pulses |
| [planning/](planning/README.md) | How models are run as collaborators |
| [product/](product/README.md) | What was compiled: gates, catalog, living docs, ingest, tests |
| [ai/](ai/README.md) | Nested consent; per-turn pack; AI-off floor |
| [forensic/](forensic/README.md) | How the running program compares to written constraints |
| [highlights/](highlights/README.md) | Sanitized gate excerpt. Full source stays private |

Private product, planning, and archive repositories remain private.

---

## Limits

- This is not a published consumer application.
- These notes can lag the private originals.
- [evolution/](evolution/README.md) will grow as more private files are sorted.

---

**Contact:** [github.com/brmcin79-maker](https://github.com/brmcin79-maker) · brmcin79@gmail.com
