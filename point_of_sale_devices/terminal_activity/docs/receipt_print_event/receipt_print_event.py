"""Doc runtime hooks for receipt_print_event."""

class DocRuntime:
    doc_key = "receipt_print_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'archive']
