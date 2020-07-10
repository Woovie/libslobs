from typing import Callable, Any

class SLOBSQueue():
    def __init__(self):
        self.incoming = []
        self.events = {}

    def add_callback(self, callback: Callable[[dict], Any], id: str):
        self.events[id] = callback
        if id in self.events:
            return True
        else:
            return False# This is going to be a major problem, and likely python will have fucked up much greater if this happens.

    def remove_callback(self, id: str):
        self.events.pop(id)
    
    def _process_queue(self):
        for message in self.incoming:
            print(message)
        
    def _incoming(self, message: dict):
        self.incoming.append(message)