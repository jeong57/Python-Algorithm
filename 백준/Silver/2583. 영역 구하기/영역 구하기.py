from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    arr[si][sj] = 1
    count = 1
    while q:
        ci, cj = q.popleft()
        arr[ci][cj] = 1
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < M and 0 <= nj < N and not arr[ni][nj]:
                count += 1
                arr[ni][nj] = 1
                q.append((ni, nj))
    return count


M, N, K = map(int, input().split())     # M: 행, N: 열, K: 직사각형 수
arr = [[0] * N for _ in range(M)]   # arr: 전체 영역
for _ in range(K):
    # a, b: 왼쪽 아래 꼭짓점
    # c, d: 오른쪽 위 꼭짓점
    a, b, c, d = map(int, input().split())
    for i in range(M-d, M-b):
        for j in range(a, c):
            arr[i][j] = 1

result = []
for i in range(M):
    for j in range(N):
        if not arr[i][j]:
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result)