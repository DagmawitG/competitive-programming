class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            
            if ''.join(stack[-len(part):])  == part :
                count = 0
                while stack and count < len(part):
                    stack.pop()
                    count += 1
        return ''.join(stack)
                    
            
        