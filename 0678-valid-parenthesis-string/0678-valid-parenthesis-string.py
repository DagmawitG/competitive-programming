class Solution:
    def checkValidString(self, s: str) -> bool: 
        left_paranthesis = []  
        star = []              
        for i in range(len(s)):
            if s[i] == "(":                
                left_paranthesis.append(i)
            elif s[i] == "*":
                star.append(i)
            elif s[i] == ")":              
                if left_paranthesis:        
                    left_paranthesis.pop()
                elif star:               
                    star.pop()
                else:
                    return False          
        while left_paranthesis:          
            if not star:
                break
            elif star[-1] > left_paranthesis[-1]:
                star.pop()
                left_paranthesis.pop()
            elif star[-1] < left_paranthesis[-1]:
                break
                
        while left_paranthesis and star:
            if left_paranthesis[-1] < star[-1]:
                left_paranthesis.pop()
                star.pop()
            else:
                break
        
        return not left_paranthesis

        