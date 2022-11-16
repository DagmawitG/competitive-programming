# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])
        while queue:
            p,q = queue.popleft() 
          
            if (not p and q )or (p and not q):
                return False
            
            if (p and q) and p.val == q.val:
                queue.append((p.left,q.left))
                queue.append((p.right,q.right))
            elif (p and q) and p.val != q.val:
                return False
           
        return True
   
        
        
        
        
       
       
                
            
        
        