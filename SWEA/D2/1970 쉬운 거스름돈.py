import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8
    N = int(input())
    for i in range(8):
        while N >= money[i]:
            cnt[i] += 1
            N -= money[i]

    print(f'#{tc}')
    print(*cnt)