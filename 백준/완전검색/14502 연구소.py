"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

"""
from collections import deque

def bfs():
    global max_value
    q = deque()
    visited = [[0] * M for _ in range(N)]
    # 바이러스가 있는 좌표들 찾아서 큐에 넣어두기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
    while q:
        si, sj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < M:
                # 바이러스가 퍼지지 않고, 방문한 적이 없는 곳이면 체크
                if arr[ni][nj] == 0 and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 값이 0이고 방문한 적이 없으면 바이러스가 퍼지지 않은 곳
            if arr[i][j] == 0 and not visited[i][j]:
                cnt += 1
    max_value = max(max_value, cnt)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 배열 값이 0인 좌표들을 리스트에 넣기
temp = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            temp.append((i, j))
max_value = 0
K = len(temp)
# 값이 0인 좌표들 중 3개를 뽑기(조합)
for i in range(0, K-2):
    for j in range(i+1, K-1):
        for k in range(j+1, K):
            # 뽑은 3개 좌표에 벽 세우기
            arr[temp[i][0]][temp[i][1]] = arr[temp[j][0]][temp[j][1]] = arr[temp[k][0]][temp[k][1]] = 1
            bfs()
            # 함수를 돌리고 나서는 다시 벽 없애줘야 한다.
            arr[temp[i][0]][temp[i][1]] = arr[temp[j][0]][temp[j][1]] = arr[temp[k][0]][temp[k][1]] = 0
print(max_value)
