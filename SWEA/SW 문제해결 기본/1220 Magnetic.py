import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # 열 기준
    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                for k in range(i+1, N):
                    if arr[k][j] == 1:
                        break
                    elif arr[k][j] == 2:
                        cnt += 1
                        break
    print(f'#{test_case} {cnt}')
