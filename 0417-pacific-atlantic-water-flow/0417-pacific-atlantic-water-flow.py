class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        result = []
        
        pacific = set()
        atlantic = set()
        
       
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        
        def bfs(r,c,visited):
            queue = deque([(r,c)])
            visited.add((r,c))
            while queue:
                r,c = queue.popleft()
                for x,y in direction:
                    nr = r+x 
                    nc = c + y
                    if inbound(nr,nc) and heights[r][c] <= heights[nr][nc] and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        
                        
        for r in range(row):     
            bfs(r,0,pacific)
            bfs(r,col-1,atlantic)
        for c in range(col):
            bfs(0,c,pacific)
            bfs(row-1,c,atlantic)
            
        return pacific & atlantic
                    
            
                    
            
            
            
            
       
        
        
        
        
        
       