import uuid
from typing import Callable, Any

class SLOBSPayloads():
    def __init__(self):
        self.token = str(uuid.uuid1())

    def create_payload(self, method: str, resource: str, *args: Any):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": method,
            "params": {
                "resource": resource,
                "args": list(args) if args else None
            }
        }