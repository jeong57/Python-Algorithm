import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    half = N//2
    total = 0
    for i in range(half+1):
        for j in range(half-i, half+i+1):
            total += arr[i][j]
    for i in range(half+1, N):
        for j in range(i-half, N-i+half):
            total += arr[i][j]
    print(f'#{tc} {total}')
