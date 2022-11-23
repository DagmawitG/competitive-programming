# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = [] 
        def bfs(node):
            if not node:
                    return
            queue = deque([node])
            
            while queue:
                temp = []
                for _ in range(len(queue)):
                    
                    node = queue.popleft()
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                        
                    
                result.append(temp)
        bfs(root)
        
        for i in range(1,len(result),2):
            result[i].reverse()
        return result

            
            
        