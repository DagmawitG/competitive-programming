class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        nums2 = list(range(0,n+1,1))
        ans = 0
        print(nums2)
  
        
        for i in range(len(nums2)):
            if nums2[i] not in nums:
                ans = nums2[i]
                print(ans)
            else:
                continue
        return ans
        
                
        