class Solution:
    def isSafe(self,i,j,board,n):
        if i == 0:
            return True
        #Checking for left diagnol 
        
        temp1 = i - 1
        temp2 = j - 1
        
        while temp1 >= 0 and temp2 >= 0:
            if board[temp1][temp2] == 'Q':
                return False
            temp1 -= 1
            temp2 -= 1
        
        #Checking for right diagnol
        
        temp1 = i - 1
        temp2 = j + 1
        
        while temp1 >= 0 and temp2 < n:
            if board[temp1][temp2] == "Q":
                return False
            temp1 -= 1
            temp2 += 1
            
            
        #Checking for upside
        
        while i >= 0:
            if board[i-1][j] == "Q":
                return False 
            i -= 1
            
        return True
            
            
            
    def solveNQueensHelper(self,n,i,board,ans):
        if i == n:
            temp = []
            for i in range(n):
                tempans = ''
                for j in range(n):
                    tempans += board[i][j]
                temp.append(tempans)
            ans.append(temp)
            
#             print(board)
            return

        

        for j in range(n):
            if self.isSafe(i,j,board,n):
                board[i][j] = "Q"
                self.solveNQueensHelper(n,i+1,board,ans)
                board[i][j] = "."
        return
        
        
        
    
    def solveNQueens(self, n):
        board = [['.' for i in range(n)] for j in range(n)]
        ans = []
        self.solveNQueensHelper(n,0,board,ans)
        # print(ans)
        return ans
        