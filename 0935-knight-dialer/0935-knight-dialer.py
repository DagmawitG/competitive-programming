class Solution:
    def __init__(self):
        self.matrix = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.inValidRC = set([(3,0),(3,2)])
        
    def validMoves(self,row,col):
        direction = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(-1,-2),(1,-2)]
        validJumps = [] 
        for r,c in direction:
            new_row = row + r
            new_col = col + c
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and (new_row,new_col) not in self.inValidRC:
                validJumps.append((new_row,new_col))
        return validJumps
                
    def recursionKnightDialer(self,row,col,n,cache):
        distinctNumber = 0
        if n == 0:
            return 1
        
        if (row,col,n) in cache:
            return cache[(row,col,n)]
        
        for (new_row,new_col) in self.validMoves(row,col):
            distinctNumber += self.recursionKnightDialer(new_row,new_col,n-1,cache)
            
        cache[(row,col,n)] = distinctNumber
        return cache[(row,col,n)]
        
                                          
    def knightDialer(self, n: int) -> int:      
        distinctNumber = 0
        if n == 0:
            return distinctNumber
        cache = {}
        for row in range(self.rows):
            for col in range(self.cols):
                if (row,col) not in self.inValidRC:
                    distinctNumber += self.recursionKnightDialer(row,col,n-1,cache)
        return distinctNumber % (10**9 + 7)
        
        
        