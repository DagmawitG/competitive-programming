class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        dpList = [[0]*(n) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dpList[i][j] = 1
                else:
                    dpList[i][j] = dpList[i-1][j] + dpList[i][j-1]
        return dpList[-1][-1]
        
        