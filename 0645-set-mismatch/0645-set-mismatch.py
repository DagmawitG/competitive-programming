class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        numSet = set(nums)
        dictionary = Counter(nums)
        for key,val in dictionary.items():
            if val == 2:
                result.append(key)
        for i in range(1,len(nums)+1):
            if i not in numSet:
                result.append(i)
        return result
           
        