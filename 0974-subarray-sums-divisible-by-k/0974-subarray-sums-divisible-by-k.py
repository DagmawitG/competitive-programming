class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        curr = 0
        m = {0: 1}

        for i in range(len(nums)):
            curr = (curr + nums[i] % k + k) % k
            count += m.get(curr, 0)
            m[curr] = m.get(curr, 0) + 1

        return count
        