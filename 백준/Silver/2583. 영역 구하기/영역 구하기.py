import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(si, sj):
    global count
    arr[si][sj] = 1
    count += 1
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = si + di, sj + dj
        if 0 <= ni < M and 0 <= nj < N and not arr[ni][nj]:
            dfs(ni, nj)


M, N, K = map(int, input().split())     # M: 행, N: 열, K: 직사각형 수
arr = [[0] * N for _ in range(M)]   # arr: 전체 영역
for _ in range(K):
    # a, b: 왼쪽 아래 꼭짓점 / c, d: 오른쪽 위 꼭짓점
    a, b, c, d = map(int, input().split())
    for i in range(M-d, M-b):
        for j in range(a, c):
            arr[i][j] = 1

result = []
for i in range(M):
    for j in range(N):
        if not arr[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))
print(*result)