class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        balance = True
        if(len(s) % 2 != 0):
           
            return False
        else:
            for i in range(len(s)):
                if s[i] == "(" or s[i] == "[" or s[i] =="{":
                    stack.append(s[i])
                else:
                    if (len(stack) == 0):
                        balance = False
                        break
                    elif s[i] == ")" or s[i] == "]" or s[i] == "}": 
                        val = stack[-1]
                        if((val == "[" and s[i]=="]") or (val == "(" and s[i]==")") or (val == "{" and s[i]=="}") ):
                            stack.pop()
                        else:
                            balance = False
                            break

        if(len(stack)!=0):
            balance = False
        return balance