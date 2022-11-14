class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[len(word2) - i] * (len(word1)+1) for i in range(len(word2))]
        memo.append([len(word1) - x for x in range(len(word1) + 1)])
        for row in range(len(memo)-2,-1,-1):
            for col in range(len(memo[0])-2,-1,-1):
                if word2[row] == word1[col]:
                    memo[row][col] = memo[row+1][col+1]
                else:
                    insert = memo[row][col+1] 
                    delete = memo[row+1][col] 
                    replace = memo[row+1][col+1] 
                    memo[row][col] = 1 + min(insert,delete,replace)
        return memo[0][0]
        