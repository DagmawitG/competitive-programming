# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursion(root)
        
    def recursion(self,node):
        if not node:
            return 0
        left = self.recursion(node.left)
        right = self.recursion(node.right)
        answer = max(left,right) + 1
        
        return answer
    
        
    
        
        
        
       
            
        
        
        

           
        
                
                
            
        
            
        