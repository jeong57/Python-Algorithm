import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    memo = [0] * len(lst)
    i = 0
    cnt = 0
    while memo != lst:
        if lst[i] != memo[i]:
            memo[i:] = [lst[i]] * (len(lst)-i)
            cnt += 1
        i += 1
    print(f'#{tc} {cnt}')

