def dfs(si, sj):
    global cnt
    arr[si][sj] = 0
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = si+di, sj+dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and not visited[ni][nj]:
            cnt += 1
            dfs(ni, nj)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            cnt = 1
            dfs(i, j)
            result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)
