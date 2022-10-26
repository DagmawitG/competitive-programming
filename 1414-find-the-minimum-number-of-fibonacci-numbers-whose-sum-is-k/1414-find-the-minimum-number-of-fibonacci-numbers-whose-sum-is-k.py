class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [0, 1]  
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        i = len(fib)-1
        count = 0
        while k > 0: 
            if k >= fib[i]: 
                count += 1
                k -= fib[i]
            i -= 1
        return count