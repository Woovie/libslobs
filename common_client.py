import uuid, threading, asyncio, configparser
import libslobs.common_websocket
import libslobs.common_payloads
import libslobs.common_queue
from typing import Callable, Any

class Client():
    def __init__(self, api_token: str, url: str, verbosity: int = None):
        self.url = url
        self.api_token = api_token
        self.connection_string = str(uuid.uuid1())
        self.slobs_websocket_url = f"{self.url}{self.connection_string}/websocket"
        self.websocket = libslobs.common_websocket.WebSocket(self.slobs_websocket_url)
        self.queue = libslobs.common_queue.Queue()
        self.verbosity = verbosity
        self.threads = {}
        self.threads['queue_processor'] = threading.Thread(target=self.queue.start)
        self.threads['websocket_recv'] = threading.Thread(target=self.websocket.start, args=[self.queue])
        self.authid = None
    
    def connect(self):
        output = self.websocket.connect()
        if output == 'o':
            self.start_threads()
            self.auth()

    def start_threads(self):
        self.threads['queue_processor'].start()
        self.threads['websocket_recv'].start()

    def auth(self):
        payload = libslobs.common_payloads.create_payload('auth', 'TcpServerService', self.api_token)
        self.authid = payload['id']
        auth_output = self.websocket.exec_return(payload)
        print(auth_output)