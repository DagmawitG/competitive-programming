class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        
        
        def dfs(row,col,i):
            if i == len(word):
                return True
            if 0 > row or row >= rows or 0 > col or col >= cols or (row,col) in path or board[row][col] != word[i]:
                return False
            
            path.add((row,col))
            found = dfs(row+1,col,i+1) or dfs(row-1,col,i+1) or dfs(row,col+1,i+1) or dfs(row,col-1,i+1)
            
            path.remove((row,col))       
            return found
            
           
        
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c]:
                    if dfs(r,c,0):
                        return True
        return False
                
                
            
                
                
            
        
        