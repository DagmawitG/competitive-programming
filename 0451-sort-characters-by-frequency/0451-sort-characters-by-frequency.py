class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        
        heap = []
        for key in counter:
            heapq.heappush(heap,(-counter[key],key))
            
        heapq.heapify(heap)
        
        while heap:
            value = heapq.heappop(heap)
            ans += -(value[0]) * value[1]
            
        return ans
        
        
        