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
                
            return res[::-1]
       
        
        str1 = getDigit(l1)
        str2 = getDigit(l2)
        added = int(str1) + int(str2)
        added = str(added)
        
        first = added[-1]
        head = ListNode(first)
        dummy = ListNode(0)
        dummy.next = head
        
        for i in range(len(added)-2,-1,-1):
            temp = ListNode(int(added[i]))
            head.next = temp
            head = head.next
        return dummy.next
        
      