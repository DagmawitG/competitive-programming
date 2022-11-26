"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
       
        
        
        
        
        def flattenList(prev,curr):
            if not curr:
                return prev
            prev.next = curr
            curr.prev = prev
            
            nextPointer = curr.next
            tail = flattenList(curr,curr.child)
            curr.child = None
            return flattenList(tail,nextPointer)
        
        dummy = Node(None,None,head,None)
        flattenList(dummy,head)
        dummy.next.prev = None
        return dummy.next
            
            
            
            
        