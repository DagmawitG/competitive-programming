class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        l=r=0
        while l <= r and r < len(nums):
            if nums[l] != 1:
                l += 1
                r +=1
            else:
                r += 1
                if  r < len(nums) and nums[r]==0:
                    maxi = max(maxi,r-l)
                    l = r = r+1
                    
                
                    
        return max(maxi,r-l)
        
        
        