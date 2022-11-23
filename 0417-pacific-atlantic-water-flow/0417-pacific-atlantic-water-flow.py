class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        self.rows= len(heights)
        self.cols = len(heights[0])
        
        for r in range(self.rows):
            self.dfs(r,0,heights,pacific)
            self.dfs(r,self.cols-1,heights,atlantic)
            
        for c in range(self.cols):
            self.dfs(0,c,heights,pacific)
            self.dfs(self.rows-1,c,heights,atlantic)
            
        return pacific & atlantic
            
        
    def inbound(self,row,col):
        return 0 <= row < self.rows and 0 <= col < self.cols
        
        
    def dfs(self,row,col,heights,visited):
        visited.add((row,col))
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        
       
        for i,j in direction:
            new_row = row + i
            new_col = col + j
            if self.inbound(new_row,new_col) and (new_row,new_col) not in visited and heights[row][col] <= heights[new_row][new_col]:
                self.dfs(new_row,new_col,heights,visited)
                visited.add((new_row,new_col))

                
            
        
         
        
        
        
         