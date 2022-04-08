class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        outDegree = defaultdict(list)
        queue = []
        count = 0
       
        for a,b in prerequisites:
            outDegree[b].append(a)
            inDegree[a] += 1
             
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
       
        while queue:
            a = queue.pop()
            count += 1
            for j in outDegree[a]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    queue.append(j)
        return count == numCourses
            
            
            
        
        