import asyncio, websockets, json

class SLOBSWebSocket():
    def __init__(self, url = None):
        self.ws = None
        self.url = url
        self.loop = asyncio.get_event_loop()

    async def _connect(self):
        self.ws = await websockets.connect(self.url)
        response = await self.ws.recv()
        return response

    async def _exec(self, cmd):
        await self.ws.send(cmd)
        received = await self.ws.recv()
        return received

    async def _recv(self):
        received = await self.ws.recv()
        return received

    def connect(self):
        return self.loop.run_until_complete(self._connect())

    def exec(self, cmd):
        return self.loop.run_until_complete(self._exec(self._encode_sockjs_array(cmd)))
    
    def _decode_sockjs_array(self, arr):
        return json.loads(json.loads(arr[2:-1]))
    
    def _encode_sockjs_array(self, arr):
        return json.dumps(json.dumps(arr))
