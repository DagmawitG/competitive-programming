class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        child = {}
        parent = {}
        maxArea = 0
        
        def findParent(node):
            if node != parent[node]:
                parent[node] = findParent(parent[node])
            return parent[node]

        def union(node1, node2):
            nonlocal maxArea
            parent1, parent2 = findParent(node1), findParent(node2)
            if parent1 != parent2:
                parent1,parent2 = sorted([parent1,parent2], key= lambda x:child[x])
                parent[parent1] = parent2
                child[parent2] += child[parent1]
                maxArea = max(maxArea,child[parent2])
                
                
        maxArea = 0        
        for i in range(n):
            for j in range(m):
                # p1, p2 = findParent(i), findParent(j)
                if grid[i][j] == 1:
                    x = (i, j)
                    parent[x] = x
                    child[x] = 1
                    maxArea = max(maxArea, 1)
                    
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        union(x, (i-1, j))
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        union(x, (i, j-1))
                    
        
        return maxArea
     
                   
        
        