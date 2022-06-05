class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set() #Checking that only one queen is in a column

        posDiag = set() #Positive Diagnol defined as (row + column)
        negDiag = set() #Negative Diagnol defined as (row - column)
        
        res = 0 #Empty variable for result
        
        def backtrack(r):
            if r == n: #Looking to see if the board is valid
                nonlocal res
                res += 1 #Incrementing result by one
                return
            
            for c in range(n): #If there are more valid boards then loop through diags
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                    
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                    
                backtrack(r + 1)
                
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res
        