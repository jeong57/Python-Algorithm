from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj, total):
    global result
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    arr[si][sj] = 2
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    total += arr[ni][nj]
                    arr[ni][nj] = 2
                    q.append((ni, nj))
    if total > result:
        result = total


N, M = map(int, input().split())    # N: 행, M: 열
arr = [list(map(int, input().split())) for _ in range(N)]   # arr: 도화지
result = 0
cnt = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1
            bfs(i, j, 1)
print(cnt)
print(result)