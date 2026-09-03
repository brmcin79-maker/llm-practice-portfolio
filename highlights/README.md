# Logic highlights

One proof of a gate in code. Curated excerpts of the core Python used to keep a **deterministic floor** and to **gate** optional AI. Full source stays in the private product repository.

**Status:** work in progress. This is not shipped product code.

**Contact:** [github.com/brmcin79-maker](https://github.com/brmcin79-maker) · brmcin79@gmail.com

| File | What it is |
|------|------------|
| [quiet-help.py](quiet-help.py) | Sanitized excerpt of `_apply_quiet_slots` (from `domains/tasks/stay_with.py`). Quiet help may suggest a handle; local still names the take. Not shipped product code. |
| [typed-line.svg](typed-line.svg) | How a typed line is handled — local floor, then optional gated model. Also on the [repository README](../README.md#daniel-v2-context). |

Read the excerpt as a **gate**, not as a synonym engine. Unknown model slots fall through to `None` — local still moves. Companion papers: [how he thinks with a model](../forensic/HOW_DANIEL_THINKS_WITH_MODEL.md) · [AI overview](../ai/README.md).
