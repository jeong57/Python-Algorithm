import sys
sys.stdin = open('동철이의 일 분배_input.txt')


def perm(n, k, sup):
    global max_value
    if sup == 0:
        return

    if n == k:
        if sup*100 > max_value:
            max_value = sup*100
    if sup*100 < max_value:
        return

    else:
        for i in range(k, n):
            nums[i], nums[k] = nums[k], nums[i]
            perm(n, k+1, sup*arr[k][nums[k]]/100)
            nums[i], nums[k] = nums[k], nums[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = list(range(N))
    max_value = 0
    perm(N, 0, 1)
    print('#%d %.6f' % (tc, max_value))
