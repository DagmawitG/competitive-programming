class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)
        if len(sets) == len(nums): return False
        else: return True
        