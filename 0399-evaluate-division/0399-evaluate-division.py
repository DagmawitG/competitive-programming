class Solution:         
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = {}
        
        def buildGraph(equations,values):
        
            def addEdges(first,second,value):
                if first in graph:
                    graph[first].append((second,value)) 
                else:
                    graph[first] = [(second,value)]
           
            for equation,value in zip(equations,values):
                first, second = equation
                addEdges(first,second,value)
                addEdges(second,first,1/value)
            
        def evaluateDivision(query):    
            value1,value2 = query
            if value1 not in graph or value2 not in graph:
                return -1.0
            queue = deque([(value1,1.0)])
            visited = set()
            
            while queue:
                value, product = queue.popleft()
                if value == value2:
                    return product
                
                visited.add(value)
                for second, val in graph[value]:
                    if second not in visited:
                        queue.append((second,product*val))
            return -1.0
                        
        result = []
        buildGraph(equations,values)
        for query in queries:
            result.append(evaluateDivision(query))
        return result
            
                        

              
        
        
       
       
        
        
        
        
        