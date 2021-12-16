class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = nums[0]+nums[-1]
        i = 0
        j = len(nums)-1
        while(i<j):
            
            val = nums[i] + nums[j]
            result = max(val,result)

            i += 1
            j -= 1
        return result