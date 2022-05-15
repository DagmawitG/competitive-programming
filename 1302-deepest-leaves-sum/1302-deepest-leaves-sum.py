# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levels = {}
        
        def dfs(curr,prevVal,level):
            if curr==None:
                return
            level+=1
            if level in levels:
                levels[level]+=curr.val
            else:
                levels[level]=curr.val
                
            dfs(curr.left,curr.val,level)
            dfs(curr.right,curr.val,level)
            
        dfs(root,0,0)
        return levels[max(levels)]
        