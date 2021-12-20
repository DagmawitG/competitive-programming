class MyCircularDeque:
    
    def __init__(self, k: int):
        self.circularDeque = []*k
        self.k = k
        

    def insertFront(self, value: int) -> bool:
        if(self.isFull()== False):
            self.circularDeque.insert(0,value)
            return True
        return False
        
            
      
    def insertLast(self, value: int) -> bool:
        if(self.isFull()== False):
            self.circularDeque.append(value)
            return True
        return False
        

    def deleteFront(self) -> bool:
        if(self.isEmpty()== False):
           
            self.circularDeque.pop(0)
            return True
        return False
        

    def deleteLast(self) -> bool:
        if(self.isEmpty()== False):
            
            self.circularDeque.pop()
            return True
        return False
        

    def getFront(self) -> int:
        if(self.isEmpty()== False):
            return self.circularDeque[0]
        return -1
        

    def getRear(self) -> int:
        if(self.isEmpty()== False):
            return self.circularDeque[-1]
        return -1
        

    def isEmpty(self) -> bool:
        if(len(self.circularDeque)):
            return False
        return True
        

    def isFull(self) -> bool:
       
        if(len(self.circularDeque) == self.k):
           
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()