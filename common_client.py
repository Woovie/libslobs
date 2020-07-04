import uuid
import slobs.payloads.common_payloads as common_payloads
import slobs.common_queue as common_queue
import slobs.common_websocket as common_websocket
import slobs.common_config as common_config

class SLOBSClient():
    def __init__(self):
        self.config = common_config.SLOBSConfig().config
        self.connection_string = str(uuid.uuid1())
        self.slobs_websocket_url = f"{self.config['slobs-client']['url']}{self.connection_string}/websocket"
        self.connection_handler = common_websocket.SLOBSWebSocket(self.slobs_websocket_url)
        self.auth_token = self.config['slobs-client']['api-token']
        self.queue = common_queue.SLOBSQueue()

    def connect(self):
        return self.connection_handler.connect()

    def auth(self):
        return self.connection_handler.auth(self.auth_token)