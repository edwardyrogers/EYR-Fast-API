from memory.memory_cortex import MemoryCortex
from memory.memory_store import MemoryStore


class EpisodicEventStore(MemoryStore):
    def __init__(self):
        self.events = []

    def add(self, event): self.events.append(event)
    def get(self, key): return self.events[key] if key < len(self.events) else None
    def update(self, key, event): self.events[key] = event
    def delete(self, key): self.events.pop(key)
    def all(self): return self.events[-5:]  # return recent

class EpisodicMemoryCortex(MemoryCortex):
    def __init__(self):
        self.event_store = EpisodicEventStore()

    def query(self, query):
        return f"Recent events: {self.event_store.all()}"

    def store(self, data):
        self.event_store.add(data)

    def forget(self, key=None):
        self.event_store.events.clear()

    def update(self, key, data):
        self.event_store.update(key, data)
