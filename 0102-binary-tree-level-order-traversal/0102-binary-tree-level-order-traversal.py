# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result  = []
        def bfs(node):
            if not node:
                return []
            queue = deque()
            queue.append(node)
            while queue: 
                t = []
                for i in range(len(queue)):
                    temp = queue.popleft()
                    t.append(temp.val)
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
                result.append(t)
               
            return result 
        return bfs(root)
    
                    
                    
                
        
        
        