import libslobs.payloads.common_payloads as common_payloads

class SLOBSPerformanceService(common_payloads.SLOBSPayloads):
    def __init__(self):
        common_payloads.SLOBSPayloads.__init__(self)
        self.resource = "PerformanceService"

    def getModel(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getModel",
            "params": {
                "resource": self.resource
            }
        }