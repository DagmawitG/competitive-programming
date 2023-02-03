import random

class Solution:
    def __init__(self, w: List[int]):
        self.weights = w

    def pickIndex(self) -> int:
        rand = random.uniform(0, sum(self.weights))
        for i, weight in enumerate(self.weights):
            rand -= weight
            if rand <= 0:
                return i

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()