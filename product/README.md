# The product — what was coded

**Kind:** Public map of the private product repository (`Brooke-Daniel/daniel-v2`). Not the application. Not a feature list you can run.

**Status:** work in progress. Architecture and written law are further along than everyday collaborative feel.

**Snapshot:** 2026-09-01 · product `79eeb97` · command table **309** · catalog areas **17**

**Contact:** [github.com/brmcin79-maker](https://github.com/brmcin79-maker) · brmcin79@gmail.com

Parent: [repository README](../README.md) · [planning map](../planning/README.md) · [evolution](../evolution/README.md) · [AI overview](../ai/README.md)

The Python stays private. This page is what stands out once planning became code: the gates, the laws that were compiled, and a few features that are easy to miss if you only read a command list.

---

## What stands out

Daniel is a **local program** that you sit with in a terminal. He is not a vendor chatbot with a CLI wrapped around it. The model is optional pattern-sense. The sitting still moves when AI is off.

Three things are unusual together — not as a market claim, as the mix that was actually built:

1. **Law is not vendored into the app.** Constitutions live in the planning repository. Product code lives in a second repository so copies do not drift. Chat is not law.
2. **One command table is the catalog.** HELP, Atlas, and a bounded README AUTO block are generated from `surface.commands.COMMAND_TABLE` (`REFRESH DOCS`). V1 could show living docs that did not match the parser. This sitting was designed not to repeat that.
3. **Planning arrives as a paper, then as a test.** A Continuous Fidelity (CF) paper is the only coding handoff. Complete means smoke + receipt + push. The tree has on the order of **seventy** `test_cf*_smoke.py` files. That is law checked as behavior, not as a prompt.

The [evolution](../evolution/README.md) page is how that mix was learned. This page is what compiled.

---

## What you sit with

| Piece | What it is in the product |
|-------|---------------------------|
| **Ledger** | Tasks and project headings on disk. Writes wait for a yes you meant (a digit, YES, or a typed command that exists). |
| **Pulse** | Each typed line is pulse N on the banner. Important turns write a **spine** event. You can search by pulse, date, or chat — not by scrolling a host thread. |
| **Stay-with** | Talk through named work. Local classifies the line (stuck, empty, nod, leftover). When you stall, he puts **one method** on the table that is still this task. |
| **Banner** | Honest modes: local logic on; AI chat off until connected; live web off until consent; quiet help off until its own door. |
| **Living docs** | One command table, several views: HELP (start-here), **Atlas** (map of what he can do, people words), **README AUTO** (bounded generated middle). `REFRESH DOCS` rebuilds them. Snapshot is *now*; Atlas/README are the encyclopedia — one write does not cascade both. |

Intelligence, as coded: **continuity with consent** (files remember; writes wait) and **pathing when blocked** (one next method). He is not a second mind and not a house model.

---

## How the private tree is shaped

Names only. Source stays in `Brooke-Daniel/daniel-v2`.

```text
Daniel V2/
  main.py                 Boot, classify, dispatch
  CANON_POINTER.md        Planning is a separate repository
  kernel/                 Banner, session state, paths
  surface/                Command table, router, handlers
  spine/                  Events, index, boundary, graph projection
  domains/                Tasks, AI gates, memory, docs, …
  packages/               Help, voice, boot, alignment
  adapters/               Optional model providers
  contracts/              Catalog built from the command table
  tests/                  CF and milestone smokes
  data/                   Local runtime (spine, session) — not shipped as product
```

`main.py` bumps the pulse, sets turn meta so every spine event shares this beat, then: command → pending wizard → stay-with / talk → optional free chat. The model is not the first reader of the line.

---

## Planning that became code

Written law is not copied into Python files. It is **enacted**: one CF paper names the hole; the coder changes one seam; a smoke locks the receipt.

| Planning lock | What you can point at in the product |
|---------------|--------------------------------------|
| **N-03** — local decides the beat and speaks | Classifier and stay-talk templates; AI off still moves |
| **C-03** — menus are never the model | Numbered lists and Atlas plains from local templates |
| **C-04 / C-05** — lists are for a yes | Digits dispatch; liking a suggestion is not a write |
| **C-08** — banner honesty | DET / AI / NET / quiet help on the wrap |
| **C-09 / S-01 / S-05** — every important turn emits a hold | `set_turn_meta` + `append_event` + `SHOW BOUNDARY` |
| **O-02 / O-04** — cognizance from local facts; one method when blocked | Stay-with rungs; gather-prefer; pathing |
| **O-07 / A-03** — quiet help nested, off by default | Separate switch; needs a live chat path; fail → local card |
| **A-02** — model has no tool belt | Local fetches; pack a strip; reply is a candidate |
| **Defined words (C-05 / C-12)** | `DEFINED WORD UPDATE`; catalog meanings, not chat slang |
| **Living catalog** | `REFRESH DOCS` from the command table |
| **CF-0xx paper** | Matching `tests/test_cf0xx_*_smoke.py` |

If this page and a private `governance/` chunk disagree, the **chunk** wins. Forensic maps ([how he hears](../forensic/HOW_DANIEL_RESPONDS.md), [thinks locally](../forensic/HOW_DANIEL_THINKS_LOCAL.md), [thinks with a model](../forensic/HOW_DANIEL_THINKS_WITH_MODEL.md)) compare the running program to those locks.

---

## The gates (law you can trip)

These are not prompt instructions. They are code paths.

| Gate | What it blocks |
|------|----------------|
| **Command table first** | Unknown English is not a silent write. Stay-with or leftover reprint, not a new task from a shrug. |
| **Numbered consent** | A digit is a yes to the printed list. After talk shelves the list, a bare `2` is stale until SHOW MENU. |
| **Nested AI doors** | Connect a chat path. Then quiet help (smaller). Then live web. Then paid models. HOW WE WORK (Ask me first / Stay with me / Keep us moving) cannot turn any of those on. |
| **CONSTRAINT MAP** | A local picture of which AI / NET / paid gates are actually open. Not a gateway. |
| **Hot-slice pack** | A model pulse gets identity + a few defined words + what is in front + this-turn strip. Not the house. |
| **Local wins after** | Strip fake ids, unlabeled web, quotes not in a granted strip, kits and rooms not in the named take. |
| **Sanitize** | Scrub secrets before share or before a string goes toward a model. |
| **No silent true-delete** | Complete / drop / archive retain. `DELETE SESSION FOREVER` still leaves a searchable tombstone. |
| **Ingest is environment** | Storing a file does not call the model. Talk later may grant a named section. |
| **Two-home halt** | Product without Planning is not a license to invent law from README. |

[ai/](../ai/README.md) is the longer consent story. This table is what the product *enforces*.

---

## Features that deserve a mention

Not a tour of all 309 commands. These are the ones that show the education compiled.

**Stay-with and pathing.** You can talk through a named job without the model. Stuck → one method. Empty possession → need-list, not invented kit. That floor is the product. Collaborative feel is still being earned ([pulse barriers](../forensic/HOW_DANIEL_PULSES.md); [leftover](../forensic/HOW_DANIEL_RESPONDS.md)).

**Pulses as an address.** `SEARCH PULSE`, `SEARCH CHAT`, date filters, session chronicles. V1 pulse journals can be migrated (`MIGRATE PULSE PACKS`) without deleting sources. Enhanced activity is findable after the window dies. That job started as LLM-scripted turn/pulse reports; it is now a spine.

**Atlas, README, living docs.** The command registry from LLM scripting became a **catalog bound to code**. HELP, Atlas, and a bounded README AUTO block are views of `COMMAND_TABLE`, not essays a model maintains. Atlas is Daniel’s map of what he can do — required `plain` sentences, internals scrubbed. Browser Atlas is a reading map; commands listed there do not run. The model must not author Atlas or README. V1 could print living docs that the parser did not have (“0 parser commands”). `REFRESH DOCS` is how this sitting refuses that drift. Snapshot is a point-in-time pack; it does not silently rebuild the encyclopedia.

**People words vs internals.** Dual register is coded: menus and stay-talk in people sentences; JUMP / LENS / chunk ids stay off the screen. Defined words exist so “ledger” and “task” do not drift into chat synonyms.

**Honesty commands.** `CONSTRAINT MAP`, `SHOW BOUNDARY`, `CONTEXT CHECK`, `STATUS` / `STATUS DETAILS`, `HOW WE WORK`. The banner is supposed to match what is on. If it says AI is on, chat must work.

**Optional model, many paths.** Hybrid usual order is Groq → OpenRouter → Gemini → Ollama. Paid OpenAI / Anthropic stay behind `ALLOW PAID AI`. Failover is for a path you already connected. It is not the floor.

**Share without handing the house to a model.** Snapshot, share packs, present kits, sanitize-first. Export is local.

**Scenario Build.** A guided walk from a dumped situation to a plan and optional ledger rows. Local. Not “the model invented your project.”

**Maintenance as a product surface.** HEALTH, audit, ROADMAP (what this app shipped — not their bathroom plan), debloat *advise* that does not apply itself.

---

## Honest limits

- This is not documentation of a completed consumer app. Stay-talk and quiet help are wanted and not yet a reliable earn every Try. What is still being solved — collaboration, beat logic, spine awareness applied to this pulse — is named on the [root README](../README.md) and in [HOW_DANIEL_PULSES.md](../forensic/HOW_DANIEL_PULSES.md).
- Paint can still leak kit the local take did not name. Those holes are named on the forensic maps, not hidden.
- A public page that listed every command would pretend the catalog is the product. The catalog is the **index**. The product is the floor plus the gates.
- Constitutions are not in this folder. Do not treat this overview as law.

---

**Contact:** [github.com/brmcin79-maker](https://github.com/brmcin79-maker) · brmcin79@gmail.com
