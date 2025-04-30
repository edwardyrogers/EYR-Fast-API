class MemoryStore:
    def add(self, item): 
        raise NotImplementedError
        
    def get(self, key): 
        raise NotImplementedError
        
    def update(self, key, item): 
        raise NotImplementedError
        
    def delete(self, key): 
        raise NotImplementedError
        
    def all(self): 
        raise NotImplementedError
        
