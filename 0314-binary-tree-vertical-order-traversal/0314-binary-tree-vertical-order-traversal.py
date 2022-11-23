# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnDictionary = {}
        def bfs(node):    
            queue = deque([(node,0)])
            while queue:
                node, col = queue.popleft()
                if node:
                    if col in columnDictionary:
                        columnDictionary[col].append(node.val)
                    else:
                        columnDictionary[col] = [node.val]
                    if node.left:
                        queue.append((node.left, col-1))
                    if node.right:
                        queue.append((node.right, col+1))

        bfs(root)
        result = []
        for key in sorted(columnDictionary.keys()):
            result.append(columnDictionary[key])
        return result
            
        


        

        
        
        
        