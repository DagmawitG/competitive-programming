class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row =  len(grid)
        col = len(grid[0])
        direction = ((0,1),(0,-1),(1,0),(-1,0))
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        visited = set()
        islands = 0
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                for x,y in direction:
                    nr = row + x
                    nc = col + y
                    if (inbound(nr,nc)) and (grid[nr][nc] == '1') and ((nr,nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                
               
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
                
                
                    
                    
                    
                 
                
            
            
            
        