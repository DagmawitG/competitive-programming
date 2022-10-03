class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i,val in enumerate(nums):
            dif = target - val
            if dif in mapping:
                return [mapping[dif],i]
            mapping[val]=i
        return
        
        