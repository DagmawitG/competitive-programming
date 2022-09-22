# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.setrecursionlimit(10**6)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        return self.helper(None,head)
        
        
    def helper(self,subList,node):
        temp = node.next
        node.next = subList
        if temp != None:
            return self.helper(node,temp)
            
        return node
            
        
        
        
            
        