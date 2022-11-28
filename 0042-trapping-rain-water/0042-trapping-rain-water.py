class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l,r = 0,len(height)-1
        left_max = height[l]
        right_max = height[r]
       
        
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max,height[l])
                result += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max,height[r])
                result += right_max - height[r]
                
           
               
        return result
                
                
   
        
        