from collections import defaultdict 
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.lis=[]
        self.cap=defaultdict(int)
        

    def get(self, key: int) -> int:
        if key in self.lis:
            self.lis.remove(key)
            self.lis.append(key)
            return self.cap[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.lis:
            if len(self.lis)<self.capacity:
                self.lis.append(key)
            else:
                self.lis.pop(0)
                self.lis.append(key)
        else:
            self.lis.remove(key)
            self.lis.append(key)
        self.cap[key]=value
