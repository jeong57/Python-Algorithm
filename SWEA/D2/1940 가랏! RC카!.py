import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # v: 현재 속도, d: 이동거리
    v = d = 0
    for i in range(N):
        if arr[i][0] == 0:
            d += v
        elif arr[i][0] == 1:
            v += arr[i][1]
            d += v
        elif arr[i][0] == 2:
            if v < arr[i][1]:
                v = 0
            else:
                v -= arr[i][1]
            d += v
    print(f'#{tc} {d}')
