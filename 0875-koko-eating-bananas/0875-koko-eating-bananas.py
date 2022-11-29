class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
       
        minK= right
        
        while left <= right:
            mid = (right + left)//2
            hour = 0
            for pile in piles:
                res = math.ceil(pile/mid)
                hour += res
            
            if hour <= h:
                minK = min(minK,mid)
                right = mid - 1
            else:
                left = mid + 1
                
        return minK
                
                
                
           
            
       