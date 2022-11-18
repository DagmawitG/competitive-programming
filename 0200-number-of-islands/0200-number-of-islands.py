class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        def isValid(r,c):
            return 0 <= r < row and 0 <= c < col
        
        def bfs(r,c):
            queue = deque([])
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                i,j = queue.popleft()
                for x,y in direction:
                    nr = i + x
                    nc = j + y
                    if isValid(nr,nc) and grid[nr][nc] == '1' and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
        
        islands = 0                
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
                
        return islands
                    
                    
        
                
            
            
        
       
                    
                    
                 
                
            
            
            
        