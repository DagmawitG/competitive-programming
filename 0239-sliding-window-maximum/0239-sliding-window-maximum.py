class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        dequeToUse = deque()
        result = []
        while right < len(nums):
            while dequeToUse and dequeToUse[-1] < nums[right]:
                dequeToUse.pop()
            dequeToUse.append(nums[right])
            right += 1
            
         
            if right - left == k:
                result.append(dequeToUse[0])
                if dequeToUse[0]== nums[left]:
                    dequeToUse.popleft()
                left += 1
                
           
            
        return result
        