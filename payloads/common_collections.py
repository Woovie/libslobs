import libslobs.payloads.common_payloads as common_payloads

class SLOBSSceneCollectionsService(common_payloads.SLOBSPayloads):
    def __init__(self):
        common_payloads.SLOBSPayloads.__init__(self)
        self.resource = "SceneCollectionsService"

    def activeCollection(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "activeCollection",
            "params": {
                "resource": self.resource
            }
        }

    def collectionAdded(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": ""
            }
        }

    def collectionRemove(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": ""
            }
        }

    def collectionSwitched(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": ""
            }
        }

    def collectionUpdated(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": ""
            }
        }

    def collectionWillSwitch(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": ""
            }
        }

    def collections(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "collections",
            "params": {
                "resource": self.resource
            }
        }

    def create(self, options):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": self.resource
            }
        }
    
    def delete(self, id):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": self.resource
            }
        }
    
    def fetchSceneCollectionsSchema(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": self.resource
            }
        }

    def load(self, id):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": ""
            }
        }
    
    def rename(self, newName, id):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "",
            "params": {
                "resource": self.resource
            }
        }