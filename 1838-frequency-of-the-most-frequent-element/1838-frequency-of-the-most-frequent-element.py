class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=r=0
        ans=total=0
        while r < len(nums):
            total += nums[r]
            while(nums[r]) *(r-l+1) > total + k:
                total -= nums[l]
                l += 1 
            ans = max(ans,r-l+1)
            r += 1
        return ans
                
                
            
           
                
        
        
        
        