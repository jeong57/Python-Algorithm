"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

"""

"""
10 4790
1
5
10
50
100
500
1000
5000
10000
50000

"""
from sys import stdin
input = stdin.readline

stack = []  # 동전의 가치(오름차순)
N, K = map(int, input().split())
for i in range(N):
    stack.append(int(input()))

i = -1  # 동전 액수가 큰 것부터 내려오기
result = 0
while K:
    if K >= stack[i]:   # 동전 액수가 K보다 작으면 빼기
        K -= stack[i]
        result += 1
    else:               # 동적 액수가 K보다 크면 더 작은 동전 사용
        i -= 1
print(result)
