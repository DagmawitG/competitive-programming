class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missed = 0
        each = len(nums)
        for i in range(len(nums)):
            missed ^= i
            each ^= nums[i]
        return missed ^ each
            
        
        