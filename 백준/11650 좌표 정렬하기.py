"""
5
3 4
1 1
1 -1
2 2
3 3

"""
from sys import stdin
input = stdin.readline

N = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(N))
arr.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*arr[i])
