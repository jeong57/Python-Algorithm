import sys
sys.stdin = open('전자카트_input.txt')


def battery(a):
    result = 0
    for i in range(len(a)-1):
        result += arr[a[i]-1][a[i+1]-1]
    return result


def perm(n, k):     # n: 배열의 크기, k: 깊이
    global min_value
    if n == k:
        cnt_value = battery(p)
        if cnt_value > min_value:
            return
        if cnt_value < min_value:
            min_value = cnt_value
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                p[k] = temp[i]
                perm(n, k+1)
                visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp = list(range(1, N+1))
    visited = [0] * N
    p = [0] * N + [1]
    p[0] = temp[0]
    visited[0] = 1
    min_value = 987654321
    perm(N, 1)
    print(f'#{tc} {min_value}')
