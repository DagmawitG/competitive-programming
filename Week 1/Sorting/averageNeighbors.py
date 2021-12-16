class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)-1,1):
            prev = i-1
            nextIndex = i + 1
            if(nums[prev] < nums[i] and nums[nextIndex] > nums[i]):
                nums[i],nums[nextIndex] = nums[nextIndex],nums[i]
        return nums