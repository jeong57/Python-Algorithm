from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj):
    global sheep, wolf
    q = deque()
    q.append((si, sj))
    n_sheep, n_wolf = 0, 0
    visited[si][sj] = 1
    if arr[si][sj] == 'o':
        n_sheep += 1
    elif arr[si][sj] == 'v':
        n_wolf += 1

    while q:
        si, sj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = si+di, sj+dj
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and arr[ni][nj] != '#':
                q.append((ni, nj))
                visited[ni][nj] = 1
                if arr[ni][nj] == 'o':
                    n_sheep += 1
                elif arr[ni][nj] == 'v':
                    n_wolf += 1
    if n_sheep > n_wolf:
        sheep += n_sheep
    else:
        wolf += n_wolf


R, C = map(int, input().split())    # R: 행, C: 열
arr = [list(input().rstrip()) for _ in range(R)]
sheep = 0   # 최종 양 수
wolf = 0    # 최종 늑대 수
visited = [[0] * C for _ in range(R)]   # 방문 체크
for i in range(R):
    for j in range(C):
        if not visited[i][j] and (arr[i][j] == 'o' or arr[i][j] == 'v'):
            bfs(i, j)
print(sheep, wolf)