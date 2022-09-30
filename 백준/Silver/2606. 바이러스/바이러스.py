import sys
input = sys.stdin.readline


def dfs(v):
    global cnt
    visited[v] = 1
    for w in range(1, N+1):
        if adj[v][w] and not visited[w]:
            cnt += 1
            dfs(w)


N = int(input())    # N: 컴퓨터의 수
M = int(input())    # M: 직접 연결돼 있는 컴퓨터 쌍의 수
adj = [[0] * (N+1) for _ in range(N+1)]     # 인접행렬
visited = [0] * (N+1)   # 바이러스 감염여부 체크
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1   # 방향성 없음

dfs(1)  # 1번 컴퓨터부터 시작
print(cnt)
