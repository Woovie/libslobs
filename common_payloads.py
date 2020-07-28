import uuid
from typing import Callable, Any

def create_payload(method: str, resource: str, *args: Any):
    token = str(uuid.uuid1())
    return {
        "jsonrpc": "2.0",
        "id": token,
        "method": method,
        "params": {
            "resource": resource,
            "args": list(args) if args else None
        }
    }