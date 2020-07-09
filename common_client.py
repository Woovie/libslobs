import uuid
import libslobs.common_queue as queue
import libslobs.common_websocket as websocket
import libslobs.common_payloads as payloads

class SLOBSClient():
    def __init__(self, auth_token: str, url: str):
        self.url = url
        self.auth_token = auth_token
        self.connection_string = str(uuid.uuid1())
        self.slobs_websocket_url = f"{self.url}{self.connection_string}/websocket"
        self.connection_handler = websocket.SLOBSWebSocket(self.slobs_websocket_url)
        self.queue = queue.SLOBSQueue()

    def connect(self):
        return self.connection_handler.connect()

    def auth(self):
        payload = payloads.SLOBSPayloads().create_payload("auth", "TcpServerService", self.auth_token)
        result = self.connection_handler.exec(payload)
        decoded = self.connection_handler._decode_sockjs_array(result)
        if 'error' in decoded:
            print(decoded)
            return False
        elif 'result' in decoded:
            return decoded['result']
        else:
            print(decoded)
            return False

    def send(self, method: str, resource: str, callback = None, *args):
        payload = payloads.SLOBSPayloads().create_payload(method, resource, args)
        self.connection_handler.send(payload, callback)
