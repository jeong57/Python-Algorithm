import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    result = 'Possible'
    for i in range(N):
        if (i+1) > (lst[i]//M)*K:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')
