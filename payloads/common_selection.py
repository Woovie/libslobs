import libslobs.payloads.common_payloads as common_payloads

class SLOBSSelectionService(common_payloads.SLOBSPayloads):
    def __init__(self):
        common_payloads.SLOBSPayloads.__init__(self)
        self.resource = "SelectionService"

    def sceneId(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "sceneId",
            "params": {
                "resource": self.resource
            }
        }

    def add(self, ids):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "add",
            "params": {
                "resource": self.resource,
                "args": [ids]
            }
        }

    def centerOnScreen(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "centerOnScreen",
            "params": {
                "resource": self.resource
            }
        }

    def clone(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "clone",
            "params": {
                "resource": self.resource
            }
        }

    def copyTo(self, sceneId, folderId, duplicateSources):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "sceneId",
            "params": {
                "resource": self.resource,
                "args": [sceneId, folderId, duplicateSources]
            }
        }

    def deselect(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "deselect",
            "params": {
                "resource": self.resource
            }
        }

    def fitToScreen(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "fitToScreen",
            "params": {
                "resource": self.resource
            }
        }

    def flipX(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "flipX",
            "params": {
                "resource": self.resource
            }
        }

    def flipY(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "flipY",
            "params": {
                "resource": self.resource
            }
        }

    def getBoundingRect(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getBoundingRect",
            "params": {
                "resource": self.resource
            }
        }

    def getFolders(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getFolders",
            "params": {
                "resource": self.resource
            }
        }

    def getIds(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getIds",
            "params": {
                "resource": self.resource
            }
        }

    def getInverted(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getInverted",
            "params": {
                "resource": self.resource
            }
        }

    def getInvertedIds(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getInvertedIds",
            "params": {
                "resource": self.resource
            }
        }

    def getItems(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getItems",
            "params": {
                "resource": self.resource
            }
        }

    def getLastSelected(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getLastSelected",
            "params": {
                "resource": self.resource
            }
        }

    def getLastSelectedId(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getLastSelectedId",
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

    def getRootNodes(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getRootNodes",
            "params": {
                "resource": self.resource
            }
        }

    def getScene(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getScene",
            "params": {
                "resource": self.resource
            }
        }

    def getSize(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getSize",
            "params": {
                "resource": self.resource
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

    def getVisualItems(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getVisualItems",
            "params": {
                "resource": self.resource
            }
        }

    def invert(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "invert",
            "params": {
                "resource": self.resource
            }
        }

    def isSceneFolder(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "isSceneFolder",
            "params": {
                "resource": self.resource
            }
        }

    def isSceneItem(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "isSceneItem",
            "params": {
                "resource": self.resource
            }
        }

    def isSelected(self, nodeId):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "isSelected",
            "params": {
                "resource": self.resource,
                "args": [nodeId]
            }
        }

    def moveTo(self, sceneId, folderId):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "moveTo",
            "params": {
                "resource": self.resource,
                "args": [sceneId, folderId]
            }
        }

    def placeAfter(self, sceneNodeId):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "placeAfter",
            "params": {
                "resource": self.resource,
                "args": [sceneNodeId]
            }
        }

    def placeBefore(self, sceneNodeId):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "placeBefore",
            "params": {
                "resource": self.resource,
                "args": [sceneNodeId]
            }
        }

    def remove(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "remove",
            "params": {
                "resource": self.resource
            }
        }

    def reset(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "reset",
            "params": {
                "resource": self.resource
            }
        }

    def resetTransform(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "resetTransform",
            "params": {
                "resource": self.resource
            }
        }

    def rotate(self, deg):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "rotate",
            "params": {
                "resource": self.resource,
                "args": [deg]
            }
        }

    def scale(self, scale, origin):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "scale",
            "params": {
                "resource": self.resource,
                "args": [scale, origin]
            }
        }

    def scaleWithOffset(self, scale, offset):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "scaleWithOffset",
            "params": {
                "resource": self.resource,
                "args": [scale, offset]
            }
        }

    def select(self, ids):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "select",
            "params": {
                "resource": self.resource,
                "args": [ids]
            }
        }

    def selectAll(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "selectAll",
            "params": {
                "resource": self.resource
            }
        }

    def setContentCrop(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "setContentCrop",
            "params": {
                "resource": self.resource
            }
        }

    def setParent(self, folderId):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "setParent",
            "params": {
                "resource": self.resource,
                "args": [folderId]
            }
        }

    def setRecordingVisible(self, recordingVisible):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "setRecordingVisible",
            "params": {
                "resource": self.resource,
                "args": [recordingVisible]
            }
        }

    def setSettings(self, settings):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "setSettings",
            "params": {
                "resource": self.resource,
                "args": [settings]
            }
        }

    def setStreamVisible(self, streamVisible):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "setStreamVisible",
            "params": {
                "resource": self.resource,
                "args": [streamVisible]
            }
        }

    def setTransform(self, transform):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "setTransform",
            "params": {
                "resource": self.resource,
                "args": [transform]
            }
        }

    def setVisibility(self, visible):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "setVisibility",
            "params": {
                "resource": self.resource,
                "args": [visible]
            }
        }

    def stretchToScreen(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "stretchToScreen",
            "params": {
                "resource": self.resource
            }
        }