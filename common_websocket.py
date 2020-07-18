import asyncio, websockets, json
import libslobs.common_queue

class SLOBSWebSocket():
    def __init__(self, url = None):
        self.ws = None
        self.url = url
        self.loop = asyncio.new_event_loop()
        self.queue = None

    async def _connect(self):
        self.ws = await websockets.connect(self.url)
        response = await self.ws.recv()
        return response

    async def _exec(self, cmd: str):
        await self.ws.send(cmd)

    async def _recv(self):
        while True:
            received = await self.ws.recv()
            self.queue._incoming(self.decode_sockjs_array(received))

    def start(self, queue):
        self.queue = queue
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._recv())

    def connect(self):
        asyncio.set_event_loop(self.loop)
        return self.loop.run_until_complete(self._connect())

    def exec(self, cmd: str):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._exec(self.encode_sockjs_array(cmd)))

    async def exec_return(self, cmd: str):
        message_id = cmd['id']
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        encoded_cmd = self.encode_sockjs_array(cmd)
        await self.ws.send(encoded_cmd)
        result = None
        while not result:
            response = await self.ws.recv()
            decoded_response = self.decode_sockjs_array(response)
            if decoded_response['id'] == message_id:
                result = decoded_response
        return result

    @staticmethod
    def decode_sockjs_array(arr: str):
        return json.loads(json.loads(arr[2:-1]))
    
    @staticmethod
    def encode_sockjs_array(arr: dict):
        return json.dumps(json.dumps(arr))