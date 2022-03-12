"""
2
4
2 4 7 10
5
1 3 2 4 10
"""


def danjo(multi):
    while multi:
        if (multi // 10) % 10 > multi % 10:
            return -1
        else:
            multi //= 10
    return 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_value = 0
    for i in range(N-1):
        for j in range(i+1, N):
            multi = arr[i] * arr[j]
            if danjo(multi) == 1:
                if multi > max_value:
                    max_value = multi
    if max_value == 0:
        result = -1
    else:
        result = max_value
    print(f'#{tc} {result}')
