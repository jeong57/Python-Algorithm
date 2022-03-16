import sys
sys.stdin = open("노드의 거리_input.txt")


def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in range(1, V+1):
            if adj[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1
    if not visited[G]:
        return 0
    else:
        return visited[G]-1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V: 노드 개수, E: 간선 수
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        s, e = map(int, input().split())
        adj[s][e] = adj[e][s] = 1   # 방향성 없음
    S, G = map(int, input().split())    # S: 출발노드, G: 도착노드
    print(f'#{tc} {bfs(S)}')
