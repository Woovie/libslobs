import libslobs.payloads.common_payloads as common_payloads

class SLOBSSourcesService(common_payloads.SLOBSPayloads):
    def __init__(self):
        common_payloads.SLOBSPayloads.__init__(self)
        self.resource = "SourcesService"

    def sourceAdded(self):# Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "sourceAdded",
            "params": {
                "resource": self.resource
            }
        }

    def sourceRemoved(self):# Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "sourceRemoved",
            "params": {
                "resource": self.resource
            }
        }

    def sourceUpdated(self):# Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "sourceUpdated",
            "params": {
                "resource": self.resource
            }
        }

    def addFile(self, path):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "addFile",
            "params": {
                "resource": self.resource,
                "args": [path]
            }
        }

    def createSource(self, name, sourceType, settings, options):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "createSource",
            "params": {
                "resource": self.resource,
                "args": [name, sourceType, settings, options]
            }
        }

    def getAvailableSourcesTypesList(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getAvailableSourcesTypesList",
            "params": {
                "resource": self.resource
            }
        }

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

    def getSourcesByName(self, name):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getSourcesByName",
            "params": {
                "resource": self.resource,
                "args": [name]
            }
        }

    def removeSource(self, id):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "removeSource",
            "params": {
                "resource": self.resource,
                "args": [id]
            }
        }

    def showAddSource(self, sourceType):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "showAddSource",
            "params": {
                "resource": self.resource,
                "args": [sourceType]
            }
        }

    def showShowcase(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "showShowcase",
            "params": {
                "resource": self.resource
            }
        }

    def showSourceProperties(self, sourceId):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "showSourceProperties",
            "params": {
                "resource": self.resource,
                "args": [sourceId]
            }
        }