class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        def isValid(r,c):
            return 0 <= r < row and 0 <= c < col
        
        def dfs(r,c):
            grid[r][c]='0'
            for x,y in direction:
                nr = r + x
                nc = c + y
                if isValid(nr,nc) and grid[nr][nc] == '1':
                    dfs(nr,nc)
                    grid[nr][nc]='0'
                         
                    
        
        islands = 0                
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
                
        return islands
                    
                    
        
                
            
            
        
       
                    
                    
                 
                
            
            
            
        