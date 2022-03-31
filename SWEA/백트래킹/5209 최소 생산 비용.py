import sys
sys.stdin = open('최소 생산 비용_input.txt')


def perm(n, k, cnt_sum):     # n: 배열 길이, k: 깊이
    global min_result
    if cnt_sum > min_result:
        return
    if n == k:
        if cnt_sum < min_result:
            min_result = cnt_sum
    else:
        for i in range(k, n):
            T[i], T[k] = T[k], T[i]
            perm(n, k+1, cnt_sum+arr[k][T[k]])
            T[i], T[k] = T[k], T[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    T = list(range(N))
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_result = 987654321
    perm(N, 0, 0)
    print(f'#{tc} {min_result}')
