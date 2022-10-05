class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        
        prod = float('-inf')
        while(l<=r):
            ans = 0
            if height[l] > height[r]:
                ans = (r-l)*height[r]
                r -= 1
            else:
                ans = (r-l)*height[l]
                l += 1
                
            prod = max(prod,ans)
        return prod
            

        