class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        if maxDoubles == 0:
            return target - 1
        while target > 1 :
            if maxDoubles == 0:
                count += target-1
                break
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
                
            count += 1
        return count 
            
        