from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        si, sj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and farm[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())     # M: 가로, N: 세로, K: 배추 개수
    farm = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    cnt = 0
    visited = [[0] * M for _ in range(N)]   # 방문체크
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and farm[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)