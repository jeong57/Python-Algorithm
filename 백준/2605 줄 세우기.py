"""
5
0 1 1 3 2
"""

N = int(input())
lst = [0] + list(map(int, input().split()))
result = []
for std in range(1, N+1):
    result.append(std)
    if lst[std] != 0:
        a = result.pop()
        # insert(a, b)는 리스트의 a번째 위치에 b를 삽입
        result.insert(std-lst[std]-1, a)
print(*result)
