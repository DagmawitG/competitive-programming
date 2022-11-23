class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        self.rows= len(heights)
        self.cols = len(heights[0])
        '''
        pacific - row - (0 - rows - 1) and col = 0
        atlantic - row - (rows -1) and col = (0,cols - 1)
        '''
        
        for r in range(self.rows):
            self.bfs(r,0,heights,pacific)
            self.bfs(r,self.cols-1,heights,atlantic)
            
        for c in range(self.cols):
            self.bfs(0,c,heights,pacific)
            self.bfs(self.rows-1,c,heights,atlantic)
            
        return pacific & atlantic
            
        
    def inbound(self,row,col):
        return 0 <= row < self.rows and 0 <= col < self.cols
        
        
    def bfs(self,r,c,heights,visited):
        queue = deque([(r,c)])
        visited.add((r,c))
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while queue:
            row,col = queue.popleft()
            for i,j in direction:
                new_row = row + i
                new_col = col + j
                if self.inbound(new_row,new_col) and (new_row,new_col) not in visited and heights[row][col] <= heights[new_row][new_col]:
                    queue.append((new_row,new_col))
                    visited.add((new_row,new_col))
                    
                
            
        
         
        
        
        
         