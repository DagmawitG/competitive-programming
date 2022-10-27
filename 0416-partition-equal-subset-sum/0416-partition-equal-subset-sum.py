class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum %2 != 0:
            return False
        memo = {}
        target = totalSum//2
        return self.helper(0,target,memo,nums)  
        
    def helper(self,index,target,memo,nums):
        if target == 0:
            return True
        if index >= len(nums) or target < 0:
            return False
        if (index,target) in memo:
            return memo[(index,target)]
        memo[(index,target)] = self.helper(index+1,target,memo,nums) or self.helper(index+1,target-nums[index],memo,nums)
        
        return memo[(index,target)]
          
        
    