class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)-1):
            
            if(nums[i] == nums[i+1]):
                nums[i+1] += 1
                count += 1
            elif(nums[i] > nums[i+1]):
                res = (nums[i] - nums[i+1]) + 1
                nums[i+1] += res
                count += res
            
      
                
        return count
                
        