# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            current = head
            prev = current.next
            current.next = prev.next
            prev.next = current
            current.next = self.swapPairs(current.next)
        
            return prev
       
            
            
           
            
        
       
        