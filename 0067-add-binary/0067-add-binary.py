class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        carry = 0
        ret = ""
        l1, l2 = len(a) - 1, len(b) - 1
        while l1 >= 0 or l2 >= 0 or carry == 1:
            if l1 >= 0:
                carry += int(a[l1])
                l1 -= 1
            if l2 >= 0:
                carry += int(b[l2])
                l2 -= 1
            ret = str(carry % 2) + ret
            carry //= 2
        return ret
        