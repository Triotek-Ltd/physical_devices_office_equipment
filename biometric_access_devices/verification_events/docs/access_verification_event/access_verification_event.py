"""Doc runtime hooks for access_verification_event."""

class DocRuntime:
    doc_key = "access_verification_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'link', 'archive']
