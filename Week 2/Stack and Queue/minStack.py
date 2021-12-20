class MinStack:
    
    def __init__(self):
        stack = []
        self.stack = stack
    

    def push(self, val: int) -> None:
        self.stack.append(val)
      
    def pop(self) -> None:
        if len(self.stack)!= 0:
            self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack)!= 0:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.stack)!= 0:
            ans = self.stack[0]
            for i in self.stack:
                if ans> i:
                    ans = i
                
           
            return ans
        
            