class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sTOt = {}
        tTOs = {}
        for i in range(len(s)):
            charS,charT = s[i],t[i]
            if (charS in sTOt and sTOt[charS] != charT) or (charT in tTOs and tTOs[charT] != charS):
                return False
            sTOt[charS] = charT
            tTOs[charT] = charS
        return True
            
                

        