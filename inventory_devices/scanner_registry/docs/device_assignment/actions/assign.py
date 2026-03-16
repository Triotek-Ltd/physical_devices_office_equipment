"""Action handler seed for device_assignment:assign."""

from __future__ import annotations


DOC_ID = "device_assignment"
ACTION_ID = "assign"
ACTION_RULE = {'allowed_in_states': ['draft', 'active', 'returned'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['scanner_device', 'scan_event_log', 'device_sync_event'], 'borrowed_fields': ['device identity from scanner_device'], 'inferred_roles': ['operations coordinator']}, 'actors': ['operations coordinator'], 'action_actors': {'create': ['operations coordinator'], 'assign': ['operations coordinator'], 'close': ['operations coordinator'], 'archive': ['operations coordinator']}}

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
