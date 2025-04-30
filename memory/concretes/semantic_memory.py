from memory.memory_cortex import MemoryCortex
from memory.memory_store import MemoryStore


class SemanticDocumentStore(MemoryStore):
    def __init__(self):
        self.vector_store = []

    def add(self, doc): self.vector_store.append(doc)
    def get(self, key): return self.vector_store[key]
    def update(self, key, doc): self.vector_store[key] = doc
    def delete(self, key): self.vector_store.pop(key)
    def all(self): return self.vector_store

    def search(self, query):
        return f"Top matches for: '{query}'"

class SemanticMemoryCortex(MemoryCortex):
    def __init__(self):
        super().__init__()
        self.doc_store = SemanticDocumentStore()

    def query(self, query):
        return self.doc_store.search(query)

    def store(self, data):
        self.doc_store.add(data)

    def forget(self, key=None):
        self.doc_store.vector_store.clear()

    def update(self, key, data):
        self.doc_store.update(key, data)
