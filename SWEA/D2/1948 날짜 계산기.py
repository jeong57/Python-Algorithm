import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())

    months = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0

    if m1 == m2:
        result = d2 - d1
    else:
        for i in range(m1+1, m2):
            result += days[i]
        result += days[m1]-d1
        result += d2

    print(f'#{tc} {result+1}')
