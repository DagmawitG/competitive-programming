class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = ["()"]
        op = "()"
        for i in range(1,n):
            prev = res
            curr = []
            while len(prev) > 0:
                c = prev.pop(0)
                for i in range(len(c)+1): # r = "()"
                    curr.append(c[:i]+op +c[i:])
            res= curr
        return list(set(res))
        