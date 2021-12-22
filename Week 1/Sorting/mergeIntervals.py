class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
      
        values = [intervals[0]]
        for i in range(1,len(intervals)):
            if values[-1][1] >= intervals[i][0] :
                values[-1][1]=max(intervals[i][1],values[-1][1])
            else:
                values.append(intervals[i])
         
          
        return values