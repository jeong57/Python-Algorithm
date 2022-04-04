import sys
sys.stdin = open('최소 신장 트리_input.txt')


def mst():
    tot = 0
    u = 0       # 시작점: 0으로 초기화
    D[u] = 0
    # 가중치 최소값 찾기
    for _ in range(V+1):
        min_value = 987654321
        for v in range(V+1):
            if not visited[v] and D[v] < min_value:
                min_value = D[v]
                u = v
        # 방문처리
        visited[u] = 1
        tot += adj[PI[u]][u]
        # 인접한 정점 업데이트
        for v in range(V+1):
            if adj[u][v] != 0 and not visited[v]:
                if adj[u][v] < D[v]:
                    D[v] = adj[u][v]
                    PI[v] = u
    return tot


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V: 마지막 노드번호(0번부터 시작), E: 간선 개수
    adj = [[0] * (V+1) for _ in range(V+1)]
    D = [987654321] * (V+1)     # 가중치 (무한대로 초기화)
    PI = list(range(V+1))     # 부모노드
    visited = [0] * (V+1)       # 방문체크

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = adj[n2][n1] = w   # 방향성 없음
    print(f'#{tc} {mst()}')
