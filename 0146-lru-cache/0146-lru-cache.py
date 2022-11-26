class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev= None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
        
    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            self.insert(self.hashMap[key])
            return self.hashMap[key].val
        return -1        
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        self.hashMap[key] = Node(key,value)
        self.insert(self.hashMap[key])
        if len(self.hashMap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashMap[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)