class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        res = []
        # timePoints.sort()
        # print(timePoints)
        for i in range(len(timePoints)):
            hrToMin = 0
            minu = 0
           
            time =(int(timePoints[i][:2]) * 60) + int(timePoints[i][3:])
            res.append(time)
        res.sort()
        ans = 1440 + (res[0] - res[-1])
        for i in range(1,len(res)):
            ans = min(ans,res[i] - res[i-1])
        return ans
            
            
            
       
        
                
            
                
            
            
#             for j in range(i+1,len(timePoints)):
                
#                 timeDiff = 0
#                 hrToMin = 0
#                 if timePoints[i][:2] == '00' and timePoints[j][:2] == '00':
#                     hrToMin = 0
#                 else:
#                     hrToMin = int(timePoints)

#                 if timePoints[i][3:] == '00' and timePoints[j][3:] == '00':
#                     timeDiff = 0 + hrToMin 
               
#                 timeDiff = (hrToMin + (int(timePoints[j][3:]) - int(timePoints[i][3:]))) 
#                 res.append(abs(timeDiff))
                
               
           
            
        # return min(res)
                
            
            
     