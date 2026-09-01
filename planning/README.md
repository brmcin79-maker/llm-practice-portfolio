# Daniel V2 Planning — public map

This document describes the **Planning** workspace for Daniel V2: what it is for, how it is organized, how law is stored, and how language-model collaborators are split so chat is not the authority. It is a map of **how models are run during development**.

It lives in the public [LLM Practice Portfolio](https://github.com/brmcin79-maker/llm-practice-portfolio). The working Planning repository and the product repository are **private**. This file is a map of the system, not a substitute for the private files, and not the product itself.

The short product picture is in the [repository README](../README.md).

**Status:** work in progress. Architecture and written law are further along than everyday collaborative feel. This is not a finished application.

**Contact:** [github.com/brmcin79-maker](https://github.com/brmcin79-maker) · brmcin79@gmail.com

**License:** [MIT](../LICENSE)

---

## 1. Purpose

Daniel V2 is a **local-first work companion**. Today the sitting is a terminal program. It keeps a ledger of tasks and projects, counts conversation turns as pulses, and stays on the job in front until the person pauses, leaves, or confirms a write.

**Planning** is the design home for that product. It exists so that:

- Product behavior is decided in writing **before** code changes.
- Optional language models do not become the source of truth.
- Multiple AI tools (Cursor agents, Google AI Studio) can work on the same sitting without inventing a parallel constitution from chat memory.
- History can be archived without deleting the live lock.

Planning is **not** the Python application. The application lives in a sibling product repository. Constitutions are **not** copied into the product. Copies drift. Agents attach both homes, or they stop.

---

## 2. What Daniel is (and is not)

Readers who only see this overview should not have to guess the product.

**He is**

- A local program with a durable ledger, a pulse log (the spine), and a stay-with loop for talking through named work.
- Designed so intelligence means **continuity with consent** and **pathing when blocked**: files remember; writes need a yes the person meant; when they stall, the program puts one next method on the table that is still this task.
- Honest about modes: local logic on by default; optional model chat off until connected; optional live web off until consent.

**He is not**

- A chatbot wrapper around a single vendor model.
- An autonomous agent that plans, talks, and calls tools as the product.
- A therapy product.
- A finished consumer application.

The current design bet (north star **N-03**): **local decides the beat and speaks it.** Optional models may help the program hear a line. They do not run the sitting. AI off still moves. That is a design choice, not a claim of uniqueness in the market.

---

## 3. Two homes

| Home | Role | Typical GitHub project |
|------|------|------------------------|
| **Planning** | Law, sitting script, coding papers, Studio pastes, forensic maps | `Brooke-Daniel/Daniel-V2-Planning` |
| **Product** | Runnable Python (`python main.py`), tests, command table, spine | `Brooke-Daniel/daniel-v2` |
| **Archive** | Historical experiments and early methods. **Not law.** | `brmcin79-maker/AI-LLM-Archive` (private) |
| **V1 (Task Logger)** | First local product. Frozen. Behavior reference only. | Local folder `task logger agent` — not in development |

Those GitHub projects are the working remotes. They are not this public portfolio. The private archive is source material only. How the LLM practice evolved: [`../evolution/`](../evolution/README.md).

**Hard rules (how the homes stay separate)**

- Planning is not nested inside the product folder.
- Constitutions are not copied into product files. Copies drift.
- A chat thread is not law.
- Secrets (API keys) live in a local env file on the product machine. They are never committed.

If an agent is given **only** the product repo, it is instructed to open `CANON_POINTER.md` and **stop** until Planning is attached. Inventing law from README or from memory is forbidden.

---

## 4. How this folder is accessed

### 4.1 Humans (Designer)

The person who owns the sitting (called **Designer** in the docs) works in Cursor with both folders as workspace roots, or reviews papers and Try logs outside the IDE. They carry receipts between chats. They Try the product themselves. They decide Want / Do not want on law. They do not treat Studio chat as a merge.

### 4.2 Cursor agents (planner and coder)

Cursor reads this repo because it is on disk (desktop) or because the GitHub project is attached to a cloud job.

Always-on rules (`.cursor/rules/`) send each agent to `BOOT.md` first, then to **that** walker’s role file. Law is the chunk files under `governance/`, not chat memory. After a job the walker does an ordinary `git push`. Force-push and git-config edits are out of scope.

A cloud job that only *names* Planning in a prompt does not have the files. The Planning GitHub project has to be attached to the job.

**Read walk (every planner or coder turn)**

```text
BOOT.md
  → PLANNER_ROLE.md  or  CODER_ROLE.md
  → SITTING_SCRIPT_CURRENT.md
  → SITTING_INGEST.md          (receipts; not law)
  → matching governance/*/INDEX.md
  → only the listed chunk files
  → overwrite SITTING_INGEST.md
  → coder: the one CF paper named in the sitting
```

**Build walk (coder only):** update protocol + nervous-system coverage, plus organism/AI chunks if the paper cites them.

**Guide-update walk (planner only):** when law itself must move, before a coder starts. Chunks have a six-part shape (Job, When, Locks, Do not, Body, INDEX row). Old ids go to `ARCHIVE/` with a note. No silent deletes.

### 4.3 Google AI Studio

Studio does **not** pull GitHub. It sees a **frozen snapshot**: paste, upload, or re-import after Planning is pushed.

Studio is brainstorm only. It returns a receipt in chat. It does not write product code, does not push, and does not author the paper the coder executes. `AGENTS.md` and `GEMINI.md` are injected so Studio knows the three walkers.

### 4.4 What “access” is not

- Planning is not a public wiki that updates itself when product code changes.
- Chat history is never canon.
- The small Vite/React tree under `src/` is a local docs viewer for the Designer, not the product and not required to understand the folder.

---

## 5. Three walkers

Work is split on purpose so a model does not plan, code, and grade itself in one sitting.

| Walker | Job | Pushes | Must not |
|--------|-----|--------|----------|
| **Cursor planner** | Assess a Try against law. Write Studio requirements. After Studio returns, cut one coding paper. | Planning, twice per loop (requirements, then paper) | Write product Python |
| **Cursor coder** | Implement **one** Continuous Fidelity (CF) paper. Smoke if named. Fill the return receipt. Mark Complete. | Product always; Planning if the receipt lives there | Invent the next slice; wait for Try to mark Complete |
| **AI Studio** | Brainstorm against the planner’s paste | Never | Code, push, or become law |

**Loop (simplified)**

1. Coder ships a paper → Complete → push.
2. Designer Tries. A failed Try is a **new** CF row, not the shipped paper left Open.
3. Planner assesses and writes Studio requirements → push Planning.
4. Designer opens a new Studio sitting with that paste or an upload.
5. Studio returns a brainstorm receipt.
6. Planner compares to chunks (chunks win), writes the next coding paper → push Planning.
7. Designer opens a new coder chat on that paper.

Sitting policy may skip Studio for a leftover. The planner still does not write product.

---

## 6. What “law” means here

Law is a set of **chunk files** under `governance/`. Each family has an `INDEX.md` that lists when to open which chunk. Agents are told to open the INDEX first, then only the listed files.

Chat, sitting notes, Studio receipts, forensic maps, and archived papers are **not** law. If they disagree with a chunk, the **chunk** wins.

### 6.1 Authority (who wins)

| If they disagree | Winner |
|------------------|--------|
| Designer Want / Do not want vs a draft sentence | The matching **chunk** |
| Thin vs “fewer features” | `governance/parity/` |
| What to build *this sitting* | `SITTING_SCRIPT_CURRENT.md` (does not invent law) |
| Which file to open; live vs archive | `BOOT.md` |
| Next CF id; parked follow-ons | `MILESTONES/CONTINUOUS_FIDELITY.md` |
| Anything in `ARCHIVE/` | History. Chunks win. |
| `SITTING_INGEST.md` | Receipts only |
| This chat’s memory | Never |

### 6.2 Law families

| Family | What it governs | Examples |
|--------|-----------------|----------|
| **North star** (`governance/north-star/`) | Filters for every enhancement; living docs; who runs the sitting | Stronger / slimmer / adaptable; one catalog many views; local mouth (N-03) |
| **Organism** (`governance/organism/`) | Role in the sitting: focus, outstanding work, keep-the-ball, stay-with, autonomy | Companion not waiter; JUMP vs LENS as Designer words; quiet help needs a live path |
| **Communication** (`governance/communication/`) | People sentences, menus, HELP, Atlas, banner honesty, how to update copy | Warm, specific, continuous; every build emits a hold the boundary can see (C-09) |
| **AI** (`governance/ai/`) | Optional model as pattern-sense on **granted** facts | Local fetches and packs; model has no tool belt; reply is a candidate |
| **Substrate** (`governance/substrate/`) | Nervous-system **architecture** (ledger, stream, graph, outbox, reaching) | Coverage of the bus is communication C-09, not a second program |
| **Parity** (`governance/parity/`) | Thin means less bloat, not less Daniel; what Complete is allowed to mean | CF Complete is code + push, not Designer Try |
| **New organs** (`governance/new-organs/`) | Gate before adding a new ability | Extend a seam; do not patch the kernel “just this once” |

Chunks are short on purpose. Long constitutions were split so a walker opens only what the question needs.

### 6.3 How a chunk is shaped

When law moves, the planner follows a fixed shape: **Job**, **When**, **Locks**, **Do not**, **Body**, plus an INDEX row and an amend-log entry. That is the guide-update walk. It is how the folder stays a system instead of a pile of essays.

---

## 7. Folder map

This is the layout of the **private** Planning tree. Names are stable enough to learn; dates and “next paper” rows move.

```text
Daniel V2 Planning/
  BOOT.md                      Dispatcher. Start here.
  README.md                    Internal map for walkers (not this public file).
  AGENTS.md · GEMINI.md        Studio inject: three walkers.
  PLANNER_ROLE.md
  CODER_ROLE.md
  STUDIO_ROLE.md
  SITTING_SCRIPT_CURRENT.md    This sitting’s next piece.
  SITTING_INGEST.md            Last receipts. Overwritten each turn.
  MAP_CURRENT_SHIPPED.md       What the product does today + Try lines.
  governance/                  Law (chunks + INDEX files).
  MILESTONES/                  CF papers, hygiene notes, Continuous Fidelity log.
  STUDIO/                      Pastes (requirements) and receipts (keep/cut). Not law.
  FORENSIC/                    How-Daniel maps, deferred backlog. Not law.
  ARCHIVE/                     Folded papers and old sources.
  .cursor/rules/               Always-on agent routing.
  scripts/                     e.g. forensic pack builder for Studio.
  tools/                       Occasional canon split / archive helpers.
  src/                         Optional local markdown viewer (Vite). Not the product.
```

### 7.1 Root walker files

| File | Function |
|------|----------|
| `BOOT.md` | Start-here: walks, two GitHub homes, authority matrix, live table of contents |
| `PLANNER_ROLE.md` / `CODER_ROLE.md` / `STUDIO_ROLE.md` | Job descriptions. Prevents one chat from doing all three jobs |
| `SITTING_SCRIPT_CURRENT.md` | Which CF paper is live; what is parked |
| `SITTING_INGEST.md` | What the last walker opened and concluded |
| `WALKER_FILE_INVENTORY.md` | Alignment checklist for pointers and environments. Not law |
| `MAP_CURRENT_SHIPPED.md` | Operator map of shipped behavior, in people words |
| `TASKING_EVOLUTION.md` | Garden / relationship brainstorm. **Discuss only. Not law.** |
| `PROGRAM.md` | Stub that points at BOOT |

### 7.2 `governance/`

The constitution. Opened through INDEX files, not by globbing the whole tree. Subfolders: `north-star`, `organism`, `communication`, `ai`, `substrate`, `parity`, `new-organs`. `TRANSFER_LEDGERS.md` records keep / merge / supersede / archive of older text.

### 7.3 `MILESTONES/`

**Continuous Fidelity** is the live delivery program: Designer Tries the map; each wrong feel becomes one CF paper; the coder ships that hole; leftover folds forward as a new id.

A CF paper is the **only** coding handoff. It includes locks, as-built spots, tests to run, and a Return receipt. Complete means smoke + receipt + push. Designer Try is leftover hunt, not a Complete gate.

Hygiene files (for example after a Try) fold Studio keep/cut into chunks and name the next paper. They are planner work, not coder papers.

### 7.4 `STUDIO/`

| Kind | Who writes | What it is |
|------|------------|------------|
| `STUDIO_PASTE_*.md` | Planner | Requirements for a Studio sitting |
| `STUDIO_RECEIPT_*.md` | Planner | Keep/cut after Studio returns |

New papers go here, not at the Planning root. `STUDIO/INDEX.md` is the ledger of those files. Studio never writes these files itself.

A generated forensic pack (`STUDIO_PASTE_FORENSIC_PACK.md`) can be uploaded as sitting memory. It is not law. Rebuild: `python scripts/build_studio_forensic_pack.py`.

### 7.5 `FORENSIC/` (private) and `forensic/` (this folder)

In the private Planning tree, `FORENSIC/` holds maps of how Daniel responds, thinks (local and with a model), talks, and tasks. Written so a walker can see the machine without treating the map as a lock. A deferred-ID register and an ID crosswalk also live there. Evidence packs sit under `ARCHIVE/forensic/`.

**This public repository copies the five how-Daniel maps** into [`../forensic/`](../forensic/README.md), with private `governance/` links turned into chunk-id labels. Hold / drift / fail language is kept. The ID soup is not copied. Parked themes (live web, calc recipes, garden organ, item notes) are summarized in [`parked-work.md`](../forensic/parked-work.md).

| Paper | What it maps |
|-------|----------------|
| [How he hears and answers](../forensic/HOW_DANIEL_RESPONDS.md) | Typed-line classifier, stay-with consume order, Try 720–733 leftover |
| [How he thinks locally](../forensic/HOW_DANIEL_THINKS_LOCAL.md) | AI-off floor, spine, menu digits, gather-prefer |
| [How he thinks with a model](../forensic/HOW_DANIEL_THINKS_WITH_MODEL.md) | Quiet help, paint, sandwich, gates |
| [How he talks](../forensic/HOW_DANIEL_TALKS.md) | Dual register, people words, defined words |
| [How he tasks](../forensic/HOW_DANIEL_TASKS.md) | Ledger, writes, project heading, complete/drop, stay-one |
| [How a pulse applies awareness](../forensic/HOW_DANIEL_PULSES.md) | Clock; hold vs spine vs pack; barriers still being earned |

### 7.6 `ARCHIVE/`

History: old milestone papers, source constitutions, maps. `BOOT.md` says not to open Archive unless the dispatcher or a ledger row cites a path. Chunks still win.

---

## 8. How Planning relates to the running product

The product has its own layout (kernel, spine, surface, domains, packages, adapters). Planning does not duplicate that code. A public map of that home is [`../product/`](../product/README.md).

What Planning **does** specify for the product:

- Who may speak on which screen (menus stay local; optional chat is gated).
- That every important turn should emit a **hold** the rest of the program can see (spine + active boundary). That is the “nervous system” in builder words. People using Daniel never hear that phrase.
- Living documentation in the **product**: Atlas, HELP, and a bounded README AUTO block are supposed to project a catalog built from the real command table. That is product machinery (`REFRESH DOCS`), not this Planning folder auto-rewriting itself.
- Stay-with behavior is evolved as CF slices against `domains/tasks/stay_with.py` and related helpers — always from a named paper, not from a Studio essay.

---

## 9. GitHub practice

| Practice | Rule |
|----------|------|
| Remotes | Two projects, two histories. Ordinary push to `origin`. |
| Branch | Work lands on `main` after the walker’s job. |
| Force-push | Forbidden in this sitting. |
| `git config` | Agents must not change it. |
| Secrets | Never on GitHub. |
| Studio | Does not clone or push. A new Studio sitting is opened from a pushed snapshot. |
| Drive | A local copy is convenience, not a third canon. |

A complete cloud or desktop sitting has **both** GitHub projects available — Planning and product.

---

## 10. What this planning map is

This file is a map of:

- Why a planning repo exists beside a code repo
- How written law is kept small, indexed, and winning over chat
- How Cursor and Studio are constrained so they do not collapse into one unsupervised agent
- How delivery is sliced (Continuous Fidelity) instead of a single “build the product” prompt
- How the machine is described when law is compared to the running program ([forensic maps](../forensic/README.md))

It is not a feature list, not proof that stay-talk is finished, and not permission to treat Studio output as specification.

Private Planning opens at `BOOT.md`. The product repo alone opens at `CANON_POINTER.md` and expects Planning to be attached.

---

## 11. Honest limits

- The Planning tree is large. Many milestone files are **Complete** history; the live lock is `BOOT.md` + `governance/` + the sitting script.
- Internal `README.md` in the private repo can lag the sitting. `BOOT.md` is the dispatcher.
- Forensic maps and Studio receipts are working memory. They can be wrong relative to chunks; chunks win. The copies in this folder can also lag the private originals.
- The product still has open stay-talk work. A public overview that implied a finished partner would be inaccurate.

---

## 12. One paragraph

Daniel V2 Planning is the written operating system for building a local work companion: constitutions in small chunks, one coding paper at a time, and three named walkers so models brainstorm, plan, and implement in separate jobs. The code lives in a second private repository. This public document is a map of that planning system for readers who will not open the private files.

---

## 13. License

This overview (README, forensic copies, and this repository’s other files) is released under the [MIT License](../LICENSE).

**Contact:** [github.com/brmcin79-maker](https://github.com/brmcin79-maker) · brmcin79@gmail.com

---

*Overview of the Planning workspace for Daniel V2. Not law. Not the product repository.*
