class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        arr = [] * (len(nums))
        val = n/3
        counts = Counter(nums)
        for key,value in counts.items():
            if value > val:
                arr.append(key)
        return arr