class Solution:
    def maximumSwap(self, num: int) -> int:
        max_num = sorted(list(str(num)))[::-1]
        position = 0
        num = list(str(num))
        for i in range(len(max_num)):
            if num[i] != max_num[i]:
                for j in range(len(num) - 1, -1, -1):
                    if num[j] == max_num[i]:
                        position = j
                        break
                num[position], num[i] = num[i], num[position]
                break
        return int("".join(str(i) for i in num))
