# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node = head
        n = 0
        while node:
            n += 1
            node = node.next
        result = []
        node = head
        prev = None
        q = n // k
        remainder = n % k
        for i in range(k):
            result.append(node)
            for j in range(q):
                prev = node
                node = node.next
            if remainder and node:
                prev = node
                node = node.next
                remainder -= 1
            if prev:
                prev.next = None
        return result
                
                
            
            
            
            
            
             
                
                
            
            
        