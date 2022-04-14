class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        child = [1] * n
        parent = list(range(n))
        
        def findParent(node):
            if node != parent[node]:
                return findParent(parent[node])
            return node

        def union(node1,node2):
            parent1 = findParent(node1)
            parent2 = findParent(node2)
            if parent1 != parent2:
                
                parent1,parent2 = sorted([parent1,parent2], key= lambda x:child[x])
                parent[parent1] = parent2
                child[parent2] += child[parent1]
                child[parent1] = 0
                
                
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]==1:
                    union(i,j)
                    # print(child)
        result = 0
        for c in child:
            result += int(bool(c))
        return result
                
            
            
                
        

        
        # visited = set()
        # province = 0
        # def dfs(city):
        #     visited.add(city)
        #     for i in range(len(isConnected[city])):
        #         if isConnected[city][i] == 1 and i not in visited:
        #             dfs(i)
        # for i in range(len(isConnected)):
        #     if i not in visited:
        #         dfs(i)
        #         province += 1
        # return province
        
                
            
            
        