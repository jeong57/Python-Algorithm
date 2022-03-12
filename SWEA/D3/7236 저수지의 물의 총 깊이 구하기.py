import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    max_value = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            cnt = 0
            if arr[i][j] == 'W':
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if arr[ni][nj] == 'W':
                        cnt += 1
                if cnt == 0:
                    cnt = 1
            if cnt > max_value:
                max_value = cnt

    print(f'#{tc} {max_value}')
