class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        n = len(s1)
        left = 0
        right = n-1
        while left <= right and right < len(s2):
            count2 = Counter(s2[left:right+1])
           
            if count1 == count2:
                return True
            left  += 1
            right += 1
        return False
            
        