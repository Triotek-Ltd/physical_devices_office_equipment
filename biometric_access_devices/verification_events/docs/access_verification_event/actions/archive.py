"""Action handler seed for access_verification_event:archive."""

from __future__ import annotations


DOC_ID = "access_verification_event"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['received', 'normalized', 'linked'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['access_device', 'access_exception_case', 'biometric_check_case'], 'borrowed_fields': ['device/site context from access_device'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'record': ['case owner'], 'archive': ['case owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
