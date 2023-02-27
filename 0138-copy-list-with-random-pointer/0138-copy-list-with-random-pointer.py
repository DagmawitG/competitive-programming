"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        node_to_clone = dict()
        node = head
        clone_head = Node(head.val)
        node_to_clone[head] = clone_head
        clone_node = clone_head
        while node.next:
            clone_node.next = Node(node.next.val)
            node = node.next
            clone_node = clone_node.next
            node_to_clone[node] = clone_node
        node = head
        while node:
            if node.random:
                clone_node = node_to_clone[node]
                clone_node.random = node_to_clone[node.random]
            node = node.next
        return clone_head

        