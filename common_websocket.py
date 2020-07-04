import asyncio, websockets, json
import libslobs.payloads.common_payloads as common_payloads
import libslobs.common_config as common_config

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

    def auth(self, token):
        payload = common_payloads.SLOBSPayloads().auth(token)
        result = self.exec(payload)#fails
        decoded = self._decode_sockjs_array(result)
        if 'error' in decoded:
            print(decoded)
            return False
        elif 'result' in decoded:
            return decoded['result']
        else:
            print(decoded)
            return False

    def exec(self, cmd):
        return self.loop.run_until_complete(self._exec(self._encode_sockjs_array(cmd)))
    
    def _decode_sockjs_array(self, arr):
        return json.loads(json.loads(arr[2:-1]))
    
    def _encode_sockjs_array(self, arr):
        return json.dumps(json.dumps(arr))