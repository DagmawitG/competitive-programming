class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for l in range(len(nums)-1):
            r = l + 1
            while(r<len(nums)):
                if nums[l] + nums[r] == target:
                    return [l,r]
                r += 1
        
        
                    