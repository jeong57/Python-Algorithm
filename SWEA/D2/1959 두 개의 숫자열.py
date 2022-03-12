import sys
sys.stdin = open('input.txt')


def multi(L, S, l_arr, s_arr): # L가 더 큰 배열
    max_value = 0
    for i in range(L-S+1):
        tot = 0
        for j in range(S):
            tot += l_arr[i+j]*s_arr[j]
        if tot > max_value:
            max_value = tot
    return max_value


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    if N > M:
        result = multi(N, M, ai, bi)
    else:
        result = multi(M, N, bi, ai)
    print(f'#{tc} {result}')
