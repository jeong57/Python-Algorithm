import sys
input = sys.stdin.readline


def dfs(v):
    global cnt
    visited[v] = 1
    for w in range(N+1):
        if adj[v][w] and not visited[w]:
            cnt += 1
            dfs(w)


N = int(input())    # N: 컴퓨터의 수
M = int(input())    # M: 직접 연결된 컴퓨터 쌍의 수
adj = [[0] * (N+1) for _ in range(N+1)]     # adj: 컴퓨터 간 관계(인접행렬)
for i in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1   # 연결 상태 파악(양방향)
visited = [0] * (N+1)   # 방문체크
cnt = 0
dfs(1)
print(cnt)