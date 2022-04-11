class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ = 0
        result = 0
        sumDict = {0:1}
        for i in range(len(nums)):
            summ += nums[i]
            dif = summ - k
            result += sumDict.get(dif,0)
            sumDict[summ] = sumDict.get(summ,0) + 1
        return result
            
            
        