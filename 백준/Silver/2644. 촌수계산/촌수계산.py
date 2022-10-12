import sys
input = sys.stdin.readline


def bfs(v):
    q = [v]
    while q:
        v = q.pop()
        for w in range(N+1):
            if w in adj[v] and relation[w] == 0:
                relation[w] = relation[v] + 1
                q.append(w)


N = int(input())    # N: 전체 사람의 수
a, b = map(int, input().split())    # A, B: 촌수를 계산해야 하는 두 사람의 번호
M = int(input())    # M: 부모 자식들 간의 관계의 개수
adj = [[] for _ in range(N+1)]    # 부모 자식간의 관계
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

relation = [0] * (N+1)  # 촌수 계산
bfs(a)
if relation[b]:
    print(relation[b])
else:
    print(-1)