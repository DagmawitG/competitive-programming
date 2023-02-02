class Solution:
    def numberOfWays(self, s: str) -> int:
        result = 0
        current1, current0 = 0, 0
        total1, total0 = 0, 0
        
        for ele in s:
            if ele == '0':
                total0 += 1
            else:
                total1 += 1
        
        if s[0] == '1':
            current1 += 1
        else:
            current0 += 1
			
       
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                current0 += 1
                result += current1 * (total1 - current1)
            else:
                current1 += 1
                result += current0 * (total0 - current0)
                
        return result
        