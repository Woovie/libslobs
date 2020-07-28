import uuid, threading, asyncio, configparser, random
import libslobs.common_websocket as websocket
import libslobs.common_payloads as payloads
import libslobs.common_queue as queue
import libslobs.common_sockjs as sockjs
from typing import Callable, Any

class Client():
    def __init__(self, api_token: str, url: str, verbosity: int = None):
        self.url = url
        self.api_token = api_token
        self.connection_string = str(uuid.uuid1())
        self.server_number = f"{random.randrange(1, 10**3):03}"
        self.websocket_url = f"{self.url}/{self.server_number}/{self.connection_string}/websocket"
        self.websocket = websocket.WebSocket(self.websocket_url)
        self.queue = queue.Queue()
        self.verbosity = verbosity
        self.threads = {}
        self.threads['queue_processor'] = threading.Thread(target=self.queue.start)
        self.threads['websocket_recv'] = threading.Thread(target=self.websocket.start, args=[self.queue])
        self.authid = None
    
    def connect(self):
        output = self.websocket.connect()
        if output == 'o':
            self.start_threads()
            auth_result = self.auth()
            if auth_result:
                return True

    def start_threads(self):
        self.threads['queue_processor'].start()
        self.threads['websocket_recv'].start()

    def auth(self):
        payload = payloads.create_payload('auth', 'TcpServerService', self.api_token)
        self.authid = payload['id']
        auth_output = self.websocket.exec_return(payload)
        if 'result' in auth_output:
            if auth_output['result']:
                return True
            else:
                print(auth_output)
                return False
        else:
            print(auth_output)
            return False