class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0]) 
        islands = 0
        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] == '1':
                    self.dfs(row,col,grid)
                    islands += 1
                
                    
        return islands
                    
      
    def inbound(self,r,c):
        return 0 <= r < self.m and 0 <= c < self.n
    
    
    def dfs(self,row,col,grid):
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        grid[row][col] = '0'
        for x,y in direction:
            new_row = row + x
            new_col = col + y

            if self.inbound(new_row, new_col) and  grid[new_row][new_col] == '1': 
                self.dfs(new_row,new_col,grid)
                grid[new_row][new_col] = '0'
                
                
                    
                    
    
        

'''
        
  ["1","1","1","1","0"]
  ["1","1","0","1","0"]
  ["1","1","0","0","0"]
  ["0","0","0","0","0"]
    
    

    
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]

    number of islands = 3
    
    
    cases
    - if all values in the grid are 1s or if it's all a land
    - if all values are 0s, if it's only water
    - if we have 1 island 
    - islands > 1
    
    check
    - if it's inbound
    - visited
    - and the grid[m][n] == 1
    
    BFS or DFS 
    Time complexity = O(m*n)
    Space complexity = O(N) - visited dicitonary to track the visited values
    
'''
    