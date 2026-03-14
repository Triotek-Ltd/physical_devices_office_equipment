"""Doc runtime hooks for terminal_session."""

class DocRuntime:
    doc_key = "terminal_session"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['open', 'assign', 'close', 'archive']
