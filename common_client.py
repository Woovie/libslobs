import uuid, threading
import libslobs.common_websocket
import libslobs.common_payloads
import libslobs.common_queue
from typing import Callable, Any

class SLOBSClient():
    def __init__(self, api_token: str, url: str, verbosity: int = None):
        self.url = url
        self.api_token = api_token
        self.connection_string = str(uuid.uuid1())
        self.slobs_websocket_url = f"{self.url}{self.connection_string}/websocket"
        self.connection_handler = libslobs.common_websocket.SLOBSWebSocket(self.slobs_websocket_url)
        self.queue = libslobs.common_queue.SLOBSQueue()
        self.verbosity = verbosity
        self.threads = {}

    def connect(self):
        returned = self.connection_handler.connect()
        if returned == 'o':
            return True
        else:
            return False

    def auth(self):
        payload = libslobs.common_payloads.SLOBSPayloads().create_payload("auth", "TcpServerService", self.api_token)
        result = self.connection_handler.exec(payload)
        decoded = self.connection_handler._decode_sockjs_array(result)
        if 'error' in decoded:
            return False, decoded
        elif 'result' in decoded:
            return True, decoded

    def send(self, method: str, resource: str, callback: Callable[[dict], Any] = None, *args):
        if callback and hasattr(callback, '__call__'):# throw it in queue for callback
            payload = libslobs.common_payloads.SLOBSPayloads().create_payload(method, resource, args)
            payload_result = self.connection_handler.exec(payload)
            queue_result = self.queue.add_callback(callback, payload['id'])

        else:
            return False# Some error needs to happen here.
        

    def recv(self, payload: dict):# So we will get back a dict from SLOBS here
        return True