class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = 0
        mini = float('inf')
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                mini = min(nums[i], mini)
                res = max(nums[i + 1] - mini, res)
        if res > 0:
            return res
        else:
            return -1
        

        