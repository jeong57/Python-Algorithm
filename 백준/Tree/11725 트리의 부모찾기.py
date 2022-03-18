"""
7
1 6
6 3
3 5
4 1
2 4
4 7

"""
from sys import stdin
input = stdin.readline


def bfs(v):
    global parent
    q = []
    visited = [0] * (N + 1)
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        for node in tree[v]:        # 인접리스트에 있는 노드 번호 확인
            if not visited[node]:   # 방문체크
                q.append(node)
                visited[node] = 1
                parent[node] = v
    return parent


N = int(input())
tree = [[] for _ in range(N+1)]     # 인접리스트
parent = [0]*(N+1)  # 부모노드 정보
for i in range(N-1):
    a, b = map(int, input().split())
    # 방향성 없음
    tree[a].append(b)
    tree[b].append(a)
bfs(1)
for i in range(2, N+1):
    print(parent[i])
