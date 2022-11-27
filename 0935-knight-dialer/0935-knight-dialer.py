class Solution:

    
    def __init__(self):
        self.mat = [[1, 2, 3], [4,5,6], [7,8,9], ['*', 0, '#']]
        self.nrows = len(self.mat)
        self.ncols = len(self.mat[0])
        self.in_valid = set([(3,0), (3,2)])
    
    def valid_jumps(self, row, col):
        valid = []
        for r_inc, c_inc in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1,-2), (-1, -2)]:
            n_row, n_col = row + r_inc, col + c_inc
            if 0<= n_row < self.nrows and 0 <= n_col < self.ncols and (n_row, n_col) not in self.in_valid:
                valid.append((n_row, n_col))
        return valid
    
    def recursive_dialer(self, row, col, jumps, cache):
        if jumps == 0: return 1
        if (row,col, jumps) in cache: return cache[(row, col, jumps)]
        max_number = 0
        
        for n_row, n_col in self.valid_jumps(row, col):
            ret = self.recursive_dialer(n_row, n_col, jumps-1, cache)
            max_number += ret
        
        cache[(row, col, jumps)] = max_number
        
        return cache[(row, col, jumps)]
    
    def knightDialer(self, n: int) -> int:
        max_number = 0
        if n == 0: return max_number
        cache = {}
        
        for row in range(self.nrows):
            for col in range(self.ncols):
                if (row, col) not in self.in_valid:
                    max_number += self.recursive_dialer(row, col, n-1, cache)
        
        return max_number % (10**9 + 7)