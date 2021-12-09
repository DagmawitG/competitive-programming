m,n = map(int, input().split())
result = 0
if (m % 2 ==0):
    result = (m//2)* n
else:
    result = ((m//2)* n) + n//2
print(result)