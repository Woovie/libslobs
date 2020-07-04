import libslobs.payloads.common_payloads as common_payloads

class SLOBSTransitionsService(common_payloads.SLOBSPayloads):
    def __init__(self):
        common_payloads.SLOBSPayloads.__init__(self)
        self.resource = "TransitionsService"

    def studioModeChanged(self):# Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "studioModeChanged",
            "params": {
                "resource": self.resource
            }
        }

    def disableStudioMode(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "disableStudioMode",
            "params": {
                "resource": self.resource
            }
        }

    def enableStudioMode(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "enableStudioMode",
            "params": {
                "resource": self.resource
            }
        }

    def executeStudioModeTransition(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "executeStudioModeTransition",
            "params": {
                "resource": self.resource
            }
        }

    def getModel(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getModel",
            "params": {
                "resource": self.resource
            }
        }