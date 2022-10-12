def dfs(v):
    for w in adj[v]:
        if relation[w] == 0:
            relation[w] = relation[v] + 1
            dfs(w)


N = int(input())    # N: 전체 사람의 수
a, b = map(int, input().split())    # A, B: 촌수를 계산해야 하는 두 사람의 번호
M = int(input())    # M: 부모 자식들 간의 관계의 개수
adj = [[] for _ in range(N+1)]    # 부모 자식간의 관계
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

relation = [0] * (N+1)  # 촌수 계산
dfs(a)
print(relation[b] if relation[b] else -1)