class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.recur(n,0,memo)
    
    def recur(self,n,step,memo):
        if step == n:
            return 1
        if step > n:
            return 0
        if step in memo:
            return memo[step]
        else:
            memo[step] = self.recur(n,step+1,memo) + self.recur(n,step+2,memo)
            return memo[step]
        
        
        