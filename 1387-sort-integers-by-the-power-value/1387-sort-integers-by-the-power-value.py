class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1:1}
        
        def recursion(n):
            if n in cache:
                return cache[n]
            else:
                if n % 2 == 0:
                    cache[n] = 1 + recursion(n//2)
                else:
                    cache[n] = 1 + recursion(3*n+1)
                    
                return cache[n]
        ans = []   
        for i in range(lo,hi+1):
            ans.append(i)
            # recursion(i)
            
        ans.sort(key=lambda x:recursion(x))
        return ans[k-1]
        
      
        