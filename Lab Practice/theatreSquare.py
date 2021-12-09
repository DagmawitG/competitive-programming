import math
m,n,a = map(int, input().split())
stones = math.ceil(m/a) * math.ceil(n/a)
print(stones)