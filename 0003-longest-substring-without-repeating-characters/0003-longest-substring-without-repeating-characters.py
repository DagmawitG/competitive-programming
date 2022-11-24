class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        count = defaultdict(int)
        minValue = 0
      
        while l <= r and r < len(s):    
            while count[s[r]] > 0:
                count[s[l]] -= 1
                l += 1
            count[s[r]] += 1  
            minValue = max(minValue,r-l+1)
            r += 1
                    
                   
                
                
        
        return minValue
        
        
       
            