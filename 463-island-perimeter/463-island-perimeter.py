class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        row = len(grid)
        col = len(grid[0])
        visited = set()
        side = 0
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        def dfs(r,c):
            nonlocal side
            
            for d in directions:
                
                nr = r + d[0]
                nc = c + d[1]
                if not inbound(nr,nc) or grid[nr][nc] == 0:
                    side += 1
                elif (nr,nc) not in visited:
                    visited.add((nr,nc))
                    dfs(nr,nc)
                    
                    
            return side
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    return dfs(r,c)
               
      
                
        
       
                
                
                    
                    
                
            
        
        