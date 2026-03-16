"""Action handler seed for maintenance_case:repair."""

from __future__ import annotations


DOC_ID = "maintenance_case"
ACTION_ID = "repair"
ACTION_RULE = {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'resolved'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['device_record', 'device_job_log', 'supply_level_snapshot'], 'borrowed_fields': ['device', 'site context from device_record'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'assign': ['case owner'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_repair(payload: dict, context: dict | None = None) -> dict:
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
