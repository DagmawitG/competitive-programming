"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloneMap = {}
        if not node:
            return  
        visited = set()
        
        def bfs(node):
            queue = deque([(node)])
            while queue:
                cur = queue.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                if cur not in cloneMap :
                    cloneMap[cur] = Node(cur.val)
                    
                for neighbor in cur.neighbors:
                    if neighbor not in cloneMap:
                        cloneMap[neighbor] = Node(neighbor.val)
                    cloneMap[cur].neighbors.append(cloneMap[neighbor])
                    queue.append(neighbor)
                    
            return cloneMap[node]
           
        return bfs(node)            
        
                    
        
     
        