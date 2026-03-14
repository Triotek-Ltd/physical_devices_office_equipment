"""Doc runtime hooks for maintenance_case."""

class DocRuntime:
    doc_key = "maintenance_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'repair', 'resolve', 'close', 'archive']
