class MemoryCortex:
    def query(self, query: str) -> str:
        raise NotImplementedError

    def store(self, data: dict):
        raise NotImplementedError

    def forget(self, key: str = None):
        raise NotImplementedError

    def update(self, key: str, data: dict):
        raise NotImplementedError
