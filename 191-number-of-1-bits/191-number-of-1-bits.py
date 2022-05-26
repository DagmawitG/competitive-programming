class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = format(n,"b")
        strr = str(binary)
        count = 0
        for i in range(len(strr)):
            if strr[i]=="1":
                count += 1
        
        return count

            
        
        
        
        