class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                front = s[:left] + s[left+1:]
                back = s[:right] + s[right+1:]
                
                return front == front[::-1] or back == back[::-1]
               
                
            left += 1
            right -= 1
            
        return True
    
                
        