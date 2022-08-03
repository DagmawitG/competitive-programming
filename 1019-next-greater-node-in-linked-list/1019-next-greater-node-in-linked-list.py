# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head):
        prev = None
        current = head
        while(current != None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = []
        stack = []
        head = self.reverseList(head)
        
        while(head != None):
            if(len(stack)==0):
                result.append(0)
               
                stack.append(head.val)
                head = head.next
            elif(stack[-1] > head.val):
                
                result.append(stack[-1])
                
                stack.append(head.val)
                head = head.next
            else:
                stack.pop()
        return result[::-1]
        