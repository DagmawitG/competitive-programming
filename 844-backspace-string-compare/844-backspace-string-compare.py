class Solution:
   
    
    def stacks(self,s):
        stack = []
        for i in s:
            if i != '#' :
                stack.append(i)
            elif stack:
                stack.pop()
        return stack
    def backspaceCompare(self, s: str, t: str) -> bool:
        x = self.stacks(s)
        y = self.stacks(t)
        return x==y
    