"""Doc runtime hooks for supply_level_snapshot."""

class DocRuntime:
    doc_key = "supply_level_snapshot"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
