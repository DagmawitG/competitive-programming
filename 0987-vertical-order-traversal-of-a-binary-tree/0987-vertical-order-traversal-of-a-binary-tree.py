# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        nodes = defaultdict(list)
        queue = deque([(root, 0, 0)])
        while queue:
            node, x, y = queue.popleft()
            nodes[x].append((y, node.val))
            if node.left:
                queue.append((node.left, x - 1, y + 1))
            if node.right:
                queue.append((node.right, x + 1, y + 1))
        
        result = []
        for x in sorted(nodes):
            values = [node[1] for node in sorted(nodes[x], key=lambda x: (x[0], x[1]))]
            result.append(values)
        return result
