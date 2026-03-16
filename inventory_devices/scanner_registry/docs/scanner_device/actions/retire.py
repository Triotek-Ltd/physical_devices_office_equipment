"""Action handler seed for scanner_device:retire."""

from __future__ import annotations


DOC_ID = "scanner_device"
ACTION_ID = "retire"
ACTION_RULE = {'allowed_in_states': ['draft', 'provisioned', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['scan_event_log', 'device_assignment', 'device_sync_event'], 'borrowed_fields': ['site/location context from warehouse or operations setup'], 'inferred_roles': ['operations coordinator']}, 'actors': ['operations coordinator'], 'action_actors': {'create': ['operations coordinator'], 'assign': ['operations coordinator'], 'retire': ['operations coordinator'], 'archive': ['operations coordinator']}}

def handle_retire(payload: dict, context: dict | None = None) -> dict:
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
