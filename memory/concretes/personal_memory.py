from memory.memory_cortex import MemoryCortex
from memory.memory_store import MemoryStore


class PersonalDataStore(MemoryStore):
    def __init__(self):
        self.data = {}

    def add(self, data): self.data.update(data)
    def get(self, key): return self.data.get(key)
    def update(self, key, value): self.data[key] = value
    def delete(self, key): self.data.pop(key, None)
    def all(self): return self.data

class PersonalMemoryCortex(MemoryCortex):
    def __init__(self):
        super().__init__()
        self.data_store = PersonalDataStore()

    def query(self, query):
        return f"Personal data: {self.data_store.get(query)}"

    def store(self, data):
        self.data_store.add(data)

    def forget(self, key=None):
        if key:
            self.data_store.delete(key)
        else:
            self.data_store.profile.clear()

    def update(self, key, data):
        self.data_store.update(key, data)
