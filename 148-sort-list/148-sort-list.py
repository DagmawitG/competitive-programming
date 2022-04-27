# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        sortList = []
        while current != None:
            sortList.append(current.val)
            current = current.next
        sortList.sort()
        temp = head
        for i in sortList:
            temp.val = i
            temp = temp.next
            
        
        return head