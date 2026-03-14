"""Doc runtime hooks for access_device."""

class DocRuntime:
    doc_key = "access_device"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'provision', 'activate', 'retire', 'archive']
