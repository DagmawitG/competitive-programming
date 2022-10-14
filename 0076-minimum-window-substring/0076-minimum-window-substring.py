class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        tDict,sDict = {},{}
        for i in t:
            tDict[i] = 1 + tDict.get(i,0)
        res,resLength = [-1,-1],float('inf')
        have,need = 0 ,len(t)
        l=0
        for r in range(len(s)):
            char = s[r]
            sDict[char] = 1 + sDict.get(char,0)
            if char in tDict and tDict[char] >= sDict[char]:
                have += 1
                
            while have == need:
                if(r -l+1) < resLength:
                    res=[l,r]
                    resLength = r-l+1
                sDict[s[l]] -= 1
                if s[l] in tDict and sDict[s[l]] < tDict[s[l]]:
                    have -= 1
                l += 1
        l,r = res
       
        return s[l:r+1] if resLength != float('inf') else ""
            
                    

                    
            
           
                
       
        