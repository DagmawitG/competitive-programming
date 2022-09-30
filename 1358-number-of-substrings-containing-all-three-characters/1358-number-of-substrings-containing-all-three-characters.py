class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = a = b = c= 0
        l = 0
        n = len(s)
        for r in range(len(s)):
            if s[r]=='a': 
                a+=1
            elif s[r]=='b': 
                b+=1
            else: 
                c += 1
            while a>0 and b > 0 and c>0:
                res += n - r
                if s[l]=='a': 
                    a -= 1
                elif s[l]== 'b':
                    b -= 1
                else: 
                    c -= 1
                l += 1
        return res
            
            
        
    
        