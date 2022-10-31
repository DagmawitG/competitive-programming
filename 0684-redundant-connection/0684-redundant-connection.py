class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)
        
    def find(self,node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,node1,node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        if p1 == p2:
            return True
        
        if self.size[node1] > self.size[node2]:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            # print(self.parent)
            self.size[p2] += self.size[p1]
        return False
               
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint = UnionFind(1000)
        ans = None
        for edge in edges:
            if disjoint.union(edge[0],edge[1]):
                ans = edge       
        return ans
                
                
        
    
    

        
        