# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        return self.bfs(root)
        
    def bfs(self,node):
        queue = deque([node])
        result = []
        while queue:
            tempList = []
            
            for i in range(len(queue)): 
                item = queue.popleft()
                tempList.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
               
                    
            result.append(tempList)
        return result
            
        
        
       
        