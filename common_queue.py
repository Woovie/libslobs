from typing import Callable, Any
import asyncio
from time import sleep, time
from threading import Condition

class SLOBSQueue():
    def __init__(self):
        self.incoming = []
        self.events = {}
        self.loop = asyncio.new_event_loop()
        self.condition = Condition()

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
        with self.condition:
            while not len(self.incoming) > 0:
                self.condition.wait()
            for message in self.incoming:
                self._process_queue_message(message)

    def _process_queue_message(self, message: str):
        if 'id' in message:
            if message['id'] in self.events:
                self.events[message['id']](message)
                self.incoming.remove(message)

    def _incoming(self, message: dict):
        self.incoming.append(message)