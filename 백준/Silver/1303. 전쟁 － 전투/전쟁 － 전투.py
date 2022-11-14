from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj, color):
    army = 0
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        si, sj = q.popleft()
        army += 1
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = si+di, sj+dj
            if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj]:
                if arr[ni][nj] == color:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    return army


N, M = map(int, input().split())    # N: 가로(j), M: 세로(i)
arr = [list(input().rstrip()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]   # 방문체크

result_w = 0
result_b = 0
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if arr[i][j] == 'W':
                result_w += (bfs(i, j, 'W') ** 2)
            else:
                result_b += (bfs(i, j, 'B') ** 2)
print(result_w, result_b)