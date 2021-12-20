class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        intMap = map(int, nums)
        intList = list(intMap)
        intList.sort()
        return str(intList[-k])