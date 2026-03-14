"""Doc runtime hooks for scanner_device."""

class DocRuntime:
    doc_key = "scanner_device"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'provision', 'assign', 'retire', 'archive']
