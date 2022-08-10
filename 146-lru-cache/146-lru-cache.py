class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self. prev = self.next = None
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapCache = {}
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right,self.left
    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev    
    def insert(self,node):
        prev = self.right.prev
        last = self.right
        prev.next = node
        last.prev = node
        node.prev = prev
        node.next = last
    def get(self, key: int) -> int:
        if key in self.mapCache:
            self.remove(self.mapCache[key])
            self.insert(self.mapCache[key])
            return self.mapCache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.mapCache:
            self.remove(self.mapCache[key])
        self.mapCache[key] = Node(key,value)
        self.insert(self.mapCache[key])
          
        if self.capacity < len(self.mapCache): 
            i = self.left.next
            self.remove(i)
            del self.mapCache[i.key]
            
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)