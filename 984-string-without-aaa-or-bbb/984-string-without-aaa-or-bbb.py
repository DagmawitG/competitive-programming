class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
       
        while a or b:
            checkA = False
            if len(res) >= 2 and res[-1] == res[-2]:
                if res[-1] == 'b':
                    checkA = True
            else:
                if a >= b:
                    checkA = True
            if checkA:
                a -= 1
                res.append('a')
            else:
                b -= 1
                res.append('b')
        return ''.join(res)
                
                
                    
                
        