from memory.memory_cortex import MemoryCortex
from memory.memory_store import MemoryStore

class ShortTermDataStore(MemoryStore):
    def __init__(self):
        self.data = {}

    def add(self, data): self.data.update(data)
    def get(self, key): return self.data.get(key)
    def update(self, key, value): self.data[key] = value
    def delete(self, key): self.data.pop(key, None)
    def all(self): return self.data
    
class ShortTermMemoryCortex(MemoryCortex):
    def __init__(self):
        self.data_store = ShortTermDataStore()

    def query(self, user_query):
        return self.data_store.get(user_query, "Not found in short-term memory.")

    def store(self, data):
        self.data_store.update(data)

    def forget(self, key=None):
        if key:
            self.data_store.pop(key, None)
        else:
            self.data_store.clear()

    def update(self, key, data):
        self.data_store[key] = data
