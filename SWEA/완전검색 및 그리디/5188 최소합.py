import sys
sys.stdin = open('최소합_input.txt')


def dfs(si, sj, cnt_sum):
    global result
    # 가지치기
    if cnt_sum > result:
        return
    # 종료 조건
    if si == N-1 and sj == N-1:
        # 정답 처리
        if cnt_sum < result:
            result = cnt_sum
    # 하부함수 호출
    visited[si][sj] = 1
    for di, dj in [(0, 1), (1, 0)]:
        ni, nj = si+di, sj+dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            dfs(ni, nj, cnt_sum+arr[ni][nj])
            visited[ni][nj] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]     # 방문체크
    result = 987654321
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {result}')
