import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 0
    max_value = lst[-1]
    for i in range(N-2, -1, -1):
        if lst[i] < max_value:
            result += max_value - lst[i]
        else:
            max_value = lst[i]
    print(f'#{tc} {result}')


