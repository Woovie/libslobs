import uuid

class SLOBSPayloads():
    def __init__(self):
        self.token = str(uuid.uuid1())

    def auth(self, token):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "auth",
            "params": {
                "resource": "TcpServerService",
                "args": [
                    token
                ]
            }
        }

    def get_scene_items(self, sceneid):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getItems",
            "params": {
                "resource": f"Scene[\"{sceneid}\"]",
            }
        }



#class SLOBS(SLOBSPayloads):

#class SLOBSAudioService(SLOBSPayloads):

#class SLOBSNotificationsService(SLOBSPayloads):

#class SLOBSPerformanceService(SLOBSPayloads):

#class SLOBSSceneCollectionsService(SLOBSPayloads):

#class SLOBSSelectionService(SLOBSPayloads):

#class SLOBSSourceService(SLOBSPayloads):

#class SLOBSTransitionsService(SLOBSPayloads):
