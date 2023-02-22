class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans=zeros=0
        for i in range(len(s)):
            zeros+=1 if s[i] == '0' else 0
            
            if s[i] == '1' and zeros:
                ans=max(ans+1,zeros)
        return ans
        