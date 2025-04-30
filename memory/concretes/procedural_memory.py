from memory.memory_cortex import MemoryCortex
from memory.memory_store import MemoryStore


class ProceduralWorkflowStore(MemoryStore):
    def __init__(self):
        self.vector_store = []

    def add(self, doc): self.vector_store.append(doc)
    def get(self, key): return self.vector_store[key]
    def update(self, key, doc): self.vector_store[key] = doc
    def delete(self, key): self.vector_store.pop(key)
    def all(self): return self.vector_store

    def search(self, query):
        return f"Top matches for: '{query}'"

class ProceduralMemoryCortex(MemoryCortex):
    def __init__(self):
        self.workflow_store = ProceduralWorkflowStore()

    def query(self, task_name: str) -> str:
        return self.workflow_store.get(task_name)

    def store(self, data: dict):
        for name, steps in data.items():
            self.workflow_store.add(name, steps)

    def forget(self, key: str = None):
        if key:
            self.workflow_store.delete(key)
        else:
            self.workflow_store.workflows.clear()

    def update(self, key: str, data: str):
        self.workflow_store.update(key, data)