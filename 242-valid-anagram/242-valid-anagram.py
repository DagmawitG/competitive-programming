class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = Counter(s)
        dictT = Counter(t)
        return dictS == dictT
        