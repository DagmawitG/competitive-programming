class MyQueue:
    
    def __init__(self):
        queue = []
        self.queue = queue
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        if(self.empty() == False):
            return self.queue.pop(0)
        

    def peek(self) -> int:
         if(self.empty() == False):
            return self.queue[0]
        
        

    def empty(self) -> bool:
        if(len(self.queue)):
            return False
        return True
        

