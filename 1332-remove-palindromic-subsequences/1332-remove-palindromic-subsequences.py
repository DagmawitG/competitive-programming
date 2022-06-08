class Solution:
    def checkPalindrome(self,s):
            i=0
            j=len(s)-1
            check = False
            while i <= j:
                if s[i] != s[j]:
                    check= False
                    break
                else:
                    check = True
                i += 1
                j -= 1
            return check
    def removePalindromeSub(self, s: str) -> int:
       
        if self.checkPalindrome(s):
            return 1
        else:
            return 2
            
        
        
       
                
        