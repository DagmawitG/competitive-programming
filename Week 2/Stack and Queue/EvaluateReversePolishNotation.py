class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expressions = "+-*/"
        for i in tokens:
            if (i not in expressions ):
                stack.append(int(i))
            else:
                n = stack.pop()
                m = stack.pop()
                if i=="+":
                    stack.append(m+n)
                elif i=="-":
                    stack.append(m-n)
                elif i=="*":
                    stack.append(m*n)
                elif i=="/":
                    stack.append(int(m/n))
                    
                
        return stack[0]
            
       
        
        
        