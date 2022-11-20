class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = {i:[] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            prerequisiteMap[course].append(pre)
        visited = set()
        
        def dfs(course):
            if prerequisiteMap[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for pre in prerequisiteMap[course]:
                
                if not dfs(pre):
                    return False
           
                
            visited.remove(course)
            prerequisiteMap[course] = []
            return True
        
       
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        

        
        