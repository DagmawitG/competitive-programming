class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row,col = len(matrix[0]),len(matrix)
        
        result = []
        for i in range(row):
            result.append([])
            
            for j in range(col):
                result[-1].append(matrix[j][i])

        return result
   
        