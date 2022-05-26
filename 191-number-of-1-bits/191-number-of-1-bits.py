class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n >0:
            if n & 1:
                count += 1
            n >>= 1
        return count
                
        
#         binary = format(n,"b")
       
#         count = 0
#         for i in range(len(str(binary))):
#             if binary[i]=="1":
#                 count += 1
        
#         return count


            
        
        
        
        