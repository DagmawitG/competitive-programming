"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}
        if not node:
            return
        
        def dfs(node):
            if node in mapping:
                return mapping[node]
            
            cloned = Node(node.val)
            mapping[node] = cloned
            for neighbor in node.neighbors: 
                cloned.neighbors.append(dfs(neighbor))
                
            return cloned
        return dfs(node)
                
            
            
            
            
            
        
        