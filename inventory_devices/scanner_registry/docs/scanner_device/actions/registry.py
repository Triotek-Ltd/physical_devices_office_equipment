"""Action registry seed for scanner_device."""

from __future__ import annotations


DOC_ID = "scanner_device"
ALLOWED_ACTIONS = ['create', 'provision', 'assign', 'retire', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'provisioned', 'active'], 'transitions_to': None}, 'provision': {'allowed_in_states': ['draft', 'provisioned', 'active'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['draft', 'provisioned', 'active'], 'transitions_to': None}, 'retire': {'allowed_in_states': ['draft', 'provisioned', 'active'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'provisioned', 'active'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
