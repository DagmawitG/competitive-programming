class Solution:
   
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        length= len(pref)
        for word in words:
            if word[:length]== pref:
                count+=1
        return count
