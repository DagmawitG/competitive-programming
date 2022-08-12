class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        l = 0
        r = len(nums)
        while l < r:
            mid = l +(r-l)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if l < len(nums) and nums[l] == target:
            result[0] = l
            
        l = 0
        r = len(nums)
        while l < r:
            mid = l +(r-l)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        if 0 <= r-1 < len(nums) and nums[r-1] == target:
            result[1] = r-1
        return result
            
                
                
            
                    
        
        