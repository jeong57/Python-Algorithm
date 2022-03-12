"""
2
3
4
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ni = nj = 0
    move = 0
    for i in range(1, N*N+1):
        arr[ni][nj] = i
        ni += di[move]
        nj += dj[move]
        if 0 > ni or ni >= N or 0 > nj or nj >= N or arr[ni][nj] != 0:
            ni -= di[move]
            nj -= dj[move]
            move = (move + 1) % 4
            ni += di[move]
            nj += dj[move]

    print(f'#{tc}')
    for i in arr:
        print(*i)
