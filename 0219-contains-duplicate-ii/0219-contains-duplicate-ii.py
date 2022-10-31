class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ansDict = {}
        for i in range(len(nums)):
            if nums[i] in ansDict:
                if abs(i-ansDict[nums[i]]) <= k:
                    return True
            ansDict[nums[i]] = i
               
        return False
        