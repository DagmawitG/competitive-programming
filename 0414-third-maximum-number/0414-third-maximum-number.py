class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        size = len(nums)
        s1 = set()
        nums.sort(reverse=True)
        for i in range(size):
            s1.add(nums[i])
            if len(s1) == 3:
                break
        if len(s1) < 3:
            return max(nums)
        else:
            return min(s1)
        