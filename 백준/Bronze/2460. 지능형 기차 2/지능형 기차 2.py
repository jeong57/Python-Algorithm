import sys
input = sys.stdin.readline


result = 0
max_result = 0
for i in range(10):
    a, b = map(int, input().split())
    result -= a
    result += b
    max_result = max(result, max_result)
print(max_result)