"""Doc runtime hooks for access_exception_case."""

class DocRuntime:
    doc_key = "access_exception_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'clear', 'escalate', 'close', 'archive']
