import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+1)]
    result = 0
    for i in range(N+1):
        cnt = cnt2 = 0
        for j in range(N+1):
            if arr[i][j]:
                cnt += 1
            if arr[j][i]:
                cnt2 += 1
            if arr[i][j] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
            if arr[j][i] == 0:
                if cnt2 == K:
                    result += 1
                cnt2 = 0

    print(f'#{tc} {result}')
