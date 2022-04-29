class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        maxi = 1
        l = 0
        # while r < len(prices) and l <= r:
        for r in range(1,len(prices)):
            if prices[r] == prices[r-1]-1:
                maxi += r-l+1
            else:
                l = r
                maxi += r-l+1      
        return maxi
            
           
            
                
                

            
        