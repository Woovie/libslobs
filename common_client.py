import uuid, threading, asyncio
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
        self.threads['queue_processor'] = threading.Thread(target=self.queue.start)
        self.threads['websocket_recv'] = threading.Thread(target=self.connection_handler.start, args=[self.queue])
        self.authid = None