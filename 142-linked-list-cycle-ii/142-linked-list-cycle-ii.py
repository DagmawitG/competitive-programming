# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:     
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        if fast.next == None or fast.next.next == None:
            return None
        
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
        
        
        
        
        
        
        