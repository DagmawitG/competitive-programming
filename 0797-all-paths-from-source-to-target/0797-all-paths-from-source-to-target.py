class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start = 0
        target = len(graph)-1
        queue = deque([(start,[start])])
        result = []
        while queue:
            current, path = queue.popleft()
            if current == target:
                result.append(path)
                
            for node in graph[current]:
                queue.append((node,path+[node]))
        return result
       
                
        
        
        
        
        
        