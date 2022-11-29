class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs,key=lambda x: x[1]-x[0])
        n = len(costs)//2
        costB = 0
        costA = 0
        for i in range(len(costs)):
            if i < n:
                costB += costs[i][1]
            else:
                costA += costs[i][0]
            
        return costA + costB
        
            
        
        
        
        
        ''' 0        1          2       3
         [[10,20],[30,200],[40,50],[10,20]]
         
         person 0 = min(10,20) =  10
         
         
        
        '''