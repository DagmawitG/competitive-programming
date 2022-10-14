class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,index,high = 0,0,len(nums)-1
        while index <= high:
            if nums[index] ==0:
                nums[low],nums[index] =nums[index],nums[low]
                low += 1
                index += 1
            elif nums[index] == 2:
                nums[high],nums[index] = nums[index],nums[high]
                high -= 1
                
            else:
                index += 1
        return nums
        