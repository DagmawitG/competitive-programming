class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        
       
        prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
               
                prefix_sum[i][j] = mat[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
        
        res = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                
                r1, r2 = max(0, i - k) + 1, min(n - 1, i + k) + 1
                c1, c2 = max(0, j - k) + 1, min(m - 1, j + k) + 1
                
                res[i][j] = prefix_sum[r2][c2] - prefix_sum[r1 - 1][c2] - prefix_sum[r2][c1 - 1] + prefix_sum[r1 - 1][c1 - 1]
        
        return res
