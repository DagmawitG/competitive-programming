class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        you = 0
        if len(piles)==3:
            return piles[1]
        else:
            res = (len(piles)//3)-1 
            j = len(piles)-2
            while(j> res):
                you += piles[j]
                j-=2
            return you