# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefixSum = 0
        mapping = {}
        mapping[0] = node = ListNode(0)
        current = node.next = head

        while current:
            prefixSum += current.val
            mapping[prefixSum] = current
            current = current.next

        head = node
        prefixSum = 0

        while head:
            prefixSum += head.val
            head.next = mapping[prefixSum].next
            head = head.next

        return node.next
                
                
                
            
            
        print(res)
            
        