class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
       
        def dfs(node,level):
            nonlocal result
            if not node:
                return
            
            if level >= len(result):
                result.append(node.val)
            else:
                result[level] = max(node.val,result[level])
            
            
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)
        dfs(root,0)
        
        return result
            
            
            
            
        