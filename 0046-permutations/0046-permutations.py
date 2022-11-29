class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def backtrack(current):
            if len(current) == len(nums):
                permutations.append(current.copy())
                
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                    
                current.append(nums[i])
                backtrack(current)
                current.pop()
        backtrack([])
        return permutations
        
        
        
        