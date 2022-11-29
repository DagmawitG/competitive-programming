class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        frequency = defaultdict(int)
        for i in range(len(s) - minSize+1):
            substring = s[i:i+minSize]
            if len(set(substring)) <= maxLetters:
                frequency[substring] += 1
        
        if frequency:
            return max(frequency.values())
        
        else:
            return 0
        
        