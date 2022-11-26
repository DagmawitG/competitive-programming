# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.setrecursionlimit(10**6)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            nxtPtr = current.next
            current.next = previous
            previous = current
            current = nxtPtr
        return previous
        
        
            
            
      
        
        
        

        
        
            
        