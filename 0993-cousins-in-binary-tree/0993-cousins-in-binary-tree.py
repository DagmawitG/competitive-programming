# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return False
        
        
            
        
        
        
        def dfs(root, x, y, depth, parent):
            if not root:
                return 
            
            if root.val == x:
                self.x_parent = parent
                self.x_depth = depth
            if root.val == y:
                self.y_parent = parent
                self.y_depth = depth
                
            dfs(root.left,x,y,depth+1,root)
            dfs(root.right,x,y,depth+1,root)
    
        dfs(root,x,y,0,None)
        
        if self.x_parent != self.y_parent and self.x_depth == self.y_depth:
            return True
        else:
            return False
            
           