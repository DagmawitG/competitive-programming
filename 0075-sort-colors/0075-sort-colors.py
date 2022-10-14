class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0]*3
        for i in range(len(nums)):
            freq[nums[i]] += 1
        index = 0
        for j in range(len(freq)):
            count = freq[j]
            while(count):
                nums[index] = j
                index += 1
                count -= 1
        return nums
                
            
        
        