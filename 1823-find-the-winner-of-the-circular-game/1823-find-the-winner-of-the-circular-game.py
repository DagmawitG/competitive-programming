class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1,n+1)]
        return self.recur(nums,1,0,k)
        
        
    def recur(self,nums,cnt,i,k):
        if len(nums)==1:
            return nums[0]
        
        if cnt == k:
            nums.pop(i)
            cnt = 1
        else:
            cnt += 1
            i += 1
        
        if i == len(nums):
            i = 0
        return self.recur(nums,cnt,i,k)

            
            
            
    