import sys
sys.stdin = open('input.txt')


def omok(arr):
    direction = [(0, 1), (1, 1), (1, 0), (1, -1)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    ni = i
                    nj = j
                    cnt = 0
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += direction[k][0]
                        nj += direction[k][1]
                        if cnt >= 5:
                            return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {omok(arr)}')
