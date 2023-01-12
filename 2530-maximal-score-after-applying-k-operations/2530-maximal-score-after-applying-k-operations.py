class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        scoreHeap = []
        ans = 0
        for num in nums:
            heapq.heappush(scoreHeap, -num)
        
        for i in range(k):
            num = -heapq.heappop(scoreHeap)
            ans += num
            num = (num+2)//3
            heapq.heappush(scoreHeap, -num)
        return ans
            
        
        