# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getDigit(node):
            res = ''
            while node:
                res += str(node.val)
                node = node.next
                
            return res
        x = getDigit(l1)
        y = getDigit(l2)
        added = int(x)+int(y)
        added = str(added)
        
        dummy = ListNode(0)
        head = ListNode(int(added[0]))
        dummy.next = head
        for i in range(1,len(added)):
            temp = ListNode(int(added[i]))
            head.next = temp
            head = head.next
        return dummy.next
        
        
        