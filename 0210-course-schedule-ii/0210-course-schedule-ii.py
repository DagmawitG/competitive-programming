class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        outdegree = {i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            outdegree[pre].append(crs)
            indegree[crs] += 1
       
        queue = []
       
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        result = [] 
        count = 0
        while queue:
            course = queue.pop()
            result.append(course)
            count += 1
            for prerequisites in outdegree[course]:
                indegree[prerequisites] -= 1
                if indegree[prerequisites] == 0:
                    queue.append(prerequisites)
                    
        if count == numCourses:
            return result
        else:
            return []
                    
        