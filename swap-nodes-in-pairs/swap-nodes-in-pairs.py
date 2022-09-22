# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        if head == None or head.next == None:
            return head 
        
        
        temp = head.next
        head.next = temp.next
        temp.next = head
        head = temp
        subList = self.swapPairs(head.next.next)
        
        head.next.next = subList
        return head
        
        
        
        
       
        
        
       
        
       
        
        