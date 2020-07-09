from typing import Callable

class SLOBSQueue():
    def __init__(self):
        self.incoming = []
        self.events = {}

    def add_callback(self, callback: Callable[[str], str], id: str):
        self.events[id] = callback

    def remove_callback(self, id: str):
        self.events.pop(id)