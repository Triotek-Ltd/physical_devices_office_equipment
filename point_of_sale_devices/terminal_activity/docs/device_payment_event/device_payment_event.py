"""Doc runtime hooks for device_payment_event."""

class DocRuntime:
    doc_key = "device_payment_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'link', 'archive']
