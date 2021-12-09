class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if (nums[i]==nums[j] and i<j):
                    count = count + 1
        return count