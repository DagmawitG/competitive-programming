class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        start = 0
        target = len(graph)-1
        stack = [(start,[start])]
        result = []
        while stack:
            current, path = stack.pop()
            if current == target:
                result.append(path)     
            for node in graph[current]:
                stack.append((node,path + [node]))
                
        return result
                
                
        
        
        