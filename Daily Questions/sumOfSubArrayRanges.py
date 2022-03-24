class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            minNum , maxNum = nums[i],nums[i]
            j = i
            while j < len(nums):
                minNum = min(minNum,nums[j])
                maxNum = max(maxNum,nums[j])
                ans += maxNum - minNum
                j += 1
                
        return ans