class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def recur(i,total):
            if i == len(nums):
                return 1 if total==target else 0
                
            if (i,total) in memo:
                return memo[(i,total)]
            
            memo[(i,total)] = recur(i+1,total+nums[i]) + recur(i+1,total-nums[i])
            
            return memo[(i,total)]
        return recur(0,0)
           