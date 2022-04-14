class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        child = [1] * n
        parent = list(range(n))
        
        def findParent(node):
            if node != parent[node]:
                parent[node] = findParent(parent[node])
            return parent[node]

        def union(node1, node2):
            parent1, parent2 = findParent(node1), findParent(node2)
            if parent1 != parent2:
                parent1,parent2 = sorted([parent1,parent2], key= lambda x:child[x])
                parent[parent1] = parent2
                child[parent2] += child[parent1]
        
        for i in range(n):
            for j in range(n):
                p1, p2 = findParent(i), findParent(j)
                if i != j and (isConnected[i][j] or p1 == p2):
                    union(i,j)
                    
        result = set(parent)
        return len(result)