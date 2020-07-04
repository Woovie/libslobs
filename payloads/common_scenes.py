import libslobs.payloads.common_payloads as common_payloads

class SLOBSScenesService(common_payloads.SLOBSPayloads):
    def __init__(self):
        common_payloads.SLOBSPayloads.__init__(self)
        self.resource = "ScenesService"

    def activeScene(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "activeScene",
            "params": {
                "resource": self.resource
            }
        }

    def activeSceneId(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "activeSceneId",
            "params": {
                "resource": self.resource
            }
        }

    def itemAdded(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "itemAdded",
            "params": {
                "resource": self.resource
            }
        }

    def itemRemove(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "itemRemove",
            "params": {
                "resource": self.resource
            }
        }

    def itemUpdated(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "itemUpdated",
            "params": {
                "resource": self.resource
            }
        }

    def sceneAdded(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "sceneAdded",
            "params": {
                "resource": self.resource
            }
        }

    def sceneRemoved(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "sceneRemoved",
            "params": {
                "resource": self.resource
            }
        }

    def sceneSwitched(self):#Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "sceneSwitched",
            "params": {
                "resource": self.resource
            }
        }

    def createScene(self, name):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "createScene",
            "params": {
                "resource": self.resource,
                "args": [name]
            }
        }

    def getScene(self, id):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getScene",
            "params": {
                "resource": self.resource,
                "args": [id]
            }
        }

    def makeSceneActive(self, id):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "makeSceneActive",
            "params": {
                "resource": self.resource,
                "args": [id]
            }
        }

    def removeScene(self, id):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "removeScene",
            "params": {
                "resource": self.resource,
                "args": [id]
            }
        }