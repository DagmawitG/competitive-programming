class Solution:
    def decodeString(self, s: str) -> str:
       
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                subString = ''
                while stack[-1] != '[':
                    subString = stack.pop() + subString
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                res = subString * int(k)
                stack.append(res)
                
        return ''.join(stack)

                    
                    
                
        