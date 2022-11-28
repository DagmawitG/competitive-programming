class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        outdegree = {i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            outdegree[pre].append(crs)
            indegree[crs] += 1
       
        queue = []
        count = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            course = queue.pop()
            count += 1
            for prerequisites in outdegree[course]:
                indegree[prerequisites] -= 1
                if indegree[prerequisites] == 0:
                    queue.append(prerequisites)
                    
        return count == numCourses
                    
                
                
                
            
       
        
                
       
        