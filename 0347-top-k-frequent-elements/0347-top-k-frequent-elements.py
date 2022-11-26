class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        print(counter)
            
        heap = []
        for key in counter:
            heapq.heappush(heap,((-counter[key],key)))
        heapq.heapify(heap)
        
        answer = []    
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer
            
            
        