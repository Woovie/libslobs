from typing import Callable, Any
import asyncio
from time import sleep, time

class SLOBSQueue():
    def __init__(self):
        self.incoming = []
        self.events = {}
        self.loop = asyncio.new_event_loop()

    def start(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._process_queue())

    def add_callback(self, callback: Callable[[dict], Any], id: str):
        self.events[id] = callback
        if id in self.events:
            return True
        else:
            return False# This is going to be a major problem, and likely python will have fucked up much greater if this happens.

    def remove_callback(self, id: str):
        self.events.pop(id)
    
    def _process_queue(self):
        while True:
            if len(self.incoming) > 0:
                for message in self.incoming:
                    self._process_queue_message(message)
                sleep(-time()%0.01667)
            else:
                sleep(0.01667)

    def _process_queue_message(self, message: str):
        if 'id' in message:
            if message['id'] in self.events:
                self.events[message['id']](message)
                self.incoming.remove(message)

    def _incoming(self, message: dict):
        self.incoming.append(message)