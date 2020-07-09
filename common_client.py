import uuid
import libslobs.common_queue as queue
import libslobs.common_websocket as websocket
import libslobs.common_config as config
import libslobs.common_payloads as payloads

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
        payload = payloads.SLOBSPayloads().create_pipeline("auth", "TcpServerService", self.auth_token)
        result = self.connection_handler.exec(payload)#fails
        decoded = self.connection_handler._decode_sockjs_array(result)
        if 'error' in decoded:
            print(decoded)
            return False
        elif 'result' in decoded:
            return decoded['result']
        else:
            print(decoded)
            return False

    def send(self):
        return True