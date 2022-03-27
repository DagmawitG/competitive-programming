class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) %2 == 1:
            return False
        minS, maxS = 0 , 0 
      
        for i in range(len(s)):
            if  locked[i] == "1" :
                if s[i] == "(" :
                    minS += 1
                    maxS += 1
                else:
                    if(maxS < 1):
                        return False
                    maxS-=1
                    if(minS > 0):
                        minS-= 1
            else:
                maxS+=1
                if(minS > 0):
                    minS -=1
             
        if minS == 0:
            return True
        return False
        
       