from collections import deque
import sys
input = sys.stdin.readline


def red_green_strong(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if grid[si][sj] == 'R':
                    if grid[ni][nj] == 'R':
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                elif grid[si][sj] == 'G':
                    if grid[ni][nj] == 'G':
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                elif grid[si][sj] == 'B':
                    if grid[ni][nj] == 'B':
                        q.append((ni, nj))
                        visited[ni][nj] = 1


def red_green_weak(si, sj):
    q = deque()
    q.append((si, sj))
    visited2[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited2[ni][nj]:
                if grid[si][sj] == 'R' or grid[si][sj] == 'G':
                    if grid[ni][nj] == 'R' or grid[ni][nj] == 'G':
                        q.append((ni, nj))
                        visited2[ni][nj] = 1
                elif grid[si][sj] == 'B':
                    if grid[ni][nj] == 'B':
                        q.append((ni, nj))
                        visited2[ni][nj] = 1


N = int(input())    # N: 그리드 한 변의 크기
grid = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]   # 적록색약 아닌 사람 방문체크
visited2 = [[0] * N for _ in range(N)]  # 적록색약인 사람 방문체크

cnt1, cnt2 = 0, 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            red_green_strong(i, j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            red_green_weak(i, j)
            cnt2 += 1
print(cnt1, cnt2)
