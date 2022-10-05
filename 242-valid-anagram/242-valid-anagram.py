class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS = {}
        dictT = {}
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i],0)
            dictT[t[i]] = 1 + dictT.get(t[i],0)
        for ch in dictS:
            if dictS[ch] != dictT.get(ch,0):
                return False
        return True
            
        
        