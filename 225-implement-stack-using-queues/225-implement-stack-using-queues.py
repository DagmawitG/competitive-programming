class MyStack:

    def __init__(self):
        self.queue1 = []
        
    def push(self, x: int) -> None:
        self.queue1.append(x)
        
    def pop(self) -> int:
        top = self.queue1[-1]
        self.queue1 = self.queue1[:-1]
        return top
             
    def top(self) -> int:
        if self.empty()== False:
            return self.queue1[-1]
        

    def empty(self) -> bool:
        if len(self.queue1)== 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()