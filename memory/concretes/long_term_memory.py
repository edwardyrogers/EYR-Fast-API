from memory.memory_cortex import MemoryCortex
from memory.memory_store import MemoryStore

class LongTermDataStore(MemoryStore):
    def __init__(self):
        self.data = {}

    def add(self, data): self.data.update(data)
    def get(self, key): return self.data.get(key)
    def update(self, key, value): self.data[key] = value
    def delete(self, key): self.data.pop(key, None)
    def all(self): return self.data
    
class LongTermMemoryCortex(MemoryCortex):
    def __init__(self):
        self.data_store = LongTermDataStore()

    def query(self, user_query):
        return self.data_store.get(user_query, "Not found in long-term memory.")

    def store(self, data):
        self.data_store.update(data)

    def forget(self, key=None):
        if key:
            self.data_store.data.pop(key, None)
        else:
            self.data_store.data.clear()

    def update(self, key, data):
        self.data_store[key] = data
