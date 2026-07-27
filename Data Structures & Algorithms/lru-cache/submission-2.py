class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        

    def get(self, key: int) -> int:
        print('getting', key, self.cache)
        for idx, [key_, value] in enumerate(self.cache):
            if key_ == key:
                self.cache.pop(idx)
                self.cache.append([key_, value])
                return value
        return -1

    def put(self, key: int, value: int) -> None:
        print('putting', key, self.cache)
        for idx, [key_, value_] in enumerate(self.cache):
            if key_ == key:
                self.cache.pop(idx)
                self.cache.append([key_, value])
                return
        self.cache.append([key, value])
        if len(self.cache) > self.capacity:
            self.cache.pop(0)
        return
        
