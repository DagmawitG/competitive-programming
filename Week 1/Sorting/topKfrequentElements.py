class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_keys = sorted(count, key=count.get)
        return sorted_keys[-k:]