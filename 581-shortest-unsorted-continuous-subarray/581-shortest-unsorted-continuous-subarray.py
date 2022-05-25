class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right, maxVal = -1, float("-inf")
        for i in range(len(nums)):
            if nums[i] >= maxVal: maxVal = nums[i]
            else: right = i
        left, minVal = len(nums), float("inf")
        #Find Min Index
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= minVal: minVal = nums[i]
            else: left = i
        return 0 if left>right else right-left+1
            
        