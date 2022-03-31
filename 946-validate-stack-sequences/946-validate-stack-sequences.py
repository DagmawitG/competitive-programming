class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        
        if len(popped) != len(pushed):
            return False
        for num in pushed:
            stack.append(num)
            while(len(stack) > 0 and stack[len(stack)-1] == popped[i]):
                stack.pop()
                i += 1
        if len(stack) == 0:
            return True
        return False
       
        