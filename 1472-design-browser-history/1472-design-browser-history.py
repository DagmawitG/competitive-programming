class BrowserHistory:
    def __init__(self, homepage: str):
        self.backward = [homepage]
        self.front = []
       
    def visit(self, url: str) -> None:
        self.backward.append(url)
        self.front = []
    def back(self, steps: int) -> str:
        while len(self.backward) > 1 and steps > 0:
            self.front.append(self.backward.pop())
            steps -= 1
        return self.backward[-1]
    def forward(self, steps: int) -> str:
        
        while len(self.front) > 0 and steps > 0:
            self.backward.append(self.front.pop())
            steps -= 1
        return self.backward[-1] 
            


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)