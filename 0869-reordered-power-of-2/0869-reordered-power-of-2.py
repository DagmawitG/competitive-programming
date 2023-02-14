class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))
        i = 1
        iterate = 0
        while iterate <= 30:
            iterate += 1
            tmp_i = str(i)
            tmp = Counter(tmp_i)
            if tmp == count:
                return True
            i *= 2
        return False
        