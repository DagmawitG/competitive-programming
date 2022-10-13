# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
            
        def recur(node):
            if node:
                if node.val < val:
                    if node.right:
                        recur(node.right)
                    else:
                        new = TreeNode(val)
                        if node.val > new.val:
                            node.left = new
                        else:
                            node.right = new

                else:
                    if node.left:
                        recur(node.left)
                    else:
                        new = TreeNode(val)
                        if node.val > new.val:
                            node.left = new
                        else:
                            node.right = new
        recur(root)
        return root
                
                    
            