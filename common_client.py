import uuid
import libslobs.common_queue as queue
import libslobs.common_websocket as websocket
import libslobs.common_config as config

class SLOBSClient():
    def __init__(self):
        self.config = config.SLOBSConfig().config
        self.connection_string = str(uuid.uuid1())
        self.slobs_websocket_url = f"{self.config['slobs-client']['url']}{self.connection_string}/websocket"
        self.connection_handler = websocket.SLOBSWebSocket(self.slobs_websocket_url)
        self.auth_token = self.config['slobs-client']['api-token']
        self.queue = queue.SLOBSQueue()

    def connect(self):
        return self.connection_handler.connect()

    def auth(self):
        return self.connection_handler.auth(self.auth_token)


client_test = SLOBSClient()
client_test.connect()
client_test.auth()