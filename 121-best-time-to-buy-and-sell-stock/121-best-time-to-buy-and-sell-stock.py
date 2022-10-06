class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            maximum = max(maximum,prices[i]-minPrice)
            if minPrice > prices[i]:
                minPrice = prices[i]
        return maximum
        
        