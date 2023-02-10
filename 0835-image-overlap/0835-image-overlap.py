from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        v1 = []
        v2 = []

        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    v1.append((i, j))
                if img2[i][j] == 1:
                    v2.append((i, j))

        ans = 0
        m = defaultdict(int)
        for i in v1:
            for j in v2:
                x = i[0] - j[0]
                y = i[1] - j[1]
                m[(x, y)] += 1
                ans = max(ans, m[(x, y)])

        return ans
