class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        ans = 0
        dictionary = defaultdict(int)
        while l <= r and r < len(s):
            while dictionary[s[r]] > 0:
                dictionary[s[l]] -= 1
                l += 1  
            dictionary[s[r]] += 1
            ans = max(ans,r-l+1)
            r += 1       
        return ans
                
                    
                    
                
            