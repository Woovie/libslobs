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
        self.threads['queue_processor'] = threading.Thread(target=self.queue._process_queue)
        self.threads['websocket_recv'] = threading.Thread(target=self.connection_handler.process_recv, args=[self.queue])

    def connect(self) -> bool:
        returned = self.connection_handler.connect()
        if returned == 'o':
            for thread in self.threads:
                self.threads[thread].start()
            return True
        else:
            return False

    def auth(self, callback: Callable[[dict], Any]): 
        self.send("auth", "TcpServerService", self.api_token, callback=callback)

    def send(self, method: str, resource: str, *args, callback: Callable[[dict], Any] = None):
        payload = libslobs.common_payloads.SLOBSPayloads().create_payload(method, resource, args)
        if callback and hasattr(callback, '__call__'):
            self.queue.add_callback(callback, payload['id'])
        self.connection_handler.exec(payload)
        

    def recv(self, payload: dict):# So we will get back a dict from SLOBS here
        return True