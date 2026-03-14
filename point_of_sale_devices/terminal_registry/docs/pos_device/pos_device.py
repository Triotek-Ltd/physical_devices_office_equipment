"""Doc runtime hooks for pos_device."""

class DocRuntime:
    doc_key = "pos_device"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'provision', 'activate', 'retire', 'archive']
