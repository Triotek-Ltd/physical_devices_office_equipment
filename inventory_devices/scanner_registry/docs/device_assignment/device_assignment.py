"""Doc runtime hooks for device_assignment."""

class DocRuntime:
    doc_key = "device_assignment"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'return', 'close', 'archive']
