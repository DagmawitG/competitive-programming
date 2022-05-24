class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count = 0
        stack = [-1]
        for i,e in enumerate(s):
            if e == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                   
                    
                    count = max(i-stack[-1],count)
                
        return count
        