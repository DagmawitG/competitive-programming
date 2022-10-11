# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        ans = 0
        def dfs(node,res):
            if node:
                res += str(node.val)
            if node.left:
                dfs(node.left,res)
            if node.right:
                dfs(node.right,res)
            if not node.left and not node.right:
                result.append(res)
        dfs(root,'')
        for val in result:
            ans += int(val)
        return ans
                
                
                
            
            
            
            
        