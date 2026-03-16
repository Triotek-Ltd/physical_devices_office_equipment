"""Action handler seed for device_payment_event:link."""

from __future__ import annotations


DOC_ID = "device_payment_event"
ACTION_ID = "link"
ACTION_RULE = {'allowed_in_states': ['received', 'normalized', 'linked'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['pos_device', 'terminal_session', 'card_authorization_record', 'payment_intent_record'], 'borrowed_fields': ['device/site context from pos_device'], 'inferred_roles': ['approver', 'finance officer']}, 'actors': ['approver', 'finance officer'], 'action_actors': {'record': ['approver'], 'archive': ['approver']}}

def handle_link(payload: dict, context: dict | None = None) -> dict:
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
