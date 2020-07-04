import libslobs.payloads.common_payloads as common_payloads

class SLOBSAudioService(common_payloads.SLOBSPayloads):
    def __init__(self):
        common_payloads.SLOBSPayloads.__init__(self)
        self.resource = "AudioService"
    
    def getSource(self, sourceId):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getSource",
            "params": {
                "resource": self.resource,
                "args": [sourceId]
            }
        } 

    def getSources(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getSources",
            "params": {
                "resource": self.resource
            }
        }

    def getSourcesForCurrentScene(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getSourcesForCurrentScene",
            "params": {
                "resource": self.resource
            }
        }

    def getSourcesForScene(self, sceneId):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getSourcesForScene",
            "params": {
                "resource": self.resource,
                "args": [sceneId]
            }
        }