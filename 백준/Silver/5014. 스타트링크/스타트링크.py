from collections import deque


def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == G:
            return count[G]
        for w in (v+U, v-D):
            if 0 < w <= F and not visited[w]:
                visited[w] = 1
                q.append(w)
                count[w] = count[v] + 1
    if count[G] == 0:
        return "use the stairs"


# F: 총 층수, S: 현재 층, G: 목적지
# U: 위 버튼, D: 아래 버튼
F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)   # 방문체크
count = [0] * (F+1)
print(bfs(S))
