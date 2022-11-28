class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n
        
        max_left[0] = 0
        max_right[n-1] = 0
        
        for i in range(1,n):
            max_left[i] = max(max_left[i-1],height[i-1])
            
        for j in range(n-2,-1,-1):
            max_right[j] = max(max_right[j+1],height[j+1])
            
        for i in range(n):
            max_trapping = min(max_left[i],max_right[i]) - height[i]
            if max_trapping > 0:
                result += max_trapping
        return result
            
        
            
        
        