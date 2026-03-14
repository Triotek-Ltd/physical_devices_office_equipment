"""Doc runtime hooks for device_sync_event."""

class DocRuntime:
    doc_key = "device_sync_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'retry', 'archive']
