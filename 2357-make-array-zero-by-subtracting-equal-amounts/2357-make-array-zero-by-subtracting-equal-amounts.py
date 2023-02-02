class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nonDuplicate = set()
        for num in nums:
            if num != 0:
                nonDuplicate.add(num)
                
        return len(nonDuplicate)
        