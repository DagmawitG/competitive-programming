# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node,sub):
            if not node and not sub:
                return True
            if not node or not sub:
                return False
            return node.val == sub.val and dfs(node.left,sub.left) and dfs(node.right,sub.right)
        
        if not root:
            return
               
        if root.val == subRoot.val and dfs(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            
