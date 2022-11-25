class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary = Counter(s)
        for i,ch in enumerate(s):
            if dictionary[ch] == 1:
                return i
        return -1
        