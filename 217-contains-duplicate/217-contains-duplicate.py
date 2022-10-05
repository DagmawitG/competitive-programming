class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set()
        for val in nums:
            if val in sets:return True
            else: sets.add(val)
        return False
                

        
        
        