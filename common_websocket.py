import asyncio, websockets, json
import libslobs.common_queue
import libslobs.common_sockjs as sockjs
 
class WebSocket():
    def __init__(self, url = None):
        self.ws = None
        self.url = url
        self.loop = asyncio.new_event_loop()
        self.queue = None

    async def _connect(self):
        self.ws = await websockets.connect(self.url)
        response = await self.ws.recv()
        return response

    async def _disconnect(self):
        await self.ws.close()
        return True

    async def _exec(self, cmd: str):
        await self.ws.send(cmd)

    async def _recv(self):
        while True:
            received = await self.ws.recv()# This will properly hold the thread, so we can use while True without issue here. I truly want to process incoming messages _as fast as possible_
            self.queue._incoming(sockjs.decode_sockjs_array(received))

    def start(self, queue: libslobs.common_queue.Queue):
        self.queue = queue
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._recv())

    def connect(self):
        asyncio.set_event_loop(self.loop)
        return self.loop.run_until_complete(self._connect())

    def disconnect(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(self._disconnect())

    def exec(self, cmd: dict):# dict = libslobs.common_payloads.Payload.create_payload
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._exec(sockjs.encode_sockjs_array(cmd)))

    def exec_return(self, cmd: dict):# dict = libslobs.common_payloads.Payload.create_payload
        self.exec(cmd)
        result = None
        while not result:
            for item in self.queue.incoming:
                if self._process_exec_return(cmd, item):
                    self.queue.incoming.remove(item)
                    result = item
                    break
        return result

    def _process_exec_return(self, cmd: dict, item: dict):# dict = libslobs.common_payloads.Payload.create_payload
        if item['id'] == cmd['id']:
            return item
        else:
            return None