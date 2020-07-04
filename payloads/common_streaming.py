import payloads.common_payloads

class SLOBSStreamingService(payloads.SLOBSPayloads):
    def __init__(self):
        payloads.SLOBSPayloads.__init__(self)
        self.resource = "StreamingService"

    def recordingStatusChange(self):# Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "recordingStatusChange",
            "params": {
                "resource": self.resource
            }
        }

    def replayBufferStatusChange(self):# Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "replayBufferStatusChange",
            "params": {
                "resource": self.resource
            }
        }

    def streamingStatusChange(self):# Event
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "streamingStatusChange",
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
    
    def saveReplay(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "saveReplay",
            "params": {
                "resource": self.resource
            }
        }

    def startReplayBuffer(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "startReplayBuffer",
            "params": {
                "resource": self.resource
            }
        }

    def stopReplayBuffer(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "stopReplayBuffer",
            "params": {
                "resource": self.resource
            }
        }

    def toggleRecording(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "toggleRecording",
            "params": {
                "resource": self.resource
            }
        }

    def toggleStreaming(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "toggleStreaming",
            "params": {
                "resource": self.resource
            }
        }