class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        
        result = []
        def dfs(n,number):
            if n == 0:
                result.append(number)
                return result
            
            last_digit = number % 10
            nextDigits = set([last_digit+k,last_digit-k])
            for next_number in nextDigits:
                if 0 <= next_number <= 9:
                    dfs(n-1,number*10+next_number)
                    
        for number in range(1,10):
            dfs(n-1,number)
        return result

            
            
            
        