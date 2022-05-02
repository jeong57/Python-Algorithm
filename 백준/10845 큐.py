from sys import stdin
from collections import deque
input = stdin.readline


N = int(input())
q = deque()

for i in range(N):
    arr = list(input().rstrip().split())
    if arr[0] == 'push':
        q.append(int(arr[1]))
    elif arr[0] == 'pop':
        print(q.popleft()) if q else print(-1)
    elif arr[0] == 'size':
        print(len(q))
    elif arr[0] == 'empty':
        print(0) if q else print(1)
    elif arr[0] == 'front':
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)
