"""Action handler seed for terminal_session:assign."""

from __future__ import annotations


DOC_ID = "terminal_session"
ACTION_ID = "assign"
ACTION_RULE = {'allowed_in_states': ['opened', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['pos_device', 'receipt_print_event', 'device_payment_event'], 'borrowed_fields': ['terminal identity', 'site from pos_device'], 'inferred_roles': ['finance officer']}, 'actors': ['finance officer'], 'action_actors': {'assign': ['finance officer'], 'close': ['finance officer'], 'archive': ['finance officer']}}

def handle_assign(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
