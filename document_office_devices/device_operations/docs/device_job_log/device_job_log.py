"""Doc runtime hooks for device_job_log."""

class DocRuntime:
    doc_key = "device_job_log"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'archive']
