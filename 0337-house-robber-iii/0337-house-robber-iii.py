# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        
        def dfs(node):
            
            if not node:
                return 0,0
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            case1 = node.val + leftSum[1] + rightSum[1]
            case2 = max(leftSum) + max(rightSum)
            
            return case1,case2
        
        return max(dfs(root))
        
        
             
            
            
            
                
            
                
            
            
        