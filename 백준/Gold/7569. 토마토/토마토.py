from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while q:
        sh, si, sj = q.popleft()
        for dh, di, dj in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            nh, ni, nj = sh+dh, si+di, sj+dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M:
                if arr[nh][ni][nj] == 0 and not visited[nh][ni][nj]:
                    arr[nh][ni][nj] = arr[sh][si][sj] + 1
                    visited[nh][ni][nj] = 1
                    q.append((nh, ni, nj))


M, N, H = map(int, input().split())     # M: 세로, N: 가로, H: 높이
arr = list([[0] * M for _ in range(N)] for _ in range(H))

for h in range(H):
    for i in range(N):
        arr[h][i] = list(map(int, input().split()))

visited = list([[0] * M for _ in range(N)] for _ in range(H))   # 방문체크

q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                q.append((h, i, j))

bfs()

flag = False
answer = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 0:
                flag = True
                break
            answer = max(answer, arr[h][i][j])

if flag:
    answer = -1
elif answer == -1:
    answer = 0
else:
    answer -= 1

print(answer)