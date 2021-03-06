# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # break into two equal parts
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        secHalf = slow.next
        prev = slow.next = None
        while secHalf:
            temp = secHalf.next
            secHalf.next = prev
            prev = secHalf
            secHalf = temp
            
        first , second = head, prev
        while second:
            temp1,temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2
            
            
        