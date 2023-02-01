class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        bloom = sorted(zip(growTime, plantTime), reverse=True)

        bloomTime = 0
        result = 0
    
        for growT, plantT in bloom:
            bloomTime += plantT
            result = max(result, bloomTime + growT)

        return result