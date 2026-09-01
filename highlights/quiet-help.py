# Portfolio highlight — AI gating & logic bridge
# Source: Daniel V2 / domains/tasks/stay_with.py  →  _apply_quiet_slots
# Sanitized excerpt. Not shipped product code.


def _apply_quiet_slots(hold: dict, text: str, slots: dict) -> str | None:
    """Quiet help may suggest a handle. Local still names the take."""

    # [EXTRACT]: Read the model's gated slots — never raw model prose.
    meaning = str(slots.get("meaning") or "")
    shape = str(slots.get("talk_shape") or "")
    thought = " ".join(str(slots.get("thought") or "").split()).strip()

    # [INTEGRITY]: Block AI from repeating or cloning history.
    if thought_clones_last_take(hold, thought):
        thought = ""
        slots = {**slots, "thought": ""}

    # [GUARDRAIL]: Prevent AI from overriding local deterministic rules.
    # A nod or a stuck line is not "ask-last." Local owns that family.
    if is_nod(text) and meaning == "ask-last":
        return None
    if is_nod(text) and shape == "reprint last take":
        return None
    if is_stuck(text) and meaning == "ask-last":
        return None
    if is_stuck(text) and shape == "reprint last take":
        return None
    if meaning == "nod" and shape == "sibling":
        return None

    # [GUARDRAIL]: A grounded answer to an open item-ask is local, not leftover.
    if item_ask_is_open(hold) and is_item_answer(text):
        return _answer_to_ask_keep_ball(hold, text)

    # [ROUTING]: Map AI intent to specific local logic gates.
    if meaning == "named-possession" or is_named_possession(text):
        return _named_possession_keep_ball(hold, text)

    if meaning == "defer-look":
        return _defer_look_keep_ball(hold, text)

    if meaning == "empty" or shape in {
        "empty sit-with",
        "deepen ground",
        "need-list",
    }:
        handle = str(slots.get("object") or "").strip() or thought
        return _amend_keep_ball(hold, text, handle=handle)

    if hold.get("last_take_kind") == "need_list":
        if meaning in {"nod", "list-offer-accept"} or is_nod(text):
            return _eval_keep_ball(hold, text)
        return _amend_keep_ball(hold, text)

    if meaning == "list-offer-accept" or shape == "start-list-beat":
        return _eval_keep_ball(hold, "okay")

    if shape in {"listed-lens", "list-door", "their-line", "default-offer"}:
        # [GUARDRAIL]: No thought, no paint. Lens only after stuck or a nod.
        if not thought:
            return None
        if shape == "listed-lens" and not (is_stuck(text) or is_nod(text)):
            return None
        return _quiet_thought_keep_ball(hold, text, slots)

    if thought and (meaning in {"nod", "stuck"} or shape in {"ground-stay", "work-talk"}):
        return _quiet_thought_keep_ball(hold, text, slots)

    if meaning in {"nod", "stuck"} or shape in {"ground-stay", "work-talk"}:
        return _eval_keep_ball(hold, text)

    if meaning == "ask-last" or shape == "reprint last take":
        return _ask_last_keep_ball(hold, text)

    if meaning == "leftover-not-a-title":
        return _eval_keep_ball(hold, "okay")

    if shape == "sibling":
        return _eval_keep_ball(hold, text)

    # [GUARDRAIL]: Unknown slot → floor. Local still moves. AI off still moves.
    return None
