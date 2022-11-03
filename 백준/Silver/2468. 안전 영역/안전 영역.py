from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj, num):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        si, sj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N and land[ni][nj] > num and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))


N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]

max_land = 0
for i in range(N):
    max_land = max(max_land, max(land[i]))

result = 0
for n in range(max_land):
    visited = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if land[i][j] > n and not visited[i][j]:
                bfs(i, j, n)
                count += 1
    result = max(result, count)
print(result)
