import libslobs.payloads.common_payloads as common_payloads

class SLOBSTcpServerService(common_payloads.SLOBSPayloads):
    def __init__(self):
        common_payloads.SLOBSPayloads.__init__(self)
        self.resource = "TcpServerService"

    def auth(self, token):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "auth",
            "params": {
                "resource": self.resource,
                "args": [token]
            }
        }

    def unsubscribe(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "unsubscribe",
            "params": {
                "resource": self.resource
            }
        }

    def listenAllSubscriptions(self):# Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "listenAllSubscriptions",
            "params": {
                "resource": self.resource
            }
        }

    def forceRequests(self, force):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "unsubscribe",
            "params": {
                "resource": self.resource,
                "args": [force]
            }
        }