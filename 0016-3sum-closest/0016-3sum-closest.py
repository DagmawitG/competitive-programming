class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        bestAbs = float('inf')
        summBest = 0
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums)-1
            
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                absVal = abs(target - summ)
                if absVal < bestAbs:
                    bestAbs = absVal
                    summBest = summ    
                
                if summ > target:
                    r -= 1
                elif summ < target:
                    l += 1
                else:
                    return summ
                
        return summBest
                
                
            
        
        
        