"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

"""
from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    q = deque()
    idx = deque()
    result = []
    sp = list(map(int, input().split()))
    for i in range(N):
        q.append(sp[i])
        idx.append(i)

    while q:
        if q[0] != max(q):
            q.append(q.popleft())
            idx.append(idx.popleft())
        else:
            q.popleft()
            result.append(idx.popleft())
    print(result.index(M)+1)
