class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        maxSum = float('-inf')
        windowSum = 0.0
        for right in range(len(nums)): 
            
            windowSum += nums[right]
            if right >= k-1:
                maxSum = max(windowSum, maxSum)
                windowSum -= nums[left]
                left += 1
        return maxSum/k
                
            
            
            
    
   
            
        
        