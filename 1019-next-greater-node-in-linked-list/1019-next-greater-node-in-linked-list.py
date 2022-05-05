# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sizeNodes(self,head):
        count=0
        
        while head :
            head = head.next
            count += 1
        return count
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        temp = []
        count = self.sizeNodes(head)
        result = [0]*count
       
        while head:

            while stack and temp[stack[-1]]<head.val:
                result[stack.pop()] = head.val
            temp.append(head.val)
            stack.append(len(temp)-1)
            head = head.next     
           
            
        return result
            
            
        
        
    
        
        
        