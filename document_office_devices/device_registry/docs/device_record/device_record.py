"""Doc runtime hooks for device_record."""

class DocRuntime:
    doc_key = "device_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'provision', 'activate', 'retire', 'archive']
