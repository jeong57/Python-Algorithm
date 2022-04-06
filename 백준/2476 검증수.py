"""
0 4 2 5 6

"""

lst = list(map(int, input().split()))
result = 0
for num in lst:
    result += num ** 2
print(result % 10)
