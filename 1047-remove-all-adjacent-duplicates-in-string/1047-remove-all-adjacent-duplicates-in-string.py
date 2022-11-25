class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char,1])
            
            if stack[-1][1] == 2:
                stack.pop()
                
        result = ''
        for letter in stack:
            result += letter[0]
        return result
                
        